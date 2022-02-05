---
article_html: "<p>Markata is a tool for handling directories of markdown.</p>\n<hr
  />\n<h2 id=\"post-class\">Post <code>class</code></h2>\n<p>None</p>\n<details>\n<summary>Post
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">class</span>
  <span class=\"nc\">Post</span><span class=\"p\">(</span><span class=\"n\">frontmatter</span><span
  class=\"o\">.</span><span class=\"n\">Post</span><span class=\"p\">):</span>\n    <span
  class=\"n\">html</span><span class=\"p\">:</span> <span class=\"nb\">str</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"set_phase-function\">set_phase <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>set_phase
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">set_phase</span><span class=\"p\">(</span><span class=\"n\">function</span><span
  class=\"p\">:</span> <span class=\"n\">Callable</span><span class=\"p\">)</span>
  <span class=\"o\">-&gt;</span> <span class=\"n\">Any</span><span class=\"p\">:</span>\n
  \   <span class=\"k\">def</span> <span class=\"nf\">wrapper</span><span class=\"p\">(</span><span
  class=\"bp\">self</span><span class=\"p\">:</span> <span class=\"n\">Markata</span><span
  class=\"p\">,</span> <span class=\"o\">*</span><span class=\"n\">args</span><span
  class=\"p\">:</span> <span class=\"n\">Tuple</span><span class=\"p\">,</span> <span
  class=\"o\">**</span><span class=\"n\">kwargs</span><span class=\"p\">:</span> <span
  class=\"n\">Dict</span><span class=\"p\">)</span> <span class=\"o\">-&gt;</span>
  <span class=\"n\">Any</span><span class=\"p\">:</span>\n        <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">phase</span> <span class=\"o\">=</span> <span
  class=\"n\">function</span><span class=\"o\">.</span><span class=\"vm\">__name__</span>\n
  \       <span class=\"n\">result</span> <span class=\"o\">=</span> <span class=\"n\">function</span><span
  class=\"p\">(</span><span class=\"bp\">self</span><span class=\"p\">,</span> <span
  class=\"o\">*</span><span class=\"n\">args</span><span class=\"p\">,</span> <span
  class=\"o\">**</span><span class=\"n\">kwargs</span><span class=\"p\">)</span>\n
  \       <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">phase</span>
  <span class=\"o\">=</span> <span class=\"n\">function</span><span class=\"o\">.</span><span
  class=\"vm\">__name__</span>\n        <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">phase_file</span><span class=\"o\">.</span><span class=\"n\">write_text</span><span
  class=\"p\">(</span><span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">phase</span><span class=\"p\">)</span>\n        <span class=\"k\">return</span>
  <span class=\"n\">result</span>\n\n    <span class=\"k\">return</span> <span class=\"n\">wrapper</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"markata-class\">Markata <code>class</code></h2>\n<p>None</p>\n<details>\n<summary>Markata
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">class</span>
  <span class=\"nc\">Markata</span><span class=\"p\">:</span>\n    <span class=\"k\">def</span>
  <span class=\"fm\">__init__</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">,</span> <span class=\"n\">console</span><span class=\"p\">:</span>
  <span class=\"n\">Console</span> <span class=\"o\">=</span> <span class=\"kc\">None</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"kc\">None</span><span
  class=\"p\">:</span>\n        <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">phase</span> <span class=\"o\">=</span> <span class=\"s2\">&quot;starting&quot;</span>\n
  \       <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">MARKATA_CACHE_DIR</span>
  <span class=\"o\">=</span> <span class=\"n\">Path</span><span class=\"p\">(</span><span
  class=\"s2\">&quot;.&quot;</span><span class=\"p\">)</span> <span class=\"o\">/</span>
  <span class=\"s2\">&quot;.markata.cache&quot;</span>\n        <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">MARKATA_CACHE_DIR</span><span class=\"o\">.</span><span
  class=\"n\">mkdir</span><span class=\"p\">(</span><span class=\"n\">exist_ok</span><span
  class=\"o\">=</span><span class=\"kc\">True</span><span class=\"p\">)</span>\n        <span
  class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">phase_file</span><span
  class=\"p\">:</span> <span class=\"n\">Path</span> <span class=\"o\">=</span> <span
  class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">MARKATA_CACHE_DIR</span>
  <span class=\"o\">/</span> <span class=\"s2\">&quot;phase.txt&quot;</span>\n        <span
  class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">registered_attrs</span>
  <span class=\"o\">=</span> <span class=\"n\">hookspec</span><span class=\"o\">.</span><span
  class=\"n\">registered_attrs</span>\n        <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">configure</span><span class=\"p\">()</span>\n
  \       <span class=\"k\">if</span> <span class=\"n\">console</span> <span class=\"ow\">is</span>
  <span class=\"ow\">not</span> <span class=\"kc\">None</span><span class=\"p\">:</span>\n
  \           <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">_console</span>
  <span class=\"o\">=</span> <span class=\"n\">console</span>\n\n    <span class=\"nd\">@property</span>\n
  \   <span class=\"k\">def</span> <span class=\"nf\">cache</span><span class=\"p\">(</span><span
  class=\"bp\">self</span><span class=\"p\">)</span> <span class=\"o\">-&gt;</span>
  <span class=\"n\">FanoutCache</span><span class=\"p\">:</span>\n        <span class=\"k\">return</span>
  <span class=\"n\">FanoutCache</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">MARKATA_CACHE_DIR</span><span class=\"p\">,</span>
  <span class=\"n\">statistics</span><span class=\"o\">=</span><span class=\"kc\">True</span><span
  class=\"p\">)</span>\n\n    <span class=\"k\">def</span> <span class=\"fm\">__getattr__</span><span
  class=\"p\">(</span><span class=\"bp\">self</span><span class=\"p\">,</span> <span
  class=\"n\">item</span><span class=\"p\">:</span> <span class=\"nb\">str</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"n\">Any</span><span
  class=\"p\">:</span>\n        <span class=\"k\">if</span> <span class=\"n\">item</span>
  <span class=\"ow\">in</span> <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"vm\">__dict__</span><span class=\"o\">.</span><span class=\"n\">keys</span><span
  class=\"p\">():</span>\n            <span class=\"k\">return</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"fm\">__getitem__</span><span class=\"p\">(</span><span
  class=\"n\">item</span><span class=\"p\">)</span>\n        <span class=\"k\">elif</span>
  <span class=\"n\">item</span> <span class=\"ow\">in</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">registered_attrs</span><span class=\"o\">.</span><span
  class=\"n\">keys</span><span class=\"p\">():</span>\n            <span class=\"n\">stage_to_run_to</span>
  <span class=\"o\">=</span> <span class=\"nb\">max</span><span class=\"p\">(</span>\n
  \               <span class=\"p\">[</span><span class=\"n\">attr</span><span class=\"p\">[</span><span
  class=\"s2\">&quot;lifecycle&quot;</span><span class=\"p\">]</span> <span class=\"k\">for</span>
  <span class=\"n\">attr</span> <span class=\"ow\">in</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">registered_attrs</span><span class=\"p\">[</span><span
  class=\"n\">item</span><span class=\"p\">]]</span>\n            <span class=\"p\">)</span><span
  class=\"o\">.</span><span class=\"n\">name</span>\n            <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">run</span><span class=\"p\">(</span><span
  class=\"n\">stage_to_run_to</span><span class=\"p\">)</span>\n            <span
  class=\"k\">return</span> <span class=\"nb\">getattr</span><span class=\"p\">(</span><span
  class=\"bp\">self</span><span class=\"p\">,</span> <span class=\"n\">item</span><span
  class=\"p\">)</span>\n        <span class=\"k\">else</span><span class=\"p\">:</span>\n
  \           <span class=\"k\">raise</span> <span class=\"ne\">AttributeError</span><span
  class=\"p\">(</span><span class=\"n\">item</span><span class=\"p\">)</span>\n\n
  \   <span class=\"nd\">@property</span>\n    <span class=\"k\">def</span> <span
  class=\"nf\">server</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"n\">Server</span><span
  class=\"p\">:</span>\n        <span class=\"k\">try</span><span class=\"p\">:</span>\n
  \           <span class=\"k\">return</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">_server</span>\n        <span class=\"k\">except</span>
  <span class=\"ne\">AttributeError</span><span class=\"p\">:</span>\n\n            <span
  class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">_server</span><span
  class=\"p\">:</span> <span class=\"n\">Server</span> <span class=\"o\">=</span>
  <span class=\"n\">Server</span><span class=\"p\">(</span><span class=\"n\">directory</span><span
  class=\"o\">=</span><span class=\"nb\">str</span><span class=\"p\">(</span><span
  class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">config</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;output_dir&quot;</span><span class=\"p\">]))</span>\n
  \           <span class=\"k\">return</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">server</span>\n\n    <span class=\"nd\">@property</span>\n
  \   <span class=\"k\">def</span> <span class=\"nf\">runner</span><span class=\"p\">(</span><span
  class=\"bp\">self</span><span class=\"p\">)</span> <span class=\"o\">-&gt;</span>
  <span class=\"n\">Runner</span><span class=\"p\">:</span>\n        <span class=\"k\">try</span><span
  class=\"p\">:</span>\n            <span class=\"k\">return</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">_runner</span>\n        <span class=\"k\">except</span>
  <span class=\"ne\">AttributeError</span><span class=\"p\">:</span>\n\n            <span
  class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">_runner</span><span
  class=\"p\">:</span> <span class=\"n\">Runner</span> <span class=\"o\">=</span>
  <span class=\"n\">Runner</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">)</span>\n            <span class=\"k\">return</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">runner</span>\n\n    <span class=\"nd\">@property</span>\n
  \   <span class=\"k\">def</span> <span class=\"nf\">plugins</span><span class=\"p\">(</span><span
  class=\"bp\">self</span><span class=\"p\">)</span> <span class=\"o\">-&gt;</span>
  <span class=\"n\">Plugins</span><span class=\"p\">:</span>\n        <span class=\"k\">try</span><span
  class=\"p\">:</span>\n            <span class=\"k\">return</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">_plugins</span>\n        <span class=\"k\">except</span>
  <span class=\"ne\">AttributeError</span><span class=\"p\">:</span>\n\n            <span
  class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">_plugins</span><span
  class=\"p\">:</span> <span class=\"n\">Plugins</span> <span class=\"o\">=</span>
  <span class=\"n\">Plugins</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">)</span>\n        <span class=\"k\">return</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">plugins</span>\n\n    <span class=\"nd\">@property</span>\n
  \   <span class=\"k\">def</span> <span class=\"nf\">summary</span><span class=\"p\">(</span><span
  class=\"bp\">self</span><span class=\"p\">)</span> <span class=\"o\">-&gt;</span>
  <span class=\"n\">Summary</span><span class=\"p\">:</span>\n        <span class=\"k\">try</span><span
  class=\"p\">:</span>\n            <span class=\"k\">return</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">_summary</span>\n        <span class=\"k\">except</span>
  <span class=\"ne\">AttributeError</span><span class=\"p\">:</span>\n\n            <span
  class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">_summary</span><span
  class=\"p\">:</span> <span class=\"n\">Summary</span> <span class=\"o\">=</span>
  <span class=\"n\">Summary</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">)</span>\n            <span class=\"k\">return</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">summary</span>\n\n    <span class=\"k\">def</span>
  <span class=\"nf\">__rich__</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"n\">Table</span><span
  class=\"p\">:</span>\n\n        <span class=\"n\">grid</span> <span class=\"o\">=</span>
  <span class=\"n\">Table</span><span class=\"o\">.</span><span class=\"n\">grid</span><span
  class=\"p\">()</span>\n        <span class=\"n\">grid</span><span class=\"o\">.</span><span
  class=\"n\">add_column</span><span class=\"p\">(</span><span class=\"s2\">&quot;label&quot;</span><span
  class=\"p\">)</span>\n        <span class=\"n\">grid</span><span class=\"o\">.</span><span
  class=\"n\">add_column</span><span class=\"p\">(</span><span class=\"s2\">&quot;value&quot;</span><span
  class=\"p\">)</span>\n\n        <span class=\"k\">for</span> <span class=\"n\">label</span><span
  class=\"p\">,</span> <span class=\"n\">value</span> <span class=\"ow\">in</span>
  <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">describe</span><span
  class=\"p\">()</span><span class=\"o\">.</span><span class=\"n\">items</span><span
  class=\"p\">():</span>\n            <span class=\"n\">grid</span><span class=\"o\">.</span><span
  class=\"n\">add_row</span><span class=\"p\">(</span><span class=\"n\">label</span><span
  class=\"p\">,</span> <span class=\"n\">value</span><span class=\"p\">)</span>\n\n
  \       <span class=\"k\">return</span> <span class=\"n\">grid</span>\n\n    <span
  class=\"k\">def</span> <span class=\"nf\">bust_cache</span><span class=\"p\">(</span><span
  class=\"bp\">self</span><span class=\"p\">)</span> <span class=\"o\">-&gt;</span>
  <span class=\"n\">Markata</span><span class=\"p\">:</span>\n        <span class=\"k\">with</span>
  <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">cache</span>
  <span class=\"k\">as</span> <span class=\"n\">cache</span><span class=\"p\">:</span>\n
  \           <span class=\"n\">cache</span><span class=\"o\">.</span><span class=\"n\">clear</span><span
  class=\"p\">()</span>\n        <span class=\"k\">return</span> <span class=\"bp\">self</span>\n\n
  \   <span class=\"nd\">@set_phase</span>\n    <span class=\"k\">def</span> <span
  class=\"nf\">configure</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"n\">Markata</span><span
  class=\"p\">:</span>\n        <span class=\"n\">sys</span><span class=\"o\">.</span><span
  class=\"n\">path</span><span class=\"o\">.</span><span class=\"n\">append</span><span
  class=\"p\">(</span><span class=\"n\">os</span><span class=\"o\">.</span><span class=\"n\">getcwd</span><span
  class=\"p\">())</span>\n        <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">config</span> <span class=\"o\">=</span> <span class=\"p\">{</span><span
  class=\"o\">**</span><span class=\"n\">DEFUALT_CONFIG</span><span class=\"p\">,</span>
  <span class=\"o\">**</span><span class=\"n\">standard_config</span><span class=\"o\">.</span><span
  class=\"n\">load</span><span class=\"p\">(</span><span class=\"s2\">&quot;markata&quot;</span><span
  class=\"p\">)}</span>\n        <span class=\"k\">if</span> <span class=\"nb\">isinstance</span><span
  class=\"p\">(</span><span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">config</span><span class=\"p\">[</span><span class=\"s2\">&quot;glob_patterns&quot;</span><span
  class=\"p\">],</span> <span class=\"nb\">str</span><span class=\"p\">):</span>\n
  \           <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">config</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;glob_patterns&quot;</span><span class=\"p\">]</span>
  <span class=\"o\">=</span> <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">config</span><span class=\"p\">[</span><span class=\"s2\">&quot;glob_patterns&quot;</span><span
  class=\"p\">]</span><span class=\"o\">.</span><span class=\"n\">split</span><span
  class=\"p\">(</span><span class=\"s2\">&quot;,&quot;</span><span class=\"p\">)</span>\n
  \       <span class=\"k\">elif</span> <span class=\"nb\">isinstance</span><span
  class=\"p\">(</span><span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">config</span><span class=\"p\">[</span><span class=\"s2\">&quot;glob_patterns&quot;</span><span
  class=\"p\">],</span> <span class=\"nb\">list</span><span class=\"p\">):</span>\n
  \           <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">config</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;glob_patterns&quot;</span><span class=\"p\">]</span>
  <span class=\"o\">=</span> <span class=\"nb\">list</span><span class=\"p\">(</span><span
  class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">config</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;glob_patterns&quot;</span><span class=\"p\">])</span>\n
  \       <span class=\"k\">else</span><span class=\"p\">:</span>\n            <span
  class=\"k\">raise</span> <span class=\"ne\">TypeError</span><span class=\"p\">(</span><span
  class=\"s2\">&quot;glob_patterns must be list or str&quot;</span><span class=\"p\">)</span>\n
  \       <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">glob_patterns</span>
  <span class=\"o\">=</span> <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">config</span><span class=\"p\">[</span><span class=\"s2\">&quot;glob_patterns&quot;</span><span
  class=\"p\">]</span>\n\n        <span class=\"k\">if</span> <span class=\"s2\">&quot;hooks&quot;</span>
  <span class=\"ow\">not</span> <span class=\"ow\">in</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">config</span><span class=\"p\">:</span>\n
  \           <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">hooks</span>
  <span class=\"o\">=</span> <span class=\"p\">[</span><span class=\"s2\">&quot;&quot;</span><span
  class=\"p\">]</span>\n        <span class=\"k\">if</span> <span class=\"nb\">isinstance</span><span
  class=\"p\">(</span><span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">config</span><span class=\"p\">[</span><span class=\"s2\">&quot;hooks&quot;</span><span
  class=\"p\">],</span> <span class=\"nb\">str</span><span class=\"p\">):</span>\n
  \           <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">hooks</span>
  <span class=\"o\">=</span> <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">config</span><span class=\"p\">[</span><span class=\"s2\">&quot;hooks&quot;</span><span
  class=\"p\">]</span><span class=\"o\">.</span><span class=\"n\">split</span><span
  class=\"p\">(</span><span class=\"s2\">&quot;,&quot;</span><span class=\"p\">)</span>\n
  \       <span class=\"k\">if</span> <span class=\"nb\">isinstance</span><span class=\"p\">(</span><span
  class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">config</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;hooks&quot;</span><span class=\"p\">],</span>
  <span class=\"nb\">list</span><span class=\"p\">):</span>\n            <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">hooks</span> <span class=\"o\">=</span> <span
  class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">config</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;hooks&quot;</span><span class=\"p\">]</span>\n\n
  \       <span class=\"k\">if</span> <span class=\"s2\">&quot;disabled_hooks&quot;</span>
  <span class=\"ow\">not</span> <span class=\"ow\">in</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">config</span><span class=\"p\">:</span>\n
  \           <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">disabled_hooks</span>
  <span class=\"o\">=</span> <span class=\"p\">[</span><span class=\"s2\">&quot;&quot;</span><span
  class=\"p\">]</span>\n        <span class=\"k\">if</span> <span class=\"nb\">isinstance</span><span
  class=\"p\">(</span><span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">config</span><span class=\"p\">[</span><span class=\"s2\">&quot;disabled_hooks&quot;</span><span
  class=\"p\">],</span> <span class=\"nb\">str</span><span class=\"p\">):</span>\n
  \           <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">disabled_hooks</span>
  <span class=\"o\">=</span> <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">config</span><span class=\"p\">[</span><span class=\"s2\">&quot;disabled_hooks&quot;</span><span
  class=\"p\">]</span><span class=\"o\">.</span><span class=\"n\">split</span><span
  class=\"p\">(</span><span class=\"s2\">&quot;,&quot;</span><span class=\"p\">)</span>\n
  \       <span class=\"k\">if</span> <span class=\"nb\">isinstance</span><span class=\"p\">(</span><span
  class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">config</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;disabled_hooks&quot;</span><span class=\"p\">],</span>
  <span class=\"nb\">list</span><span class=\"p\">):</span>\n            <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">disabled_hooks</span> <span class=\"o\">=</span>
  <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">config</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;disabled_hooks&quot;</span><span class=\"p\">]</span>\n\n
  \       <span class=\"k\">try</span><span class=\"p\">:</span>\n            <span
  class=\"n\">default_index</span> <span class=\"o\">=</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">hooks</span><span class=\"o\">.</span><span
  class=\"n\">index</span><span class=\"p\">(</span><span class=\"s2\">&quot;default&quot;</span><span
  class=\"p\">)</span>\n            <span class=\"n\">hooks</span> <span class=\"o\">=</span>
  <span class=\"p\">[</span>\n                <span class=\"o\">*</span><span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">hooks</span><span class=\"p\">[:</span><span
  class=\"n\">default_index</span><span class=\"p\">],</span>\n                <span
  class=\"o\">*</span><span class=\"n\">DEFAULT_HOOKS</span><span class=\"p\">,</span>\n
  \               <span class=\"o\">*</span><span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">hooks</span><span class=\"p\">[</span><span class=\"n\">default_index</span>
  <span class=\"o\">+</span> <span class=\"mi\">1</span> <span class=\"p\">:],</span>\n
  \           <span class=\"p\">]</span>\n            <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">hooks</span> <span class=\"o\">=</span> <span
  class=\"p\">[</span><span class=\"n\">hook</span> <span class=\"k\">for</span> <span
  class=\"n\">hook</span> <span class=\"ow\">in</span> <span class=\"n\">hooks</span>
  <span class=\"k\">if</span> <span class=\"n\">hook</span> <span class=\"ow\">not</span>
  <span class=\"ow\">in</span> <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">disabled_hooks</span><span class=\"p\">]</span>\n        <span class=\"k\">except</span>
  <span class=\"ne\">ValueError</span><span class=\"p\">:</span>\n            <span
  class=\"c1\"># &#39;default&#39; is not in hooks , do not replace with default_hooks</span>\n
  \           <span class=\"k\">pass</span>\n\n        <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">_pm</span> <span class=\"o\">=</span> <span
  class=\"n\">pluggy</span><span class=\"o\">.</span><span class=\"n\">PluginManager</span><span
  class=\"p\">(</span><span class=\"s2\">&quot;markata&quot;</span><span class=\"p\">)</span>\n
  \       <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">_pm</span><span
  class=\"o\">.</span><span class=\"n\">add_hookspecs</span><span class=\"p\">(</span><span
  class=\"n\">hookspec</span><span class=\"o\">.</span><span class=\"n\">MarkataSpecs</span><span
  class=\"p\">)</span>\n        <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">_register_hooks</span><span class=\"p\">()</span>\n\n        <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">_pm</span><span class=\"o\">.</span><span
  class=\"n\">hook</span><span class=\"o\">.</span><span class=\"n\">configure</span><span
  class=\"p\">(</span><span class=\"n\">markata</span><span class=\"o\">=</span><span
  class=\"bp\">self</span><span class=\"p\">)</span>\n        <span class=\"k\">return</span>
  <span class=\"bp\">self</span>\n\n    <span class=\"k\">def</span> <span class=\"nf\">get_plugin_config</span><span
  class=\"p\">(</span><span class=\"bp\">self</span><span class=\"p\">,</span> <span
  class=\"n\">path_or_name</span><span class=\"p\">:</span> <span class=\"nb\">str</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"n\">Dict</span><span
  class=\"p\">:</span>\n\n        <span class=\"n\">key</span> <span class=\"o\">=</span>
  <span class=\"n\">Path</span><span class=\"p\">(</span><span class=\"n\">path_or_name</span><span
  class=\"p\">)</span><span class=\"o\">.</span><span class=\"n\">stem</span>\n\n
  \       <span class=\"k\">try</span><span class=\"p\">:</span>\n            <span
  class=\"n\">config</span> <span class=\"o\">=</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">config</span><span class=\"p\">[</span><span
  class=\"n\">key</span><span class=\"p\">]</span>\n        <span class=\"k\">except</span>
  <span class=\"ne\">KeyError</span><span class=\"p\">:</span>\n            <span
  class=\"n\">config</span> <span class=\"o\">=</span> <span class=\"p\">{}</span>\n
  \       <span class=\"k\">if</span> <span class=\"ow\">not</span> <span class=\"nb\">isinstance</span><span
  class=\"p\">(</span><span class=\"n\">config</span><span class=\"p\">,</span> <span
  class=\"nb\">dict</span><span class=\"p\">):</span>\n            <span class=\"k\">raise</span>
  <span class=\"ne\">TypeError</span><span class=\"p\">(</span><span class=\"s2\">&quot;must
  use dict&quot;</span><span class=\"p\">)</span>\n        <span class=\"k\">if</span>
  <span class=\"s2\">&quot;cache_expire&quot;</span> <span class=\"ow\">not</span>
  <span class=\"ow\">in</span> <span class=\"n\">config</span><span class=\"o\">.</span><span
  class=\"n\">keys</span><span class=\"p\">():</span>\n            <span class=\"n\">config</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;cache_expire&quot;</span><span class=\"p\">]</span>
  <span class=\"o\">=</span> <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">config</span><span class=\"p\">[</span><span class=\"s2\">&quot;default_cache_expire&quot;</span><span
  class=\"p\">]</span>\n        <span class=\"k\">if</span> <span class=\"s2\">&quot;config_key&quot;</span>
  <span class=\"ow\">not</span> <span class=\"ow\">in</span> <span class=\"n\">config</span><span
  class=\"o\">.</span><span class=\"n\">keys</span><span class=\"p\">():</span>\n
  \           <span class=\"n\">config</span><span class=\"p\">[</span><span class=\"s2\">&quot;config_key&quot;</span><span
  class=\"p\">]</span> <span class=\"o\">=</span> <span class=\"n\">key</span>\n        <span
  class=\"k\">return</span> <span class=\"n\">config</span>\n\n    <span class=\"k\">def</span>
  <span class=\"nf\">get_config</span><span class=\"p\">(</span>\n        <span class=\"bp\">self</span><span
  class=\"p\">,</span> <span class=\"n\">key</span><span class=\"p\">:</span> <span
  class=\"nb\">str</span><span class=\"p\">,</span> <span class=\"n\">warn</span><span
  class=\"p\">:</span> <span class=\"nb\">bool</span> <span class=\"o\">=</span> <span
  class=\"kc\">True</span><span class=\"p\">,</span> <span class=\"n\">suggested</span><span
  class=\"p\">:</span> <span class=\"n\">Optional</span><span class=\"p\">[</span><span
  class=\"nb\">str</span><span class=\"p\">]</span> <span class=\"o\">=</span> <span
  class=\"kc\">None</span>\n    <span class=\"p\">)</span> <span class=\"o\">-&gt;</span>
  <span class=\"n\">Any</span><span class=\"p\">:</span>\n        <span class=\"k\">if</span>
  <span class=\"n\">key</span> <span class=\"ow\">in</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">config</span><span class=\"o\">.</span><span
  class=\"n\">keys</span><span class=\"p\">():</span>\n            <span class=\"k\">return</span>
  <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">config</span><span
  class=\"p\">[</span><span class=\"n\">key</span><span class=\"p\">]</span>\n        <span
  class=\"k\">else</span><span class=\"p\">:</span>\n\n            <span class=\"k\">if</span>
  <span class=\"n\">suggested</span> <span class=\"ow\">is</span> <span class=\"kc\">None</span><span
  class=\"p\">:</span>\n                <span class=\"n\">suggested</span> <span class=\"o\">=</span>
  <span class=\"n\">textwrap</span><span class=\"o\">.</span><span class=\"n\">dedent</span><span
  class=\"p\">(</span>\n                    <span class=\"sa\">f</span><span class=\"s2\">&quot;&quot;&quot;</span>\n<span
  class=\"s2\">                        \\[markata]</span>\n<span class=\"s2\">                        </span><span
  class=\"si\">{</span><span class=\"n\">key</span><span class=\"si\">}</span><span
  class=\"s2\"> = value</span>\n<span class=\"s2\">                    &quot;&quot;&quot;</span>
  \ <span class=\"c1\"># noqa: W605</span>\n                <span class=\"p\">)</span>\n
  \           <span class=\"k\">if</span> <span class=\"n\">warn</span><span class=\"p\">:</span>\n
  \               <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">console</span><span
  class=\"o\">.</span><span class=\"n\">log</span><span class=\"p\">(</span>\n                    <span
  class=\"n\">textwrap</span><span class=\"o\">.</span><span class=\"n\">dedent</span><span
  class=\"p\">(</span>\n                        <span class=\"sa\">f</span><span class=\"s2\">&quot;&quot;&quot;</span>\n<span
  class=\"s2\">                        Warning site_name is not set in markata config,
  sitemap will</span>\n<span class=\"s2\">                        be missing root
  site_name</span>\n<span class=\"s2\">                        to resolve this open
  your markata.toml and add</span>\n\n<span class=\"s2\">                        </span><span
  class=\"si\">{</span><span class=\"n\">suggested</span><span class=\"si\">}</span><span
  class=\"s2\"></span>\n\n<span class=\"s2\">                        &quot;&quot;&quot;</span>\n
  \                   <span class=\"p\">),</span>\n                    <span class=\"n\">style</span><span
  class=\"o\">=</span><span class=\"s2\">&quot;yellow&quot;</span><span class=\"p\">,</span>\n
  \               <span class=\"p\">)</span>\n\n    <span class=\"k\">def</span> <span
  class=\"nf\">make_hash</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">,</span> <span class=\"o\">*</span><span class=\"n\">keys</span><span
  class=\"p\">:</span> <span class=\"nb\">str</span><span class=\"p\">)</span> <span
  class=\"o\">-&gt;</span> <span class=\"nb\">str</span><span class=\"p\">:</span>\n
  \       <span class=\"n\">str_keys</span> <span class=\"o\">=</span> <span class=\"p\">[</span><span
  class=\"nb\">str</span><span class=\"p\">(</span><span class=\"n\">key</span><span
  class=\"p\">)</span> <span class=\"k\">for</span> <span class=\"n\">key</span> <span
  class=\"ow\">in</span> <span class=\"n\">keys</span><span class=\"p\">]</span>\n
  \       <span class=\"k\">return</span> <span class=\"n\">hashlib</span><span class=\"o\">.</span><span
  class=\"n\">md5</span><span class=\"p\">(</span><span class=\"s2\">&quot;&quot;</span><span
  class=\"o\">.</span><span class=\"n\">join</span><span class=\"p\">(</span><span
  class=\"n\">str_keys</span><span class=\"p\">)</span><span class=\"o\">.</span><span
  class=\"n\">encode</span><span class=\"p\">(</span><span class=\"s2\">&quot;utf-8&quot;</span><span
  class=\"p\">))</span><span class=\"o\">.</span><span class=\"n\">hexdigest</span><span
  class=\"p\">()</span>\n\n    <span class=\"nd\">@property</span>\n    <span class=\"k\">def</span>
  <span class=\"nf\">phase</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"nb\">str</span><span
  class=\"p\">:</span>\n        <span class=\"k\">return</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">_phase</span>\n\n    <span class=\"nd\">@phase</span><span
  class=\"o\">.</span><span class=\"n\">setter</span>\n    <span class=\"k\">def</span>
  <span class=\"nf\">phase</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">,</span> <span class=\"n\">value</span><span class=\"p\">:</span> <span
  class=\"nb\">str</span><span class=\"p\">)</span> <span class=\"o\">-&gt;</span>
  <span class=\"kc\">None</span><span class=\"p\">:</span>\n        <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">_phase</span> <span class=\"o\">=</span> <span
  class=\"n\">value</span>\n\n    <span class=\"nd\">@property</span>\n    <span class=\"k\">def</span>
  <span class=\"nf\">content_dir_hash</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"nb\">str</span><span
  class=\"p\">:</span>\n        <span class=\"n\">hashes</span> <span class=\"o\">=</span>
  <span class=\"p\">[</span><span class=\"n\">dirhash</span><span class=\"p\">(</span><span
  class=\"nb\">dir</span><span class=\"p\">)</span> <span class=\"k\">for</span> <span
  class=\"nb\">dir</span> <span class=\"ow\">in</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">content_directories</span><span class=\"p\">]</span>\n
  \       <span class=\"k\">return</span> <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">make_hash</span><span class=\"p\">(</span><span class=\"o\">*</span><span
  class=\"n\">hashes</span><span class=\"p\">)</span>\n\n    <span class=\"nd\">@property</span>\n
  \   <span class=\"k\">def</span> <span class=\"nf\">console</span><span class=\"p\">(</span><span
  class=\"bp\">self</span><span class=\"p\">)</span> <span class=\"o\">-&gt;</span>
  <span class=\"n\">Console</span><span class=\"p\">:</span>\n        <span class=\"k\">try</span><span
  class=\"p\">:</span>\n            <span class=\"k\">return</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">_console</span>\n        <span class=\"k\">except</span>
  <span class=\"ne\">AttributeError</span><span class=\"p\">:</span>\n            <span
  class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">_console</span>
  <span class=\"o\">=</span> <span class=\"n\">Console</span><span class=\"p\">()</span>\n
  \           <span class=\"k\">return</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">_console</span>\n\n    <span class=\"k\">def</span>
  <span class=\"nf\">describe</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"nb\">dict</span><span
  class=\"p\">[</span><span class=\"nb\">str</span><span class=\"p\">,</span> <span
  class=\"nb\">str</span><span class=\"p\">]:</span>\n        <span class=\"k\">return</span>
  <span class=\"p\">{</span><span class=\"s2\">&quot;version&quot;</span><span class=\"p\">:</span>
  <span class=\"n\">__version__</span><span class=\"p\">,</span> <span class=\"s2\">&quot;phase&quot;</span><span
  class=\"p\">:</span> <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">phase</span><span class=\"p\">}</span>\n\n    <span class=\"k\">def</span>
  <span class=\"nf\">_to_dict</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"nb\">dict</span><span
  class=\"p\">[</span><span class=\"nb\">str</span><span class=\"p\">,</span> <span
  class=\"n\">Iterable</span><span class=\"p\">]:</span>\n        <span class=\"k\">return</span>
  <span class=\"p\">{</span><span class=\"s2\">&quot;config&quot;</span><span class=\"p\">:</span>
  <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">config</span><span
  class=\"p\">,</span> <span class=\"s2\">&quot;articles&quot;</span><span class=\"p\">:</span>
  <span class=\"p\">[</span><span class=\"n\">a</span><span class=\"o\">.</span><span
  class=\"n\">to_dict</span><span class=\"p\">()</span> <span class=\"k\">for</span>
  <span class=\"n\">a</span> <span class=\"ow\">in</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">articles</span><span class=\"p\">]}</span>\n\n
  \   <span class=\"k\">def</span> <span class=\"nf\">to_dict</span><span class=\"p\">(</span><span
  class=\"bp\">self</span><span class=\"p\">)</span> <span class=\"o\">-&gt;</span>
  <span class=\"nb\">dict</span><span class=\"p\">:</span>\n        <span class=\"k\">try</span><span
  class=\"p\">:</span>\n            <span class=\"k\">return</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">_to_dict</span><span class=\"p\">()</span>\n
  \       <span class=\"k\">except</span> <span class=\"ne\">AttributeError</span><span
  class=\"p\">:</span>\n            <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">render</span><span class=\"p\">()</span>\n            <span class=\"k\">return</span>
  <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">_to_dict</span><span
  class=\"p\">()</span>\n\n    <span class=\"k\">def</span> <span class=\"nf\">to_json</span><span
  class=\"p\">(</span><span class=\"bp\">self</span><span class=\"p\">)</span> <span
  class=\"o\">-&gt;</span> <span class=\"nb\">str</span><span class=\"p\">:</span>\n
  \       <span class=\"kn\">import</span> <span class=\"nn\">json</span>\n\n        <span
  class=\"k\">return</span> <span class=\"n\">json</span><span class=\"o\">.</span><span
  class=\"n\">dumps</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">to_dict</span><span class=\"p\">(),</span>
  <span class=\"n\">indent</span><span class=\"o\">=</span><span class=\"mi\">4</span><span
  class=\"p\">,</span> <span class=\"n\">sort_keys</span><span class=\"o\">=</span><span
  class=\"kc\">True</span><span class=\"p\">,</span> <span class=\"n\">default</span><span
  class=\"o\">=</span><span class=\"nb\">str</span><span class=\"p\">)</span>\n\n
  \   <span class=\"k\">def</span> <span class=\"nf\">_register_hooks</span><span
  class=\"p\">(</span><span class=\"bp\">self</span><span class=\"p\">)</span> <span
  class=\"o\">-&gt;</span> <span class=\"kc\">None</span><span class=\"p\">:</span>\n
  \       <span class=\"k\">for</span> <span class=\"n\">hook</span> <span class=\"ow\">in</span>
  <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">hooks</span><span
  class=\"p\">:</span>\n            <span class=\"k\">try</span><span class=\"p\">:</span>\n
  \               <span class=\"c1\"># module style plugins</span>\n                <span
  class=\"n\">plugin</span> <span class=\"o\">=</span> <span class=\"n\">importlib</span><span
  class=\"o\">.</span><span class=\"n\">import_module</span><span class=\"p\">(</span><span
  class=\"n\">hook</span><span class=\"p\">)</span>\n            <span class=\"k\">except</span>
  <span class=\"ne\">ModuleNotFoundError</span> <span class=\"k\">as</span> <span
  class=\"n\">e</span><span class=\"p\">:</span>\n                <span class=\"c1\">#
  class style plugins</span>\n                <span class=\"k\">if</span> <span class=\"s2\">&quot;.&quot;</span>
  <span class=\"ow\">in</span> <span class=\"n\">hook</span><span class=\"p\">:</span>\n
  \                   <span class=\"n\">mod</span> <span class=\"o\">=</span> <span
  class=\"n\">importlib</span><span class=\"o\">.</span><span class=\"n\">import_module</span><span
  class=\"p\">(</span><span class=\"s2\">&quot;.&quot;</span><span class=\"o\">.</span><span
  class=\"n\">join</span><span class=\"p\">(</span><span class=\"n\">hook</span><span
  class=\"o\">.</span><span class=\"n\">split</span><span class=\"p\">(</span><span
  class=\"s2\">&quot;.&quot;</span><span class=\"p\">)[:</span><span class=\"o\">-</span><span
  class=\"mi\">1</span><span class=\"p\">]))</span>\n                    <span class=\"n\">plugin</span>
  <span class=\"o\">=</span> <span class=\"nb\">getattr</span><span class=\"p\">(</span><span
  class=\"n\">mod</span><span class=\"p\">,</span> <span class=\"n\">hook</span><span
  class=\"o\">.</span><span class=\"n\">split</span><span class=\"p\">(</span><span
  class=\"s2\">&quot;.&quot;</span><span class=\"p\">)[</span><span class=\"o\">-</span><span
  class=\"mi\">1</span><span class=\"p\">])</span>\n                <span class=\"k\">else</span><span
  class=\"p\">:</span>\n                    <span class=\"k\">raise</span> <span class=\"n\">e</span>\n\n
  \           <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">_pm</span><span
  class=\"o\">.</span><span class=\"n\">register</span><span class=\"p\">(</span><span
  class=\"n\">plugin</span><span class=\"p\">)</span>\n\n    <span class=\"k\">def</span>
  <span class=\"fm\">__iter__</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">,</span> <span class=\"n\">description</span><span class=\"p\">:</span>
  <span class=\"nb\">str</span> <span class=\"o\">=</span> <span class=\"s2\">&quot;working...&quot;</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"n\">Iterable</span><span
  class=\"p\">[</span><span class=\"n\">frontmatter</span><span class=\"o\">.</span><span
  class=\"n\">Post</span><span class=\"p\">]:</span>\n        <span class=\"n\">articles</span><span
  class=\"p\">:</span> <span class=\"n\">Iterable</span><span class=\"p\">[</span><span
  class=\"n\">frontmatter</span><span class=\"o\">.</span><span class=\"n\">Post</span><span
  class=\"p\">]</span> <span class=\"o\">=</span> <span class=\"n\">track</span><span
  class=\"p\">(</span>\n            <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">articles</span><span class=\"p\">,</span> <span class=\"n\">description</span><span
  class=\"o\">=</span><span class=\"n\">description</span><span class=\"p\">,</span>
  <span class=\"n\">transient</span><span class=\"o\">=</span><span class=\"kc\">True</span><span
  class=\"p\">,</span> <span class=\"n\">console</span><span class=\"o\">=</span><span
  class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">console</span>\n
  \       <span class=\"p\">)</span>\n        <span class=\"k\">return</span> <span
  class=\"n\">articles</span>\n\n    <span class=\"k\">def</span> <span class=\"nf\">iter_articles</span><span
  class=\"p\">(</span><span class=\"bp\">self</span><span class=\"p\">,</span> <span
  class=\"n\">description</span><span class=\"p\">:</span> <span class=\"nb\">str</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"n\">Iterable</span><span
  class=\"p\">[</span><span class=\"n\">frontmatter</span><span class=\"o\">.</span><span
  class=\"n\">Post</span><span class=\"p\">]:</span>\n        <span class=\"n\">articles</span><span
  class=\"p\">:</span> <span class=\"n\">Iterable</span><span class=\"p\">[</span><span
  class=\"n\">frontmatter</span><span class=\"o\">.</span><span class=\"n\">Post</span><span
  class=\"p\">]</span> <span class=\"o\">=</span> <span class=\"n\">track</span><span
  class=\"p\">(</span>\n            <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">articles</span><span class=\"p\">,</span> <span class=\"n\">description</span><span
  class=\"o\">=</span><span class=\"n\">description</span><span class=\"p\">,</span>
  <span class=\"n\">transient</span><span class=\"o\">=</span><span class=\"kc\">True</span><span
  class=\"p\">,</span> <span class=\"n\">console</span><span class=\"o\">=</span><span
  class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">console</span>\n
  \       <span class=\"p\">)</span>\n        <span class=\"k\">return</span> <span
  class=\"n\">articles</span>\n\n    <span class=\"nd\">@set_phase</span>\n    <span
  class=\"k\">def</span> <span class=\"nf\">glob</span><span class=\"p\">(</span><span
  class=\"bp\">self</span><span class=\"p\">)</span> <span class=\"o\">-&gt;</span>
  <span class=\"n\">Markata</span><span class=\"p\">:</span>\n        <span class=\"sd\">&quot;&quot;&quot;run
  glob hooks</span>\n\n<span class=\"sd\">        Glob hooks should append file lists
  to the markata object for later</span>\n<span class=\"sd\">        hooks to build
  from.  The default loader will utilize the `files`</span>\n<span class=\"sd\">        attribute
  for loading.</span>\n<span class=\"sd\">        &quot;&quot;&quot;</span>\n\n        <span
  class=\"k\">try</span><span class=\"p\">:</span>\n            <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">_pm</span><span class=\"o\">.</span><span
  class=\"n\">hook</span><span class=\"o\">.</span><span class=\"n\">glob</span><span
  class=\"p\">(</span><span class=\"n\">markata</span><span class=\"o\">=</span><span
  class=\"bp\">self</span><span class=\"p\">)</span>\n        <span class=\"k\">except</span>
  <span class=\"ne\">AttributeError</span><span class=\"p\">:</span>\n            <span
  class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">configure</span><span
  class=\"p\">()</span>\n            <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">_pm</span><span class=\"o\">.</span><span class=\"n\">hook</span><span
  class=\"o\">.</span><span class=\"n\">glob</span><span class=\"p\">(</span><span
  class=\"n\">markata</span><span class=\"o\">=</span><span class=\"bp\">self</span><span
  class=\"p\">)</span>\n\n        <span class=\"k\">return</span> <span class=\"bp\">self</span>\n\n
  \   <span class=\"nd\">@set_phase</span>\n    <span class=\"k\">def</span> <span
  class=\"nf\">load</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"n\">Markata</span><span
  class=\"p\">:</span>\n        <span class=\"k\">try</span><span class=\"p\">:</span>\n
  \           <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">_pm</span><span
  class=\"o\">.</span><span class=\"n\">hook</span><span class=\"o\">.</span><span
  class=\"n\">load</span><span class=\"p\">(</span><span class=\"n\">markata</span><span
  class=\"o\">=</span><span class=\"bp\">self</span><span class=\"p\">)</span>\n        <span
  class=\"k\">except</span> <span class=\"ne\">AttributeError</span><span class=\"p\">:</span>\n
  \           <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">glob</span><span
  class=\"p\">()</span>\n            <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">_pm</span><span class=\"o\">.</span><span class=\"n\">hook</span><span
  class=\"o\">.</span><span class=\"n\">load</span><span class=\"p\">(</span><span
  class=\"n\">markata</span><span class=\"o\">=</span><span class=\"bp\">self</span><span
  class=\"p\">)</span>\n        <span class=\"k\">return</span> <span class=\"bp\">self</span>\n\n
  \   <span class=\"c1\"># @set_phase</span>\n    <span class=\"k\">def</span> <span
  class=\"nf\">pre_render</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"n\">Markata</span><span
  class=\"p\">:</span>\n        <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">_pm</span><span class=\"o\">.</span><span class=\"n\">hook</span><span
  class=\"o\">.</span><span class=\"n\">pre_render</span><span class=\"p\">(</span><span
  class=\"n\">markata</span><span class=\"o\">=</span><span class=\"bp\">self</span><span
  class=\"p\">)</span>\n        <span class=\"k\">return</span> <span class=\"bp\">self</span>\n\n
  \   <span class=\"c1\"># @set_phase</span>\n    <span class=\"k\">def</span> <span
  class=\"nf\">render</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"n\">Markata</span><span
  class=\"p\">:</span>\n        <span class=\"k\">try</span><span class=\"p\">:</span>\n
  \           <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">_pm</span><span
  class=\"o\">.</span><span class=\"n\">hook</span><span class=\"o\">.</span><span
  class=\"n\">pre_render</span><span class=\"p\">(</span><span class=\"n\">markata</span><span
  class=\"o\">=</span><span class=\"bp\">self</span><span class=\"p\">)</span>\n            <span
  class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">_pm</span><span
  class=\"o\">.</span><span class=\"n\">hook</span><span class=\"o\">.</span><span
  class=\"n\">render</span><span class=\"p\">(</span><span class=\"n\">markata</span><span
  class=\"o\">=</span><span class=\"bp\">self</span><span class=\"p\">)</span>\n            <span
  class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">_pm</span><span
  class=\"o\">.</span><span class=\"n\">hook</span><span class=\"o\">.</span><span
  class=\"n\">post_render</span><span class=\"p\">(</span><span class=\"n\">markata</span><span
  class=\"o\">=</span><span class=\"bp\">self</span><span class=\"p\">)</span>\n        <span
  class=\"k\">except</span> <span class=\"ne\">AttributeError</span><span class=\"p\">:</span>\n
  \           <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">load</span><span
  class=\"p\">()</span>\n            <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">_pm</span><span class=\"o\">.</span><span class=\"n\">hook</span><span
  class=\"o\">.</span><span class=\"n\">pre_render</span><span class=\"p\">(</span><span
  class=\"n\">markata</span><span class=\"o\">=</span><span class=\"bp\">self</span><span
  class=\"p\">)</span>\n            <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">_pm</span><span class=\"o\">.</span><span class=\"n\">hook</span><span
  class=\"o\">.</span><span class=\"n\">render</span><span class=\"p\">(</span><span
  class=\"n\">markata</span><span class=\"o\">=</span><span class=\"bp\">self</span><span
  class=\"p\">)</span>\n            <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">_pm</span><span class=\"o\">.</span><span class=\"n\">hook</span><span
  class=\"o\">.</span><span class=\"n\">post_render</span><span class=\"p\">(</span><span
  class=\"n\">markata</span><span class=\"o\">=</span><span class=\"bp\">self</span><span
  class=\"p\">)</span>\n        <span class=\"k\">return</span> <span class=\"bp\">self</span>\n\n
  \   <span class=\"c1\"># @set_phase</span>\n    <span class=\"k\">def</span> <span
  class=\"nf\">post_render</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"n\">Markata</span><span
  class=\"p\">:</span>\n        <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">_pm</span><span class=\"o\">.</span><span class=\"n\">hook</span><span
  class=\"o\">.</span><span class=\"n\">post_render</span><span class=\"p\">(</span><span
  class=\"n\">markata</span><span class=\"o\">=</span><span class=\"bp\">self</span><span
  class=\"p\">)</span>\n        <span class=\"k\">return</span> <span class=\"bp\">self</span>\n\n
  \   <span class=\"c1\"># @set_phase</span>\n    <span class=\"k\">def</span> <span
  class=\"nf\">save</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"n\">Markata</span><span
  class=\"p\">:</span>\n        <span class=\"k\">try</span><span class=\"p\">:</span>\n
  \           <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">_pm</span><span
  class=\"o\">.</span><span class=\"n\">hook</span><span class=\"o\">.</span><span
  class=\"n\">save</span><span class=\"p\">(</span><span class=\"n\">markata</span><span
  class=\"o\">=</span><span class=\"bp\">self</span><span class=\"p\">)</span>\n        <span
  class=\"k\">except</span> <span class=\"ne\">AttributeError</span><span class=\"p\">:</span>\n
  \           <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">render</span><span
  class=\"p\">()</span>\n            <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">_pm</span><span class=\"o\">.</span><span class=\"n\">hook</span><span
  class=\"o\">.</span><span class=\"n\">save</span><span class=\"p\">(</span><span
  class=\"n\">markata</span><span class=\"o\">=</span><span class=\"bp\">self</span><span
  class=\"p\">)</span>\n        <span class=\"k\">return</span> <span class=\"bp\">self</span>\n\n
  \   <span class=\"k\">def</span> <span class=\"nf\">run</span><span class=\"p\">(</span><span
  class=\"bp\">self</span><span class=\"p\">,</span> <span class=\"n\">lifecycle</span><span
  class=\"p\">:</span> <span class=\"n\">LifeCycle</span> <span class=\"o\">=</span>
  <span class=\"kc\">None</span><span class=\"p\">)</span> <span class=\"o\">-&gt;</span>
  <span class=\"n\">Markata</span><span class=\"p\">:</span>\n        <span class=\"k\">if</span>
  <span class=\"n\">lifecycle</span> <span class=\"ow\">is</span> <span class=\"kc\">None</span><span
  class=\"p\">:</span>\n            <span class=\"n\">lifecycle</span> <span class=\"o\">=</span>
  <span class=\"nb\">getattr</span><span class=\"p\">(</span><span class=\"n\">LifeCycle</span><span
  class=\"p\">,</span> <span class=\"nb\">max</span><span class=\"p\">(</span><span
  class=\"n\">LifeCycle</span><span class=\"o\">.</span><span class=\"n\">_member_map_</span><span
  class=\"p\">))</span>\n\n        <span class=\"k\">if</span> <span class=\"nb\">isinstance</span><span
  class=\"p\">(</span><span class=\"n\">lifecycle</span><span class=\"p\">,</span>
  <span class=\"nb\">str</span><span class=\"p\">):</span>\n            <span class=\"n\">lifecycle</span>
  <span class=\"o\">=</span> <span class=\"n\">LifeCycle</span><span class=\"p\">[</span><span
  class=\"n\">lifecycle</span><span class=\"p\">]</span>\n\n        <span class=\"n\">stages_to_run</span>
  <span class=\"o\">=</span> <span class=\"p\">[</span><span class=\"n\">m</span>
  <span class=\"k\">for</span> <span class=\"n\">m</span> <span class=\"ow\">in</span>
  <span class=\"n\">LifeCycle</span><span class=\"o\">.</span><span class=\"n\">_member_map_</span>
  <span class=\"k\">if</span> <span class=\"n\">LifeCycle</span><span class=\"p\">[</span><span
  class=\"n\">m</span><span class=\"p\">]</span> <span class=\"o\">&lt;=</span> <span
  class=\"n\">lifecycle</span><span class=\"p\">]</span>\n\n        <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">console</span><span class=\"o\">.</span><span
  class=\"n\">log</span><span class=\"p\">(</span><span class=\"sa\">f</span><span
  class=\"s2\">&quot;running </span><span class=\"si\">{</span><span class=\"n\">stages_to_run</span><span
  class=\"si\">}</span><span class=\"s2\">&quot;</span><span class=\"p\">)</span>\n
  \       <span class=\"k\">for</span> <span class=\"n\">stage</span> <span class=\"ow\">in</span>
  <span class=\"n\">stages_to_run</span><span class=\"p\">:</span>\n            <span
  class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">console</span><span
  class=\"o\">.</span><span class=\"n\">log</span><span class=\"p\">(</span><span
  class=\"sa\">f</span><span class=\"s2\">&quot;</span><span class=\"si\">{</span><span
  class=\"n\">stage</span><span class=\"si\">}</span><span class=\"s2\"> running&quot;</span><span
  class=\"p\">)</span>\n            <span class=\"nb\">getattr</span><span class=\"p\">(</span><span
  class=\"bp\">self</span><span class=\"p\">,</span> <span class=\"n\">stage</span><span
  class=\"p\">)()</span>\n            <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">console</span><span class=\"o\">.</span><span class=\"n\">log</span><span
  class=\"p\">(</span><span class=\"sa\">f</span><span class=\"s2\">&quot;</span><span
  class=\"si\">{</span><span class=\"n\">stage</span><span class=\"si\">}</span><span
  class=\"s2\"> complete&quot;</span><span class=\"p\">)</span>\n\n        <span class=\"k\">with</span>
  <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">cache</span>
  <span class=\"k\">as</span> <span class=\"n\">cache</span><span class=\"p\">:</span>\n
  \           <span class=\"n\">hits</span><span class=\"p\">,</span> <span class=\"n\">misses</span>
  <span class=\"o\">=</span> <span class=\"n\">cache</span><span class=\"o\">.</span><span
  class=\"n\">stats</span><span class=\"p\">()</span>\n\n        <span class=\"k\">if</span>
  <span class=\"n\">hits</span> <span class=\"o\">+</span> <span class=\"n\">misses</span>
  <span class=\"o\">&gt;</span> <span class=\"mi\">0</span><span class=\"p\">:</span>\n
  \           <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">console</span><span
  class=\"o\">.</span><span class=\"n\">log</span><span class=\"p\">(</span><span
  class=\"sa\">f</span><span class=\"s2\">&quot;cache hit rate </span><span class=\"si\">{</span><span
  class=\"nb\">round</span><span class=\"p\">(</span><span class=\"n\">hits</span><span
  class=\"o\">/</span> <span class=\"p\">(</span><span class=\"n\">hits</span> <span
  class=\"o\">+</span> <span class=\"n\">misses</span><span class=\"p\">)</span><span
  class=\"o\">*</span><span class=\"mi\">100</span><span class=\"p\">,</span> <span
  class=\"mi\">2</span><span class=\"p\">)</span><span class=\"si\">}</span><span
  class=\"s2\">%&quot;</span><span class=\"p\">)</span>\n        <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">console</span><span class=\"o\">.</span><span
  class=\"n\">log</span><span class=\"p\">(</span><span class=\"sa\">f</span><span
  class=\"s2\">&quot;cache hits/misses </span><span class=\"si\">{</span><span class=\"n\">hits</span><span
  class=\"si\">}</span><span class=\"s2\">/</span><span class=\"si\">{</span><span
  class=\"n\">misses</span><span class=\"si\">}</span><span class=\"s2\">&quot;</span><span
  class=\"p\">)</span>\n\n        <span class=\"k\">return</span> <span class=\"bp\">self</span>\n\n
  \   <span class=\"k\">def</span> <span class=\"nf\">filter</span><span class=\"p\">(</span><span
  class=\"bp\">self</span><span class=\"p\">,</span> <span class=\"nb\">filter</span><span
  class=\"p\">:</span> <span class=\"nb\">str</span><span class=\"p\">)</span> <span
  class=\"o\">-&gt;</span> <span class=\"n\">List</span><span class=\"p\">:</span>\n
  \       <span class=\"k\">def</span> <span class=\"nf\">evalr</span><span class=\"p\">(</span><span
  class=\"n\">a</span><span class=\"p\">:</span> <span class=\"n\">Post</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"n\">Any</span><span
  class=\"p\">:</span>\n            <span class=\"k\">try</span><span class=\"p\">:</span>\n
  \               <span class=\"k\">return</span> <span class=\"nb\">eval</span><span
  class=\"p\">(</span><span class=\"nb\">filter</span><span class=\"p\">,</span> <span
  class=\"p\">{</span><span class=\"o\">**</span><span class=\"n\">a</span><span class=\"o\">.</span><span
  class=\"n\">to_dict</span><span class=\"p\">(),</span> <span class=\"s2\">&quot;timedelta&quot;</span><span
  class=\"p\">:</span> <span class=\"n\">timedelta</span><span class=\"p\">},</span>
  <span class=\"p\">{})</span>\n            <span class=\"k\">except</span> <span
  class=\"ne\">AttributeError</span><span class=\"p\">:</span>\n                <span
  class=\"k\">return</span> <span class=\"nb\">eval</span><span class=\"p\">(</span><span
  class=\"nb\">filter</span><span class=\"p\">,</span> <span class=\"p\">{</span><span
  class=\"o\">**</span><span class=\"n\">a</span><span class=\"p\">,</span> <span
  class=\"s2\">&quot;timedelta&quot;</span><span class=\"p\">:</span> <span class=\"n\">timedelta</span><span
  class=\"p\">},</span> <span class=\"p\">{})</span>\n\n        <span class=\"k\">return</span>
  <span class=\"p\">[</span><span class=\"n\">a</span> <span class=\"k\">for</span>
  <span class=\"n\">a</span> <span class=\"ow\">in</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">articles</span> <span class=\"k\">if</span>
  <span class=\"n\">evalr</span><span class=\"p\">(</span><span class=\"n\">a</span><span
  class=\"p\">)]</span>\n\n    <span class=\"k\">def</span> <span class=\"nf\">map</span><span
  class=\"p\">(</span>\n        <span class=\"bp\">self</span><span class=\"p\">,</span>
  <span class=\"n\">func</span><span class=\"p\">:</span> <span class=\"nb\">str</span>
  <span class=\"o\">=</span> <span class=\"s2\">&quot;title&quot;</span><span class=\"p\">,</span>
  <span class=\"nb\">filter</span><span class=\"p\">:</span> <span class=\"nb\">str</span>
  <span class=\"o\">=</span> <span class=\"s2\">&quot;True&quot;</span><span class=\"p\">,</span>
  <span class=\"n\">sort</span><span class=\"p\">:</span> <span class=\"nb\">str</span>
  <span class=\"o\">=</span> <span class=\"s2\">&quot;True&quot;</span>\n    <span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"n\">List</span><span
  class=\"p\">:</span>\n        <span class=\"kn\">import</span> <span class=\"nn\">copy</span>\n\n
  \       <span class=\"k\">def</span> <span class=\"nf\">try_sort</span><span class=\"p\">(</span><span
  class=\"n\">a</span><span class=\"p\">:</span> <span class=\"n\">Any</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"nb\">int</span><span
  class=\"p\">:</span>\n\n            <span class=\"k\">try</span><span class=\"p\">:</span>\n
  \               <span class=\"n\">value</span> <span class=\"o\">=</span> <span
  class=\"nb\">eval</span><span class=\"p\">(</span><span class=\"n\">sort</span><span
  class=\"p\">,</span> <span class=\"n\">a</span><span class=\"o\">.</span><span class=\"n\">to_dict</span><span
  class=\"p\">(),</span> <span class=\"p\">{})</span>\n            <span class=\"k\">except</span>
  <span class=\"ne\">NameError</span><span class=\"p\">:</span>\n                <span
  class=\"k\">return</span> <span class=\"o\">-</span><span class=\"mi\">1</span>\n
  \           <span class=\"k\">try</span><span class=\"p\">:</span>\n                <span
  class=\"k\">return</span> <span class=\"nb\">int</span><span class=\"p\">(</span><span
  class=\"n\">value</span><span class=\"p\">)</span>\n            <span class=\"k\">except</span>
  <span class=\"ne\">TypeError</span><span class=\"p\">:</span>\n                <span
  class=\"k\">try</span><span class=\"p\">:</span>\n                    <span class=\"k\">return</span>
  <span class=\"nb\">int</span><span class=\"p\">(</span><span class=\"n\">value</span><span
  class=\"o\">.</span><span class=\"n\">timestamp</span><span class=\"p\">())</span>\n
  \               <span class=\"k\">except</span> <span class=\"ne\">Exception</span><span
  class=\"p\">:</span>\n                    <span class=\"k\">try</span><span class=\"p\">:</span>\n
  \                       <span class=\"k\">return</span> <span class=\"nb\">int</span><span
  class=\"p\">(</span>\n                            <span class=\"n\">datetime</span><span
  class=\"o\">.</span><span class=\"n\">datetime</span><span class=\"o\">.</span><span
  class=\"n\">combine</span><span class=\"p\">(</span>\n                                <span
  class=\"n\">value</span><span class=\"p\">,</span> <span class=\"n\">datetime</span><span
  class=\"o\">.</span><span class=\"n\">datetime</span><span class=\"o\">.</span><span
  class=\"n\">min</span><span class=\"o\">.</span><span class=\"n\">time</span><span
  class=\"p\">()</span>\n                            <span class=\"p\">)</span><span
  class=\"o\">.</span><span class=\"n\">timestamp</span><span class=\"p\">()</span>\n
  \                       <span class=\"p\">)</span>\n                    <span class=\"k\">except</span>
  <span class=\"ne\">Exception</span><span class=\"p\">:</span>\n                        <span
  class=\"k\">try</span><span class=\"p\">:</span>\n                            <span
  class=\"k\">return</span> <span class=\"nb\">sum</span><span class=\"p\">([</span><span
  class=\"nb\">ord</span><span class=\"p\">(</span><span class=\"n\">c</span><span
  class=\"p\">)</span> <span class=\"k\">for</span> <span class=\"n\">c</span> <span
  class=\"ow\">in</span> <span class=\"nb\">str</span><span class=\"p\">(</span><span
  class=\"n\">value</span><span class=\"p\">)])</span>\n                        <span
  class=\"k\">except</span> <span class=\"ne\">Exception</span><span class=\"p\">:</span>\n
  \                           <span class=\"k\">return</span> <span class=\"o\">-</span><span
  class=\"mi\">1</span>\n\n        <span class=\"n\">articles</span> <span class=\"o\">=</span>
  <span class=\"n\">copy</span><span class=\"o\">.</span><span class=\"n\">copy</span><span
  class=\"p\">(</span><span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">articles</span><span class=\"p\">)</span>\n        <span class=\"n\">articles</span><span
  class=\"o\">.</span><span class=\"n\">sort</span><span class=\"p\">(</span><span
  class=\"n\">key</span><span class=\"o\">=</span><span class=\"n\">try_sort</span><span
  class=\"p\">)</span>\n        <span class=\"k\">return</span> <span class=\"p\">[</span>\n
  \           <span class=\"nb\">eval</span><span class=\"p\">(</span><span class=\"n\">func</span><span
  class=\"p\">,</span> <span class=\"p\">{</span><span class=\"o\">**</span><span
  class=\"n\">a</span><span class=\"o\">.</span><span class=\"n\">to_dict</span><span
  class=\"p\">(),</span> <span class=\"s2\">&quot;timedelta&quot;</span><span class=\"p\">:</span>
  <span class=\"n\">timedelta</span><span class=\"p\">},</span> <span class=\"p\">{})</span>\n
  \           <span class=\"k\">for</span> <span class=\"n\">a</span> <span class=\"ow\">in</span>
  <span class=\"n\">articles</span>\n            <span class=\"k\">if</span> <span
  class=\"nb\">eval</span><span class=\"p\">(</span><span class=\"nb\">filter</span><span
  class=\"p\">,</span> <span class=\"p\">{</span><span class=\"o\">**</span><span
  class=\"n\">a</span><span class=\"o\">.</span><span class=\"n\">to_dict</span><span
  class=\"p\">(),</span> <span class=\"s2\">&quot;timedelta&quot;</span><span class=\"p\">:</span>
  <span class=\"n\">timedelta</span><span class=\"p\">},</span> <span class=\"p\">{})</span>\n
  \       <span class=\"p\">]</span>\n</code></pre></div>\n</details>\n<hr />\n<h2
  id=\"clif-function\">clif <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>clif
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">clif</span><span class=\"p\">()</span> <span class=\"o\">-&gt;</span>
  <span class=\"kc\">None</span><span class=\"p\">:</span>\n    <span class=\"kn\">import</span>
  <span class=\"nn\">sys</span>\n    <span class=\"kn\">import</span> <span class=\"nn\">time</span>\n\n
  \   <span class=\"kn\">from</span> <span class=\"nn\">rich</span> <span class=\"kn\">import</span>
  <span class=\"n\">pretty</span><span class=\"p\">,</span> <span class=\"n\">traceback</span>\n\n
  \   <span class=\"k\">if</span> <span class=\"s2\">&quot;--no-rich&quot;</span>
  <span class=\"ow\">not</span> <span class=\"ow\">in</span> <span class=\"n\">sys</span><span
  class=\"o\">.</span><span class=\"n\">argv</span><span class=\"p\">:</span>\n        <span
  class=\"n\">pretty</span><span class=\"o\">.</span><span class=\"n\">install</span><span
  class=\"p\">()</span>\n        <span class=\"n\">traceback</span><span class=\"o\">.</span><span
  class=\"n\">install</span><span class=\"p\">()</span>\n\n    <span class=\"n\">m</span>
  <span class=\"o\">=</span> <span class=\"n\">Markata</span><span class=\"p\">()</span>\n\n
  \   <span class=\"k\">if</span> <span class=\"s2\">&quot;--quiet&quot;</span> <span
  class=\"ow\">in</span> <span class=\"n\">sys</span><span class=\"o\">.</span><span
  class=\"n\">argv</span> <span class=\"ow\">or</span> <span class=\"s2\">&quot;-q&quot;</span>
  <span class=\"ow\">in</span> <span class=\"n\">sys</span><span class=\"o\">.</span><span
  class=\"n\">argv</span><span class=\"p\">:</span>\n        <span class=\"n\">m</span><span
  class=\"o\">.</span><span class=\"n\">console</span><span class=\"o\">.</span><span
  class=\"n\">quiet</span> <span class=\"o\">=</span> <span class=\"kc\">True</span>\n
  \   <span class=\"k\">else</span><span class=\"p\">:</span>\n        <span class=\"n\">m</span><span
  class=\"o\">.</span><span class=\"n\">console</span><span class=\"o\">.</span><span
  class=\"n\">print</span><span class=\"p\">(</span><span class=\"s2\">&quot;console
  options:&quot;</span><span class=\"p\">,</span> <span class=\"n\">m</span><span
  class=\"o\">.</span><span class=\"n\">console</span><span class=\"o\">.</span><span
  class=\"n\">options</span><span class=\"p\">)</span>\n\n    <span class=\"k\">if</span>
  <span class=\"s2\">&quot;--to-dict&quot;</span> <span class=\"ow\">in</span> <span
  class=\"n\">sys</span><span class=\"o\">.</span><span class=\"n\">argv</span><span
  class=\"p\">:</span>\n        <span class=\"n\">m</span><span class=\"o\">.</span><span
  class=\"n\">console</span><span class=\"o\">.</span><span class=\"n\">quiet</span>
  <span class=\"o\">=</span> <span class=\"kc\">True</span>\n        <span class=\"n\">data</span>
  <span class=\"o\">=</span> <span class=\"n\">m</span><span class=\"o\">.</span><span
  class=\"n\">to_dict</span><span class=\"p\">()</span>\n        <span class=\"n\">m</span><span
  class=\"o\">.</span><span class=\"n\">console</span><span class=\"o\">.</span><span
  class=\"n\">quiet</span> <span class=\"o\">=</span> <span class=\"kc\">False</span>\n
  \       <span class=\"n\">m</span><span class=\"o\">.</span><span class=\"n\">console</span><span
  class=\"o\">.</span><span class=\"n\">print</span><span class=\"p\">(</span><span
  class=\"n\">data</span><span class=\"p\">)</span>\n        <span class=\"k\">return</span>\n\n
  \   <span class=\"k\">if</span> <span class=\"s2\">&quot;--draft&quot;</span> <span
  class=\"ow\">in</span> <span class=\"n\">sys</span><span class=\"o\">.</span><span
  class=\"n\">argv</span><span class=\"p\">:</span>\n        <span class=\"nb\">print</span><span
  class=\"p\">(</span><span class=\"s2\">&quot;</span><span class=\"se\">\\n</span><span
  class=\"s2\">&quot;</span><span class=\"o\">.</span><span class=\"n\">join</span><span
  class=\"p\">([</span><span class=\"n\">a</span><span class=\"p\">[</span><span class=\"s2\">&quot;path&quot;</span><span
  class=\"p\">]</span> <span class=\"k\">for</span> <span class=\"n\">a</span> <span
  class=\"ow\">in</span> <span class=\"n\">m</span><span class=\"o\">.</span><span
  class=\"n\">articles</span> <span class=\"k\">if</span> <span class=\"n\">a</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;status&quot;</span><span class=\"p\">]</span>
  <span class=\"o\">==</span> <span class=\"s2\">&quot;draft&quot;</span><span class=\"p\">]))</span>\n\n
  \       <span class=\"k\">return</span>\n\n    <span class=\"k\">if</span> <span
  class=\"s2\">&quot;--today&quot;</span> <span class=\"ow\">in</span> <span class=\"n\">sys</span><span
  class=\"o\">.</span><span class=\"n\">argv</span><span class=\"p\">:</span>\n        <span
  class=\"nb\">print</span><span class=\"p\">(</span><span class=\"s2\">&quot;</span><span
  class=\"se\">\\n</span><span class=\"s2\">&quot;</span><span class=\"o\">.</span><span
  class=\"n\">join</span><span class=\"p\">([</span><span class=\"n\">a</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;path&quot;</span><span class=\"p\">]</span>
  <span class=\"k\">for</span> <span class=\"n\">a</span> <span class=\"ow\">in</span>
  <span class=\"n\">m</span><span class=\"o\">.</span><span class=\"n\">articles</span>
  <span class=\"k\">if</span> <span class=\"n\">a</span><span class=\"p\">[</span><span
  class=\"s2\">&quot;date&quot;</span><span class=\"p\">]</span> <span class=\"o\">==</span>
  <span class=\"n\">a</span><span class=\"p\">[</span><span class=\"s2\">&quot;today&quot;</span><span
  class=\"p\">]]))</span>\n        <span class=\"k\">return</span>\n\n    <span class=\"k\">if</span>
  <span class=\"s2\">&quot;--scheduled&quot;</span> <span class=\"ow\">in</span> <span
  class=\"n\">sys</span><span class=\"o\">.</span><span class=\"n\">argv</span><span
  class=\"p\">:</span>\n        <span class=\"nb\">print</span><span class=\"p\">(</span><span
  class=\"s2\">&quot;</span><span class=\"se\">\\n</span><span class=\"s2\">&quot;</span><span
  class=\"o\">.</span><span class=\"n\">join</span><span class=\"p\">([</span><span
  class=\"n\">a</span><span class=\"p\">[</span><span class=\"s2\">&quot;path&quot;</span><span
  class=\"p\">]</span> <span class=\"k\">for</span> <span class=\"n\">a</span> <span
  class=\"ow\">in</span> <span class=\"n\">m</span><span class=\"o\">.</span><span
  class=\"n\">articles</span> <span class=\"k\">if</span> <span class=\"n\">a</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;date&quot;</span><span class=\"p\">]</span>
  <span class=\"o\">&gt;</span> <span class=\"n\">a</span><span class=\"p\">[</span><span
  class=\"s2\">&quot;today&quot;</span><span class=\"p\">]]))</span>\n        <span
  class=\"k\">return</span>\n\n    <span class=\"k\">if</span> <span class=\"s2\">&quot;--back-days&quot;</span>
  <span class=\"ow\">in</span> <span class=\"n\">sys</span><span class=\"o\">.</span><span
  class=\"n\">argv</span><span class=\"p\">:</span>\n        <span class=\"nb\">print</span><span
  class=\"p\">(</span><span class=\"s2\">&quot;</span><span class=\"se\">\\n</span><span
  class=\"s2\">&quot;</span><span class=\"o\">.</span><span class=\"n\">join</span><span
  class=\"p\">([</span><span class=\"n\">a</span><span class=\"p\">[</span><span class=\"s2\">&quot;path&quot;</span><span
  class=\"p\">]</span> <span class=\"k\">for</span> <span class=\"n\">a</span> <span
  class=\"ow\">in</span> <span class=\"n\">m</span><span class=\"o\">.</span><span
  class=\"n\">articles</span> <span class=\"k\">if</span> <span class=\"n\">a</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;date&quot;</span><span class=\"p\">]</span>
  <span class=\"o\">&gt;</span> <span class=\"n\">a</span><span class=\"p\">[</span><span
  class=\"s2\">&quot;today&quot;</span><span class=\"p\">]]))</span>\n        <span
  class=\"k\">return</span>\n\n    <span class=\"k\">if</span> <span class=\"s2\">&quot;--watch&quot;</span>
  <span class=\"ow\">in</span> <span class=\"n\">sys</span><span class=\"o\">.</span><span
  class=\"n\">argv</span><span class=\"p\">:</span>\n\n        <span class=\"nb\">hash</span>
  <span class=\"o\">=</span> <span class=\"n\">m</span><span class=\"o\">.</span><span
  class=\"n\">content_dir_hash</span>\n        <span class=\"n\">m</span><span class=\"o\">.</span><span
  class=\"n\">run</span><span class=\"p\">()</span>\n        <span class=\"n\">console</span>
  <span class=\"o\">=</span> <span class=\"n\">Console</span><span class=\"p\">()</span>\n
  \       <span class=\"k\">with</span> <span class=\"n\">console</span><span class=\"o\">.</span><span
  class=\"n\">status</span><span class=\"p\">(</span><span class=\"s2\">&quot;waiting
  for change&quot;</span><span class=\"p\">,</span> <span class=\"n\">spinner</span><span
  class=\"o\">=</span><span class=\"s2\">&quot;aesthetic&quot;</span><span class=\"p\">,</span>
  <span class=\"n\">speed</span><span class=\"o\">=</span><span class=\"mf\">0.2</span><span
  class=\"p\">):</span>\n            <span class=\"k\">while</span> <span class=\"kc\">True</span><span
  class=\"p\">:</span>\n                <span class=\"k\">if</span> <span class=\"n\">m</span><span
  class=\"o\">.</span><span class=\"n\">content_dir_hash</span> <span class=\"o\">!=</span>
  <span class=\"nb\">hash</span><span class=\"p\">:</span>\n                    <span
  class=\"nb\">hash</span> <span class=\"o\">=</span> <span class=\"n\">m</span><span
  class=\"o\">.</span><span class=\"n\">content_dir_hash</span>\n                    <span
  class=\"n\">m</span><span class=\"o\">.</span><span class=\"n\">run</span><span
  class=\"p\">()</span>\n                <span class=\"n\">time</span><span class=\"o\">.</span><span
  class=\"n\">sleep</span><span class=\"p\">(</span><span class=\"mf\">0.1</span><span
  class=\"p\">)</span>\n\n    <span class=\"n\">m</span><span class=\"o\">.</span><span
  class=\"n\">run</span><span class=\"p\">()</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"wrapper-function\">wrapper <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>wrapper
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">wrapper</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">:</span> <span class=\"n\">Markata</span><span class=\"p\">,</span>
  <span class=\"o\">*</span><span class=\"n\">args</span><span class=\"p\">:</span>
  <span class=\"n\">Tuple</span><span class=\"p\">,</span> <span class=\"o\">**</span><span
  class=\"n\">kwargs</span><span class=\"p\">:</span> <span class=\"n\">Dict</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"n\">Any</span><span
  class=\"p\">:</span>\n        <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">phase</span> <span class=\"o\">=</span> <span class=\"n\">function</span><span
  class=\"o\">.</span><span class=\"vm\">__name__</span>\n        <span class=\"n\">result</span>
  <span class=\"o\">=</span> <span class=\"n\">function</span><span class=\"p\">(</span><span
  class=\"bp\">self</span><span class=\"p\">,</span> <span class=\"o\">*</span><span
  class=\"n\">args</span><span class=\"p\">,</span> <span class=\"o\">**</span><span
  class=\"n\">kwargs</span><span class=\"p\">)</span>\n        <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">phase</span> <span class=\"o\">=</span> <span
  class=\"n\">function</span><span class=\"o\">.</span><span class=\"vm\">__name__</span>\n
  \       <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">phase_file</span><span
  class=\"o\">.</span><span class=\"n\">write_text</span><span class=\"p\">(</span><span
  class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">phase</span><span
  class=\"p\">)</span>\n        <span class=\"k\">return</span> <span class=\"n\">result</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"init-method\"><strong>init</strong> <code>method</code></h2>\n<p>None</p>\n<details>\n<summary><strong>init</strong>
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"fm\">__init__</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">,</span> <span class=\"n\">console</span><span class=\"p\">:</span>
  <span class=\"n\">Console</span> <span class=\"o\">=</span> <span class=\"kc\">None</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"kc\">None</span><span
  class=\"p\">:</span>\n        <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">phase</span> <span class=\"o\">=</span> <span class=\"s2\">&quot;starting&quot;</span>\n
  \       <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">MARKATA_CACHE_DIR</span>
  <span class=\"o\">=</span> <span class=\"n\">Path</span><span class=\"p\">(</span><span
  class=\"s2\">&quot;.&quot;</span><span class=\"p\">)</span> <span class=\"o\">/</span>
  <span class=\"s2\">&quot;.markata.cache&quot;</span>\n        <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">MARKATA_CACHE_DIR</span><span class=\"o\">.</span><span
  class=\"n\">mkdir</span><span class=\"p\">(</span><span class=\"n\">exist_ok</span><span
  class=\"o\">=</span><span class=\"kc\">True</span><span class=\"p\">)</span>\n        <span
  class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">phase_file</span><span
  class=\"p\">:</span> <span class=\"n\">Path</span> <span class=\"o\">=</span> <span
  class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">MARKATA_CACHE_DIR</span>
  <span class=\"o\">/</span> <span class=\"s2\">&quot;phase.txt&quot;</span>\n        <span
  class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">registered_attrs</span>
  <span class=\"o\">=</span> <span class=\"n\">hookspec</span><span class=\"o\">.</span><span
  class=\"n\">registered_attrs</span>\n        <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">configure</span><span class=\"p\">()</span>\n
  \       <span class=\"k\">if</span> <span class=\"n\">console</span> <span class=\"ow\">is</span>
  <span class=\"ow\">not</span> <span class=\"kc\">None</span><span class=\"p\">:</span>\n
  \           <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">_console</span>
  <span class=\"o\">=</span> <span class=\"n\">console</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"cache-method\">cache <code>method</code></h2>\n<p>None</p>\n<details>\n<summary>cache
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">cache</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"n\">FanoutCache</span><span
  class=\"p\">:</span>\n        <span class=\"k\">return</span> <span class=\"n\">FanoutCache</span><span
  class=\"p\">(</span><span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">MARKATA_CACHE_DIR</span><span class=\"p\">,</span> <span class=\"n\">statistics</span><span
  class=\"o\">=</span><span class=\"kc\">True</span><span class=\"p\">)</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"getattr-method\"><strong>getattr</strong> <code>method</code></h2>\n<p>None</p>\n<details>\n<summary><strong>getattr</strong>
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"fm\">__getattr__</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">,</span> <span class=\"n\">item</span><span class=\"p\">:</span> <span
  class=\"nb\">str</span><span class=\"p\">)</span> <span class=\"o\">-&gt;</span>
  <span class=\"n\">Any</span><span class=\"p\">:</span>\n        <span class=\"k\">if</span>
  <span class=\"n\">item</span> <span class=\"ow\">in</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"vm\">__dict__</span><span class=\"o\">.</span><span
  class=\"n\">keys</span><span class=\"p\">():</span>\n            <span class=\"k\">return</span>
  <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"fm\">__getitem__</span><span
  class=\"p\">(</span><span class=\"n\">item</span><span class=\"p\">)</span>\n        <span
  class=\"k\">elif</span> <span class=\"n\">item</span> <span class=\"ow\">in</span>
  <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">registered_attrs</span><span
  class=\"o\">.</span><span class=\"n\">keys</span><span class=\"p\">():</span>\n
  \           <span class=\"n\">stage_to_run_to</span> <span class=\"o\">=</span>
  <span class=\"nb\">max</span><span class=\"p\">(</span>\n                <span class=\"p\">[</span><span
  class=\"n\">attr</span><span class=\"p\">[</span><span class=\"s2\">&quot;lifecycle&quot;</span><span
  class=\"p\">]</span> <span class=\"k\">for</span> <span class=\"n\">attr</span>
  <span class=\"ow\">in</span> <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">registered_attrs</span><span class=\"p\">[</span><span class=\"n\">item</span><span
  class=\"p\">]]</span>\n            <span class=\"p\">)</span><span class=\"o\">.</span><span
  class=\"n\">name</span>\n            <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">run</span><span class=\"p\">(</span><span class=\"n\">stage_to_run_to</span><span
  class=\"p\">)</span>\n            <span class=\"k\">return</span> <span class=\"nb\">getattr</span><span
  class=\"p\">(</span><span class=\"bp\">self</span><span class=\"p\">,</span> <span
  class=\"n\">item</span><span class=\"p\">)</span>\n        <span class=\"k\">else</span><span
  class=\"p\">:</span>\n            <span class=\"k\">raise</span> <span class=\"ne\">AttributeError</span><span
  class=\"p\">(</span><span class=\"n\">item</span><span class=\"p\">)</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"server-method\">server <code>method</code></h2>\n<p>None</p>\n<details>\n<summary>server
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">server</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"n\">Server</span><span
  class=\"p\">:</span>\n        <span class=\"k\">try</span><span class=\"p\">:</span>\n
  \           <span class=\"k\">return</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">_server</span>\n        <span class=\"k\">except</span>
  <span class=\"ne\">AttributeError</span><span class=\"p\">:</span>\n\n            <span
  class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">_server</span><span
  class=\"p\">:</span> <span class=\"n\">Server</span> <span class=\"o\">=</span>
  <span class=\"n\">Server</span><span class=\"p\">(</span><span class=\"n\">directory</span><span
  class=\"o\">=</span><span class=\"nb\">str</span><span class=\"p\">(</span><span
  class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">config</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;output_dir&quot;</span><span class=\"p\">]))</span>\n
  \           <span class=\"k\">return</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">server</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"runner-method\">runner <code>method</code></h2>\n<p>None</p>\n<details>\n<summary>runner
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">runner</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"n\">Runner</span><span
  class=\"p\">:</span>\n        <span class=\"k\">try</span><span class=\"p\">:</span>\n
  \           <span class=\"k\">return</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">_runner</span>\n        <span class=\"k\">except</span>
  <span class=\"ne\">AttributeError</span><span class=\"p\">:</span>\n\n            <span
  class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">_runner</span><span
  class=\"p\">:</span> <span class=\"n\">Runner</span> <span class=\"o\">=</span>
  <span class=\"n\">Runner</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">)</span>\n            <span class=\"k\">return</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">runner</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"plugins-method\">plugins <code>method</code></h2>\n<p>None</p>\n<details>\n<summary>plugins
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">plugins</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"n\">Plugins</span><span
  class=\"p\">:</span>\n        <span class=\"k\">try</span><span class=\"p\">:</span>\n
  \           <span class=\"k\">return</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">_plugins</span>\n        <span class=\"k\">except</span>
  <span class=\"ne\">AttributeError</span><span class=\"p\">:</span>\n\n            <span
  class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">_plugins</span><span
  class=\"p\">:</span> <span class=\"n\">Plugins</span> <span class=\"o\">=</span>
  <span class=\"n\">Plugins</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">)</span>\n        <span class=\"k\">return</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">plugins</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"summary-method\">summary <code>method</code></h2>\n<p>None</p>\n<details>\n<summary>summary
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">summary</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"n\">Summary</span><span
  class=\"p\">:</span>\n        <span class=\"k\">try</span><span class=\"p\">:</span>\n
  \           <span class=\"k\">return</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">_summary</span>\n        <span class=\"k\">except</span>
  <span class=\"ne\">AttributeError</span><span class=\"p\">:</span>\n\n            <span
  class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">_summary</span><span
  class=\"p\">:</span> <span class=\"n\">Summary</span> <span class=\"o\">=</span>
  <span class=\"n\">Summary</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">)</span>\n            <span class=\"k\">return</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">summary</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"rich-method\"><strong>rich</strong> <code>method</code></h2>\n<p>None</p>\n<details>\n<summary><strong>rich</strong>
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">__rich__</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"n\">Table</span><span
  class=\"p\">:</span>\n\n        <span class=\"n\">grid</span> <span class=\"o\">=</span>
  <span class=\"n\">Table</span><span class=\"o\">.</span><span class=\"n\">grid</span><span
  class=\"p\">()</span>\n        <span class=\"n\">grid</span><span class=\"o\">.</span><span
  class=\"n\">add_column</span><span class=\"p\">(</span><span class=\"s2\">&quot;label&quot;</span><span
  class=\"p\">)</span>\n        <span class=\"n\">grid</span><span class=\"o\">.</span><span
  class=\"n\">add_column</span><span class=\"p\">(</span><span class=\"s2\">&quot;value&quot;</span><span
  class=\"p\">)</span>\n\n        <span class=\"k\">for</span> <span class=\"n\">label</span><span
  class=\"p\">,</span> <span class=\"n\">value</span> <span class=\"ow\">in</span>
  <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">describe</span><span
  class=\"p\">()</span><span class=\"o\">.</span><span class=\"n\">items</span><span
  class=\"p\">():</span>\n            <span class=\"n\">grid</span><span class=\"o\">.</span><span
  class=\"n\">add_row</span><span class=\"p\">(</span><span class=\"n\">label</span><span
  class=\"p\">,</span> <span class=\"n\">value</span><span class=\"p\">)</span>\n\n
  \       <span class=\"k\">return</span> <span class=\"n\">grid</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"bust_cache-method\">bust_cache <code>method</code></h2>\n<p>None</p>\n<details>\n<summary>bust_cache
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">bust_cache</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"n\">Markata</span><span
  class=\"p\">:</span>\n        <span class=\"k\">with</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">cache</span> <span class=\"k\">as</span> <span
  class=\"n\">cache</span><span class=\"p\">:</span>\n            <span class=\"n\">cache</span><span
  class=\"o\">.</span><span class=\"n\">clear</span><span class=\"p\">()</span>\n
  \       <span class=\"k\">return</span> <span class=\"bp\">self</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"configure-method\">configure <code>method</code></h2>\n<p>None</p>\n<details>\n<summary>configure
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">configure</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"n\">Markata</span><span
  class=\"p\">:</span>\n        <span class=\"n\">sys</span><span class=\"o\">.</span><span
  class=\"n\">path</span><span class=\"o\">.</span><span class=\"n\">append</span><span
  class=\"p\">(</span><span class=\"n\">os</span><span class=\"o\">.</span><span class=\"n\">getcwd</span><span
  class=\"p\">())</span>\n        <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">config</span> <span class=\"o\">=</span> <span class=\"p\">{</span><span
  class=\"o\">**</span><span class=\"n\">DEFUALT_CONFIG</span><span class=\"p\">,</span>
  <span class=\"o\">**</span><span class=\"n\">standard_config</span><span class=\"o\">.</span><span
  class=\"n\">load</span><span class=\"p\">(</span><span class=\"s2\">&quot;markata&quot;</span><span
  class=\"p\">)}</span>\n        <span class=\"k\">if</span> <span class=\"nb\">isinstance</span><span
  class=\"p\">(</span><span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">config</span><span class=\"p\">[</span><span class=\"s2\">&quot;glob_patterns&quot;</span><span
  class=\"p\">],</span> <span class=\"nb\">str</span><span class=\"p\">):</span>\n
  \           <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">config</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;glob_patterns&quot;</span><span class=\"p\">]</span>
  <span class=\"o\">=</span> <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">config</span><span class=\"p\">[</span><span class=\"s2\">&quot;glob_patterns&quot;</span><span
  class=\"p\">]</span><span class=\"o\">.</span><span class=\"n\">split</span><span
  class=\"p\">(</span><span class=\"s2\">&quot;,&quot;</span><span class=\"p\">)</span>\n
  \       <span class=\"k\">elif</span> <span class=\"nb\">isinstance</span><span
  class=\"p\">(</span><span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">config</span><span class=\"p\">[</span><span class=\"s2\">&quot;glob_patterns&quot;</span><span
  class=\"p\">],</span> <span class=\"nb\">list</span><span class=\"p\">):</span>\n
  \           <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">config</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;glob_patterns&quot;</span><span class=\"p\">]</span>
  <span class=\"o\">=</span> <span class=\"nb\">list</span><span class=\"p\">(</span><span
  class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">config</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;glob_patterns&quot;</span><span class=\"p\">])</span>\n
  \       <span class=\"k\">else</span><span class=\"p\">:</span>\n            <span
  class=\"k\">raise</span> <span class=\"ne\">TypeError</span><span class=\"p\">(</span><span
  class=\"s2\">&quot;glob_patterns must be list or str&quot;</span><span class=\"p\">)</span>\n
  \       <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">glob_patterns</span>
  <span class=\"o\">=</span> <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">config</span><span class=\"p\">[</span><span class=\"s2\">&quot;glob_patterns&quot;</span><span
  class=\"p\">]</span>\n\n        <span class=\"k\">if</span> <span class=\"s2\">&quot;hooks&quot;</span>
  <span class=\"ow\">not</span> <span class=\"ow\">in</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">config</span><span class=\"p\">:</span>\n
  \           <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">hooks</span>
  <span class=\"o\">=</span> <span class=\"p\">[</span><span class=\"s2\">&quot;&quot;</span><span
  class=\"p\">]</span>\n        <span class=\"k\">if</span> <span class=\"nb\">isinstance</span><span
  class=\"p\">(</span><span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">config</span><span class=\"p\">[</span><span class=\"s2\">&quot;hooks&quot;</span><span
  class=\"p\">],</span> <span class=\"nb\">str</span><span class=\"p\">):</span>\n
  \           <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">hooks</span>
  <span class=\"o\">=</span> <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">config</span><span class=\"p\">[</span><span class=\"s2\">&quot;hooks&quot;</span><span
  class=\"p\">]</span><span class=\"o\">.</span><span class=\"n\">split</span><span
  class=\"p\">(</span><span class=\"s2\">&quot;,&quot;</span><span class=\"p\">)</span>\n
  \       <span class=\"k\">if</span> <span class=\"nb\">isinstance</span><span class=\"p\">(</span><span
  class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">config</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;hooks&quot;</span><span class=\"p\">],</span>
  <span class=\"nb\">list</span><span class=\"p\">):</span>\n            <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">hooks</span> <span class=\"o\">=</span> <span
  class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">config</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;hooks&quot;</span><span class=\"p\">]</span>\n\n
  \       <span class=\"k\">if</span> <span class=\"s2\">&quot;disabled_hooks&quot;</span>
  <span class=\"ow\">not</span> <span class=\"ow\">in</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">config</span><span class=\"p\">:</span>\n
  \           <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">disabled_hooks</span>
  <span class=\"o\">=</span> <span class=\"p\">[</span><span class=\"s2\">&quot;&quot;</span><span
  class=\"p\">]</span>\n        <span class=\"k\">if</span> <span class=\"nb\">isinstance</span><span
  class=\"p\">(</span><span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">config</span><span class=\"p\">[</span><span class=\"s2\">&quot;disabled_hooks&quot;</span><span
  class=\"p\">],</span> <span class=\"nb\">str</span><span class=\"p\">):</span>\n
  \           <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">disabled_hooks</span>
  <span class=\"o\">=</span> <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">config</span><span class=\"p\">[</span><span class=\"s2\">&quot;disabled_hooks&quot;</span><span
  class=\"p\">]</span><span class=\"o\">.</span><span class=\"n\">split</span><span
  class=\"p\">(</span><span class=\"s2\">&quot;,&quot;</span><span class=\"p\">)</span>\n
  \       <span class=\"k\">if</span> <span class=\"nb\">isinstance</span><span class=\"p\">(</span><span
  class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">config</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;disabled_hooks&quot;</span><span class=\"p\">],</span>
  <span class=\"nb\">list</span><span class=\"p\">):</span>\n            <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">disabled_hooks</span> <span class=\"o\">=</span>
  <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">config</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;disabled_hooks&quot;</span><span class=\"p\">]</span>\n\n
  \       <span class=\"k\">try</span><span class=\"p\">:</span>\n            <span
  class=\"n\">default_index</span> <span class=\"o\">=</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">hooks</span><span class=\"o\">.</span><span
  class=\"n\">index</span><span class=\"p\">(</span><span class=\"s2\">&quot;default&quot;</span><span
  class=\"p\">)</span>\n            <span class=\"n\">hooks</span> <span class=\"o\">=</span>
  <span class=\"p\">[</span>\n                <span class=\"o\">*</span><span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">hooks</span><span class=\"p\">[:</span><span
  class=\"n\">default_index</span><span class=\"p\">],</span>\n                <span
  class=\"o\">*</span><span class=\"n\">DEFAULT_HOOKS</span><span class=\"p\">,</span>\n
  \               <span class=\"o\">*</span><span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">hooks</span><span class=\"p\">[</span><span class=\"n\">default_index</span>
  <span class=\"o\">+</span> <span class=\"mi\">1</span> <span class=\"p\">:],</span>\n
  \           <span class=\"p\">]</span>\n            <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">hooks</span> <span class=\"o\">=</span> <span
  class=\"p\">[</span><span class=\"n\">hook</span> <span class=\"k\">for</span> <span
  class=\"n\">hook</span> <span class=\"ow\">in</span> <span class=\"n\">hooks</span>
  <span class=\"k\">if</span> <span class=\"n\">hook</span> <span class=\"ow\">not</span>
  <span class=\"ow\">in</span> <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">disabled_hooks</span><span class=\"p\">]</span>\n        <span class=\"k\">except</span>
  <span class=\"ne\">ValueError</span><span class=\"p\">:</span>\n            <span
  class=\"c1\"># &#39;default&#39; is not in hooks , do not replace with default_hooks</span>\n
  \           <span class=\"k\">pass</span>\n\n        <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">_pm</span> <span class=\"o\">=</span> <span
  class=\"n\">pluggy</span><span class=\"o\">.</span><span class=\"n\">PluginManager</span><span
  class=\"p\">(</span><span class=\"s2\">&quot;markata&quot;</span><span class=\"p\">)</span>\n
  \       <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">_pm</span><span
  class=\"o\">.</span><span class=\"n\">add_hookspecs</span><span class=\"p\">(</span><span
  class=\"n\">hookspec</span><span class=\"o\">.</span><span class=\"n\">MarkataSpecs</span><span
  class=\"p\">)</span>\n        <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">_register_hooks</span><span class=\"p\">()</span>\n\n        <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">_pm</span><span class=\"o\">.</span><span
  class=\"n\">hook</span><span class=\"o\">.</span><span class=\"n\">configure</span><span
  class=\"p\">(</span><span class=\"n\">markata</span><span class=\"o\">=</span><span
  class=\"bp\">self</span><span class=\"p\">)</span>\n        <span class=\"k\">return</span>
  <span class=\"bp\">self</span>\n</code></pre></div>\n</details>\n<hr />\n<h2 id=\"get_plugin_config-method\">get_plugin_config
  <code>method</code></h2>\n<p>None</p>\n<details>\n<summary>get_plugin_config source</summary>\n<div
  class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span> <span class=\"nf\">get_plugin_config</span><span
  class=\"p\">(</span><span class=\"bp\">self</span><span class=\"p\">,</span> <span
  class=\"n\">path_or_name</span><span class=\"p\">:</span> <span class=\"nb\">str</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"n\">Dict</span><span
  class=\"p\">:</span>\n\n        <span class=\"n\">key</span> <span class=\"o\">=</span>
  <span class=\"n\">Path</span><span class=\"p\">(</span><span class=\"n\">path_or_name</span><span
  class=\"p\">)</span><span class=\"o\">.</span><span class=\"n\">stem</span>\n\n
  \       <span class=\"k\">try</span><span class=\"p\">:</span>\n            <span
  class=\"n\">config</span> <span class=\"o\">=</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">config</span><span class=\"p\">[</span><span
  class=\"n\">key</span><span class=\"p\">]</span>\n        <span class=\"k\">except</span>
  <span class=\"ne\">KeyError</span><span class=\"p\">:</span>\n            <span
  class=\"n\">config</span> <span class=\"o\">=</span> <span class=\"p\">{}</span>\n
  \       <span class=\"k\">if</span> <span class=\"ow\">not</span> <span class=\"nb\">isinstance</span><span
  class=\"p\">(</span><span class=\"n\">config</span><span class=\"p\">,</span> <span
  class=\"nb\">dict</span><span class=\"p\">):</span>\n            <span class=\"k\">raise</span>
  <span class=\"ne\">TypeError</span><span class=\"p\">(</span><span class=\"s2\">&quot;must
  use dict&quot;</span><span class=\"p\">)</span>\n        <span class=\"k\">if</span>
  <span class=\"s2\">&quot;cache_expire&quot;</span> <span class=\"ow\">not</span>
  <span class=\"ow\">in</span> <span class=\"n\">config</span><span class=\"o\">.</span><span
  class=\"n\">keys</span><span class=\"p\">():</span>\n            <span class=\"n\">config</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;cache_expire&quot;</span><span class=\"p\">]</span>
  <span class=\"o\">=</span> <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">config</span><span class=\"p\">[</span><span class=\"s2\">&quot;default_cache_expire&quot;</span><span
  class=\"p\">]</span>\n        <span class=\"k\">if</span> <span class=\"s2\">&quot;config_key&quot;</span>
  <span class=\"ow\">not</span> <span class=\"ow\">in</span> <span class=\"n\">config</span><span
  class=\"o\">.</span><span class=\"n\">keys</span><span class=\"p\">():</span>\n
  \           <span class=\"n\">config</span><span class=\"p\">[</span><span class=\"s2\">&quot;config_key&quot;</span><span
  class=\"p\">]</span> <span class=\"o\">=</span> <span class=\"n\">key</span>\n        <span
  class=\"k\">return</span> <span class=\"n\">config</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"get_config-method\">get_config <code>method</code></h2>\n<p>None</p>\n<details>\n<summary>get_config
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">get_config</span><span class=\"p\">(</span>\n        <span class=\"bp\">self</span><span
  class=\"p\">,</span> <span class=\"n\">key</span><span class=\"p\">:</span> <span
  class=\"nb\">str</span><span class=\"p\">,</span> <span class=\"n\">warn</span><span
  class=\"p\">:</span> <span class=\"nb\">bool</span> <span class=\"o\">=</span> <span
  class=\"kc\">True</span><span class=\"p\">,</span> <span class=\"n\">suggested</span><span
  class=\"p\">:</span> <span class=\"n\">Optional</span><span class=\"p\">[</span><span
  class=\"nb\">str</span><span class=\"p\">]</span> <span class=\"o\">=</span> <span
  class=\"kc\">None</span>\n    <span class=\"p\">)</span> <span class=\"o\">-&gt;</span>
  <span class=\"n\">Any</span><span class=\"p\">:</span>\n        <span class=\"k\">if</span>
  <span class=\"n\">key</span> <span class=\"ow\">in</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">config</span><span class=\"o\">.</span><span
  class=\"n\">keys</span><span class=\"p\">():</span>\n            <span class=\"k\">return</span>
  <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">config</span><span
  class=\"p\">[</span><span class=\"n\">key</span><span class=\"p\">]</span>\n        <span
  class=\"k\">else</span><span class=\"p\">:</span>\n\n            <span class=\"k\">if</span>
  <span class=\"n\">suggested</span> <span class=\"ow\">is</span> <span class=\"kc\">None</span><span
  class=\"p\">:</span>\n                <span class=\"n\">suggested</span> <span class=\"o\">=</span>
  <span class=\"n\">textwrap</span><span class=\"o\">.</span><span class=\"n\">dedent</span><span
  class=\"p\">(</span>\n                    <span class=\"sa\">f</span><span class=\"s2\">&quot;&quot;&quot;</span>\n<span
  class=\"s2\">                        \\[markata]</span>\n<span class=\"s2\">                        </span><span
  class=\"si\">{</span><span class=\"n\">key</span><span class=\"si\">}</span><span
  class=\"s2\"> = value</span>\n<span class=\"s2\">                    &quot;&quot;&quot;</span>
  \ <span class=\"c1\"># noqa: W605</span>\n                <span class=\"p\">)</span>\n
  \           <span class=\"k\">if</span> <span class=\"n\">warn</span><span class=\"p\">:</span>\n
  \               <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">console</span><span
  class=\"o\">.</span><span class=\"n\">log</span><span class=\"p\">(</span>\n                    <span
  class=\"n\">textwrap</span><span class=\"o\">.</span><span class=\"n\">dedent</span><span
  class=\"p\">(</span>\n                        <span class=\"sa\">f</span><span class=\"s2\">&quot;&quot;&quot;</span>\n<span
  class=\"s2\">                        Warning site_name is not set in markata config,
  sitemap will</span>\n<span class=\"s2\">                        be missing root
  site_name</span>\n<span class=\"s2\">                        to resolve this open
  your markata.toml and add</span>\n\n<span class=\"s2\">                        </span><span
  class=\"si\">{</span><span class=\"n\">suggested</span><span class=\"si\">}</span><span
  class=\"s2\"></span>\n\n<span class=\"s2\">                        &quot;&quot;&quot;</span>\n
  \                   <span class=\"p\">),</span>\n                    <span class=\"n\">style</span><span
  class=\"o\">=</span><span class=\"s2\">&quot;yellow&quot;</span><span class=\"p\">,</span>\n
  \               <span class=\"p\">)</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"make_hash-method\">make_hash <code>method</code></h2>\n<p>None</p>\n<details>\n<summary>make_hash
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">make_hash</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">,</span> <span class=\"o\">*</span><span class=\"n\">keys</span><span
  class=\"p\">:</span> <span class=\"nb\">str</span><span class=\"p\">)</span> <span
  class=\"o\">-&gt;</span> <span class=\"nb\">str</span><span class=\"p\">:</span>\n
  \       <span class=\"n\">str_keys</span> <span class=\"o\">=</span> <span class=\"p\">[</span><span
  class=\"nb\">str</span><span class=\"p\">(</span><span class=\"n\">key</span><span
  class=\"p\">)</span> <span class=\"k\">for</span> <span class=\"n\">key</span> <span
  class=\"ow\">in</span> <span class=\"n\">keys</span><span class=\"p\">]</span>\n
  \       <span class=\"k\">return</span> <span class=\"n\">hashlib</span><span class=\"o\">.</span><span
  class=\"n\">md5</span><span class=\"p\">(</span><span class=\"s2\">&quot;&quot;</span><span
  class=\"o\">.</span><span class=\"n\">join</span><span class=\"p\">(</span><span
  class=\"n\">str_keys</span><span class=\"p\">)</span><span class=\"o\">.</span><span
  class=\"n\">encode</span><span class=\"p\">(</span><span class=\"s2\">&quot;utf-8&quot;</span><span
  class=\"p\">))</span><span class=\"o\">.</span><span class=\"n\">hexdigest</span><span
  class=\"p\">()</span>\n</code></pre></div>\n</details>\n<hr />\n<h2 id=\"phase-method\">phase
  <code>method</code></h2>\n<p>None</p>\n<details>\n<summary>phase source</summary>\n<div
  class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span> <span class=\"nf\">phase</span><span
  class=\"p\">(</span><span class=\"bp\">self</span><span class=\"p\">)</span> <span
  class=\"o\">-&gt;</span> <span class=\"nb\">str</span><span class=\"p\">:</span>\n
  \       <span class=\"k\">return</span> <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">_phase</span>\n</code></pre></div>\n</details>\n<hr />\n<h2 id=\"phase-method_1\">phase
  <code>method</code></h2>\n<p>None</p>\n<details>\n<summary>phase source</summary>\n<div
  class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span> <span class=\"nf\">phase</span><span
  class=\"p\">(</span><span class=\"bp\">self</span><span class=\"p\">,</span> <span
  class=\"n\">value</span><span class=\"p\">:</span> <span class=\"nb\">str</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"kc\">None</span><span
  class=\"p\">:</span>\n        <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">_phase</span> <span class=\"o\">=</span> <span class=\"n\">value</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"content_dir_hash-method\">content_dir_hash <code>method</code></h2>\n<p>None</p>\n<details>\n<summary>content_dir_hash
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">content_dir_hash</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"nb\">str</span><span
  class=\"p\">:</span>\n        <span class=\"n\">hashes</span> <span class=\"o\">=</span>
  <span class=\"p\">[</span><span class=\"n\">dirhash</span><span class=\"p\">(</span><span
  class=\"nb\">dir</span><span class=\"p\">)</span> <span class=\"k\">for</span> <span
  class=\"nb\">dir</span> <span class=\"ow\">in</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">content_directories</span><span class=\"p\">]</span>\n
  \       <span class=\"k\">return</span> <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">make_hash</span><span class=\"p\">(</span><span class=\"o\">*</span><span
  class=\"n\">hashes</span><span class=\"p\">)</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"console-method\">console <code>method</code></h2>\n<p>None</p>\n<details>\n<summary>console
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">console</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"n\">Console</span><span
  class=\"p\">:</span>\n        <span class=\"k\">try</span><span class=\"p\">:</span>\n
  \           <span class=\"k\">return</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">_console</span>\n        <span class=\"k\">except</span>
  <span class=\"ne\">AttributeError</span><span class=\"p\">:</span>\n            <span
  class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">_console</span>
  <span class=\"o\">=</span> <span class=\"n\">Console</span><span class=\"p\">()</span>\n
  \           <span class=\"k\">return</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">_console</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"describe-method\">describe <code>method</code></h2>\n<p>None</p>\n<details>\n<summary>describe
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">describe</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"nb\">dict</span><span
  class=\"p\">[</span><span class=\"nb\">str</span><span class=\"p\">,</span> <span
  class=\"nb\">str</span><span class=\"p\">]:</span>\n        <span class=\"k\">return</span>
  <span class=\"p\">{</span><span class=\"s2\">&quot;version&quot;</span><span class=\"p\">:</span>
  <span class=\"n\">__version__</span><span class=\"p\">,</span> <span class=\"s2\">&quot;phase&quot;</span><span
  class=\"p\">:</span> <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">phase</span><span class=\"p\">}</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"_to_dict-method\">_to_dict <code>method</code></h2>\n<p>None</p>\n<details>\n<summary>_to_dict
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">_to_dict</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"nb\">dict</span><span
  class=\"p\">[</span><span class=\"nb\">str</span><span class=\"p\">,</span> <span
  class=\"n\">Iterable</span><span class=\"p\">]:</span>\n        <span class=\"k\">return</span>
  <span class=\"p\">{</span><span class=\"s2\">&quot;config&quot;</span><span class=\"p\">:</span>
  <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">config</span><span
  class=\"p\">,</span> <span class=\"s2\">&quot;articles&quot;</span><span class=\"p\">:</span>
  <span class=\"p\">[</span><span class=\"n\">a</span><span class=\"o\">.</span><span
  class=\"n\">to_dict</span><span class=\"p\">()</span> <span class=\"k\">for</span>
  <span class=\"n\">a</span> <span class=\"ow\">in</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">articles</span><span class=\"p\">]}</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"to_dict-method\">to_dict <code>method</code></h2>\n<p>None</p>\n<details>\n<summary>to_dict
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">to_dict</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"nb\">dict</span><span
  class=\"p\">:</span>\n        <span class=\"k\">try</span><span class=\"p\">:</span>\n
  \           <span class=\"k\">return</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">_to_dict</span><span class=\"p\">()</span>\n
  \       <span class=\"k\">except</span> <span class=\"ne\">AttributeError</span><span
  class=\"p\">:</span>\n            <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">render</span><span class=\"p\">()</span>\n            <span class=\"k\">return</span>
  <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">_to_dict</span><span
  class=\"p\">()</span>\n</code></pre></div>\n</details>\n<hr />\n<h2 id=\"to_json-method\">to_json
  <code>method</code></h2>\n<p>None</p>\n<details>\n<summary>to_json source</summary>\n<div
  class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span> <span class=\"nf\">to_json</span><span
  class=\"p\">(</span><span class=\"bp\">self</span><span class=\"p\">)</span> <span
  class=\"o\">-&gt;</span> <span class=\"nb\">str</span><span class=\"p\">:</span>\n
  \       <span class=\"kn\">import</span> <span class=\"nn\">json</span>\n\n        <span
  class=\"k\">return</span> <span class=\"n\">json</span><span class=\"o\">.</span><span
  class=\"n\">dumps</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">to_dict</span><span class=\"p\">(),</span>
  <span class=\"n\">indent</span><span class=\"o\">=</span><span class=\"mi\">4</span><span
  class=\"p\">,</span> <span class=\"n\">sort_keys</span><span class=\"o\">=</span><span
  class=\"kc\">True</span><span class=\"p\">,</span> <span class=\"n\">default</span><span
  class=\"o\">=</span><span class=\"nb\">str</span><span class=\"p\">)</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"_register_hooks-method\">_register_hooks <code>method</code></h2>\n<p>None</p>\n<details>\n<summary>_register_hooks
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">_register_hooks</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"kc\">None</span><span
  class=\"p\">:</span>\n        <span class=\"k\">for</span> <span class=\"n\">hook</span>
  <span class=\"ow\">in</span> <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">hooks</span><span class=\"p\">:</span>\n            <span class=\"k\">try</span><span
  class=\"p\">:</span>\n                <span class=\"c1\"># module style plugins</span>\n
  \               <span class=\"n\">plugin</span> <span class=\"o\">=</span> <span
  class=\"n\">importlib</span><span class=\"o\">.</span><span class=\"n\">import_module</span><span
  class=\"p\">(</span><span class=\"n\">hook</span><span class=\"p\">)</span>\n            <span
  class=\"k\">except</span> <span class=\"ne\">ModuleNotFoundError</span> <span class=\"k\">as</span>
  <span class=\"n\">e</span><span class=\"p\">:</span>\n                <span class=\"c1\">#
  class style plugins</span>\n                <span class=\"k\">if</span> <span class=\"s2\">&quot;.&quot;</span>
  <span class=\"ow\">in</span> <span class=\"n\">hook</span><span class=\"p\">:</span>\n
  \                   <span class=\"n\">mod</span> <span class=\"o\">=</span> <span
  class=\"n\">importlib</span><span class=\"o\">.</span><span class=\"n\">import_module</span><span
  class=\"p\">(</span><span class=\"s2\">&quot;.&quot;</span><span class=\"o\">.</span><span
  class=\"n\">join</span><span class=\"p\">(</span><span class=\"n\">hook</span><span
  class=\"o\">.</span><span class=\"n\">split</span><span class=\"p\">(</span><span
  class=\"s2\">&quot;.&quot;</span><span class=\"p\">)[:</span><span class=\"o\">-</span><span
  class=\"mi\">1</span><span class=\"p\">]))</span>\n                    <span class=\"n\">plugin</span>
  <span class=\"o\">=</span> <span class=\"nb\">getattr</span><span class=\"p\">(</span><span
  class=\"n\">mod</span><span class=\"p\">,</span> <span class=\"n\">hook</span><span
  class=\"o\">.</span><span class=\"n\">split</span><span class=\"p\">(</span><span
  class=\"s2\">&quot;.&quot;</span><span class=\"p\">)[</span><span class=\"o\">-</span><span
  class=\"mi\">1</span><span class=\"p\">])</span>\n                <span class=\"k\">else</span><span
  class=\"p\">:</span>\n                    <span class=\"k\">raise</span> <span class=\"n\">e</span>\n\n
  \           <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">_pm</span><span
  class=\"o\">.</span><span class=\"n\">register</span><span class=\"p\">(</span><span
  class=\"n\">plugin</span><span class=\"p\">)</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"iter-method\"><strong>iter</strong> <code>method</code></h2>\n<p>None</p>\n<details>\n<summary><strong>iter</strong>
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"fm\">__iter__</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">,</span> <span class=\"n\">description</span><span class=\"p\">:</span>
  <span class=\"nb\">str</span> <span class=\"o\">=</span> <span class=\"s2\">&quot;working...&quot;</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"n\">Iterable</span><span
  class=\"p\">[</span><span class=\"n\">frontmatter</span><span class=\"o\">.</span><span
  class=\"n\">Post</span><span class=\"p\">]:</span>\n        <span class=\"n\">articles</span><span
  class=\"p\">:</span> <span class=\"n\">Iterable</span><span class=\"p\">[</span><span
  class=\"n\">frontmatter</span><span class=\"o\">.</span><span class=\"n\">Post</span><span
  class=\"p\">]</span> <span class=\"o\">=</span> <span class=\"n\">track</span><span
  class=\"p\">(</span>\n            <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">articles</span><span class=\"p\">,</span> <span class=\"n\">description</span><span
  class=\"o\">=</span><span class=\"n\">description</span><span class=\"p\">,</span>
  <span class=\"n\">transient</span><span class=\"o\">=</span><span class=\"kc\">True</span><span
  class=\"p\">,</span> <span class=\"n\">console</span><span class=\"o\">=</span><span
  class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">console</span>\n
  \       <span class=\"p\">)</span>\n        <span class=\"k\">return</span> <span
  class=\"n\">articles</span>\n</code></pre></div>\n</details>\n<hr />\n<h2 id=\"iter_articles-method\">iter_articles
  <code>method</code></h2>\n<p>None</p>\n<details>\n<summary>iter_articles source</summary>\n<div
  class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span> <span class=\"nf\">iter_articles</span><span
  class=\"p\">(</span><span class=\"bp\">self</span><span class=\"p\">,</span> <span
  class=\"n\">description</span><span class=\"p\">:</span> <span class=\"nb\">str</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"n\">Iterable</span><span
  class=\"p\">[</span><span class=\"n\">frontmatter</span><span class=\"o\">.</span><span
  class=\"n\">Post</span><span class=\"p\">]:</span>\n        <span class=\"n\">articles</span><span
  class=\"p\">:</span> <span class=\"n\">Iterable</span><span class=\"p\">[</span><span
  class=\"n\">frontmatter</span><span class=\"o\">.</span><span class=\"n\">Post</span><span
  class=\"p\">]</span> <span class=\"o\">=</span> <span class=\"n\">track</span><span
  class=\"p\">(</span>\n            <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">articles</span><span class=\"p\">,</span> <span class=\"n\">description</span><span
  class=\"o\">=</span><span class=\"n\">description</span><span class=\"p\">,</span>
  <span class=\"n\">transient</span><span class=\"o\">=</span><span class=\"kc\">True</span><span
  class=\"p\">,</span> <span class=\"n\">console</span><span class=\"o\">=</span><span
  class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">console</span>\n
  \       <span class=\"p\">)</span>\n        <span class=\"k\">return</span> <span
  class=\"n\">articles</span>\n</code></pre></div>\n</details>\n<hr />\n<h2 id=\"glob-method\">glob
  <code>method</code></h2>\n<p>run glob hooks</p>\n<p>Glob hooks should append file
  lists to the markata object for later\nhooks to build from.  The default loader
  will utilize the <code>files</code>\nattribute for loading.</p>\n<details>\n<summary>glob
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">glob</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"n\">Markata</span><span
  class=\"p\">:</span>\n        <span class=\"sd\">&quot;&quot;&quot;run glob hooks</span>\n\n<span
  class=\"sd\">        Glob hooks should append file lists to the markata object for
  later</span>\n<span class=\"sd\">        hooks to build from.  The default loader
  will utilize the `files`</span>\n<span class=\"sd\">        attribute for loading.</span>\n<span
  class=\"sd\">        &quot;&quot;&quot;</span>\n\n        <span class=\"k\">try</span><span
  class=\"p\">:</span>\n            <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">_pm</span><span class=\"o\">.</span><span class=\"n\">hook</span><span
  class=\"o\">.</span><span class=\"n\">glob</span><span class=\"p\">(</span><span
  class=\"n\">markata</span><span class=\"o\">=</span><span class=\"bp\">self</span><span
  class=\"p\">)</span>\n        <span class=\"k\">except</span> <span class=\"ne\">AttributeError</span><span
  class=\"p\">:</span>\n            <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">configure</span><span class=\"p\">()</span>\n            <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">_pm</span><span class=\"o\">.</span><span
  class=\"n\">hook</span><span class=\"o\">.</span><span class=\"n\">glob</span><span
  class=\"p\">(</span><span class=\"n\">markata</span><span class=\"o\">=</span><span
  class=\"bp\">self</span><span class=\"p\">)</span>\n\n        <span class=\"k\">return</span>
  <span class=\"bp\">self</span>\n</code></pre></div>\n</details>\n<hr />\n<h2 id=\"load-method\">load
  <code>method</code></h2>\n<p>None</p>\n<details>\n<summary>load source</summary>\n<div
  class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span> <span class=\"nf\">load</span><span
  class=\"p\">(</span><span class=\"bp\">self</span><span class=\"p\">)</span> <span
  class=\"o\">-&gt;</span> <span class=\"n\">Markata</span><span class=\"p\">:</span>\n
  \       <span class=\"k\">try</span><span class=\"p\">:</span>\n            <span
  class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">_pm</span><span
  class=\"o\">.</span><span class=\"n\">hook</span><span class=\"o\">.</span><span
  class=\"n\">load</span><span class=\"p\">(</span><span class=\"n\">markata</span><span
  class=\"o\">=</span><span class=\"bp\">self</span><span class=\"p\">)</span>\n        <span
  class=\"k\">except</span> <span class=\"ne\">AttributeError</span><span class=\"p\">:</span>\n
  \           <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">glob</span><span
  class=\"p\">()</span>\n            <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">_pm</span><span class=\"o\">.</span><span class=\"n\">hook</span><span
  class=\"o\">.</span><span class=\"n\">load</span><span class=\"p\">(</span><span
  class=\"n\">markata</span><span class=\"o\">=</span><span class=\"bp\">self</span><span
  class=\"p\">)</span>\n        <span class=\"k\">return</span> <span class=\"bp\">self</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"pre_render-method\">pre_render <code>method</code></h2>\n<p>None</p>\n<details>\n<summary>pre_render
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">pre_render</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"n\">Markata</span><span
  class=\"p\">:</span>\n        <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">_pm</span><span class=\"o\">.</span><span class=\"n\">hook</span><span
  class=\"o\">.</span><span class=\"n\">pre_render</span><span class=\"p\">(</span><span
  class=\"n\">markata</span><span class=\"o\">=</span><span class=\"bp\">self</span><span
  class=\"p\">)</span>\n        <span class=\"k\">return</span> <span class=\"bp\">self</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"render-method\">render <code>method</code></h2>\n<p>None</p>\n<details>\n<summary>render
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">render</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"n\">Markata</span><span
  class=\"p\">:</span>\n        <span class=\"k\">try</span><span class=\"p\">:</span>\n
  \           <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">_pm</span><span
  class=\"o\">.</span><span class=\"n\">hook</span><span class=\"o\">.</span><span
  class=\"n\">pre_render</span><span class=\"p\">(</span><span class=\"n\">markata</span><span
  class=\"o\">=</span><span class=\"bp\">self</span><span class=\"p\">)</span>\n            <span
  class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">_pm</span><span
  class=\"o\">.</span><span class=\"n\">hook</span><span class=\"o\">.</span><span
  class=\"n\">render</span><span class=\"p\">(</span><span class=\"n\">markata</span><span
  class=\"o\">=</span><span class=\"bp\">self</span><span class=\"p\">)</span>\n            <span
  class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">_pm</span><span
  class=\"o\">.</span><span class=\"n\">hook</span><span class=\"o\">.</span><span
  class=\"n\">post_render</span><span class=\"p\">(</span><span class=\"n\">markata</span><span
  class=\"o\">=</span><span class=\"bp\">self</span><span class=\"p\">)</span>\n        <span
  class=\"k\">except</span> <span class=\"ne\">AttributeError</span><span class=\"p\">:</span>\n
  \           <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">load</span><span
  class=\"p\">()</span>\n            <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">_pm</span><span class=\"o\">.</span><span class=\"n\">hook</span><span
  class=\"o\">.</span><span class=\"n\">pre_render</span><span class=\"p\">(</span><span
  class=\"n\">markata</span><span class=\"o\">=</span><span class=\"bp\">self</span><span
  class=\"p\">)</span>\n            <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">_pm</span><span class=\"o\">.</span><span class=\"n\">hook</span><span
  class=\"o\">.</span><span class=\"n\">render</span><span class=\"p\">(</span><span
  class=\"n\">markata</span><span class=\"o\">=</span><span class=\"bp\">self</span><span
  class=\"p\">)</span>\n            <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">_pm</span><span class=\"o\">.</span><span class=\"n\">hook</span><span
  class=\"o\">.</span><span class=\"n\">post_render</span><span class=\"p\">(</span><span
  class=\"n\">markata</span><span class=\"o\">=</span><span class=\"bp\">self</span><span
  class=\"p\">)</span>\n        <span class=\"k\">return</span> <span class=\"bp\">self</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"post_render-method\">post_render <code>method</code></h2>\n<p>None</p>\n<details>\n<summary>post_render
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">post_render</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"n\">Markata</span><span
  class=\"p\">:</span>\n        <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">_pm</span><span class=\"o\">.</span><span class=\"n\">hook</span><span
  class=\"o\">.</span><span class=\"n\">post_render</span><span class=\"p\">(</span><span
  class=\"n\">markata</span><span class=\"o\">=</span><span class=\"bp\">self</span><span
  class=\"p\">)</span>\n        <span class=\"k\">return</span> <span class=\"bp\">self</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"save-method\">save <code>method</code></h2>\n<p>None</p>\n<details>\n<summary>save
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">save</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"n\">Markata</span><span
  class=\"p\">:</span>\n        <span class=\"k\">try</span><span class=\"p\">:</span>\n
  \           <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">_pm</span><span
  class=\"o\">.</span><span class=\"n\">hook</span><span class=\"o\">.</span><span
  class=\"n\">save</span><span class=\"p\">(</span><span class=\"n\">markata</span><span
  class=\"o\">=</span><span class=\"bp\">self</span><span class=\"p\">)</span>\n        <span
  class=\"k\">except</span> <span class=\"ne\">AttributeError</span><span class=\"p\">:</span>\n
  \           <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">render</span><span
  class=\"p\">()</span>\n            <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">_pm</span><span class=\"o\">.</span><span class=\"n\">hook</span><span
  class=\"o\">.</span><span class=\"n\">save</span><span class=\"p\">(</span><span
  class=\"n\">markata</span><span class=\"o\">=</span><span class=\"bp\">self</span><span
  class=\"p\">)</span>\n        <span class=\"k\">return</span> <span class=\"bp\">self</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"run-method\">run <code>method</code></h2>\n<p>None</p>\n<details>\n<summary>run
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">run</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">,</span> <span class=\"n\">lifecycle</span><span class=\"p\">:</span>
  <span class=\"n\">LifeCycle</span> <span class=\"o\">=</span> <span class=\"kc\">None</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"n\">Markata</span><span
  class=\"p\">:</span>\n        <span class=\"k\">if</span> <span class=\"n\">lifecycle</span>
  <span class=\"ow\">is</span> <span class=\"kc\">None</span><span class=\"p\">:</span>\n
  \           <span class=\"n\">lifecycle</span> <span class=\"o\">=</span> <span
  class=\"nb\">getattr</span><span class=\"p\">(</span><span class=\"n\">LifeCycle</span><span
  class=\"p\">,</span> <span class=\"nb\">max</span><span class=\"p\">(</span><span
  class=\"n\">LifeCycle</span><span class=\"o\">.</span><span class=\"n\">_member_map_</span><span
  class=\"p\">))</span>\n\n        <span class=\"k\">if</span> <span class=\"nb\">isinstance</span><span
  class=\"p\">(</span><span class=\"n\">lifecycle</span><span class=\"p\">,</span>
  <span class=\"nb\">str</span><span class=\"p\">):</span>\n            <span class=\"n\">lifecycle</span>
  <span class=\"o\">=</span> <span class=\"n\">LifeCycle</span><span class=\"p\">[</span><span
  class=\"n\">lifecycle</span><span class=\"p\">]</span>\n\n        <span class=\"n\">stages_to_run</span>
  <span class=\"o\">=</span> <span class=\"p\">[</span><span class=\"n\">m</span>
  <span class=\"k\">for</span> <span class=\"n\">m</span> <span class=\"ow\">in</span>
  <span class=\"n\">LifeCycle</span><span class=\"o\">.</span><span class=\"n\">_member_map_</span>
  <span class=\"k\">if</span> <span class=\"n\">LifeCycle</span><span class=\"p\">[</span><span
  class=\"n\">m</span><span class=\"p\">]</span> <span class=\"o\">&lt;=</span> <span
  class=\"n\">lifecycle</span><span class=\"p\">]</span>\n\n        <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">console</span><span class=\"o\">.</span><span
  class=\"n\">log</span><span class=\"p\">(</span><span class=\"sa\">f</span><span
  class=\"s2\">&quot;running </span><span class=\"si\">{</span><span class=\"n\">stages_to_run</span><span
  class=\"si\">}</span><span class=\"s2\">&quot;</span><span class=\"p\">)</span>\n
  \       <span class=\"k\">for</span> <span class=\"n\">stage</span> <span class=\"ow\">in</span>
  <span class=\"n\">stages_to_run</span><span class=\"p\">:</span>\n            <span
  class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">console</span><span
  class=\"o\">.</span><span class=\"n\">log</span><span class=\"p\">(</span><span
  class=\"sa\">f</span><span class=\"s2\">&quot;</span><span class=\"si\">{</span><span
  class=\"n\">stage</span><span class=\"si\">}</span><span class=\"s2\"> running&quot;</span><span
  class=\"p\">)</span>\n            <span class=\"nb\">getattr</span><span class=\"p\">(</span><span
  class=\"bp\">self</span><span class=\"p\">,</span> <span class=\"n\">stage</span><span
  class=\"p\">)()</span>\n            <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">console</span><span class=\"o\">.</span><span class=\"n\">log</span><span
  class=\"p\">(</span><span class=\"sa\">f</span><span class=\"s2\">&quot;</span><span
  class=\"si\">{</span><span class=\"n\">stage</span><span class=\"si\">}</span><span
  class=\"s2\"> complete&quot;</span><span class=\"p\">)</span>\n\n        <span class=\"k\">with</span>
  <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">cache</span>
  <span class=\"k\">as</span> <span class=\"n\">cache</span><span class=\"p\">:</span>\n
  \           <span class=\"n\">hits</span><span class=\"p\">,</span> <span class=\"n\">misses</span>
  <span class=\"o\">=</span> <span class=\"n\">cache</span><span class=\"o\">.</span><span
  class=\"n\">stats</span><span class=\"p\">()</span>\n\n        <span class=\"k\">if</span>
  <span class=\"n\">hits</span> <span class=\"o\">+</span> <span class=\"n\">misses</span>
  <span class=\"o\">&gt;</span> <span class=\"mi\">0</span><span class=\"p\">:</span>\n
  \           <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">console</span><span
  class=\"o\">.</span><span class=\"n\">log</span><span class=\"p\">(</span><span
  class=\"sa\">f</span><span class=\"s2\">&quot;cache hit rate </span><span class=\"si\">{</span><span
  class=\"nb\">round</span><span class=\"p\">(</span><span class=\"n\">hits</span><span
  class=\"o\">/</span> <span class=\"p\">(</span><span class=\"n\">hits</span> <span
  class=\"o\">+</span> <span class=\"n\">misses</span><span class=\"p\">)</span><span
  class=\"o\">*</span><span class=\"mi\">100</span><span class=\"p\">,</span> <span
  class=\"mi\">2</span><span class=\"p\">)</span><span class=\"si\">}</span><span
  class=\"s2\">%&quot;</span><span class=\"p\">)</span>\n        <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">console</span><span class=\"o\">.</span><span
  class=\"n\">log</span><span class=\"p\">(</span><span class=\"sa\">f</span><span
  class=\"s2\">&quot;cache hits/misses </span><span class=\"si\">{</span><span class=\"n\">hits</span><span
  class=\"si\">}</span><span class=\"s2\">/</span><span class=\"si\">{</span><span
  class=\"n\">misses</span><span class=\"si\">}</span><span class=\"s2\">&quot;</span><span
  class=\"p\">)</span>\n\n        <span class=\"k\">return</span> <span class=\"bp\">self</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"filter-method\">filter <code>method</code></h2>\n<p>None</p>\n<details>\n<summary>filter
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">filter</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">,</span> <span class=\"nb\">filter</span><span class=\"p\">:</span>
  <span class=\"nb\">str</span><span class=\"p\">)</span> <span class=\"o\">-&gt;</span>
  <span class=\"n\">List</span><span class=\"p\">:</span>\n        <span class=\"k\">def</span>
  <span class=\"nf\">evalr</span><span class=\"p\">(</span><span class=\"n\">a</span><span
  class=\"p\">:</span> <span class=\"n\">Post</span><span class=\"p\">)</span> <span
  class=\"o\">-&gt;</span> <span class=\"n\">Any</span><span class=\"p\">:</span>\n
  \           <span class=\"k\">try</span><span class=\"p\">:</span>\n                <span
  class=\"k\">return</span> <span class=\"nb\">eval</span><span class=\"p\">(</span><span
  class=\"nb\">filter</span><span class=\"p\">,</span> <span class=\"p\">{</span><span
  class=\"o\">**</span><span class=\"n\">a</span><span class=\"o\">.</span><span class=\"n\">to_dict</span><span
  class=\"p\">(),</span> <span class=\"s2\">&quot;timedelta&quot;</span><span class=\"p\">:</span>
  <span class=\"n\">timedelta</span><span class=\"p\">},</span> <span class=\"p\">{})</span>\n
  \           <span class=\"k\">except</span> <span class=\"ne\">AttributeError</span><span
  class=\"p\">:</span>\n                <span class=\"k\">return</span> <span class=\"nb\">eval</span><span
  class=\"p\">(</span><span class=\"nb\">filter</span><span class=\"p\">,</span> <span
  class=\"p\">{</span><span class=\"o\">**</span><span class=\"n\">a</span><span class=\"p\">,</span>
  <span class=\"s2\">&quot;timedelta&quot;</span><span class=\"p\">:</span> <span
  class=\"n\">timedelta</span><span class=\"p\">},</span> <span class=\"p\">{})</span>\n\n
  \       <span class=\"k\">return</span> <span class=\"p\">[</span><span class=\"n\">a</span>
  <span class=\"k\">for</span> <span class=\"n\">a</span> <span class=\"ow\">in</span>
  <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">articles</span>
  <span class=\"k\">if</span> <span class=\"n\">evalr</span><span class=\"p\">(</span><span
  class=\"n\">a</span><span class=\"p\">)]</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"map-method\">map <code>method</code></h2>\n<p>None</p>\n<details>\n<summary>map
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">map</span><span class=\"p\">(</span>\n        <span class=\"bp\">self</span><span
  class=\"p\">,</span> <span class=\"n\">func</span><span class=\"p\">:</span> <span
  class=\"nb\">str</span> <span class=\"o\">=</span> <span class=\"s2\">&quot;title&quot;</span><span
  class=\"p\">,</span> <span class=\"nb\">filter</span><span class=\"p\">:</span>
  <span class=\"nb\">str</span> <span class=\"o\">=</span> <span class=\"s2\">&quot;True&quot;</span><span
  class=\"p\">,</span> <span class=\"n\">sort</span><span class=\"p\">:</span> <span
  class=\"nb\">str</span> <span class=\"o\">=</span> <span class=\"s2\">&quot;True&quot;</span>\n
  \   <span class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"n\">List</span><span
  class=\"p\">:</span>\n        <span class=\"kn\">import</span> <span class=\"nn\">copy</span>\n\n
  \       <span class=\"k\">def</span> <span class=\"nf\">try_sort</span><span class=\"p\">(</span><span
  class=\"n\">a</span><span class=\"p\">:</span> <span class=\"n\">Any</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"nb\">int</span><span
  class=\"p\">:</span>\n\n            <span class=\"k\">try</span><span class=\"p\">:</span>\n
  \               <span class=\"n\">value</span> <span class=\"o\">=</span> <span
  class=\"nb\">eval</span><span class=\"p\">(</span><span class=\"n\">sort</span><span
  class=\"p\">,</span> <span class=\"n\">a</span><span class=\"o\">.</span><span class=\"n\">to_dict</span><span
  class=\"p\">(),</span> <span class=\"p\">{})</span>\n            <span class=\"k\">except</span>
  <span class=\"ne\">NameError</span><span class=\"p\">:</span>\n                <span
  class=\"k\">return</span> <span class=\"o\">-</span><span class=\"mi\">1</span>\n
  \           <span class=\"k\">try</span><span class=\"p\">:</span>\n                <span
  class=\"k\">return</span> <span class=\"nb\">int</span><span class=\"p\">(</span><span
  class=\"n\">value</span><span class=\"p\">)</span>\n            <span class=\"k\">except</span>
  <span class=\"ne\">TypeError</span><span class=\"p\">:</span>\n                <span
  class=\"k\">try</span><span class=\"p\">:</span>\n                    <span class=\"k\">return</span>
  <span class=\"nb\">int</span><span class=\"p\">(</span><span class=\"n\">value</span><span
  class=\"o\">.</span><span class=\"n\">timestamp</span><span class=\"p\">())</span>\n
  \               <span class=\"k\">except</span> <span class=\"ne\">Exception</span><span
  class=\"p\">:</span>\n                    <span class=\"k\">try</span><span class=\"p\">:</span>\n
  \                       <span class=\"k\">return</span> <span class=\"nb\">int</span><span
  class=\"p\">(</span>\n                            <span class=\"n\">datetime</span><span
  class=\"o\">.</span><span class=\"n\">datetime</span><span class=\"o\">.</span><span
  class=\"n\">combine</span><span class=\"p\">(</span>\n                                <span
  class=\"n\">value</span><span class=\"p\">,</span> <span class=\"n\">datetime</span><span
  class=\"o\">.</span><span class=\"n\">datetime</span><span class=\"o\">.</span><span
  class=\"n\">min</span><span class=\"o\">.</span><span class=\"n\">time</span><span
  class=\"p\">()</span>\n                            <span class=\"p\">)</span><span
  class=\"o\">.</span><span class=\"n\">timestamp</span><span class=\"p\">()</span>\n
  \                       <span class=\"p\">)</span>\n                    <span class=\"k\">except</span>
  <span class=\"ne\">Exception</span><span class=\"p\">:</span>\n                        <span
  class=\"k\">try</span><span class=\"p\">:</span>\n                            <span
  class=\"k\">return</span> <span class=\"nb\">sum</span><span class=\"p\">([</span><span
  class=\"nb\">ord</span><span class=\"p\">(</span><span class=\"n\">c</span><span
  class=\"p\">)</span> <span class=\"k\">for</span> <span class=\"n\">c</span> <span
  class=\"ow\">in</span> <span class=\"nb\">str</span><span class=\"p\">(</span><span
  class=\"n\">value</span><span class=\"p\">)])</span>\n                        <span
  class=\"k\">except</span> <span class=\"ne\">Exception</span><span class=\"p\">:</span>\n
  \                           <span class=\"k\">return</span> <span class=\"o\">-</span><span
  class=\"mi\">1</span>\n\n        <span class=\"n\">articles</span> <span class=\"o\">=</span>
  <span class=\"n\">copy</span><span class=\"o\">.</span><span class=\"n\">copy</span><span
  class=\"p\">(</span><span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">articles</span><span class=\"p\">)</span>\n        <span class=\"n\">articles</span><span
  class=\"o\">.</span><span class=\"n\">sort</span><span class=\"p\">(</span><span
  class=\"n\">key</span><span class=\"o\">=</span><span class=\"n\">try_sort</span><span
  class=\"p\">)</span>\n        <span class=\"k\">return</span> <span class=\"p\">[</span>\n
  \           <span class=\"nb\">eval</span><span class=\"p\">(</span><span class=\"n\">func</span><span
  class=\"p\">,</span> <span class=\"p\">{</span><span class=\"o\">**</span><span
  class=\"n\">a</span><span class=\"o\">.</span><span class=\"n\">to_dict</span><span
  class=\"p\">(),</span> <span class=\"s2\">&quot;timedelta&quot;</span><span class=\"p\">:</span>
  <span class=\"n\">timedelta</span><span class=\"p\">},</span> <span class=\"p\">{})</span>\n
  \           <span class=\"k\">for</span> <span class=\"n\">a</span> <span class=\"ow\">in</span>
  <span class=\"n\">articles</span>\n            <span class=\"k\">if</span> <span
  class=\"nb\">eval</span><span class=\"p\">(</span><span class=\"nb\">filter</span><span
  class=\"p\">,</span> <span class=\"p\">{</span><span class=\"o\">**</span><span
  class=\"n\">a</span><span class=\"o\">.</span><span class=\"n\">to_dict</span><span
  class=\"p\">(),</span> <span class=\"s2\">&quot;timedelta&quot;</span><span class=\"p\">:</span>
  <span class=\"n\">timedelta</span><span class=\"p\">},</span> <span class=\"p\">{})</span>\n
  \       <span class=\"p\">]</span>\n</code></pre></div>\n</details>\n<hr />\n<h2
  id=\"evalr-function\">evalr <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>evalr
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">evalr</span><span class=\"p\">(</span><span class=\"n\">a</span><span
  class=\"p\">:</span> <span class=\"n\">Post</span><span class=\"p\">)</span> <span
  class=\"o\">-&gt;</span> <span class=\"n\">Any</span><span class=\"p\">:</span>\n
  \           <span class=\"k\">try</span><span class=\"p\">:</span>\n                <span
  class=\"k\">return</span> <span class=\"nb\">eval</span><span class=\"p\">(</span><span
  class=\"nb\">filter</span><span class=\"p\">,</span> <span class=\"p\">{</span><span
  class=\"o\">**</span><span class=\"n\">a</span><span class=\"o\">.</span><span class=\"n\">to_dict</span><span
  class=\"p\">(),</span> <span class=\"s2\">&quot;timedelta&quot;</span><span class=\"p\">:</span>
  <span class=\"n\">timedelta</span><span class=\"p\">},</span> <span class=\"p\">{})</span>\n
  \           <span class=\"k\">except</span> <span class=\"ne\">AttributeError</span><span
  class=\"p\">:</span>\n                <span class=\"k\">return</span> <span class=\"nb\">eval</span><span
  class=\"p\">(</span><span class=\"nb\">filter</span><span class=\"p\">,</span> <span
  class=\"p\">{</span><span class=\"o\">**</span><span class=\"n\">a</span><span class=\"p\">,</span>
  <span class=\"s2\">&quot;timedelta&quot;</span><span class=\"p\">:</span> <span
  class=\"n\">timedelta</span><span class=\"p\">},</span> <span class=\"p\">{})</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"try_sort-function\">try_sort <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>try_sort
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">try_sort</span><span class=\"p\">(</span><span class=\"n\">a</span><span
  class=\"p\">:</span> <span class=\"n\">Any</span><span class=\"p\">)</span> <span
  class=\"o\">-&gt;</span> <span class=\"nb\">int</span><span class=\"p\">:</span>\n\n
  \           <span class=\"k\">try</span><span class=\"p\">:</span>\n                <span
  class=\"n\">value</span> <span class=\"o\">=</span> <span class=\"nb\">eval</span><span
  class=\"p\">(</span><span class=\"n\">sort</span><span class=\"p\">,</span> <span
  class=\"n\">a</span><span class=\"o\">.</span><span class=\"n\">to_dict</span><span
  class=\"p\">(),</span> <span class=\"p\">{})</span>\n            <span class=\"k\">except</span>
  <span class=\"ne\">NameError</span><span class=\"p\">:</span>\n                <span
  class=\"k\">return</span> <span class=\"o\">-</span><span class=\"mi\">1</span>\n
  \           <span class=\"k\">try</span><span class=\"p\">:</span>\n                <span
  class=\"k\">return</span> <span class=\"nb\">int</span><span class=\"p\">(</span><span
  class=\"n\">value</span><span class=\"p\">)</span>\n            <span class=\"k\">except</span>
  <span class=\"ne\">TypeError</span><span class=\"p\">:</span>\n                <span
  class=\"k\">try</span><span class=\"p\">:</span>\n                    <span class=\"k\">return</span>
  <span class=\"nb\">int</span><span class=\"p\">(</span><span class=\"n\">value</span><span
  class=\"o\">.</span><span class=\"n\">timestamp</span><span class=\"p\">())</span>\n
  \               <span class=\"k\">except</span> <span class=\"ne\">Exception</span><span
  class=\"p\">:</span>\n                    <span class=\"k\">try</span><span class=\"p\">:</span>\n
  \                       <span class=\"k\">return</span> <span class=\"nb\">int</span><span
  class=\"p\">(</span>\n                            <span class=\"n\">datetime</span><span
  class=\"o\">.</span><span class=\"n\">datetime</span><span class=\"o\">.</span><span
  class=\"n\">combine</span><span class=\"p\">(</span>\n                                <span
  class=\"n\">value</span><span class=\"p\">,</span> <span class=\"n\">datetime</span><span
  class=\"o\">.</span><span class=\"n\">datetime</span><span class=\"o\">.</span><span
  class=\"n\">min</span><span class=\"o\">.</span><span class=\"n\">time</span><span
  class=\"p\">()</span>\n                            <span class=\"p\">)</span><span
  class=\"o\">.</span><span class=\"n\">timestamp</span><span class=\"p\">()</span>\n
  \                       <span class=\"p\">)</span>\n                    <span class=\"k\">except</span>
  <span class=\"ne\">Exception</span><span class=\"p\">:</span>\n                        <span
  class=\"k\">try</span><span class=\"p\">:</span>\n                            <span
  class=\"k\">return</span> <span class=\"nb\">sum</span><span class=\"p\">([</span><span
  class=\"nb\">ord</span><span class=\"p\">(</span><span class=\"n\">c</span><span
  class=\"p\">)</span> <span class=\"k\">for</span> <span class=\"n\">c</span> <span
  class=\"ow\">in</span> <span class=\"nb\">str</span><span class=\"p\">(</span><span
  class=\"n\">value</span><span class=\"p\">)])</span>\n                        <span
  class=\"k\">except</span> <span class=\"ne\">Exception</span><span class=\"p\">:</span>\n
  \                           <span class=\"k\">return</span> <span class=\"o\">-</span><span
  class=\"mi\">1</span>\n</code></pre></div>\n</details>"
