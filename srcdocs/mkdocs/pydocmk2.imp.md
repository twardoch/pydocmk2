

<a name="pydocmk2.imp"></a>

# `pydocmk2.imp`


<h2><a href="./pydocmk2.html">pydocmk2</a>.imp</h2> <div class="module">  <div class="docstring">

<pre class="doc" markdown="0">This module provides utilities for importing Python objects by name.</pre>

</div>  <div class="modules"><h3>Modules</h3><ul class="list"><li>inspect</li><li>types</li></ul></div>  <div class="functions"><h3>Functions</h3><dl class="functions"><dl class="function"><dt><a name="-dir_object" href="#-dir_object"><span class="function-name">dir_object</span></a><span class="argspec">(name, sort_order, need_docstrings<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

<dl class="function"><dt><a name="-force_lazy_import" href="#-force_lazy_import"><span class="function-name">force_lazy_import</span></a><span class="argspec">(name)</span></dt><dd>

<pre class="doc" markdown="0">Import any modules off of "name" by iterating a new list rather than a generator so that this
library works with lazy imports.</pre>

</dd></dl>

<dl class="function"><dt><a name="-import_module" href="#-import_module"><span class="function-name">import_module</span></a><span class="argspec">(name)</span></dt><dd>

<pre class="doc" markdown="0">Imports a Python module assuming that the whole *name* identifies only a
Python module and no symbol inside a Python module.</pre>

</dd></dl>

<dl class="function"><dt><a name="-import_object" href="#-import_object"><span class="function-name">import_object</span></a><span class="argspec">(name)</span></dt><dd>

<pre class="doc" markdown="0">Like #<a href="#-import_object_with_scope">import_object_with_scope</a>() but returns only the object.</pre>

</dd></dl>

<dl class="function"><dt><a name="-import_object_with_scope" href="#-import_object_with_scope"><span class="function-name">import_object_with_scope</span></a><span class="argspec">(name)</span></dt><dd>

<pre class="doc" markdown="0">Imports a Python object by an absolute identifier.

# Arguments
name (str): The name of the Python object to import.

# Returns
(any, Module): The object and the module that contains it. Note that
  for plain modules loaded with this function, both elements of the
  tuple may be the same object.</pre>

</dd></dl>
</dl></div></div>


<a name="pydocmk2.imp.import_module"></a>

## `import_module`


<dl class="function"><dt><a name="-pydocmk2.imp.import_module" href="#-pydocmk2.imp.import_module"><span class="function-name">pydocmk2.imp.import_module</span></a> = import_module<span class="argspec">(name)</span></dt><dd>

<pre class="doc" markdown="0">Imports a Python module assuming that the whole *name* identifies only a
Python module and no symbol inside a Python module.</pre>

</dd></dl>



<a name="pydocmk2.imp.import_object"></a>

## `import_object`


<dl class="function"><dt><a name="-pydocmk2.imp.import_object" href="#-pydocmk2.imp.import_object"><span class="function-name">pydocmk2.imp.import_object</span></a> = import_object<span class="argspec">(name)</span></dt><dd>

<pre class="doc" markdown="0">Like #import_object_with_scope() but returns only the object.</pre>

</dd></dl>



<a name="pydocmk2.imp.import_object_with_scope"></a>

## `import_object_with_scope`


<dl class="function"><dt><a name="-pydocmk2.imp.import_object_with_scope" href="#-pydocmk2.imp.import_object_with_scope"><span class="function-name">pydocmk2.imp.import_object_with_scope</span></a> = import_object_with_scope<span class="argspec">(name)</span></dt><dd>

<pre class="doc" markdown="0">Imports a Python object by an absolute identifier.

# Arguments
name (str): The name of the Python object to import.

# Returns
(any, Module): The object and the module that contains it. Note that
  for plain modules loaded with this function, both elements of the
  tuple may be the same object.</pre>

</dd></dl>



<a name="pydocmk2.imp.force_lazy_import"></a>

## `force_lazy_import`


<dl class="function"><dt><a name="-pydocmk2.imp.force_lazy_import" href="#-pydocmk2.imp.force_lazy_import"><span class="function-name">pydocmk2.imp.force_lazy_import</span></a> = force_lazy_import<span class="argspec">(name)</span></dt><dd>

<pre class="doc" markdown="0">Import any modules off of "name" by iterating a new list rather than a generator so that this
library works with lazy imports.</pre>

</dd></dl>

