<h1 id="pydocmk2.__main__">pydocmk2.__main__</h1>



 This is used by the command-line interface. 


<h2><a href="./pydocmk2.html">pydocmk2</a>.__main__</h2> <div class="module">  <div class="docstring">
<pre class="doc">python2 -m pydocmk2 build</pre>
</div>  <div class="modules"><h3>Modules</h3><ul class="list"><li>argparse</li><li>atexit</li><li>json</li><li>os</li><li>shutil</li><li>signal</li><li>subprocess</li><li>sys</li><li>yaml</li></ul></div>  <div class="classes"><h3>Classes</h3><ul class="tree"><li><span class="class-name"><a href="./__builtin__.html#object">__builtin__.object</a></span></li><li><ul class="tree"><li><span class="class-name"><a href="./pydocmk2.__main__.html#PyDocMk">PyDocMk</a></span></li></ul></li></ul><dl class="classes"><dt class="class"><h2><a name="PyDocMk" href="#PyDocMk">class <span class="class-name">PyDocMk</span></a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>

<pre class="doc"></pre>

</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="PyDocMk-__init__" href="#PyDocMk-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>
<dl class="function"><dt><a name="PyDocMk-clean_files" href="#PyDocMk-clean_files"><span class="function-name">clean_files</span></a><span class="argspec">(self)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>
<dl class="function"><dt><a name="PyDocMk-copy_source_files" href="#PyDocMk-copy_source_files"><span class="function-name">copy_source_files</span></a><span class="argspec">(self, pages_required<span class="parameter-default">=True</span>)</span></dt><dd>
<pre class="doc">Copies all files from the `docs_dir` to the `gens_dir` defined in the
*config*. It also takes the MkDocs `pages` configuration into account
and converts the special `<< INFILE` syntax by copying them to the
`gens_dir` as well.</pre>
</dd></dl>
<dl class="function"><dt><a name="PyDocMk-default_config" href="#PyDocMk-default_config"><span class="function-name">default_config</span></a><span class="argspec">(self, blank<span class="parameter-default">=False</span>)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>
<dl class="function"><dt><a name="PyDocMk-main" href="#PyDocMk-main"><span class="function-name">main</span></a><span class="argspec">(self)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>
<dl class="function"><dt><a name="PyDocMk-makedirs" href="#PyDocMk-makedirs"><span class="function-name">makedirs</span></a><span class="argspec">(self, path)</span></dt><dd>
<pre class="doc">Create the directory *path* if it does not already exist.</pre>
</dd></dl>
<dl class="function"><dt><a name="PyDocMk-new_project" href="#PyDocMk-new_project"><span class="function-name">new_project</span></a><span class="argspec">(self)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>
<dl class="function"><dt><a name="PyDocMk-parse_args" href="#PyDocMk-parse_args"><span class="function-name">parse_args</span></a><span class="argspec">(self)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>
<dl class="function"><dt><a name="PyDocMk-process_pages" href="#PyDocMk-process_pages"><span class="function-name">process_pages</span></a><span class="argspec">(self, data, gens_dir)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>
<dl class="function"><dt><a name="PyDocMk-read_config" href="#PyDocMk-read_config"><span class="function-name">read_config</span></a><span class="argspec">(self)</span></dt><dd>
<pre class="doc">Reads and preprocesses the pydocmk2 configuration file.</pre>
</dd></dl>
<dl class="function"><dt><a name="PyDocMk-write_temp_mkdocs_config" href="#PyDocMk-write_temp_mkdocs_config"><span class="function-name">write_temp_mkdocs_config</span></a><span class="argspec">(self)</span></dt><dd>
<pre class="doc">Generates a configuration for MkDocs on-the-fly from the pydocmk2
configuration and makes sure it gets removed when this program exists.</pre>
</dd></dl>

  <h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>__dict__</dt>
<dd>
<pre class="doc">dictionary for instance variables (if defined)</pre>
</dd>
</dl>
<dl class="descriptor"><dt>__weakref__</dt>
<dd>
<pre class="doc">list of weak references to the object (if defined)</pre>
</dd>
</dl>
</dd></dl></div>  <div class="functions"><h3>Functions</h3><dl class="functions"><dl class="function"><dt><a name="-log" href="#-log"><span class="function-name">log</span></a><span class="argspec">(*args, **kwargs)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>
</dl></div></div>
<h2 id="pydocmk2.__main__.PyDocMk">PyDocMk</h2>

<dt class="class"><h2><span class="class-name">pydocmk2.__main__.PyDocMk</span> = <a name="pydocmk2.__main__.PyDocMk" href="#pydocmk2.__main__.PyDocMk">class PyDocMk</a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>

<pre class="doc"></pre>