datetime: null
description: Docs for __init__
long_description: ''
now: 2022-02-05 19:38:00.891368
path: __init__.md
slug: markata/__init__
status: published
title: __init__.py
today: 2022-02-05
---

Markata is a tool for handling directories of markdown.


---

## Post `class`

None

??? "Post source"
    ``` python
    class Post(frontmatter.Post):
        html: str
    ```


---

## set_phase `function`

None

??? "set_phase source"
    ``` python
    def set_phase(function: Callable) -> Any:
        def wrapper(self: Markata, *args: Tuple, **kwargs: Dict) -> Any:
            self.phase = function.__name__
            result = function(self, *args, **kwargs)
            self.phase = function.__name__
            self.phase_file.write_text(self.phase)
            return result

        return wrapper
    ```


---

## Markata `class`

None

??? "Markata source"
    ``` python
    class Markata:
        def __init__(self, console: Console = None) -> None:
            self.phase = "starting"
            self.MARKATA_CACHE_DIR = Path(".") / ".markata.cache"
            self.MARKATA_CACHE_DIR.mkdir(exist_ok=True)
            self.phase_file: Path = self.MARKATA_CACHE_DIR / "phase.txt"
            self.registered_attrs = hookspec.registered_attrs
            self.configure()
            if console is not None:
                self._console = console

        @property
        def cache(self) -> FanoutCache:
            return FanoutCache(self.MARKATA_CACHE_DIR, statistics=True)

        def __getattr__(self, item: str) -> Any:
            if item in self.__dict__.keys():
                return self.__getitem__(item)
            elif item in self.registered_attrs.keys():
                stage_to_run_to = max(
                    [attr["lifecycle"] for attr in self.registered_attrs[item]]
                ).name
                self.run(stage_to_run_to)
                return getattr(self, item)
            else:
                raise AttributeError(item)

        @property
        def server(self) -> Server:
            try:
                return self._server
            except AttributeError:

                self._server: Server = Server(directory=str(self.config["output_dir"]))
                return self.server

        @property
        def runner(self) -> Runner:
            try:
                return self._runner
            except AttributeError:

                self._runner: Runner = Runner(self)
                return self.runner

        @property
        def plugins(self) -> Plugins:
            try:
                return self._plugins
            except AttributeError:

                self._plugins: Plugins = Plugins(self)
            return self.plugins

        @property
        def summary(self) -> Summary:
            try:
                return self._summary
            except AttributeError:

                self._summary: Summary = Summary(self)
                return self.summary

        def __rich__(self) -> Table:

            grid = Table.grid()
            grid.add_column("label")
            grid.add_column("value")

            for label, value in self.describe().items():
                grid.add_row(label, value)

            return grid

        def bust_cache(self) -> Markata:
            with self.cache as cache:
                cache.clear()
            return self

        @set_phase
        def configure(self) -> Markata:
            sys.path.append(os.getcwd())
            self.config = {**DEFUALT_CONFIG, **standard_config.load("markata")}
            if isinstance(self.config["glob_patterns"], str):
                self.config["glob_patterns"] = self.config["glob_patterns"].split(",")
            elif isinstance(self.config["glob_patterns"], list):
                self.config["glob_patterns"] = list(self.config["glob_patterns"])
            else:
                raise TypeError("glob_patterns must be list or str")
            self.glob_patterns = self.config["glob_patterns"]

            if "hooks" not in self.config:
                self.hooks = [""]
            if isinstance(self.config["hooks"], str):
                self.hooks = self.config["hooks"].split(",")
            if isinstance(self.config["hooks"], list):
                self.hooks = self.config["hooks"]

            if "disabled_hooks" not in self.config:
                self.disabled_hooks = [""]
            if isinstance(self.config["disabled_hooks"], str):
                self.disabled_hooks = self.config["disabled_hooks"].split(",")
            if isinstance(self.config["disabled_hooks"], list):
                self.disabled_hooks = self.config["disabled_hooks"]

            try:
                default_index = self.hooks.index("default")
                hooks = [
                    *self.hooks[:default_index],
                    *DEFAULT_HOOKS,
                    *self.hooks[default_index + 1 :],
                ]
                self.hooks = [hook for hook in hooks if hook not in self.disabled_hooks]
            except ValueError:
                # 'default' is not in hooks , do not replace with default_hooks
                pass

            self._pm = pluggy.PluginManager("markata")
            self._pm.add_hookspecs(hookspec.MarkataSpecs)
            self._register_hooks()

            self._pm.hook.configure(markata=self)
            return self

        def get_plugin_config(self, path_or_name: str) -> Dict:

            key = Path(path_or_name).stem

            try:
                config = self.config[key]
            except KeyError:
                config = {}
            if not isinstance(config, dict):
                raise TypeError("must use dict")
            if "cache_expire" not in config.keys():
                config["cache_expire"] = self.config["default_cache_expire"]
            if "config_key" not in config.keys():
                config["config_key"] = key
            return config

        def get_config(
            self, key: str, warn: bool = True, suggested: Optional[str] = None
        ) -> Any:
            if key in self.config.keys():
                return self.config[key]
            else:

                if suggested is None:
                    suggested = textwrap.dedent(
                        f"""
                            \[markata]
                            {key} = value
                        """  # noqa: W605
                    )
                if warn:
                    self.console.log(
                        textwrap.dedent(
                            f"""
                            Warning site_name is not set in markata config, sitemap will
                            be missing root site_name
                            to resolve this open your markata.toml and add

                            {suggested}

                            """
                        ),
                        style="yellow",
                    )

        def make_hash(self, *keys: str) -> str:
            str_keys = [str(key) for key in keys]
            return hashlib.md5("".join(str_keys).encode("utf-8")).hexdigest()

        @property
        def phase(self) -> str:
            return self._phase

        @phase.setter
        def phase(self, value: str) -> None:
            self._phase = value

        @property
        def content_dir_hash(self) -> str:
            hashes = [dirhash(dir) for dir in self.content_directories]
            return self.make_hash(*hashes)

        @property
        def console(self) -> Console:
            try:
                return self._console
            except AttributeError:
                self._console = Console()
                return self._console

        def describe(self) -> dict[str, str]:
            return {"version": __version__, "phase": self.phase}

        def _to_dict(self) -> dict[str, Iterable]:
            return {"config": self.config, "articles": [a.to_dict() for a in self.articles]}

        def to_dict(self) -> dict:
            try:
                return self._to_dict()
            except AttributeError:
                self.render()
                return self._to_dict()

        def to_json(self) -> str:
            import json

            return json.dumps(self.to_dict(), indent=4, sort_keys=True, default=str)

        def _register_hooks(self) -> None:
            for hook in self.hooks:
                try:
                    # module style plugins
                    plugin = importlib.import_module(hook)
                except ModuleNotFoundError as e:
                    # class style plugins
                    if "." in hook:
                        mod = importlib.import_module(".".join(hook.split(".")[:-1]))
                        plugin = getattr(mod, hook.split(".")[-1])
                    else:
                        raise e

                self._pm.register(plugin)

        def __iter__(self, description: str = "working...") -> Iterable[frontmatter.Post]:
            articles: Iterable[frontmatter.Post] = track(
                self.articles, description=description, transient=True, console=self.console
            )
            return articles

        def iter_articles(self, description: str) -> Iterable[frontmatter.Post]:
            articles: Iterable[frontmatter.Post] = track(
                self.articles, description=description, transient=True, console=self.console
            )
            return articles

        @set_phase
        def glob(self) -> Markata:
            """run glob hooks

            Glob hooks should append file lists to the markata object for later
            hooks to build from.  The default loader will utilize the `files`
            attribute for loading.
            """

            try:
                self._pm.hook.glob(markata=self)
            except AttributeError:
                self.configure()
                self._pm.hook.glob(markata=self)

            return self

        @set_phase
        def load(self) -> Markata:
            try:
                self._pm.hook.load(markata=self)
            except AttributeError:
                self.glob()
                self._pm.hook.load(markata=self)
            return self

        # @set_phase
        def pre_render(self) -> Markata:
            self._pm.hook.pre_render(markata=self)
            return self

        # @set_phase
        def render(self) -> Markata:
            try:
                self._pm.hook.pre_render(markata=self)
                self._pm.hook.render(markata=self)
                self._pm.hook.post_render(markata=self)
            except AttributeError:
                self.load()
                self._pm.hook.pre_render(markata=self)
                self._pm.hook.render(markata=self)
                self._pm.hook.post_render(markata=self)
            return self

        # @set_phase
        def post_render(self) -> Markata:
            self._pm.hook.post_render(markata=self)
            return self

        # @set_phase
        def save(self) -> Markata:
            try:
                self._pm.hook.save(markata=self)
            except AttributeError:
                self.render()
                self._pm.hook.save(markata=self)
            return self

        def run(self, lifecycle: LifeCycle = None) -> Markata:
            if lifecycle is None:
                lifecycle = getattr(LifeCycle, max(LifeCycle._member_map_))

            if isinstance(lifecycle, str):
                lifecycle = LifeCycle[lifecycle]

            stages_to_run = [m for m in LifeCycle._member_map_ if LifeCycle[m] <= lifecycle]

            self.console.log(f"running {stages_to_run}")
            for stage in stages_to_run:
                self.console.log(f"{stage} running")
                getattr(self, stage)()
                self.console.log(f"{stage} complete")

            with self.cache as cache:
                hits, misses = cache.stats()

            if hits + misses > 0:
                self.console.log(f"cache hit rate {round(hits/ (hits + misses)*100, 2)}%")
            self.console.log(f"cache hits/misses {hits}/{misses}")

            return self

        def filter(self, filter: str) -> List:
            def evalr(a: Post) -> Any:
                try:
                    return eval(filter, {**a.to_dict(), "timedelta": timedelta}, {})
                except AttributeError:
                    return eval(filter, {**a, "timedelta": timedelta}, {})

            return [a for a in self.articles if evalr(a)]

        def map(
            self, func: str = "title", filter: str = "True", sort: str = "True"
        ) -> List:
            import copy

            def try_sort(a: Any) -> int:

                try:
                    value = eval(sort, a.to_dict(), {})
                except NameError:
                    return -1
                try:
                    return int(value)
                except TypeError:
                    try:
                        return int(value.timestamp())
                    except Exception:
                        try:
                            return int(
                                datetime.datetime.combine(
                                    value, datetime.datetime.min.time()
                                ).timestamp()
                            )
                        except Exception:
                            try:
                                return sum([ord(c) for c in str(value)])
                            except Exception:
                                return -1

            articles = copy.copy(self.articles)
            articles.sort(key=try_sort)
            return [
                eval(func, {**a.to_dict(), "timedelta": timedelta}, {})
                for a in articles
                if eval(filter, {**a.to_dict(), "timedelta": timedelta}, {})
            ]
    ```


