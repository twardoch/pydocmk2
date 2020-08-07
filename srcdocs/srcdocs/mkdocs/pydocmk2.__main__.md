<h1 id="pydocmk2.__main__">pydocmk2.__main__</h1>

<h2><a href="./pydocmk2.html">pydocmk2</a>.__main__</h2> <span class="file-reference">/Users/adam/Developer/vcs/github.twardoch/pub/pydocmk2/pydocmk2/__main__.py</span> <div class="module">  <div class="docstring">
<pre class="doc">python2 -m pydocmk2 build</pre>
</div>  <div class="modules"><h3>Modules</h3><ul class="list"><li><a href="./argparse.html">argparse</a></li><li><a href="./atexit.html">atexit</a></li><li><a href="./os.html">os</a></li><li><a href="./shutil.html">shutil</a></li><li><a href="./signal.html">signal</a></li><li><a href="./subprocess.html">subprocess</a></li><li><a href="./sys.html">sys</a></li><li><a href="./yaml.html">yaml</a></li></ul></div>  <div class="functions"><h3>Functions</h3><dl class="functions"><dl class="function"><dt><a name="-copy_source_files" href="#-copy_source_files"><span class="function-name">copy_source_files</span></a><span class="argspec">(config, pages_required<span class="parameter-default">=True</span>)</span></dt><dd>
<pre class="doc">Copies all files from the `docs_dir` to the `gens_dir` defined in the
*config*. It also takes the MkDocs `pages` configuration into account
and converts the special `<< INFILE` syntax by copying them to the
`gens_dir` as well.</pre>
</dd></dl>

<dl class="function"><dt><a name="-default_config" href="#-default_config"><span class="function-name">default_config</span></a><span class="argspec">(config)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>

<dl class="function"><dt><a name="-log" href="#-log"><span class="function-name">log</span></a><span class="argspec">(*args, **kwargs)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>

<dl class="function"><dt><a name="-main" href="#-main"><span class="function-name">main</span></a><span class="argspec">()</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>

<dl class="function"><dt><a name="-makedirs" href="#-makedirs"><span class="function-name">makedirs</span></a><span class="argspec">(path)</span></dt><dd>
<pre class="doc">Create the directory *path* if it does not already exist.</pre>
</dd></dl>

<dl class="function"><dt><a name="-new_project" href="#-new_project"><span class="function-name">new_project</span></a><span class="argspec">()</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>

<dl class="function"><dt><a name="-process_pages" href="#-process_pages"><span class="function-name">process_pages</span></a><span class="argspec">(data, gens_dir)</span></dt><dd>
<pre class="doc"># Also process all pages to copy files outside of the docs_dir to the gens_dir.</pre>
</dd></dl>

<dl class="function"><dt><a name="-read_config" href="#-read_config"><span class="function-name">read_config</span></a><span class="argspec">()</span></dt><dd>
<pre class="doc">Reads and preprocesses the pydocmk2 configuration file.</pre>
</dd></dl>

<dl class="function"><dt><a name="-write_temp_mkdocs_config" href="#-write_temp_mkdocs_config"><span class="function-name">write_temp_mkdocs_config</span></a><span class="argspec">(inconf)</span></dt><dd>
<pre class="doc">Generates a configuration for MkDocs on-the-fly from the pydocmk2
configuration and makes sure it gets removed when this program exists.</pre>
</dd></dl>
</dl></div></div>
<h2 id="pydocmk2.__main__.read_config">read_config</h2>

<dl class="function"><dt><a name="-pydocmk2.__main__.read_config" href="#-pydocmk2.__main__.read_config"><span class="function-name">pydocmk2.__main__.read_config</span></a> = read_config<span class="argspec">()</span></dt><dd>
<pre class="doc">Reads and preprocesses the pydocmk2 configuration file.</pre>
</dd></dl>

<h2 id="pydocmk2.__main__.write_temp_mkdocs_config">write_temp_mkdocs_config</h2>

<dl class="function"><dt><a name="-pydocmk2.__main__.write_temp_mkdocs_config" href="#-pydocmk2.__main__.write_temp_mkdocs_config"><span class="function-name">pydocmk2.__main__.write_temp_mkdocs_config</span></a> = write_temp_mkdocs_config<span class="argspec">(inconf)</span></dt><dd>
<pre class="doc">Generates a configuration for MkDocs on-the-fly from the pydocmk2
configuration and makes sure it gets removed when this program exists.</pre>
</dd></dl>

<h2 id="pydocmk2.__main__.makedirs">makedirs</h2>

<dl class="function"><dt><a name="-pydocmk2.__main__.makedirs" href="#-pydocmk2.__main__.makedirs"><span class="function-name">pydocmk2.__main__.makedirs</span></a> = makedirs<span class="argspec">(path)</span></dt><dd>
<pre class="doc">Create the directory *path* if it does not already exist.</pre>
</dd></dl>

<h2 id="pydocmk2.__main__.copy_source_files">copy_source_files</h2>

<dl class="function"><dt><a name="-pydocmk2.__main__.copy_source_files" href="#-pydocmk2.__main__.copy_source_files"><span class="function-name">pydocmk2.__main__.copy_source_files</span></a> = copy_source_files<span class="argspec">(config, pages_required<span class="parameter-default">=True</span>)</span></dt><dd>
<pre class="doc">Copies all files from the `docs_dir` to the `gens_dir` defined in the
*config*. It also takes the MkDocs `pages` configuration into account
and converts the special `<< INFILE` syntax by copying them to the
`gens_dir` as well.</pre>
</dd></dl>

