<h1 id="pydocmk2.document">pydocmk2.document</h1>

<h2><a href="./pydocmk2.html">pydocmk2</a>.document</h2> <span class="file-reference">/Users/adam/Developer/vcs/github.twardoch/pub/pydocmk2/pydocmk2/document.py</span> <div class="module">  <div class="docstring">
<pre class="doc">This module implements the structural representation of an API documentation
in separate documents and symbolic names. The final documentation is rendered
from this structured representation.</pre>
</div>  <div class="modules"><h3>Modules</h3><ul class="list"><li><a href="./os.html">os</a></li></ul></div>  <div class="classes"><h3>Classes</h3><ul class="tree"><li><span class="class-name"><a href="./__builtin__.html#object">__builtin__.object</a></span></li><li><ul class="tree"><li><span class="class-name"><a href="./pydocmk2.document.html#Document">Document</a></span></li><li><span class="class-name"><a href="./pydocmk2.document.html#Index">Index</a></span></li><li><span class="class-name"><a href="./pydocmk2.document.html#Section">Section</a></span></li></ul></li></ul><dl class="classes"><dt class="class"><h2><a name="Document" href="#Document">class <span class="class-name">Document</span></a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>

<pre class="doc">Represents a single document that may contain several #Section#s. Every
document *must* have a relative URL associated with it.

# Attributes
index (Index): The index that the document belongs to.
url (str): The relative URL of the document.</pre>

</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="Document-__init__" href="#Document-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, index, url)</span></dt><dd>
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
</dd>
<dt class="class"><h2><a name="Index" href="#Index">class <span class="class-name">Index</span></a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>

<pre class="doc">The index manages all documents and sections globally. It keeps track of
the symbolic names allocated for the sections to be able to link to them
from other sections.

# Attributes
documents (dict):
sections (dict):</pre>

</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="Index-__init__" href="#Index-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>
<dl class="function"><dt><a name="Index-new_document" href="#Index-new_document"><span class="function-name">new_document</span></a><span class="argspec">(self, filename, url<span class="parameter-default">=None</span>)</span></dt><dd>
<pre class="doc">Create a new document.

# Arguments
filename (str): The filename of the document. Must end with `.md`.
url (str): The relative URL of the document. If omitted, will be
  automatically deduced from *filename* (same without the `.md` suffix).

# Raises
ValueError: If *filename* does not end with `.md`.
ValueError: If *filename* is not a relative path.
ValueError: If a document with the specified *filename* already exists.</pre>
</dd></dl>
<dl class="function"><dt><a name="Index-new_section" href="#Index-new_section"><span class="function-name">new_section</span></a><span class="argspec">(self, doc, *args, **kwargs)</span></dt><dd>
<pre class="doc">Create a new section in the specified document. The arguments for this
method match the parameters for the #<a href="#Section">Section</a> constructor.

# Raises
ValueError: If the section identifier is already used.</pre>
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
<dt class="class"><h2><a name="Section" href="#Section">class <span class="class-name">Section</span></a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>

<pre class="doc">A section represents a part of a #Document. It contains Markdown-formatted
content that will be rendered into a file at some point.

# Attributes
doc (Document): The document that the section belongs to.
identifier (str, None): The globally unique identifier of the section. This
  identifier usually matches the name of the element that the section
  describes (eg. a class or function) and will be used for cross-referencing.
title (str, None): The title of the section. If specified, it will be
  rendered before `section.content` and the header-size will depend on
  the `section.depth`.
depth (int): The depth of the section, defaults to 1. Currently only affects
  the header-size that is rendered for the `section.title`.
content (str): The Markdown-formatted content of the section.</pre>

</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="Section-__init__" href="#Section-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, doc, identifier<span class="parameter-default">=None</span>, title<span class="parameter-default">=None</span>, depth<span class="parameter-default">=1</span>, content<span class="parameter-default">=None</span>, header_type<span class="parameter-default">='html'</span>)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>
<dl class="function"><dt><a name="Section-render" href="#Section-render"><span class="function-name">render</span></a><span class="argspec">(self, stream)</span></dt><dd>
<pre class="doc">Render the section into *stream*.</pre>
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
<dl class="descriptor"><dt>index</dt>
<dd>
<pre class="doc">Returns the #Index that this section is associated with, accessed via
`section.document`.</pre>
</dd>
</dl>
</dd></dl></div></div>
<h2 id="pydocmk2.document.Section">Section</h2>

<dt class="class"><h2><span class="class-name">pydocmk2.document.Section</span> = <a name="pydocmk2.document.Section" href="#pydocmk2.document.Section">class Section</a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>

<pre class="doc">A section represents a part of a #Document. It contains Markdown-formatted
content that will be rendered into a file at some point.

# Attributes
doc (Document): The document that the section belongs to.
identifier (str, None): The globally unique identifier of the section. This
  identifier usually matches the name of the element that the section
  describes (eg. a class or function) and will be used for cross-referencing.
title (str, None): The title of the section. If specified, it will be
  rendered before `section.content` and the header-size will depend on
  the `section.depth`.
depth (int): The depth of the section, defaults to 1. Currently only affects
  the header-size that is rendered for the `section.title`.
