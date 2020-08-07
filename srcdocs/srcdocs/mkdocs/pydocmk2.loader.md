<h1 id="pydocmk2.loader">pydocmk2.loader</h1>

<h2><a href="./pydocmk2.html">pydocmk2</a>.loader</h2> <span class="file-reference">/Users/adam/Developer/vcs/github.twardoch/pub/pydocmk2/pydocmk2/loader.py</span> <div class="module">  <div class="docstring">
<pre class="doc">This module provides implementations to load documentation information from
an identifier as it is specified in the `pydocmk.yml:generate` configuration
key. A loader basically takes care of loading the documentation content for
that name, but is not supposed to apply preprocessing.</pre>
</div>  <div class="modules"><h3>Modules</h3><ul class="list"><li><a href="./collections.html">collections</a></li><li><a href="./inspect.html">inspect</a></li><li><a href="./types.html">types</a></li><li><a href="./uuid.html">uuid</a></li></ul></div>  <div class="classes"><h3>Classes</h3><ul class="tree"><li><span class="class-name"><a href="./__builtin__.html#object">__builtin__.object</a></span></li><li><ul class="tree"><li><span class="class-name"><a href="./pydocmk2.loader.html#Parameter">Parameter</a></span></li><li><span class="class-name"><a href="./pydocmk2.loader.html#PythonLoader">PythonLoader</a></span></li></ul></li></ul><dl class="classes"><dt class="class"><h2><a name="Parameter" href="#Parameter">class <span class="class-name">Parameter</span></a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>

<pre class="doc"></pre>

</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="Parameter-__init__" href="#Parameter-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, kind, name, annotation<span class="parameter-default">=None</span>, default<span class="parameter-default">=None</span>)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>
<dl class="function"><dt><a name="Parameter-__repr__" href="#Parameter-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>
<dl class="function"><dt><a name="Parameter-__str__" href="#Parameter-__str__"><span class="function-name">__str__</span></a><span class="argspec">(self)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>
<dl class="function"><dt><a name="Parameter-replace" href="#Parameter-replace"><span class="function-name">replace</span></a><span class="argspec">(self, name<span class="parameter-default">=&lt;object object&gt;</span>, annotation<span class="parameter-default">=&lt;object object&gt;</span>, default<span class="parameter-default">=&lt;object object&gt;</span>, kind<span class="parameter-default">=&lt;object object&gt;</span>)</span></dt><dd>
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

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">KWONLY</span> = 'KWONLY'</dt></dl>
<dl><dt><span class="other-name">POS</span> = 'POS'</dt></dl>
<dl><dt><span class="other-name">VARARGS_KW</span> = 'VARARGS_KW'</dt></dl>
<dl><dt><span class="other-name">VARARGS_POS</span> = 'VARARGS_POS'</dt></dl>
<dl><dt><span class="other-name">Value</span> = &lt;class 'pydocmk2.loader.Value'&gt;<dd>
<pre class="doc"><a href="#Parameter-Value">Value</a>(value,)</pre>
</dd></dl>
</dd>
<dt class="class"><h2><a name="PythonLoader" href="#PythonLoader">class <span class="class-name">PythonLoader</span></a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>

<pre class="doc">Expects absolute identifiers to import with #import_object_with_scope().</pre>

</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="PythonLoader-__init__" href="#PythonLoader-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, config)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>
<dl class="function"><dt><a name="PythonLoader-load_section" href="#PythonLoader-load_section"><span class="function-name">load_section</span></a><span class="argspec">(self, section)</span></dt><dd>
<pre class="doc">Loads the contents of a #Section. The `section.identifier` is the name
of the <a href="./__builtin__.html#object">object</a> that we need to load.

# Arguments
  section (Section): The section to load. Fill the `section.title` and
    `section.content` values. Optionally, `section.loader_context` can
    be filled with custom arbitrary data to reference at a later point.</pre>
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
</dd></dl></div>  <div class="functions"><h3>Functions</h3><dl class="functions"><dl class="function"><dt><a name="-format_parameters_list" href="#-format_parameters_list"><span class="function-name">format_parameters_list</span></a><span class="argspec">(parameters)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>

<dl class="function"><dt><a name="-get_docstring" href="#-get_docstring"><span class="function-name">get_docstring</span></a><span class="argspec">(function)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>

<dl class="function"><dt><a name="-get_full_arg_spec" href="#-get_full_arg_spec"><span class="function-name">get_full_arg_spec</span></a><span class="argspec">(func)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>

<dl class="function"><dt><a name="-get_function_signature" href="#-get_function_signature"><span class="function-name">get_function_signature</span></a><span class="argspec">(function, owner_class<span class="parameter-default">=None</span>, strip_self_param<span class="parameter-default">=False</span>, show_module<span class="parameter-default">=False</span>, pretty<span class="parameter-default">=True</span>)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>

