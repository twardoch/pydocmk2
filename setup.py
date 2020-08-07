
import io
import re
import setuptools
import sys

with io.open('pydocmk2/__init__.py', encoding='utf8') as fp:
    version = re.search(r"__version__\s*=\s*'(.*)'", fp.read()).group(1)

with io.open('README.md', encoding='utf8') as fp:
    long_description = fp.read()

requirements = ['mkdocs-material==4.6.0', 'MkDocs==1.0.4', 'Markdown>=3.1,<3.2',
                'PyYAML>=3.12', 'six>=0.11.0', 'yapf>=0.26.0', 'pymdown-extensions>=6.2,<6.3']

setuptools.setup(
    name='pydocmk2',
    version=version,
    author='Adam Twardoch',
    author_email='adam+github@twardoch.com',
    description='Create Python API documentation in Markdown format',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/twardoch/pydocmk2',
    license='MIT + PSF2',
    packages=setuptools.find_packages(
        '.', ['test', 'test.*', 'docs', 'docs.*']),
    package_dir={'': '.'},
    include_package_data=False,
    install_requires=requirements,
    extras_require={},
    tests_require=[],
    python_requires='>=2.7',
    data_files=[],
    entry_points={
        'console_scripts': [
            'pydocmk2=pydocmk2.__main__:main',
        ]
    },
    cmdclass={},
    keywords=['markdown', 'pydoc', 'generator', 'docs', 'documentation'],
    classifiers=['Development Status :: 3 - Alpha', 'Intended Audience :: Developers', 'Intended Audience :: End Users/Desktop', 'Topic :: Software Development :: Code Generators', 'Topic :: Utilities', 'License :: OSI Approved :: MIT License',
                 'Programming Language :: Python :: 2', 'Programming Language :: Python :: 2.7'],
)
