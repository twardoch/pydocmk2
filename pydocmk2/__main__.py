# coding=utf-8
# Copyright (c) 2020  Adam Twardoch
# Copyright (c) 2017  Niklas Rosenstein
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
python2 -m pydocmk2 build
"""

from __future__ import print_function
from .document import Index
from .preprocessors.pydocmk import pydoc_html
from .imp import import_object, dir_object
import argparse

import atexit
import os
import shutil
import signal
import subprocess
import sys
import yaml
import json

# parser = ArgumentParser()
# parser.add_argument('command', choices=['generate', 'build', 'gh-deploy',
#                                        'json', 'new', 'serve', 'simple'])
# parser.add_argument('subargs', nargs='...')


def log(*args, **kwargs):
    kwargs.setdefault('file', sys.stderr)
    print(*args, **kwargs)


class PyDocMk(object):

    def __init__(self):
        self.args = None
        self.command = 'build'
        self.clean = False
        self.config_dir = os.getcwd()
        self.docs_dir = os.path.join(self.config_dir, 'srcdocs')
        self.gens_dir = os.path.join(self.config_dir, '_build/mkdocs')
        self.pre_dir = None
        self.post_dir = None
        self.config_path = os.path.join(self.config_dir, 'pydocmk.yml')
        self.mkdocs_path = None
        self.config = {}
        self.mk_config = {}
        self.python_path = 'python2'
        self.subargs = []
        self.config_custom = None

    def parse_args(self):
        parser = argparse.ArgumentParser(
            prog="pydocmk2",
            description="document Python 2 modules with MkDocs"
        )
        parser.add_argument(
            "command",
            default='build',
            choices=['generate', 'build', 'gh-deploy',
                     'json', 'new', 'serve', 'simple', 'pydoc'],
            help="""`simple`: output one .md file, e.g. `simple mypackage+ mypackage.my module+ > docs.md`,
        `pydoc`: output the content of the pydocmk preprocessor,
        `generate`: generate .md but do not run mkdocs,
        `build`: generate .md and build with mkdocs,
        `serve`: generate .md, build with mkdocs and run a webserver"""
        )
        parser.add_argument(
            "subargs",
            nargs="*",
            help="optional arguments passed to mkdocs"
        )
        parser.add_argument(
            "-F",
            "--config",
            dest="config_custom",
            type=str,
            help="extra config params as JSON: --config={'key':'value','key':'value'}"
        )
        parser.add_argument(
            "-f",
            "--config-file",
            default=self.config_path,
            type=str,
            dest="config_path",
            help="pydocmk.yml YAML config file: --config-file=pydocmk.yml"
        )
        parser.add_argument(
            "-m",
            "--mkdocs-file",
            type=str,
            dest="mkdocs_path",
            help="mkdocs.yml YAML config file to build/use: --mkdocs-file=mkdocs.yml"
        )
        parser.add_argument(
            "-p",
            "--python",
            default="python2",
            type=str,
            dest="python_path",
            help="Python executable to run mkdocs: --python=python2"
        )
        parser.add_argument(
            "-c",
            "--clean",
            dest="clean",
            action="store_true"
        )

        self.args = parser.parse_args()
        if self.args.command:
            self.command = self.args.command
        if self.args.subargs:
            self.subargs = self.args.subargs
        if self.args.clean:
            self.clean = self.args.clean
        self.config_path = self.args.config_path  # 'pydocmk.yml'
        self.config_dir = os.path.dirname(self.config_path)
        if self.args.python_path:
            self.python_path = self.args.python_path
        if self.args.config_custom:
            self.config_custom = self.args.config_custom
        if self.args.mkdocs_path:
            self.mkdocs_path = self.args.mkdocs_path

        if self.args.command in ('simple', 'pydoc') and not self.args.subargs:
            parser.error('need at least one argument')

    def read_config(self):
        """
        Reads and preprocesses the pydocmk2 configuration file.
        """

        with open(self.config_path) as fp:
            self.config = yaml.safe_load(fp)
        self.default_config(blank=False)

    def default_config(self, blank=False):
        if blank:
            self.config = {}
        if not self.mkdocs_path:
            if self.config.get('mkdocs_path', None):
                self.mkdocs_path = self.config['mkdocs_path']
            else:
                self.mkdocs_path = os.path.join(self.config_dir, 'mkdocs.yml')
        self.config.setdefault('docs_dir', 'srcdocs')
        self.docs_dir = self.config['docs_dir']
        if not os.path.isabs(self.docs_dir):
            self.docs_dir = os.path.join(self.config_dir, self.docs_dir)
        self.config.setdefault('gens_dir', '_build/mkdocs')
        self.gens_dir = self.config['gens_dir']
        if not os.path.isabs(self.gens_dir):
            self.gens_dir = os.path.join(self.config_dir, self.gens_dir)
        self.config.setdefault('site_dir', '_build/docs')
        self.config.setdefault('pydocmk_pre_dir', None)
        self.pre_dir = self.config['pydocmk_pre_dir']
        if self.pre_dir:
            if not os.path.isabs(self.pre_dir):
                self.pre_dir = os.path.join(self.config_dir, self.pre_dir)
        self.config.setdefault('pydocmk_post_dir', None)
        self.post_dir = self.config['pydocmk_post_dir']
        if self.post_dir:
            if not os.path.isabs(self.post_dir):
                self.post_dir = os.path.join(
                    self.config_dir, self.post_dir)
        if self.command in ('simple', 'pydoc'):
            self.config.setdefault('headers', 'markdown')
        else:
            self.config.setdefault('headers', 'markdown')
        self.config.setdefault('theme', 'readthedocs')
        self.config.setdefault('loader', 'pydocmk2.loader.PythonLoader')
        self.config.setdefault(
            'preprocessor', 'pydocmk2.preprocessors.pydocmk.Preprocessor')
        self.config.setdefault('additional_search_paths', [])
        self.config.setdefault('markdown_extensions', [
                               'attr_list', 'def_list', 'tables', 'abbr', 'admonition', 'codehilite', 'pymdownx.extrarawhtml'])

    def write_temp_mkdocs_config(self):
        """
        Generates a configuration for MkDocs on-the-fly from the pydocmk2
        configuration and makes sure it gets removed when this program exists.
        """
        ignored_keys = ('gens_dir', 'pages', 'headers', 'generate', 'loader',
                        'preprocessor', 'additional_search_paths', 'pydocmk_pre_dir', 'pydocmk_post_dir')

        self.mk_config = {key: value for key,
                          value in self.config.items() if key not in ignored_keys}
        self.mk_config['docs_dir'] = self.config['gens_dir']
        if 'pages' in self.config:
            self.mk_config['nav'] = self.config['pages']

        with open(self.mkdocs_path, 'w') as fp:
            yaml.dump(self.mk_config, fp)

    def makedirs(self, path):
        """
        Create the directory *path* if it does not already exist.
        """

        if not os.path.isdir(path):
            os.makedirs(path)

    # Also process all pages to copy files outside of the docs_dir to the gens_dir.

    def process_pages(self, data, gens_dir):
        for key in data:
            filename = data[key]
            if isinstance(filename, str) and '<<' in filename:
                filename, source = filename.split('<<')
                filename, source = filename.rstrip(), os.path.join(
                    self.config_dir, source.lstrip())
                outfile = os.path.join(gens_dir, filename)
                self.makedirs(os.path.dirname(outfile))
                shutil.copyfile(source, outfile)
                data[key] = filename
            elif isinstance(filename, dict):
                self.process_pages(filename, gens_dir)
            elif isinstance(filename, list):
                [self.process_pages(x, gens_dir) for x in filename]

    def clean_files(self):
        if self.clean:
            if os.path.isfile(self.mkdocs_path):
                log('Removing file %s...' % (self.mkdocs_path))
                os.remove(self.mkdocs_path)
            if os.path.isdir(self.config.get('gens_dir', None)):
                log('Cleaning generated folder %s...' % (self.gens_dir))
                shutil.rmtree(self.gens_dir)
            atexit.register(lambda: os.remove(self.mkdocs_path))

    def copy_source_files(self, pages_required=True):
        """
        Copies all files from the `docs_dir` to the `gens_dir` defined in the
        *config*. It also takes the MkDocs `pages` configuration into account
        and converts the special `<< INFILE` syntax by copying them to the
        `gens_dir` as well.
        """

        for path in self.config['additional_search_paths']:
            path = os.path.abspath(path)
            sys.path.append(path)

        # Copy all template files from the source directory into our
        # generated files directory.
        log('Started copying source files...')
        for root, dirs, files in os.walk(self.docs_dir):
            rel_root = os.path.relpath(root, self.docs_dir)
            for fname in files:
                dest_fname = os.path.join(self.gens_dir, rel_root, fname)
                self.makedirs(os.path.dirname(dest_fname))
                shutil.copyfile(os.path.join(root, fname), dest_fname)

        if 'pages' not in self.config:
            if pages_required:
                raise RuntimeError('pydocmk.yml does not have defined pages!')

            return

        for page in self.config['pages']:
            self.process_pages(page, self.gens_dir)

    def new_project(self):
        with open('pydocmk.yml', 'w') as fp:
            fp.write(
                'site_name: Welcome to pydoc-markdown\ngenerate:\npages:\n- Home: index.md << ../README.md\n')

    def main(self):
        if self.command == 'new':
            self.new_project()
            return

        if self.command == 'pydoc':
            if len(self.subargs):
                mod = self.subargs[0]
                print(pydoc_html(mod))
            return

        if self.command not in ('simple', 'pydoc'):
            self.read_config()
        else:
            self.default_config(blank=True)

        if self.config_custom:
            try:
                config_custom = json.loads(self.config_custom)
                self.config.update(config_custom)
            except ValueError:
                pass

        loader = import_object(self.config['loader'])(self.config)
        preproc = import_object(self.config['preprocessor'])(self.config)

        if self.command not in ('simple', 'pydoc'):
            self.mkdocs_path = os.path.join(
                os.path.dirname(self.config_path), 'mkdocs.yml')
            self.clean_files()
            mkdocs_exist = os.path.isfile(self.mkdocs_path)
            self.copy_source_files(pages_required=not mkdocs_exist)

            if not mkdocs_exist:
                log('Generating temporary MkDocs config...')
                self.write_temp_mkdocs_config()

        # Build the index and document structure first, we load the actual
        # docstrings at a later point.
        log('Building index...')
        index = Index()

        def add_sections(doc, object_names, depth=1):
            if isinstance(object_names, list):
                [add_sections(doc, x, depth) for x in object_names]
            elif isinstance(object_names, dict):
                for key, subsections in object_names.items():
                    add_sections(doc, key, depth)
                    add_sections(doc, subsections, depth + 1)
            elif isinstance(object_names, str):
                # Check how many levels of recursion we should be going.
                expand_depth = len(object_names)
                object_names = object_names.rstrip('+')
                expand_depth -= len(object_names)

                def create_sections(name, level):
                    if level > expand_depth:
                        return
                    log("Building %s" % (name))
                    index.new_section(doc, name, depth=depth + level,
                                      header_type=self.config.get('headers', 'html'), pre_dir=self.pre_dir, post_dir=self.post_dir)
                    sort_order = self.config.get('sort')
                    if sort_order not in ('line', 'name'):
                        sort_order = 'line'
                    need_docstrings = 'docstring' in self.config.get(
                        'filter', ['docstring'])
                    for sub in dir_object(name, sort_order, need_docstrings):
                        sub = name + '.' + sub
                        sec = create_sections(sub, level + 1)

                create_sections(object_names, 0)
            else:
                raise RuntimeError(object_names)

        # Make sure that we can find modules from the current working directory,
        # and have them take precedence over installed modules.
        sys.path.insert(0, '.')

        if self.command == 'simple':
            # In simple mode, we generate a single document from the import
            # names specified on the command-line.
            doc = index.new_document('main.md')
            add_sections(doc, self.subargs)
        else:
            for pages in self.config.get('generate') or []:
                for fname, object_names in pages.items():
                    doc = index.new_document(fname)
                    add_sections(doc, object_names)

        preproc.link_lookup = {}
        for file, doc in index.documents.items():
            for section in doc.sections:
                preproc.link_lookup[section.identifier] = file
        # Load the docstrings and fill the sections.
        log('Started generating documentation...')
        for doc in index.documents.values():
            for section in filter(lambda s: s.identifier, doc.sections):
                loader.load_section(section)
                preproc.preprocess_section(section)

        if self.command == 'simple':
            for section in doc.sections:
                section.render(sys.stdout)
            return 0

        # Write out all the generated documents.
        for fname, doc in index.documents.items():
            fname = os.path.join(self.gens_dir, fname)
            self.makedirs(os.path.dirname(fname))
            with open(fname, 'w') as fp:
                log("Writing %s..." % (fname))
                for section in doc.sections:
                    section.render(fp)

        if self.command == 'generate':
            return 0

        log("Running 'mkdocs {}'".format(self.command))
        sys.stdout.flush()

        mk_args = [self.python_path, '-m', 'mkdocs',
                   self.command, '-f', self.mkdocs_path] + self.subargs
        log(' '.join(mk_args))
        try:
            return subprocess.call(mk_args)
        except KeyboardInterrupt:
            return signal.SIGINT


if __name__ == '__main__':
    pd = PyDocMk()
    pd.parse_args()
    pd.main()