<dl class="function"><dt><a name="-get_paramaters_from_arg_spec" href="#-get_paramaters_from_arg_spec"><span class="function-name">get_paramaters_from_arg_spec</span></a><span class="argspec">(argspec, strip_self<span class="parameter-default">=False</span>)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>

<dl class="function"><dt><a name="-trim" href="#-trim"><span class="function-name">trim</span></a><span class="argspec">(docstring)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>
</dl></div></div>
<h2 id="pydocmk2.loader.PythonLoader">PythonLoader</h2>

<dt class="class"><h2><span class="class-name">pydocmk2.loader.PythonLoader</span> = <a name="pydocmk2.loader.PythonLoader" href="#pydocmk2.loader.PythonLoader">class PythonLoader</a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>

<pre class="doc">Expects absolute identifiers to import with #import_object_with_scope().</pre>

</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="PythonLoader-__init__" href="#PythonLoader-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, config)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>
<dl class="function"><dt><a name="PythonLoader-load_section" href="#PythonLoader-load_section"><span class="function-name">load_section</span></a><span class="argspec">(self, section)</span></dt><dd>
<pre class="doc">Loads the contents of a #Section. The `section.identifier` is the name
of the object that we need to load.

# Arguments
  section (Section): The section to load. Fill the `section.title` and
    `section.content` values. Optionally, `section.loader_context` can
    be filled with custom arbitrary data to reference at a later point.</pre>
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
<h3 id="pydocmk2.loader.PythonLoader.load_section">load_section</h3>

<dl class="function"><dt><a name="-pydocmk2.loader.PythonLoader.load_section" href="#-pydocmk2.loader.PythonLoader.load_section"><span class="function-name">pydocmk2.loader.PythonLoader.load_section</span></a> = load_section<span class="argspec">(self, section)</span><span class="note"> unbound <a href="./pydocmk2.loader.html#PythonLoader">pydocmk2.loader.PythonLoader</a> method</span></dt><dd>
<pre class="doc">Loads the contents of a #Section. The `section.identifier` is the name
of the object that we need to load.

# Arguments
  section (Section): The section to load. Fill the `section.title` and
    `section.content` values. Optionally, `section.loader_context` can
    be filled with custom arbitrary data to reference at a later point.</pre>
</dd></dl>

<h2 id="pydocmk2.loader.Parameter">Parameter</h2>

<dt class="class"><h2><span class="class-name">pydocmk2.loader.Parameter</span> = <a name="pydocmk2.loader.Parameter" href="#pydocmk2.loader.Parameter">class Parameter</a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>

<pre class="doc"></pre>

</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="Parameter-__init__" href="#Parameter-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, kind, name, annotation<span class="parameter-default">=None</span>, default<span class="parameter-default">=None</span>)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>
<dl class="function"><dt><a name="Parameter-__repr__" href="#Parameter-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>
<dl class="function"><dt><a name="Parameter-__str__" href="#Parameter-__str__"><span class="function-name">__str__</span></a><span class="argspec">(self)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>
<dl class="function"><dt><a name="Parameter-replace" href="#Parameter-replace"><span class="function-name">replace</span></a><span class="argspec">(self, name<span class="parameter-default">=&lt;object object&gt;</span>, annotation<span class="parameter-default">=&lt;object object&gt;</span>, default<span class="parameter-default">=&lt;object object&gt;</span>, kind<span class="parameter-default">=&lt;object object&gt;</span>)</span></dt><dd>
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

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">KWONLY</span> = 'KWONLY'</dt></dl>
<dl><dt><span class="other-name">POS</span> = 'POS'</dt></dl>
<dl><dt><span class="other-name">VARARGS_KW</span> = 'VARARGS_KW'</dt></dl>
<dl><dt><span class="other-name">VARARGS_POS</span> = 'VARARGS_POS'</dt></dl>
<dl><dt><span class="other-name">Value</span> = &lt;class 'pydocmk2.loader.Value'&gt;<dd>
<pre class="doc"><a href="#pydocmk2.loader.Parameter-Value">Value</a>(value,)</pre>
</dd></dl>
</dd>
<h3 id="pydocmk2.loader.Parameter.KWONLY">KWONLY</h3>

<span class="other-name">pydocmk2.loader.Parameter.KWONLY</span> = 'KWONLY'
<h3 id="pydocmk2.loader.Parameter.POS">POS</h3>

<span class="other-name">pydocmk2.loader.Parameter.POS</span> = 'POS'
<h3 id="pydocmk2.loader.Parameter.Value">Value</h3>