---

## clif `function`

None

??? "clif source"
    ``` python
    def clif() -> None:
        import sys
        import time

        from rich import pretty, traceback

        if "--no-rich" not in sys.argv:
            pretty.install()
            traceback.install()

        m = Markata()

        if "--quiet" in sys.argv or "-q" in sys.argv:
            m.console.quiet = True
        else:
            m.console.print("console options:", m.console.options)

        if "--to-dict" in sys.argv:
            m.console.quiet = True
            data = m.to_dict()
            m.console.quiet = False
            m.console.print(data)
            return

        if "--draft" in sys.argv:
            print("\n".join([a["path"] for a in m.articles if a["status"] == "draft"]))

            return

        if "--today" in sys.argv:
            print("\n".join([a["path"] for a in m.articles if a["date"] == a["today"]]))
            return

        if "--scheduled" in sys.argv:
            print("\n".join([a["path"] for a in m.articles if a["date"] > a["today"]]))
            return

        if "--back-days" in sys.argv:
            print("\n".join([a["path"] for a in m.articles if a["date"] > a["today"]]))
            return

        if "--watch" in sys.argv:

            hash = m.content_dir_hash
            m.run()
            console = Console()
            with console.status("waiting for change", spinner="aesthetic", speed=0.2):
                while True:
                    if m.content_dir_hash != hash:
                        hash = m.content_dir_hash
                        m.run()
                    time.sleep(0.1)

        m.run()
    ```