</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="PyDocMk-__init__" href="#PyDocMk-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>
<dl class="function"><dt><a name="PyDocMk-clean_files" href="#PyDocMk-clean_files"><span class="function-name">clean_files</span></a><span class="argspec">(self)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>
<dl class="function"><dt><a name="PyDocMk-copy_source_files" href="#PyDocMk-copy_source_files"><span class="function-name">copy_source_files</span></a><span class="argspec">(self, pages_required<span class="parameter-default">=True</span>)</span></dt><dd>
<pre class="doc">Copies all files from the `docs_dir` to the `gens_dir` defined in the
*config*. It also takes the MkDocs `pages` configuration into account
and converts the special `<< INFILE` syntax by copying them to the
`gens_dir` as well.</pre>
</dd></dl>
<dl class="function"><dt><a name="PyDocMk-default_config" href="#PyDocMk-default_config"><span class="function-name">default_config</span></a><span class="argspec">(self, blank<span class="parameter-default">=False</span>)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>
<dl class="function"><dt><a name="PyDocMk-main" href="#PyDocMk-main"><span class="function-name">main</span></a><span class="argspec">(self)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>
<dl class="function"><dt><a name="PyDocMk-makedirs" href="#PyDocMk-makedirs"><span class="function-name">makedirs</span></a><span class="argspec">(self, path)</span></dt><dd>
<pre class="doc">Create the directory *path* if it does not already exist.</pre>
</dd></dl>
<dl class="function"><dt><a name="PyDocMk-new_project" href="#PyDocMk-new_project"><span class="function-name">new_project</span></a><span class="argspec">(self)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>
<dl class="function"><dt><a name="PyDocMk-parse_args" href="#PyDocMk-parse_args"><span class="function-name">parse_args</span></a><span class="argspec">(self)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>
<dl class="function"><dt><a name="PyDocMk-process_pages" href="#PyDocMk-process_pages"><span class="function-name">process_pages</span></a><span class="argspec">(self, data, gens_dir)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>
<dl class="function"><dt><a name="PyDocMk-read_config" href="#PyDocMk-read_config"><span class="function-name">read_config</span></a><span class="argspec">(self)</span></dt><dd>
<pre class="doc">Reads and preprocesses the pydocmk2 configuration file.</pre>
</dd></dl>
<dl class="function"><dt><a name="PyDocMk-write_temp_mkdocs_config" href="#PyDocMk-write_temp_mkdocs_config"><span class="function-name">write_temp_mkdocs_config</span></a><span class="argspec">(self)</span></dt><dd>
<pre class="doc">Generates a configuration for MkDocs on-the-fly from the pydocmk2
configuration and makes sure it gets removed when this program exists.</pre>
</dd></dl>

  <h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>__dict__</dt>
<dd>
<pre class="doc">dictionary for instance variables (if defined)</pre>
</dd>
</dl>
<dl class="descriptor"><dt>__weakref__</dt>
<dd>
<pre class="doc">list of weak references to the object (if defined)</pre>
</dd>
</dl>
</dd>
<h3 id="pydocmk2.__main__.PyDocMk.read_config">read_config</h3>

<dl class="function"><dt><a name="-pydocmk2.__main__.PyDocMk.read_config" href="#-pydocmk2.__main__.PyDocMk.read_config"><span class="function-name">pydocmk2.__main__.PyDocMk.read_config</span></a> = read_config<span class="argspec">(self)</span><span class="note"> unbound <a href="./pydocmk2.__main__.html#PyDocMk">pydocmk2.__main__.PyDocMk</a> method</span></dt><dd>
<pre class="doc">Reads and preprocesses the pydocmk2 configuration file.</pre>
</dd></dl>

<h3 id="pydocmk2.__main__.PyDocMk.write_temp_mkdocs_config">write_temp_mkdocs_config</h3>

<dl class="function"><dt><a name="-pydocmk2.__main__.PyDocMk.write_temp_mkdocs_config" href="#-pydocmk2.__main__.PyDocMk.write_temp_mkdocs_config"><span class="function-name">pydocmk2.__main__.PyDocMk.write_temp_mkdocs_config</span></a> = write_temp_mkdocs_config<span class="argspec">(self)</span><span class="note"> unbound <a href="./pydocmk2.__main__.html#PyDocMk">pydocmk2.__main__.PyDocMk</a> method</span></dt><dd>
<pre class="doc">Generates a configuration for MkDocs on-the-fly from the pydocmk2
configuration and makes sure it gets removed when this program exists.</pre>
</dd></dl>

<h3 id="pydocmk2.__main__.PyDocMk.makedirs">makedirs</h3>

<dl class="function"><dt><a name="-pydocmk2.__main__.PyDocMk.makedirs" href="#-pydocmk2.__main__.PyDocMk.makedirs"><span class="function-name">pydocmk2.__main__.PyDocMk.makedirs</span></a> = makedirs<span class="argspec">(self, path)</span><span class="note"> unbound <a href="./pydocmk2.__main__.html#PyDocMk">pydocmk2.__main__.PyDocMk</a> method</span></dt><dd>
<pre class="doc">Create the directory *path* if it does not already exist.</pre>
</dd></dl>

<h3 id="pydocmk2.__main__.PyDocMk.copy_source_files">copy_source_files</h3>

<dl class="function"><dt><a name="-pydocmk2.__main__.PyDocMk.copy_source_files" href="#-pydocmk2.__main__.PyDocMk.copy_source_files"><span class="function-name">pydocmk2.__main__.PyDocMk.copy_source_files</span></a> = copy_source_files<span class="argspec">(self, pages_required<span class="parameter-default">=True</span>)</span><span class="note"> unbound <a href="./pydocmk2.__main__.html#PyDocMk">pydocmk2.__main__.PyDocMk</a> method</span></dt><dd>
<pre class="doc">Copies all files from the `docs_dir` to the `gens_dir` defined in the
*config*. It also takes the MkDocs `pages` configuration into account
and converts the special `<< INFILE` syntax by copying them to the
`gens_dir` as well.</pre>
</dd></dl>