<dt class="class"><h2><span class="class-name">pydocmk2.loader.Parameter.Value</span> = <a name="pydocmk2.loader.Parameter.Value" href="#pydocmk2.loader.Parameter.Value">class Value</a>(<a href="./__builtin__.html#tuple">__builtin__.tuple</a>)</h2></dt><dd class="class"><dd>

<pre class="doc">Value(value,)</pre>

</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd>Value</dd><dd><a href="./__builtin__.html#tuple">__builtin__.tuple</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="Value-__getnewargs__" href="#Value-__getnewargs__"><span class="function-name">__getnewargs__</span></a><span class="argspec">(self)</span></dt><dd>
<pre class="doc">Return self as a plain tuple.  Used by copy and pickle.</pre>
</dd></dl>
<dl class="function"><dt><a name="Value-__getstate__" href="#Value-__getstate__"><span class="function-name">__getstate__</span></a><span class="argspec">(self)</span></dt><dd>
<pre class="doc">Exclude the OrderedDict from pickling</pre>
</dd></dl>
<dl class="function"><dt><a name="Value-__repr__" href="#Value-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>
<pre class="doc">Return a nicely formatted representation string</pre>
</dd></dl>
<dl class="function"><dt><a name="Value-_asdict" href="#Value-_asdict"><span class="function-name">_asdict</span></a><span class="argspec">(self)</span></dt><dd>
<pre class="doc">Return a new OrderedDict which maps field names to their values</pre>
</dd></dl>
<dl class="function"><dt><a name="Value-_replace" href="#Value-_replace"><span class="function-name">_replace</span></a><span class="argspec">(_self, **kwds)</span></dt><dd>
<pre class="doc">Return a new Value object replacing specified fields with new values</pre>
</dd></dl>

  <h4 class="head-class-methods">Class methods </h4><dl class="function"><dt><a name="Value-_make" href="#Value-_make"><span class="function-name">_make</span></a><span class="argspec">(cls, iterable, new<span class="parameter-default">=&lt;built-in method __new__ of type object&gt;</span>, len<span class="parameter-default">=&lt;built-in function len&gt;</span>)</span><span class="note"> from <a href="./__builtin__.html#type">__builtin__.type</a></span></dt><dd>
<pre class="doc">Make a new Value object from a sequence or iterable</pre>
</dd></dl>

  <h4 class="head-static-methods">Static methods </h4><dl class="function"><dt><a name="Value-__new__" href="#Value-__new__"><span class="function-name">__new__</span></a><span class="argspec">(_cls, value)</span></dt><dd>
<pre class="doc">Create new instance of Value(value,)</pre>
</dd></dl>

  <h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>__dict__</dt>
<dd>
<pre class="doc">Return a new OrderedDict which maps field names to their values</pre>
</dd>
</dl>
<dl class="descriptor"><dt>value</dt>
<dd>
<pre class="doc">Alias for field number 0</pre>
</dd>
</dl>

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">_fields</span> = ('value',)</dt></dl>

  <h4 class="head-methods">Methods from <a href="./__builtin__.html#tuple">__builtin__.tuple</a></h4><dl class="function"><dt><a name="Value-__add__" href="#Value-__add__"><span class="function-name">__add__</span></a><span class="argspec">(...)</span></dt><dd>
<pre class="doc">x.<a href="#pydocmk2.loader.Parameter.Value-__add__">__add__</a>(y) <==> x+y</pre>
</dd></dl>
<dl class="function"><dt><a name="Value-__contains__" href="#Value-__contains__"><span class="function-name">__contains__</span></a><span class="argspec">(...)</span></dt><dd>
<pre class="doc">x.<a href="#pydocmk2.loader.Parameter.Value-__contains__">__contains__</a>(y) <==> y in x</pre>
</dd></dl>
<dl class="function"><dt><a name="Value-__eq__" href="#Value-__eq__"><span class="function-name">__eq__</span></a><span class="argspec">(...)</span></dt><dd>
<pre class="doc">x.<a href="#pydocmk2.loader.Parameter.Value-__eq__">__eq__</a>(y) <==> x==y</pre>
</dd></dl>
<dl class="function"><dt><a name="Value-__ge__" href="#Value-__ge__"><span class="function-name">__ge__</span></a><span class="argspec">(...)</span></dt><dd>
<pre class="doc">x.<a href="#pydocmk2.loader.Parameter.Value-__ge__">__ge__</a>(y) <==> x>=y</pre>
</dd></dl>
<dl class="function"><dt><a name="Value-__getattribute__" href="#Value-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>
<pre class="doc">x.<a href="#pydocmk2.loader.Parameter.Value-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>
</dd></dl>
<dl class="function"><dt><a name="Value-__getitem__" href="#Value-__getitem__"><span class="function-name">__getitem__</span></a><span class="argspec">(...)</span></dt><dd>
<pre class="doc">x.<a href="#pydocmk2.loader.Parameter.Value-__getitem__">__getitem__</a>(y) <==> x[y]</pre>
</dd></dl>
<dl class="function"><dt><a name="Value-__getslice__" href="#Value-__getslice__"><span class="function-name">__getslice__</span></a><span class="argspec">(...)</span></dt><dd>
<pre class="doc">x.<a href="#pydocmk2.loader.Parameter.Value-__getslice__">__getslice__</a>(i, j) <==> x[i:j]