---

## wrapper `function`

None

??? "wrapper source"
    ``` python
    def wrapper(self: Markata, *args: Tuple, **kwargs: Dict) -> Any:
            self.phase = function.__name__
            result = function(self, *args, **kwargs)
            self.phase = function.__name__
            self.phase_file.write_text(self.phase)
            return result
    ```


---

## __init__ `method`

None

??? "__init__ source"
    ``` python
    def __init__(self, console: Console = None) -> None:
            self.phase = "starting"
            self.MARKATA_CACHE_DIR = Path(".") / ".markata.cache"
            self.MARKATA_CACHE_DIR.mkdir(exist_ok=True)
            self.phase_file: Path = self.MARKATA_CACHE_DIR / "phase.txt"
            self.registered_attrs = hookspec.registered_attrs
            self.configure()
            if console is not None:
                self._console = console
    ```


---

## cache `method`

None

??? "cache source"
    ``` python
    def cache(self) -> FanoutCache:
            return FanoutCache(self.MARKATA_CACHE_DIR, statistics=True)
    ```


---

## __getattr__ `method`

None

??? "__getattr__ source"
    ``` python
    def __getattr__(self, item: str) -> Any:
            if item in self.__dict__.keys():
                return self.__getitem__(item)
            elif item in self.registered_attrs.keys():
                stage_to_run_to = max(
                    [attr["lifecycle"] for attr in self.registered_attrs[item]]
                ).name
                self.run(stage_to_run_to)
                return getattr(self, item)
            else:
                raise AttributeError(item)
    ```