content (str): The Markdown-formatted content of the section.</pre>

</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="Section-__init__" href="#Section-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, doc, identifier<span class="parameter-default">=None</span>, title<span class="parameter-default">=None</span>, depth<span class="parameter-default">=1</span>, content<span class="parameter-default">=None</span>, header_type<span class="parameter-default">='html'</span>)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>
<dl class="function"><dt><a name="Section-render" href="#Section-render"><span class="function-name">render</span></a><span class="argspec">(self, stream)</span></dt><dd>
<pre class="doc">Render the section into *stream*.</pre>
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
<dl class="descriptor"><dt>index</dt>
<dd>
<pre class="doc">Returns the #Index that this section is associated with, accessed via
`section.document`.</pre>
</dd>
</dl>
</dd>
<h3 id="pydocmk2.document.Section.index">index</h3>

<dl class="descriptor"><dt>pydocmk2.document.Section.index</dt>
<dd>
<pre class="doc">Returns the #Index that this section is associated with, accessed via
`section.document`.</pre>
</dd>
</dl>

<h3 id="pydocmk2.document.Section.render">render</h3>

<dl class="function"><dt><a name="-pydocmk2.document.Section.render" href="#-pydocmk2.document.Section.render"><span class="function-name">pydocmk2.document.Section.render</span></a> = render<span class="argspec">(self, stream)</span><span class="note"> unbound <a href="./pydocmk2.document.html#Section">pydocmk2.document.Section</a> method</span></dt><dd>
<pre class="doc">Render the section into *stream*.</pre>
</dd></dl>

<h2 id="pydocmk2.document.Document">Document</h2>

<dt class="class"><h2><span class="class-name">pydocmk2.document.Document</span> = <a name="pydocmk2.document.Document" href="#pydocmk2.document.Document">class Document</a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>

<pre class="doc">Represents a single document that may contain several #Section#s. Every
document *must* have a relative URL associated with it.

# Attributes
index (Index): The index that the document belongs to.
url (str): The relative URL of the document.</pre>

</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="Document-__init__" href="#Document-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, index, url)</span></dt><dd>
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
</dd>
<h2 id="pydocmk2.document.Index">Index</h2>

<dt class="class"><h2><span class="class-name">pydocmk2.document.Index</span> = <a name="pydocmk2.document.Index" href="#pydocmk2.document.Index">class Index</a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>

<pre class="doc">The index manages all documents and sections globally. It keeps track of
the symbolic names allocated for the sections to be able to link to them
from other sections.

# Attributes
documents (dict):
sections (dict):</pre>

</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="Index-__init__" href="#Index-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self)</span></dt><dd>
<pre class="doc"></pre>
</dd></dl>
<dl class="function"><dt><a name="Index-new_document" href="#Index-new_document"><span class="function-name">new_document</span></a><span class="argspec">(self, filename, url<span class="parameter-default">=None</span>)</span></dt><dd>
<pre class="doc">Create a new document.

# Arguments
filename (str): The filename of the document. Must end with `.md`.
url (str): The relative URL of the document. If omitted, will be
  automatically deduced from *filename* (same without the `.md` suffix).

# Raises
ValueError: If *filename* does not end with `.md`.
ValueError: If *filename* is not a relative path.
ValueError: If a document with the specified *filename* already exists.</pre>
</dd></dl>
<dl class="function"><dt><a name="Index-new_section" href="#Index-new_section"><span class="function-name">new_section</span></a><span class="argspec">(self, doc, *args, **kwargs)</span></dt><dd>
<pre class="doc">Create a new section in the specified document. The arguments for this
method match the parameters for the #Section constructor.

# Raises
ValueError: If the section identifier is already used.</pre>
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
<h3 id="pydocmk2.document.Index.new_document">new_document</h3>

<dl class="function"><dt><a name="-pydocmk2.document.Index.new_document" href="#-pydocmk2.document.Index.new_document"><span class="function-name">pydocmk2.document.Index.new_document</span></a> = new_document<span class="argspec">(self, filename, url<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./pydocmk2.document.html#Index">pydocmk2.document.Index</a> method</span></dt><dd>
<pre class="doc">Create a new document.

# Arguments
filename (str): The filename of the document. Must end with `.md`.
url (str): The relative URL of the document. If omitted, will be
  automatically deduced from *filename* (same without the `.md` suffix).

# Raises
ValueError: If *filename* does not end with `.md`.
ValueError: If *filename* is not a relative path.
ValueError: If a document with the specified *filename* already exists.</pre>
</dd></dl>

<h3 id="pydocmk2.document.Index.new_section">new_section</h3>

<dl class="function"><dt><a name="-pydocmk2.document.Index.new_section" href="#-pydocmk2.document.Index.new_section"><span class="function-name">pydocmk2.document.Index.new_section</span></a> = new_section<span class="argspec">(self, doc, *args, **kwargs)</span><span class="note"> unbound <a href="./pydocmk2.document.html#Index">pydocmk2.document.Index</a> method</span></dt><dd>
<pre class="doc">Create a new section in the specified document. The arguments for this
method match the parameters for the #Section constructor.

# Raises
ValueError: If the section identifier is already used.</pre>
</dd></dl>