Use of negative indices is not supported.</pre>
</dd></dl>
<dl class="function"><dt><a name="Value-__gt__" href="#Value-__gt__"><span class="function-name">__gt__</span></a><span class="argspec">(...)</span></dt><dd>
<pre class="doc">x.<a href="#pydocmk2.loader.Parameter.Value-__gt__">__gt__</a>(y) <==> x>y</pre>
</dd></dl>
<dl class="function"><dt><a name="Value-__hash__" href="#Value-__hash__"><span class="function-name">__hash__</span></a><span class="argspec">(...)</span></dt><dd>
<pre class="doc">x.<a href="#pydocmk2.loader.Parameter.Value-__hash__">__hash__</a>() <==> hash(x)</pre>
</dd></dl>
<dl class="function"><dt><a name="Value-__iter__" href="#Value-__iter__"><span class="function-name">__iter__</span></a><span class="argspec">(...)</span></dt><dd>
<pre class="doc">x.<a href="#pydocmk2.loader.Parameter.Value-__iter__">__iter__</a>() <==> iter(x)</pre>
</dd></dl>
<dl class="function"><dt><a name="Value-__le__" href="#Value-__le__"><span class="function-name">__le__</span></a><span class="argspec">(...)</span></dt><dd>
<pre class="doc">x.<a href="#pydocmk2.loader.Parameter.Value-__le__">__le__</a>(y) <==> x<=y</pre>
</dd></dl>
<dl class="function"><dt><a name="Value-__len__" href="#Value-__len__"><span class="function-name">__len__</span></a><span class="argspec">(...)</span></dt><dd>
<pre class="doc">x.<a href="#pydocmk2.loader.Parameter.Value-__len__">__len__</a>() <==> len(x)</pre>
</dd></dl>
<dl class="function"><dt><a name="Value-__lt__" href="#Value-__lt__"><span class="function-name">__lt__</span></a><span class="argspec">(...)</span></dt><dd>
<pre class="doc">x.<a href="#pydocmk2.loader.Parameter.Value-__lt__">__lt__</a>(y) <==> x<y</pre>
</dd></dl>
<dl class="function"><dt><a name="Value-__mul__" href="#Value-__mul__"><span class="function-name">__mul__</span></a><span class="argspec">(...)</span></dt><dd>
<pre class="doc">x.<a href="#pydocmk2.loader.Parameter.Value-__mul__">__mul__</a>(n) <==> x*n</pre>
</dd></dl>
<dl class="function"><dt><a name="Value-__ne__" href="#Value-__ne__"><span class="function-name">__ne__</span></a><span class="argspec">(...)</span></dt><dd>
<pre class="doc">x.<a href="#pydocmk2.loader.Parameter.Value-__ne__">__ne__</a>(y) <==> x!=y</pre>
</dd></dl>
<dl class="function"><dt><a name="Value-__rmul__" href="#Value-__rmul__"><span class="function-name">__rmul__</span></a><span class="argspec">(...)</span></dt><dd>
<pre class="doc">x.<a href="#pydocmk2.loader.Parameter.Value-__rmul__">__rmul__</a>(n) <==> n*x</pre>
</dd></dl>
<dl class="function"><dt><a name="Value-count" href="#Value-count"><span class="function-name">count</span></a><span class="argspec">(...)</span></dt><dd>
<pre class="doc">T.<a href="#pydocmk2.loader.Parameter.Value-count">count</a>(value) -> integer -- return number of occurrences of value</pre>
</dd></dl>
<dl class="function"><dt><a name="Value-index" href="#Value-index"><span class="function-name">index</span></a><span class="argspec">(...)</span></dt><dd>
<pre class="doc">T.<a href="#pydocmk2.loader.Parameter.Value-index">index</a>(value, [start, [stop]]) -> integer -- return first index of value.
Raises ValueError if the value is not present.</pre>
</dd></dl>
</dd>
<h3 id="pydocmk2.loader.Parameter.VARARGS_KW">VARARGS_KW</h3>

<span class="other-name">pydocmk2.loader.Parameter.VARARGS_KW</span> = 'VARARGS_KW'
<h3 id="pydocmk2.loader.Parameter.VARARGS_POS">VARARGS_POS</h3>

<span class="other-name">pydocmk2.loader.Parameter.VARARGS_POS</span> = 'VARARGS_POS'