---

## server `method`

None

??? "server source"
    ``` python
    def server(self) -> Server:
            try:
                return self._server
            except AttributeError:

                self._server: Server = Server(directory=str(self.config["output_dir"]))
                return self.server
    ```


---

## runner `method`

None

??? "runner source"
    ``` python
    def runner(self) -> Runner:
            try:
                return self._runner
            except AttributeError:

                self._runner: Runner = Runner(self)
                return self.runner
    ```


---

## plugins `method`

None

??? "plugins source"
    ``` python
    def plugins(self) -> Plugins:
            try:
                return self._plugins
            except AttributeError:

                self._plugins: Plugins = Plugins(self)
            return self.plugins
    ```


---

## summary `method`

None

??? "summary source"
    ``` python
    def summary(self) -> Summary:
            try:
                return self._summary
            except AttributeError:

                self._summary: Summary = Summary(self)
                return self.summary
    ```


---

## __rich__ `method`

None

??? "__rich__ source"
    ``` python
    def __rich__(self) -> Table:

            grid = Table.grid()
            grid.add_column("label")
            grid.add_column("value")

            for label, value in self.describe().items():
                grid.add_row(label, value)

            return grid
    ```


---

## bust_cache `method`

None

??? "bust_cache source"
    ``` python
    def bust_cache(self) -> Markata:
            with self.cache as cache:
                cache.clear()
            return self
    ```


