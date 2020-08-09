<h1 id="pydocmk2.preprocessors.pydocmk">pydocmk2.preprocessors.pydocmk</h1>

<h2><a href="./pydocmk2.html">pydocmk2</a>.<a href="./pydocmk2.preprocessors.html">preprocessors</a>.pydocmk</h2> <div class="module">  <div class="docstring">
<pre class="doc">pydocproc preprocessor</pre>
</div>  <div class="modules"><h3>Modules</h3><ul class="list"><li><a href="./__builtin__.html">__builtin__</a></li><li><a href="./codecs.html">codecs</a></li><li><a href="./collections.html">collections</a></li><li><a href="./inspect.html">inspect</a></li><li><a href="./jinja2.html">jinja2</a></li><li><a href="./os.html">os</a></li><li><a href="./pkgutil.html">pkgutil</a></li><li><a href="./pydoc.html">pydoc</a></li><li><a href="./re.html">re</a></li><li><a href="./string.html">string</a></li><li><a href="./sys.html">sys</a></li></ul></div>  <div class="classes"><h3>Classes</h3><ul class="tree"><li><span class="class-name"><a href="./__builtin__.html#object">__builtin__.object</a></span></li><li><ul class="tree"><li><span class="class-name"><a href="./pydocmk2.preprocessors.pydocmk.html#MarkdownDoc">MarkdownDoc</a></span>(<span class="bases">pydoc.HTMLDoc, __builtin__.object</span>)</li><li><span class="class-name"><a href="./pydocmk2.preprocessors.pydocmk.html#MarkdownRepr">MarkdownRepr</a></span>(<span class="bases">pydoc.TextRepr, __builtin__.object</span>)</li><li><span class="class-name"><a href="./pydocmk2.preprocessors.pydocmk.html#Preprocessor">Preprocessor</a></span></li></ul></li><li><span class="class-name"><a href="./pydoc.html#HTMLDoc">pydoc.HTMLDoc</a></span>(<span class="bases">pydoc.Doc</span>)</li><li><ul class="tree"><li><span class="class-name"><a href="./pydocmk2.preprocessors.pydocmk.html#MarkdownDoc">MarkdownDoc</a></span>(<span class="bases">pydoc.HTMLDoc, __builtin__.object</span>)</li></ul></li><li><span class="class-name"><a href="./pydoc.html#TextRepr">pydoc.TextRepr</a></span>(<span class="bases">repr.Repr</span>)</li><li><ul class="tree"><li><span class="class-name"><a href="./pydocmk2.preprocessors.pydocmk.html#MarkdownRepr">MarkdownRepr</a></span>(<span class="bases">pydoc.TextRepr, __builtin__.object</span>)</li></ul></li></ul><dl class="classes"><dt class="class"><h2><a name="MarkdownDoc" href="#MarkdownDoc">class <span class="class-name">MarkdownDoc</span></a>(<a href="./pydoc.html#HTMLDoc">pydoc.HTMLDoc</a>, <a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>

<pre class="doc">FIXME: doc* functions need an extra "level" parameter so we can the fitting h[1-6]
This required overriding the 'document' function, but can only be done once all doc*
functions are implemented.</pre>

</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./pydocmk2.preprocessors.pydocmk.html#MarkdownDoc">MarkdownDoc</a></dd><dd><a href="./pydoc.html#HTMLDoc">pydoc.HTMLDoc</a></dd><dd><a href="./pydoc.html#Doc">pydoc.Doc</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="MarkdownDoc-__init__" href="#MarkdownDoc-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, level_offset<span class="parameter-default">=0</span>, local<span class="parameter-default">=False</span>, index_url<span class="parameter-default">='./'</span>)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownDoc-classlink" href="#MarkdownDoc-classlink"><span class="function-name">classlink</span></a><span class="argspec">(self, object, modname)</span></dt><dd>
<pre class="doc">Make a link for a class.</pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownDoc-docclass" href="#MarkdownDoc-docclass"><span class="function-name">docclass</span></a><span class="argspec">(self, object, name<span class="parameter-default">=None</span>, mod<span class="parameter-default">=None</span>, funcs<span class="parameter-default">={}</span>, classes<span class="parameter-default">={}</span>, *ignored)</span></dt><dd>
<pre class="doc">Produce HTML documentation for a class <a href="./__builtin__.html#object">object</a>.</pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownDoc-docdata" href="#MarkdownDoc-docdata"><span class="function-name">docdata</span></a><span class="argspec">(self, object, name<span class="parameter-default">=None</span>, mod<span class="parameter-default">=None</span>, cl<span class="parameter-default">=None</span>)</span></dt><dd>
<pre class="doc">Produce html documentation for a data descriptor.</pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownDoc-docmodule" href="#MarkdownDoc-docmodule"><span class="function-name">docmodule</span></a><span class="argspec">(self, object, name<span class="parameter-default">=None</span>, mod<span class="parameter-default">=None</span>, *ignored)</span></dt><dd>
<pre class="doc">Produce HTML5 documentation for a module <a href="./__builtin__.html#object">object</a>.</pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownDoc-docother" href="#MarkdownDoc-docother"><span class="function-name">docother</span></a><span class="argspec">(self, object, name<span class="parameter-default">=None</span>, mod<span class="parameter-default">=None</span>, *ignored)</span></dt><dd>
<pre class="doc">Produce HTML documentation for a data <a href="./__builtin__.html#object">object</a>.</pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownDoc-docproperty" href="#MarkdownDoc-docproperty"><span class="function-name">docproperty</span></a><span class="argspec">(self, object, name<span class="parameter-default">=None</span>, mod<span class="parameter-default">=None</span>, cl<span class="parameter-default">=None</span>)</span></dt><dd>
<pre class="doc">Produce html documentation for a property.</pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownDoc-docroutine" href="#MarkdownDoc-docroutine"><span class="function-name">docroutine</span></a><span class="argspec">(self, object, name<span class="parameter-default">=None</span>, mod<span class="parameter-default">=None</span>, funcs<span class="parameter-default">={}</span>, classes<span class="parameter-default">={}</span>, methods<span class="parameter-default">={}</span>, cl<span class="parameter-default">=None</span>)</span></dt><dd>
<pre class="doc">Produce HTML documentation for a function or method <a href="./__builtin__.html#object">object</a>.</pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownDoc-formattree" href="#MarkdownDoc-formattree"><span class="function-name">formattree</span></a><span class="argspec">(self, tree, modname, parent<span class="parameter-default">=None</span>)</span></dt><dd>
<pre class="doc">Render in text a class tree as returned by inspect.getclasstree().</pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownDoc-formatvalue" href="#MarkdownDoc-formatvalue"><span class="function-name">formatvalue</span></a><span class="argspec">(self, object)</span></dt><dd>
<pre class="doc">Format an argument default value as text.</pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownDoc-getdoc" href="#MarkdownDoc-getdoc"><span class="function-name">getdoc</span></a><span class="argspec">(self, object)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownDoc-heading" href="#MarkdownDoc-heading"><span class="function-name">heading</span></a><span class="argspec">(self, level, content)</span></dt><dd>
<pre class="doc">Create a HTML heading</pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownDoc-listing" href="#MarkdownDoc-listing"><span class="function-name">listing</span></a><span class="argspec">(self, items, formatter<span class="parameter-default">=None</span>)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownDoc-markup" href="#MarkdownDoc-markup"><span class="function-name">markup</span></a><span class="argspec">(self, text, escape<span class="parameter-default">=None</span>, funcs<span class="parameter-default">={}</span>, classes<span class="parameter-default">={}</span>, methods<span class="parameter-default">={}</span>)</span></dt><dd>
<pre class="doc">Mark up some plain text, given a context of symbols to look for.
Each context dictionary maps <a href="./__builtin__.html#object">object</a> names to anchor names.

i.e. Replaces plaintext URLs with linked versions
Also escapes input text</pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownDoc-modpkglink" href="#MarkdownDoc-modpkglink"><span class="function-name">modpkglink</span></a><span class="argspec">(self, data)</span></dt><dd>
<pre class="doc">Make a link for a module or package to display in an index.</pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownDoc-modulelink" href="#MarkdownDoc-modulelink"><span class="function-name">modulelink</span></a><span class="argspec">(self, object)</span></dt><dd>
<pre class="doc">Make a link for a module.</pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownDoc-preformat" href="#MarkdownDoc-preformat"><span class="function-name">preformat</span></a><span class="argspec">(self, text)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownDoc-url" href="#MarkdownDoc-url"><span class="function-name">url</span></a><span class="argspec">(self, name)</span></dt><dd>
<pre class="doc">Create URL for a documentable thing. Mainly intended for subclassing</pre>
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

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">index_url</span> = None</dt></dl>
<dl><dt><span class="other-name">level_offset</span> = None</dt></dl>
<dl><dt><span class="other-name">local</span> = None</dt></dl>

  <h4 class="head-methods">Methods from <a href="./pydoc.html#HTMLDoc">pydoc.HTMLDoc</a></h4><dl class="function"><dt><a name="MarkdownDoc-bigsection" href="#MarkdownDoc-bigsection"><span class="function-name">bigsection</span></a><span class="argspec">(self, title, *args)</span></dt><dd>
<pre class="doc">Format a section with a big heading.</pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownDoc-escape" href="#MarkdownDoc-escape"><span class="function-name">escape</span></a><span class="argspec">(self, text)</span><span class="note"> from <a href="./pydoc.html#HTMLRepr">pydoc.HTMLRepr</a></span></dt><dd>
<pre class="doc"></pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownDoc-grey" href="#MarkdownDoc-grey"><span class="function-name">grey</span></a><span class="argspec">(self, text)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownDoc-index" href="#MarkdownDoc-index"><span class="function-name">index</span></a><span class="argspec">(self, dir, shadowed<span class="parameter-default">=None</span>)</span></dt><dd>
<pre class="doc">Generate an HTML index for a directory of modules.</pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownDoc-multicolumn" href="#MarkdownDoc-multicolumn"><span class="function-name">multicolumn</span></a><span class="argspec">(self, list, format, cols<span class="parameter-default">=4</span>)</span></dt><dd>
<pre class="doc">Format a list of items into a multi-column list.</pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownDoc-namelink" href="#MarkdownDoc-namelink"><span class="function-name">namelink</span></a><span class="argspec">(self, name, *dicts)</span></dt><dd>
<pre class="doc">Make a link for an identifier, given name-to-URL mappings.</pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownDoc-page" href="#MarkdownDoc-page"><span class="function-name">page</span></a><span class="argspec">(self, title, contents)</span></dt><dd>
<pre class="doc">Format an HTML page.</pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownDoc-repr" href="#MarkdownDoc-repr"><span class="function-name">repr</span></a><span class="argspec">(self, object)</span><span class="note"> from <a href="./pydoc.html#HTMLRepr">pydoc.HTMLRepr</a></span></dt><dd>
<pre class="doc"></pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownDoc-section" href="#MarkdownDoc-section"><span class="function-name">section</span></a><span class="argspec">(self, title, fgcol, bgcol, contents, width<span class="parameter-default">=6</span>, prelude<span class="parameter-default">=''</span>, marginalia<span class="parameter-default">=None</span>, gap<span class="parameter-default">='&amp;nbsp;'</span>)</span></dt><dd>
<pre class="doc">Format a section with a heading.</pre>
</dd></dl>

  <h4 class="head-methods">Methods from <a href="./pydoc.html#Doc">pydoc.Doc</a></h4><dl class="function"><dt><a name="MarkdownDoc-document" href="#MarkdownDoc-document"><span class="function-name">document</span></a><span class="argspec">(self, object, name<span class="parameter-default">=None</span>, *args)</span></dt><dd>
<pre class="doc">Generate documentation for an <a href="./__builtin__.html#object">object</a>.</pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownDoc-fail" href="#MarkdownDoc-fail"><span class="function-name">fail</span></a><span class="argspec">(self, object, name<span class="parameter-default">=None</span>, *args)</span></dt><dd>
<pre class="doc">Raise an exception for unimplemented types.</pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownDoc-getdocloc" href="#MarkdownDoc-getdocloc"><span class="function-name">getdocloc</span></a><span class="argspec">(self, object, basedir<span class="parameter-default">='/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7'</span>)</span></dt><dd>
<pre class="doc">Return the location of module docs or None</pre>
</dd></dl>
</dd>
<dt class="class"><h2><a name="MarkdownRepr" href="#MarkdownRepr">class <span class="class-name">MarkdownRepr</span></a>(<a href="./pydoc.html#TextRepr">pydoc.TextRepr</a>, <a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>

<pre class="doc"></pre>

</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./pydocmk2.preprocessors.pydocmk.html#MarkdownRepr">MarkdownRepr</a></dd><dd><a href="./pydoc.html#TextRepr">pydoc.TextRepr</a></dd><dd><a href="./repr.html#Repr">repr.Repr</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="MarkdownRepr-repr1" href="#MarkdownRepr-repr1"><span class="function-name">repr1</span></a><span class="argspec">(self, x, level)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownRepr-repr_string" href="#MarkdownRepr-repr_string"><span class="function-name">repr_string</span></a><span class="argspec">(self, x, level)</span></dt><dd>
<pre class="doc"></pre>
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

  <h4 class="head-methods">Methods from <a href="./pydoc.html#TextRepr">pydoc.TextRepr</a></h4><dl class="function"><dt><a name="MarkdownRepr-__init__" href="#MarkdownRepr-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownRepr-repr_instance" href="#MarkdownRepr-repr_instance"><span class="function-name">repr_instance</span></a><span class="argspec">(self, x, level)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownRepr-repr_str" href="#MarkdownRepr-repr_str"><span class="function-name">repr_str</span></a> = repr_string<span class="argspec">(self, x, level)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>

  <h4 class="head-methods">Methods from <a href="./repr.html#Repr">repr.Repr</a></h4><dl class="function"><dt><a name="MarkdownRepr-repr" href="#MarkdownRepr-repr"><span class="function-name">repr</span></a><span class="argspec">(self, x)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownRepr-repr_array" href="#MarkdownRepr-repr_array"><span class="function-name">repr_array</span></a><span class="argspec">(self, x, level)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownRepr-repr_deque" href="#MarkdownRepr-repr_deque"><span class="function-name">repr_deque</span></a><span class="argspec">(self, x, level)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownRepr-repr_dict" href="#MarkdownRepr-repr_dict"><span class="function-name">repr_dict</span></a><span class="argspec">(self, x, level)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownRepr-repr_frozenset" href="#MarkdownRepr-repr_frozenset"><span class="function-name">repr_frozenset</span></a><span class="argspec">(self, x, level)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownRepr-repr_list" href="#MarkdownRepr-repr_list"><span class="function-name">repr_list</span></a><span class="argspec">(self, x, level)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownRepr-repr_long" href="#MarkdownRepr-repr_long"><span class="function-name">repr_long</span></a><span class="argspec">(self, x, level)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownRepr-repr_set" href="#MarkdownRepr-repr_set"><span class="function-name">repr_set</span></a><span class="argspec">(self, x, level)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownRepr-repr_tuple" href="#MarkdownRepr-repr_tuple"><span class="function-name">repr_tuple</span></a><span class="argspec">(self, x, level)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>
</dd>
<dt class="class"><h2><a name="Preprocessor" href="#Preprocessor">class <span class="class-name">Preprocessor</span></a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>

<pre class="doc">This class implements the basic preprocessing.</pre>

</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="Preprocessor-__init__" href="#Preprocessor-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, config)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>
<dl class="function"><dt><a name="Preprocessor-preprocess_section" href="#Preprocessor-preprocess_section"><span class="function-name">preprocess_section</span></a><span class="argspec">(self, section)</span></dt><dd>
<pre class="doc">Preprocess the contents of *section*.</pre>
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
</dd></dl></div>  <div class="functions"><h3>Functions</h3><dl class="functions"><dl class="function"><dt><a name="-clean" href="#-clean"><span class="function-name">clean</span></a><span class="argspec">(text)</span></dt><dd>
<pre class="doc">mainly for cleaning < and > from `Repr`s</pre>
</dd></dl>

<dl class="function"><dt><a name="-doc" href="#-doc"><span class="function-name">doc</span></a><span class="argspec">(name)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>
</dl></div></div>
<h2 id="pydocmk2.preprocessors.pydocmk.clean">clean</h2>

<dl class="function"><dt><a name="-pydocmk2.preprocessors.pydocmk.clean" href="#-pydocmk2.preprocessors.pydocmk.clean"><span class="function-name">pydocmk2.preprocessors.pydocmk.clean</span></a> = clean<span class="argspec">(text)</span></dt><dd>
<pre class="doc">mainly for cleaning < and > from `Repr`s</pre>
</dd></dl>

<h2 id="pydocmk2.preprocessors.pydocmk.MarkdownDoc">MarkdownDoc</h2>

<dt class="class"><h2><span class="class-name">pydocmk2.preprocessors.pydocmk.MarkdownDoc</span> = <a name="pydocmk2.preprocessors.pydocmk.MarkdownDoc" href="#pydocmk2.preprocessors.pydocmk.MarkdownDoc">class MarkdownDoc</a>(<a href="./pydoc.html#HTMLDoc">pydoc.HTMLDoc</a>, <a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>

<pre class="doc">FIXME: doc* functions need an extra "level" parameter so we can the fitting h[1-6]
This required overriding the 'document' function, but can only be done once all doc*
functions are implemented.</pre>

</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./pydocmk2.preprocessors.pydocmk.html#MarkdownDoc">MarkdownDoc</a></dd><dd><a href="./pydoc.html#HTMLDoc">pydoc.HTMLDoc</a></dd><dd><a href="./pydoc.html#Doc">pydoc.Doc</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="MarkdownDoc-__init__" href="#MarkdownDoc-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, level_offset<span class="parameter-default">=0</span>, local<span class="parameter-default">=False</span>, index_url<span class="parameter-default">='./'</span>)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownDoc-classlink" href="#MarkdownDoc-classlink"><span class="function-name">classlink</span></a><span class="argspec">(self, object, modname)</span></dt><dd>
<pre class="doc">Make a link for a class.</pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownDoc-docclass" href="#MarkdownDoc-docclass"><span class="function-name">docclass</span></a><span class="argspec">(self, object, name<span class="parameter-default">=None</span>, mod<span class="parameter-default">=None</span>, funcs<span class="parameter-default">={}</span>, classes<span class="parameter-default">={}</span>, *ignored)</span></dt><dd>
<pre class="doc">Produce HTML documentation for a class object.</pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownDoc-docdata" href="#MarkdownDoc-docdata"><span class="function-name">docdata</span></a><span class="argspec">(self, object, name<span class="parameter-default">=None</span>, mod<span class="parameter-default">=None</span>, cl<span class="parameter-default">=None</span>)</span></dt><dd>
<pre class="doc">Produce html documentation for a data descriptor.</pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownDoc-docmodule" href="#MarkdownDoc-docmodule"><span class="function-name">docmodule</span></a><span class="argspec">(self, object, name<span class="parameter-default">=None</span>, mod<span class="parameter-default">=None</span>, *ignored)</span></dt><dd>
<pre class="doc">Produce HTML5 documentation for a module object.</pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownDoc-docother" href="#MarkdownDoc-docother"><span class="function-name">docother</span></a><span class="argspec">(self, object, name<span class="parameter-default">=None</span>, mod<span class="parameter-default">=None</span>, *ignored)</span></dt><dd>
<pre class="doc">Produce HTML documentation for a data object.</pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownDoc-docproperty" href="#MarkdownDoc-docproperty"><span class="function-name">docproperty</span></a><span class="argspec">(self, object, name<span class="parameter-default">=None</span>, mod<span class="parameter-default">=None</span>, cl<span class="parameter-default">=None</span>)</span></dt><dd>
<pre class="doc">Produce html documentation for a property.</pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownDoc-docroutine" href="#MarkdownDoc-docroutine"><span class="function-name">docroutine</span></a><span class="argspec">(self, object, name<span class="parameter-default">=None</span>, mod<span class="parameter-default">=None</span>, funcs<span class="parameter-default">={}</span>, classes<span class="parameter-default">={}</span>, methods<span class="parameter-default">={}</span>, cl<span class="parameter-default">=None</span>)</span></dt><dd>
<pre class="doc">Produce HTML documentation for a function or method object.</pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownDoc-formattree" href="#MarkdownDoc-formattree"><span class="function-name">formattree</span></a><span class="argspec">(self, tree, modname, parent<span class="parameter-default">=None</span>)</span></dt><dd>
<pre class="doc">Render in text a class tree as returned by inspect.getclasstree().</pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownDoc-formatvalue" href="#MarkdownDoc-formatvalue"><span class="function-name">formatvalue</span></a><span class="argspec">(self, object)</span></dt><dd>
<pre class="doc">Format an argument default value as text.</pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownDoc-getdoc" href="#MarkdownDoc-getdoc"><span class="function-name">getdoc</span></a><span class="argspec">(self, object)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownDoc-heading" href="#MarkdownDoc-heading"><span class="function-name">heading</span></a><span class="argspec">(self, level, content)</span></dt><dd>
<pre class="doc">Create a HTML heading</pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownDoc-listing" href="#MarkdownDoc-listing"><span class="function-name">listing</span></a><span class="argspec">(self, items, formatter<span class="parameter-default">=None</span>)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownDoc-markup" href="#MarkdownDoc-markup"><span class="function-name">markup</span></a><span class="argspec">(self, text, escape<span class="parameter-default">=None</span>, funcs<span class="parameter-default">={}</span>, classes<span class="parameter-default">={}</span>, methods<span class="parameter-default">={}</span>)</span></dt><dd>
<pre class="doc">Mark up some plain text, given a context of symbols to look for.
Each context dictionary maps object names to anchor names.

i.e. Replaces plaintext URLs with linked versions
Also escapes input text</pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownDoc-modpkglink" href="#MarkdownDoc-modpkglink"><span class="function-name">modpkglink</span></a><span class="argspec">(self, data)</span></dt><dd>
<pre class="doc">Make a link for a module or package to display in an index.</pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownDoc-modulelink" href="#MarkdownDoc-modulelink"><span class="function-name">modulelink</span></a><span class="argspec">(self, object)</span></dt><dd>
<pre class="doc">Make a link for a module.</pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownDoc-preformat" href="#MarkdownDoc-preformat"><span class="function-name">preformat</span></a><span class="argspec">(self, text)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownDoc-url" href="#MarkdownDoc-url"><span class="function-name">url</span></a><span class="argspec">(self, name)</span></dt><dd>
<pre class="doc">Create URL for a documentable thing. Mainly intended for subclassing</pre>
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

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">index_url</span> = None</dt></dl>
<dl><dt><span class="other-name">level_offset</span> = None</dt></dl>
<dl><dt><span class="other-name">local</span> = None</dt></dl>

  <h4 class="head-methods">Methods from <a href="./pydoc.html#HTMLDoc">pydoc.HTMLDoc</a></h4><dl class="function"><dt><a name="MarkdownDoc-bigsection" href="#MarkdownDoc-bigsection"><span class="function-name">bigsection</span></a><span class="argspec">(self, title, *args)</span></dt><dd>
<pre class="doc">Format a section with a big heading.</pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownDoc-escape" href="#MarkdownDoc-escape"><span class="function-name">escape</span></a><span class="argspec">(self, text)</span><span class="note"> from <a href="./pydoc.html#HTMLRepr">pydoc.HTMLRepr</a></span></dt><dd>
<pre class="doc"></pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownDoc-grey" href="#MarkdownDoc-grey"><span class="function-name">grey</span></a><span class="argspec">(self, text)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownDoc-index" href="#MarkdownDoc-index"><span class="function-name">index</span></a><span class="argspec">(self, dir, shadowed<span class="parameter-default">=None</span>)</span></dt><dd>
<pre class="doc">Generate an HTML index for a directory of modules.</pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownDoc-multicolumn" href="#MarkdownDoc-multicolumn"><span class="function-name">multicolumn</span></a><span class="argspec">(self, list, format, cols<span class="parameter-default">=4</span>)</span></dt><dd>
<pre class="doc">Format a list of items into a multi-column list.</pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownDoc-namelink" href="#MarkdownDoc-namelink"><span class="function-name">namelink</span></a><span class="argspec">(self, name, *dicts)</span></dt><dd>
<pre class="doc">Make a link for an identifier, given name-to-URL mappings.</pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownDoc-page" href="#MarkdownDoc-page"><span class="function-name">page</span></a><span class="argspec">(self, title, contents)</span></dt><dd>
<pre class="doc">Format an HTML page.</pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownDoc-repr" href="#MarkdownDoc-repr"><span class="function-name">repr</span></a><span class="argspec">(self, object)</span><span class="note"> from <a href="./pydoc.html#HTMLRepr">pydoc.HTMLRepr</a></span></dt><dd>
<pre class="doc"></pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownDoc-section" href="#MarkdownDoc-section"><span class="function-name">section</span></a><span class="argspec">(self, title, fgcol, bgcol, contents, width<span class="parameter-default">=6</span>, prelude<span class="parameter-default">=''</span>, marginalia<span class="parameter-default">=None</span>, gap<span class="parameter-default">='&amp;nbsp;'</span>)</span></dt><dd>
<pre class="doc">Format a section with a heading.</pre>
</dd></dl>

  <h4 class="head-methods">Methods from <a href="./pydoc.html#Doc">pydoc.Doc</a></h4><dl class="function"><dt><a name="MarkdownDoc-document" href="#MarkdownDoc-document"><span class="function-name">document</span></a><span class="argspec">(self, object, name<span class="parameter-default">=None</span>, *args)</span></dt><dd>
<pre class="doc">Generate documentation for an object.</pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownDoc-fail" href="#MarkdownDoc-fail"><span class="function-name">fail</span></a><span class="argspec">(self, object, name<span class="parameter-default">=None</span>, *args)</span></dt><dd>
<pre class="doc">Raise an exception for unimplemented types.</pre>
</dd></dl>
<dl class="function"><dt><a name="MarkdownDoc-getdocloc" href="#MarkdownDoc-getdocloc"><span class="function-name">getdocloc</span></a><span class="argspec">(self, object, basedir<span class="parameter-default">='/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7'</span>)</span></dt><dd>
<pre class="doc">Return the location of module docs or None</pre>
</dd></dl>
</dd>
<h3 id="pydocmk2.preprocessors.pydocmk.MarkdownDoc.heading">heading</h3>

<dl class="function"><dt><a name="-pydocmk2.preprocessors.pydocmk.MarkdownDoc.heading" href="#-pydocmk2.preprocessors.pydocmk.MarkdownDoc.heading"><span class="function-name">pydocmk2.preprocessors.pydocmk.MarkdownDoc.heading</span></a> = heading<span class="argspec">(self, level, content)</span><span class="note"> unbound <a href="./pydocmk2.preprocessors.pydocmk.html#MarkdownDoc">pydocmk2.preprocessors.pydocmk.MarkdownDoc</a> method</span></dt><dd>
<pre class="doc">Create a HTML heading</pre>
</dd></dl>

<h3 id="pydocmk2.preprocessors.pydocmk.MarkdownDoc.url">url</h3>

<dl class="function"><dt><a name="-pydocmk2.preprocessors.pydocmk.MarkdownDoc.url" href="#-pydocmk2.preprocessors.pydocmk.MarkdownDoc.url"><span class="function-name">pydocmk2.preprocessors.pydocmk.MarkdownDoc.url</span></a> = url<span class="argspec">(self, name)</span><span class="note"> unbound <a href="./pydocmk2.preprocessors.pydocmk.html#MarkdownDoc">pydocmk2.preprocessors.pydocmk.MarkdownDoc</a> method</span></dt><dd>
<pre class="doc">Create URL for a documentable thing. Mainly intended for subclassing</pre>
</dd></dl>

<h3 id="pydocmk2.preprocessors.pydocmk.MarkdownDoc.modpkglink">modpkglink</h3>

<dl class="function"><dt><a name="-pydocmk2.preprocessors.pydocmk.MarkdownDoc.modpkglink" href="#-pydocmk2.preprocessors.pydocmk.MarkdownDoc.modpkglink"><span class="function-name">pydocmk2.preprocessors.pydocmk.MarkdownDoc.modpkglink</span></a> = modpkglink<span class="argspec">(self, data)</span><span class="note"> unbound <a href="./pydocmk2.preprocessors.pydocmk.html#MarkdownDoc">pydocmk2.preprocessors.pydocmk.MarkdownDoc</a> method</span></dt><dd>
<pre class="doc">Make a link for a module or package to display in an index.</pre>
</dd></dl>

<h3 id="pydocmk2.preprocessors.pydocmk.MarkdownDoc.modulelink">modulelink</h3>

<dl class="function"><dt><a name="-pydocmk2.preprocessors.pydocmk.MarkdownDoc.modulelink" href="#-pydocmk2.preprocessors.pydocmk.MarkdownDoc.modulelink"><span class="function-name">pydocmk2.preprocessors.pydocmk.MarkdownDoc.modulelink</span></a> = modulelink<span class="argspec">(self, object)</span><span class="note"> unbound <a href="./pydocmk2.preprocessors.pydocmk.html#MarkdownDoc">pydocmk2.preprocessors.pydocmk.MarkdownDoc</a> method</span></dt><dd>
<pre class="doc">Make a link for a module.</pre>
</dd></dl>

<h3 id="pydocmk2.preprocessors.pydocmk.MarkdownDoc.classlink">classlink</h3>

<dl class="function"><dt><a name="-pydocmk2.preprocessors.pydocmk.MarkdownDoc.classlink" href="#-pydocmk2.preprocessors.pydocmk.MarkdownDoc.classlink"><span class="function-name">pydocmk2.preprocessors.pydocmk.MarkdownDoc.classlink</span></a> = classlink<span class="argspec">(self, object, modname)</span><span class="note"> unbound <a href="./pydocmk2.preprocessors.pydocmk.html#MarkdownDoc">pydocmk2.preprocessors.pydocmk.MarkdownDoc</a> method</span></dt><dd>
<pre class="doc">Make a link for a class.</pre>
</dd></dl>

<h3 id="pydocmk2.preprocessors.pydocmk.MarkdownDoc.formattree">formattree</h3>

<dl class="function"><dt><a name="-pydocmk2.preprocessors.pydocmk.MarkdownDoc.formattree" href="#-pydocmk2.preprocessors.pydocmk.MarkdownDoc.formattree"><span class="function-name">pydocmk2.preprocessors.pydocmk.MarkdownDoc.formattree</span></a> = formattree<span class="argspec">(self, tree, modname, parent<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./pydocmk2.preprocessors.pydocmk.html#MarkdownDoc">pydocmk2.preprocessors.pydocmk.MarkdownDoc</a> method</span></dt><dd>
<pre class="doc">Render in text a class tree as returned by inspect.getclasstree().</pre>
</dd></dl>

<h3 id="pydocmk2.preprocessors.pydocmk.MarkdownDoc.markup">markup</h3>

<dl class="function"><dt><a name="-pydocmk2.preprocessors.pydocmk.MarkdownDoc.markup" href="#-pydocmk2.preprocessors.pydocmk.MarkdownDoc.markup"><span class="function-name">pydocmk2.preprocessors.pydocmk.MarkdownDoc.markup</span></a> = markup<span class="argspec">(self, text, escape<span class="parameter-default">=None</span>, funcs<span class="parameter-default">={}</span>, classes<span class="parameter-default">={}</span>, methods<span class="parameter-default">={}</span>)</span><span class="note"> unbound <a href="./pydocmk2.preprocessors.pydocmk.html#MarkdownDoc">pydocmk2.preprocessors.pydocmk.MarkdownDoc</a> method</span></dt><dd>
<pre class="doc">Mark up some plain text, given a context of symbols to look for.
Each context dictionary maps object names to anchor names.

i.e. Replaces plaintext URLs with linked versions
Also escapes input text</pre>
</dd></dl>

<h3 id="pydocmk2.preprocessors.pydocmk.MarkdownDoc.docmodule">docmodule</h3>

<dl class="function"><dt><a name="-pydocmk2.preprocessors.pydocmk.MarkdownDoc.docmodule" href="#-pydocmk2.preprocessors.pydocmk.MarkdownDoc.docmodule"><span class="function-name">pydocmk2.preprocessors.pydocmk.MarkdownDoc.docmodule</span></a> = docmodule<span class="argspec">(self, object, name<span class="parameter-default">=None</span>, mod<span class="parameter-default">=None</span>, *ignored)</span><span class="note"> unbound <a href="./pydocmk2.preprocessors.pydocmk.html#MarkdownDoc">pydocmk2.preprocessors.pydocmk.MarkdownDoc</a> method</span></dt><dd>
<pre class="doc">Produce HTML5 documentation for a module object.</pre>
</dd></dl>

<h3 id="pydocmk2.preprocessors.pydocmk.MarkdownDoc.docclass">docclass</h3>

<dl class="function"><dt><a name="-pydocmk2.preprocessors.pydocmk.MarkdownDoc.docclass" href="#-pydocmk2.preprocessors.pydocmk.MarkdownDoc.docclass"><span class="function-name">pydocmk2.preprocessors.pydocmk.MarkdownDoc.docclass</span></a> = docclass<span class="argspec">(self, object, name<span class="parameter-default">=None</span>, mod<span class="parameter-default">=None</span>, funcs<span class="parameter-default">={}</span>, classes<span class="parameter-default">={}</span>, *ignored)</span><span class="note"> unbound <a href="./pydocmk2.preprocessors.pydocmk.html#MarkdownDoc">pydocmk2.preprocessors.pydocmk.MarkdownDoc</a> method</span></dt><dd>
<pre class="doc">Produce HTML documentation for a class object.</pre>
</dd></dl>

<h3 id="pydocmk2.preprocessors.pydocmk.MarkdownDoc.formatvalue">formatvalue</h3>

<dl class="function"><dt><a name="-pydocmk2.preprocessors.pydocmk.MarkdownDoc.formatvalue" href="#-pydocmk2.preprocessors.pydocmk.MarkdownDoc.formatvalue"><span class="function-name">pydocmk2.preprocessors.pydocmk.MarkdownDoc.formatvalue</span></a> = formatvalue<span class="argspec">(self, object)</span><span class="note"> unbound <a href="./pydocmk2.preprocessors.pydocmk.html#MarkdownDoc">pydocmk2.preprocessors.pydocmk.MarkdownDoc</a> method</span></dt><dd>
<pre class="doc">Format an argument default value as text.</pre>
</dd></dl>

<h3 id="pydocmk2.preprocessors.pydocmk.MarkdownDoc.docroutine">docroutine</h3>

<dl class="function"><dt><a name="-pydocmk2.preprocessors.pydocmk.MarkdownDoc.docroutine" href="#-pydocmk2.preprocessors.pydocmk.MarkdownDoc.docroutine"><span class="function-name">pydocmk2.preprocessors.pydocmk.MarkdownDoc.docroutine</span></a> = docroutine<span class="argspec">(self, object, name<span class="parameter-default">=None</span>, mod<span class="parameter-default">=None</span>, funcs<span class="parameter-default">={}</span>, classes<span class="parameter-default">={}</span>, methods<span class="parameter-default">={}</span>, cl<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./pydocmk2.preprocessors.pydocmk.html#MarkdownDoc">pydocmk2.preprocessors.pydocmk.MarkdownDoc</a> method</span></dt><dd>
<pre class="doc">Produce HTML documentation for a function or method object.</pre>
</dd></dl>

<h3 id="pydocmk2.preprocessors.pydocmk.MarkdownDoc.docproperty">docproperty</h3>

<dl class="function"><dt><a name="-pydocmk2.preprocessors.pydocmk.MarkdownDoc.docproperty" href="#-pydocmk2.preprocessors.pydocmk.MarkdownDoc.docproperty"><span class="function-name">pydocmk2.preprocessors.pydocmk.MarkdownDoc.docproperty</span></a> = docproperty<span class="argspec">(self, object, name<span class="parameter-default">=None</span>, mod<span class="parameter-default">=None</span>, cl<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./pydocmk2.preprocessors.pydocmk.html#MarkdownDoc">pydocmk2.preprocessors.pydocmk.MarkdownDoc</a> method</span></dt><dd>
<pre class="doc">Produce html documentation for a property.</pre>
</dd></dl>

<h3 id="pydocmk2.preprocessors.pydocmk.MarkdownDoc.docother">docother</h3>

<dl class="function"><dt><a name="-pydocmk2.preprocessors.pydocmk.MarkdownDoc.docother" href="#-pydocmk2.preprocessors.pydocmk.MarkdownDoc.docother"><span class="function-name">pydocmk2.preprocessors.pydocmk.MarkdownDoc.docother</span></a> = docother<span class="argspec">(self, object, name<span class="parameter-default">=None</span>, mod<span class="parameter-default">=None</span>, *ignored)</span><span class="note"> unbound <a href="./pydocmk2.preprocessors.pydocmk.html#MarkdownDoc">pydocmk2.preprocessors.pydocmk.MarkdownDoc</a> method</span></dt><dd>
<pre class="doc">Produce HTML documentation for a data object.</pre>
</dd></dl>

<h3 id="pydocmk2.preprocessors.pydocmk.MarkdownDoc.docdata">docdata</h3>

<dl class="function"><dt><a name="-pydocmk2.preprocessors.pydocmk.MarkdownDoc.docdata" href="#-pydocmk2.preprocessors.pydocmk.MarkdownDoc.docdata"><span class="function-name">pydocmk2.preprocessors.pydocmk.MarkdownDoc.docdata</span></a> = docdata<span class="argspec">(self, object, name<span class="parameter-default">=None</span>, mod<span class="parameter-default">=None</span>, cl<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./pydocmk2.preprocessors.pydocmk.html#MarkdownDoc">pydocmk2.preprocessors.pydocmk.MarkdownDoc</a> method</span></dt><dd>
<pre class="doc">Produce html documentation for a data descriptor.</pre>
</dd></dl>

<h2 id="pydocmk2.preprocessors.pydocmk.Preprocessor">Preprocessor</h2>

<dt class="class"><h2><span class="class-name">pydocmk2.preprocessors.pydocmk.Preprocessor</span> = <a name="pydocmk2.preprocessors.pydocmk.Preprocessor" href="#pydocmk2.preprocessors.pydocmk.Preprocessor">class Preprocessor</a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>

<pre class="doc">This class implements the basic preprocessing.</pre>

</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="Preprocessor-__init__" href="#Preprocessor-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, config)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>
<dl class="function"><dt><a name="Preprocessor-preprocess_section" href="#Preprocessor-preprocess_section"><span class="function-name">preprocess_section</span></a><span class="argspec">(self, section)</span></dt><dd>
<pre class="doc">Preprocess the contents of *section*.</pre>
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
<h3 id="pydocmk2.preprocessors.pydocmk.Preprocessor.preprocess_section">preprocess_section</h3>

<dl class="function"><dt><a name="-pydocmk2.preprocessors.pydocmk.Preprocessor.preprocess_section" href="#-pydocmk2.preprocessors.pydocmk.Preprocessor.preprocess_section"><span class="function-name">pydocmk2.preprocessors.pydocmk.Preprocessor.preprocess_section</span></a> = preprocess_section<span class="argspec">(self, section)</span><span class="note"> unbound <a href="./pydocmk2.preprocessors.pydocmk.html#Preprocessor">pydocmk2.preprocessors.pydocmk.Preprocessor</a> method</span></dt><dd>
<pre class="doc">Preprocess the contents of *section*.</pre>
</dd></dl>