---

## configure `method`

None

??? "configure source"
    ``` python
    def configure(self) -> Markata:
            sys.path.append(os.getcwd())
            self.config = {**DEFUALT_CONFIG, **standard_config.load("markata")}
            if isinstance(self.config["glob_patterns"], str):
                self.config["glob_patterns"] = self.config["glob_patterns"].split(",")
            elif isinstance(self.config["glob_patterns"], list):
                self.config["glob_patterns"] = list(self.config["glob_patterns"])
            else:
                raise TypeError("glob_patterns must be list or str")
            self.glob_patterns = self.config["glob_patterns"]

            if "hooks" not in self.config:
                self.hooks = [""]
            if isinstance(self.config["hooks"], str):
                self.hooks = self.config["hooks"].split(",")
            if isinstance(self.config["hooks"], list):
                self.hooks = self.config["hooks"]

            if "disabled_hooks" not in self.config:
                self.disabled_hooks = [""]
            if isinstance(self.config["disabled_hooks"], str):
                self.disabled_hooks = self.config["disabled_hooks"].split(",")
            if isinstance(self.config["disabled_hooks"], list):
                self.disabled_hooks = self.config["disabled_hooks"]

            try:
                default_index = self.hooks.index("default")
                hooks = [
                    *self.hooks[:default_index],
                    *DEFAULT_HOOKS,
                    *self.hooks[default_index + 1 :],
                ]
                self.hooks = [hook for hook in hooks if hook not in self.disabled_hooks]
            except ValueError:
                # 'default' is not in hooks , do not replace with default_hooks
                pass

            self._pm = pluggy.PluginManager("markata")
            self._pm.add_hookspecs(hookspec.MarkataSpecs)
            self._register_hooks()

            self._pm.hook.configure(markata=self)
            return self
    ```


---

## get_plugin_config `method`

None

??? "get_plugin_config source"
    ``` python
    def get_plugin_config(self, path_or_name: str) -> Dict:

            key = Path(path_or_name).stem

            try:
                config = self.config[key]
            except KeyError:
                config = {}
            if not isinstance(config, dict):
                raise TypeError("must use dict")
            if "cache_expire" not in config.keys():
                config["cache_expire"] = self.config["default_cache_expire"]
            if "config_key" not in config.keys():
                config["config_key"] = key
            return config
    ```


---

## get_config `method`

None

??? "get_config source"
    ``` python
    def get_config(
            self, key: str, warn: bool = True, suggested: Optional[str] = None
        ) -> Any:
            if key in self.config.keys():
                return self.config[key]
            else:

                if suggested is None:
                    suggested = textwrap.dedent(
                        f"""
                            \[markata]
                            {key} = value
                        """  # noqa: W605
                    )
                if warn:
                    self.console.log(
                        textwrap.dedent(
                            f"""
                            Warning site_name is not set in markata config, sitemap will
                            be missing root site_name
                            to resolve this open your markata.toml and add

                            {suggested}

                            """
                        ),
                        style="yellow",
                    )
    ```


---

## make_hash `method`

None

??? "make_hash source"
    ``` python
    def make_hash(self, *keys: str) -> str:
            str_keys = [str(key) for key in keys]
            return hashlib.md5("".join(str_keys).encode("utf-8")).hexdigest()
    ```


---

## phase `method`

None

??? "phase source"
    ``` python
    def phase(self) -> str:
            return self._phase
    ```


---

## phase `method`

None

??? "phase source"
    ``` python
    def phase(self, value: str) -> None:
            self._phase = value
    ```


---

## content_dir_hash `method`

None

??? "content_dir_hash source"
    ``` python
    def content_dir_hash(self) -> str:
            hashes = [dirhash(dir) for dir in self.content_directories]
            return self.make_hash(*hashes)
    ```


---

## console `method`

None

??? "console source"
    ``` python
    def console(self) -> Console:
            try:
                return self._console
            except AttributeError:
                self._console = Console()
                return self._console
    ```


---

## describe `method`

None

??? "describe source"
    ``` python
    def describe(self) -> dict[str, str]:
            return {"version": __version__, "phase": self.phase}
    ```


---

## _to_dict `method`

None

??? "_to_dict source"
    ``` python
    def _to_dict(self) -> dict[str, Iterable]:
            return {"config": self.config, "articles": [a.to_dict() for a in self.articles]}
    ```


---

## to_dict `method`

None

??? "to_dict source"
    ``` python
    def to_dict(self) -> dict:
            try:
                return self._to_dict()
            except AttributeError:
                self.render()
                return self._to_dict()
    ```


---

## to_json `method`

None

??? "to_json source"
    ``` python
    def to_json(self) -> str:
            import json

            return json.dumps(self.to_dict(), indent=4, sort_keys=True, default=str)
    ```


---

## _register_hooks `method`

None

??? "_register_hooks source"
    ``` python
    def _register_hooks(self) -> None:
            for hook in self.hooks:
                try:
                    # module style plugins
                    plugin = importlib.import_module(hook)
                except ModuleNotFoundError as e:
                    # class style plugins
                    if "." in hook:
                        mod = importlib.import_module(".".join(hook.split(".")[:-1]))
                        plugin = getattr(mod, hook.split(".")[-1])
                    else:
                        raise e

                self._pm.register(plugin)
    ```


---

## __iter__ `method`

None

??? "__iter__ source"
    ``` python
    def __iter__(self, description: str = "working...") -> Iterable[frontmatter.Post]:
            articles: Iterable[frontmatter.Post] = track(
                self.articles, description=description, transient=True, console=self.console
            )
            return articles
    ```


---

## iter_articles `method`

None

??? "iter_articles source"
    ``` python
    def iter_articles(self, description: str) -> Iterable[frontmatter.Post]:
            articles: Iterable[frontmatter.Post] = track(
                self.articles, description=description, transient=True, console=self.console
            )
            return articles
    ```


---

## glob `method`

run glob hooks

Glob hooks should append file lists to the markata object for later
hooks to build from.  The default loader will utilize the `files`
attribute for loading.

??? "glob source"
    ``` python
    def glob(self) -> Markata:
            """run glob hooks

            Glob hooks should append file lists to the markata object for later
            hooks to build from.  The default loader will utilize the `files`
            attribute for loading.
            """

            try:
                self._pm.hook.glob(markata=self)
            except AttributeError:
                self.configure()
                self._pm.hook.glob(markata=self)

            return self
    ```


---

## load `method`

None

??? "load source"
    ``` python
    def load(self) -> Markata:
            try:
                self._pm.hook.load(markata=self)
            except AttributeError:
                self.glob()
                self._pm.hook.load(markata=self)
            return self
    ```


---

## pre_render `method`

None

??? "pre_render source"
    ``` python
    def pre_render(self) -> Markata:
            self._pm.hook.pre_render(markata=self)
            return self
    ```


---

## render `method`

None

??? "render source"
    ``` python
    def render(self) -> Markata:
            try:
                self._pm.hook.pre_render(markata=self)
                self._pm.hook.render(markata=self)
                self._pm.hook.post_render(markata=self)
            except AttributeError:
                self.load()
                self._pm.hook.pre_render(markata=self)
                self._pm.hook.render(markata=self)
                self._pm.hook.post_render(markata=self)
            return self
    ```


---

## post_render `method`

None

??? "post_render source"
    ``` python
    def post_render(self) -> Markata:
            self._pm.hook.post_render(markata=self)
            return self
    ```


---

## save `method`

None

??? "save source"
    ``` python
    def save(self) -> Markata:
            try:
                self._pm.hook.save(markata=self)
            except AttributeError:
                self.render()
                self._pm.hook.save(markata=self)
            return self
    ```


---

## run `method`

None

??? "run source"
    ``` python
    def run(self, lifecycle: LifeCycle = None) -> Markata:
            if lifecycle is None:
                lifecycle = getattr(LifeCycle, max(LifeCycle._member_map_))

            if isinstance(lifecycle, str):
                lifecycle = LifeCycle[lifecycle]

            stages_to_run = [m for m in LifeCycle._member_map_ if LifeCycle[m] <= lifecycle]

            self.console.log(f"running {stages_to_run}")
            for stage in stages_to_run:
                self.console.log(f"{stage} running")
                getattr(self, stage)()
                self.console.log(f"{stage} complete")

            with self.cache as cache:
                hits, misses = cache.stats()

            if hits + misses > 0:
                self.console.log(f"cache hit rate {round(hits/ (hits + misses)*100, 2)}%")
            self.console.log(f"cache hits/misses {hits}/{misses}")

            return self
    ```


---

## filter `method`

None

??? "filter source"
    ``` python
    def filter(self, filter: str) -> List:
            def evalr(a: Post) -> Any:
                try:
                    return eval(filter, {**a.to_dict(), "timedelta": timedelta}, {})
                except AttributeError:
                    return eval(filter, {**a, "timedelta": timedelta}, {})

            return [a for a in self.articles if evalr(a)]
    ```


---

## map `method`

None

??? "map source"
    ``` python
    def map(
            self, func: str = "title", filter: str = "True", sort: str = "True"
        ) -> List:
            import copy

            def try_sort(a: Any) -> int:

                try:
                    value = eval(sort, a.to_dict(), {})
                except NameError:
                    return -1
                try:
                    return int(value)
                except TypeError:
                    try:
                        return int(value.timestamp())
                    except Exception:
                        try:
                            return int(
                                datetime.datetime.combine(
                                    value, datetime.datetime.min.time()
                                ).timestamp()
                            )
                        except Exception:
                            try:
                                return sum([ord(c) for c in str(value)])
                            except Exception:
                                return -1

            articles = copy.copy(self.articles)
            articles.sort(key=try_sort)
            return [
                eval(func, {**a.to_dict(), "timedelta": timedelta}, {})
                for a in articles
                if eval(filter, {**a.to_dict(), "timedelta": timedelta}, {})
            ]
    ```


---

## evalr `function`

None

??? "evalr source"
    ``` python
    def evalr(a: Post) -> Any:
                try:
                    return eval(filter, {**a.to_dict(), "timedelta": timedelta}, {})
                except AttributeError:
                    return eval(filter, {**a, "timedelta": timedelta}, {})
    ```


---

## try_sort `function`

None

??? "try_sort source"
    ``` python
    def try_sort(a: Any) -> int:

                try:
                    value = eval(sort, a.to_dict(), {})
                except NameError:
                    return -1
                try:
                    return int(value)
                except TypeError:
                    try:
                        return int(value.timestamp())
                    except Exception:
                        try:
                            return int(
                                datetime.datetime.combine(
                                    value, datetime.datetime.min.time()
                                ).timestamp()
                            )
                        except Exception:
                            try:
                                return sum([ord(c) for c in str(value)])
                            except Exception:
                                return -1
    ```