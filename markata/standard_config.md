---
article_html: "<p>Standard Config.\nA module to load tooling config from a users project
  space.</p>\n<p>Inspired from frustrations that some tools have a tool.ini, .tool.ini,\nsetup.cfg,
  or pyproject.toml.  Some allow for global configs, some don't.  Some\nproperly follow
  the users home directory, others end up in a weird temp\ndirectory.  Windows home
  directory is only more confusing.  Some will even\nrespect the users <code>$XDG_HOME</code>
  directory.</p>\n<p>This file is for any project that can be configured in plain
  text such as <code>ini</code>\nor <code>toml</code> and not requiring a .py file.
  \ Just name your tool and let users put\nconfig where it makes sense to them, no
  need to figure out resolution order.</p>\n<h2 id=\"usage\">Usage:</h2>\n<div class=\"highlight\"><pre><span></span><code><span
  class=\"kn\">from</span> <span class=\"nn\">standard_config</span> <span class=\"kn\">import</span>
  <span class=\"n\">load</span>\n\n<span class=\"c1\"># Retrieve any overrides from
  the user</span>\n<span class=\"n\">overrides</span> <span class=\"o\">=</span> <span
  class=\"p\">{</span><span class=\"s1\">&#39;setting&#39;</span><span class=\"p\">:</span>
  <span class=\"kc\">True</span><span class=\"p\">}</span>\n<span class=\"n\">config</span>
  <span class=\"o\">=</span> <span class=\"n\">load</span><span class=\"p\">(</span><span
  class=\"s1\">&#39;my_tool&#39;</span><span class=\"p\">,</span> <span class=\"n\">overrides</span><span
  class=\"p\">)</span>\n</code></pre></div>\n<h2 id=\"resolution-order\">Resolution
  Order</h2>\n<ul>\n<li>First global file with a tool key</li>\n<li>First local file
  with a tool key</li>\n<li>Environment variables prefixed with <code>TOOL</code></li>\n<li>Overrides</li>\n</ul>\n<h3
  id=\"tool-specific-ini-files\">Tool Specific Ini files</h3>\n<p>Ini file formats
  must include a <code>&lt;tool&gt;</code> key.</p>\n<div class=\"highlight\"><pre><span></span><code><span
  class=\"k\">[my_tool]</span><span class=\"w\"></span>\n<span class=\"na\">setting</span><span
  class=\"w\"> </span><span class=\"o\">=</span><span class=\"w\"> </span><span class=\"s\">True</span><span
  class=\"w\"></span>\n</code></pre></div>\n<h3 id=\"pyprojecttoml\">pyproject.toml</h3>\n<p>Toml
  files must include a <code>tool.&lt;tool&gt;</code> key</p>\n<div class=\"highlight\"><pre><span></span><code><span
  class=\"k\">[tool.my_tool]</span><span class=\"w\"></span>\n<span class=\"n\">setting</span><span
  class=\"w\"> </span><span class=\"o\">=</span><span class=\"w\"> </span><span class=\"n\">True</span><span
  class=\"w\"></span>\n</code></pre></div>\n<h3 id=\"setupcfg\">setup.cfg</h3>\n<p>setup.cfg
  files must include a <code>tool:&lt;tool&gt;</code> key</p>\n<div class=\"highlight\"><pre><span></span><code><span
  class=\"k\">[tool:my_tool]</span><span class=\"w\"></span>\n<span class=\"na\">setting</span><span
  class=\"w\"> </span><span class=\"o\">=</span><span class=\"w\"> </span><span class=\"s\">True</span><span
  class=\"w\"></span>\n</code></pre></div>\n<h3 id=\"global-files-to-consider\">global
  files to consider</h3>\n<ul>\n<li><home>/tool.ini</li>\n<li><home>/.tool</li>\n<li><home>/.tool.ini</li>\n<li><home>/.config/tool.ini</li>\n<li><home>/.config/.tool</li>\n<li><home>/.config/.tool.ini</li>\n</ul>\n<h3
  id=\"local-files-to-consider\">local files to consider</h3>\n<ul>\n<li><project_home>/tool.ini</li>\n<li><project_home>/.tool</li>\n<li><project_home>/.tool.ini</li>\n<li><project_home>/pyproject.toml</li>\n<li><project_home>/setup.cfg</li>\n</ul>\n<hr
  />\n<h2 id=\"_get_global_path_specs-function\">_get_global_path_specs <code>function</code></h2>\n<p>Generate
  a list of standard pathspecs for global config files.</p>\n<p>Args:\n    tool (str):
  name of the tool to configure</p>\n<details>\n<summary>_get_global_path_specs source</summary>\n<div
  class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span> <span class=\"nf\">_get_global_path_specs</span><span
  class=\"p\">(</span><span class=\"n\">tool</span><span class=\"p\">:</span> <span
  class=\"nb\">str</span><span class=\"p\">)</span> <span class=\"o\">-&gt;</span>
  <span class=\"n\">path_spec_type</span><span class=\"p\">:</span>\n    <span class=\"sd\">&quot;&quot;&quot;</span>\n<span
  class=\"sd\">    Generate a list of standard pathspecs for global config files.</span>\n\n<span
  class=\"sd\">    Args:</span>\n<span class=\"sd\">        tool (str): name of the
  tool to configure</span>\n<span class=\"sd\">    &quot;&quot;&quot;</span>\n    <span
  class=\"k\">try</span><span class=\"p\">:</span>\n        <span class=\"n\">home</span>
  <span class=\"o\">=</span> <span class=\"n\">Path</span><span class=\"p\">(</span><span
  class=\"n\">os</span><span class=\"o\">.</span><span class=\"n\">environ</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;XDG_HOME&quot;</span><span class=\"p\">])</span>\n
  \   <span class=\"k\">except</span> <span class=\"ne\">KeyError</span><span class=\"p\">:</span>\n
  \       <span class=\"n\">home</span> <span class=\"o\">=</span> <span class=\"n\">Path</span><span
  class=\"o\">.</span><span class=\"n\">home</span><span class=\"p\">()</span>\n\n
  \   <span class=\"k\">return</span> <span class=\"p\">[</span>\n        <span class=\"p\">{</span><span
  class=\"s2\">&quot;path_specs&quot;</span><span class=\"p\">:</span> <span class=\"n\">home</span>
  <span class=\"o\">/</span> <span class=\"sa\">f</span><span class=\"s2\">&quot;</span><span
  class=\"si\">{</span><span class=\"n\">tool</span><span class=\"si\">}</span><span
  class=\"s2\">.ini&quot;</span><span class=\"p\">,</span> <span class=\"s2\">&quot;ac_parser&quot;</span><span
  class=\"p\">:</span> <span class=\"s2\">&quot;ini&quot;</span><span class=\"p\">,</span>
  <span class=\"s2\">&quot;keys&quot;</span><span class=\"p\">:</span> <span class=\"p\">[</span><span
  class=\"n\">tool</span><span class=\"p\">]},</span>\n        <span class=\"p\">{</span><span
  class=\"s2\">&quot;path_specs&quot;</span><span class=\"p\">:</span> <span class=\"n\">home</span>
  <span class=\"o\">/</span> <span class=\"sa\">f</span><span class=\"s2\">&quot;.</span><span
  class=\"si\">{</span><span class=\"n\">tool</span><span class=\"si\">}</span><span
  class=\"s2\">&quot;</span><span class=\"p\">,</span> <span class=\"s2\">&quot;ac_parser&quot;</span><span
  class=\"p\">:</span> <span class=\"s2\">&quot;ini&quot;</span><span class=\"p\">,</span>
  <span class=\"s2\">&quot;keys&quot;</span><span class=\"p\">:</span> <span class=\"p\">[</span><span
  class=\"n\">tool</span><span class=\"p\">]},</span>\n        <span class=\"p\">{</span><span
  class=\"s2\">&quot;path_specs&quot;</span><span class=\"p\">:</span> <span class=\"n\">home</span>
  <span class=\"o\">/</span> <span class=\"sa\">f</span><span class=\"s2\">&quot;.</span><span
  class=\"si\">{</span><span class=\"n\">tool</span><span class=\"si\">}</span><span
  class=\"s2\">.ini&quot;</span><span class=\"p\">,</span> <span class=\"s2\">&quot;ac_parser&quot;</span><span
  class=\"p\">:</span> <span class=\"s2\">&quot;ini&quot;</span><span class=\"p\">,</span>
  <span class=\"s2\">&quot;keys&quot;</span><span class=\"p\">:</span> <span class=\"p\">[</span><span
  class=\"n\">tool</span><span class=\"p\">]},</span>\n        <span class=\"p\">{</span>\n
  \           <span class=\"s2\">&quot;path_specs&quot;</span><span class=\"p\">:</span>
  <span class=\"n\">home</span> <span class=\"o\">/</span> <span class=\"s2\">&quot;.config&quot;</span>
  <span class=\"o\">/</span> <span class=\"sa\">f</span><span class=\"s2\">&quot;</span><span
  class=\"si\">{</span><span class=\"n\">tool</span><span class=\"si\">}</span><span
  class=\"s2\">.ini&quot;</span><span class=\"p\">,</span>\n            <span class=\"s2\">&quot;ac_parser&quot;</span><span
  class=\"p\">:</span> <span class=\"s2\">&quot;ini&quot;</span><span class=\"p\">,</span>\n
  \           <span class=\"s2\">&quot;keys&quot;</span><span class=\"p\">:</span>
  <span class=\"p\">[</span><span class=\"n\">tool</span><span class=\"p\">],</span>\n
  \       <span class=\"p\">},</span>\n        <span class=\"p\">{</span>\n            <span
  class=\"s2\">&quot;path_specs&quot;</span><span class=\"p\">:</span> <span class=\"n\">home</span>
  <span class=\"o\">/</span> <span class=\"s2\">&quot;.config&quot;</span> <span class=\"o\">/</span>
  <span class=\"sa\">f</span><span class=\"s2\">&quot;.</span><span class=\"si\">{</span><span
  class=\"n\">tool</span><span class=\"si\">}</span><span class=\"s2\">&quot;</span><span
  class=\"p\">,</span>\n            <span class=\"s2\">&quot;ac_parser&quot;</span><span
  class=\"p\">:</span> <span class=\"s2\">&quot;ini&quot;</span><span class=\"p\">,</span>\n
  \           <span class=\"s2\">&quot;keys&quot;</span><span class=\"p\">:</span>
  <span class=\"p\">[</span><span class=\"n\">tool</span><span class=\"p\">],</span>\n
  \       <span class=\"p\">},</span>\n        <span class=\"p\">{</span>\n            <span
  class=\"s2\">&quot;path_specs&quot;</span><span class=\"p\">:</span> <span class=\"n\">home</span>
  <span class=\"o\">/</span> <span class=\"s2\">&quot;.config&quot;</span> <span class=\"o\">/</span>
  <span class=\"sa\">f</span><span class=\"s2\">&quot;.</span><span class=\"si\">{</span><span
  class=\"n\">tool</span><span class=\"si\">}</span><span class=\"s2\">.ini&quot;</span><span
  class=\"p\">,</span>\n            <span class=\"s2\">&quot;ac_parser&quot;</span><span
  class=\"p\">:</span> <span class=\"s2\">&quot;ini&quot;</span><span class=\"p\">,</span>\n
  \           <span class=\"s2\">&quot;keys&quot;</span><span class=\"p\">:</span>
  <span class=\"p\">[</span><span class=\"n\">tool</span><span class=\"p\">],</span>\n
  \       <span class=\"p\">},</span>\n    <span class=\"p\">]</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"_get_local_path_specs-function\">_get_local_path_specs <code>function</code></h2>\n<p>Generate
  a list of standard pathspecs for local, project directory config files.</p>\n<p>Args:\n
  \   tool (str): name of the tool to configure</p>\n<details>\n<summary>_get_local_path_specs
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">_get_local_path_specs</span><span class=\"p\">(</span><span class=\"n\">tool</span><span
  class=\"p\">:</span> <span class=\"nb\">str</span><span class=\"p\">,</span> <span
  class=\"n\">project_home</span><span class=\"p\">:</span> <span class=\"n\">Union</span><span
  class=\"p\">[</span><span class=\"nb\">str</span><span class=\"p\">,</span> <span
  class=\"n\">Path</span><span class=\"p\">])</span> <span class=\"o\">-&gt;</span>
  <span class=\"n\">path_spec_type</span><span class=\"p\">:</span>\n    <span class=\"sd\">&quot;&quot;&quot;</span>\n<span
  class=\"sd\">    Generate a list of standard pathspecs for local, project directory
  config files.</span>\n\n<span class=\"sd\">    Args:</span>\n<span class=\"sd\">
  \       tool (str): name of the tool to configure</span>\n<span class=\"sd\">    &quot;&quot;&quot;</span>\n
  \   <span class=\"k\">return</span> <span class=\"p\">[</span>\n        <span class=\"p\">{</span>\n
  \           <span class=\"s2\">&quot;path_specs&quot;</span><span class=\"p\">:</span>
  <span class=\"n\">Path</span><span class=\"p\">(</span><span class=\"n\">project_home</span><span
  class=\"p\">)</span> <span class=\"o\">/</span> <span class=\"sa\">f</span><span
  class=\"s2\">&quot;</span><span class=\"si\">{</span><span class=\"n\">tool</span><span
  class=\"si\">}</span><span class=\"s2\">.ini&quot;</span><span class=\"p\">,</span>\n
  \           <span class=\"s2\">&quot;ac_parser&quot;</span><span class=\"p\">:</span>
  <span class=\"s2\">&quot;ini&quot;</span><span class=\"p\">,</span>\n            <span
  class=\"s2\">&quot;keys&quot;</span><span class=\"p\">:</span> <span class=\"p\">[</span><span
  class=\"n\">tool</span><span class=\"p\">],</span>\n        <span class=\"p\">},</span>\n
  \       <span class=\"p\">{</span>\n            <span class=\"s2\">&quot;path_specs&quot;</span><span
  class=\"p\">:</span> <span class=\"n\">Path</span><span class=\"p\">(</span><span
  class=\"n\">project_home</span><span class=\"p\">)</span> <span class=\"o\">/</span>
  <span class=\"sa\">f</span><span class=\"s2\">&quot;.</span><span class=\"si\">{</span><span
  class=\"n\">tool</span><span class=\"si\">}</span><span class=\"s2\">&quot;</span><span
  class=\"p\">,</span>\n            <span class=\"s2\">&quot;ac_parser&quot;</span><span
  class=\"p\">:</span> <span class=\"s2\">&quot;ini&quot;</span><span class=\"p\">,</span>\n
  \           <span class=\"s2\">&quot;keys&quot;</span><span class=\"p\">:</span>
  <span class=\"p\">[</span><span class=\"n\">tool</span><span class=\"p\">],</span>\n
  \       <span class=\"p\">},</span>\n        <span class=\"p\">{</span>\n            <span
  class=\"s2\">&quot;path_specs&quot;</span><span class=\"p\">:</span> <span class=\"n\">Path</span><span
  class=\"p\">(</span><span class=\"n\">project_home</span><span class=\"p\">)</span>
  <span class=\"o\">/</span> <span class=\"sa\">f</span><span class=\"s2\">&quot;.</span><span
  class=\"si\">{</span><span class=\"n\">tool</span><span class=\"si\">}</span><span
  class=\"s2\">.ini&quot;</span><span class=\"p\">,</span>\n            <span class=\"s2\">&quot;ac_parser&quot;</span><span
  class=\"p\">:</span> <span class=\"s2\">&quot;ini&quot;</span><span class=\"p\">,</span>\n
  \           <span class=\"s2\">&quot;keys&quot;</span><span class=\"p\">:</span>
  <span class=\"p\">[</span><span class=\"n\">tool</span><span class=\"p\">],</span>\n
  \       <span class=\"p\">},</span>\n        <span class=\"p\">{</span>\n            <span
  class=\"s2\">&quot;path_specs&quot;</span><span class=\"p\">:</span> <span class=\"n\">Path</span><span
  class=\"p\">(</span><span class=\"n\">project_home</span><span class=\"p\">)</span>
  <span class=\"o\">/</span> <span class=\"sa\">f</span><span class=\"s2\">&quot;</span><span
  class=\"si\">{</span><span class=\"n\">tool</span><span class=\"si\">}</span><span
  class=\"s2\">.yml&quot;</span><span class=\"p\">,</span>\n            <span class=\"s2\">&quot;ac_parser&quot;</span><span
  class=\"p\">:</span> <span class=\"s2\">&quot;yaml&quot;</span><span class=\"p\">,</span>\n
  \           <span class=\"s2\">&quot;keys&quot;</span><span class=\"p\">:</span>
  <span class=\"p\">[</span><span class=\"n\">tool</span><span class=\"p\">],</span>\n
  \       <span class=\"p\">},</span>\n        <span class=\"p\">{</span>\n            <span
  class=\"s2\">&quot;path_specs&quot;</span><span class=\"p\">:</span> <span class=\"n\">Path</span><span
  class=\"p\">(</span><span class=\"n\">project_home</span><span class=\"p\">)</span>
  <span class=\"o\">/</span> <span class=\"sa\">f</span><span class=\"s2\">&quot;.</span><span
  class=\"si\">{</span><span class=\"n\">tool</span><span class=\"si\">}</span><span
  class=\"s2\">.yml&quot;</span><span class=\"p\">,</span>\n            <span class=\"s2\">&quot;ac_parser&quot;</span><span
  class=\"p\">:</span> <span class=\"s2\">&quot;yaml&quot;</span><span class=\"p\">,</span>\n
  \           <span class=\"s2\">&quot;keys&quot;</span><span class=\"p\">:</span>
  <span class=\"p\">[</span><span class=\"n\">tool</span><span class=\"p\">],</span>\n
  \       <span class=\"p\">},</span>\n        <span class=\"p\">{</span>\n            <span
  class=\"s2\">&quot;path_specs&quot;</span><span class=\"p\">:</span> <span class=\"n\">Path</span><span
  class=\"p\">(</span><span class=\"n\">project_home</span><span class=\"p\">)</span>
  <span class=\"o\">/</span> <span class=\"sa\">f</span><span class=\"s2\">&quot;</span><span
  class=\"si\">{</span><span class=\"n\">tool</span><span class=\"si\">}</span><span
  class=\"s2\">.toml&quot;</span><span class=\"p\">,</span>\n            <span class=\"s2\">&quot;ac_parser&quot;</span><span
  class=\"p\">:</span> <span class=\"s2\">&quot;toml&quot;</span><span class=\"p\">,</span>\n
  \           <span class=\"s2\">&quot;keys&quot;</span><span class=\"p\">:</span>
  <span class=\"p\">[</span><span class=\"n\">tool</span><span class=\"p\">],</span>\n
  \       <span class=\"p\">},</span>\n        <span class=\"p\">{</span>\n            <span
  class=\"s2\">&quot;path_specs&quot;</span><span class=\"p\">:</span> <span class=\"n\">Path</span><span
  class=\"p\">(</span><span class=\"n\">project_home</span><span class=\"p\">)</span>
  <span class=\"o\">/</span> <span class=\"sa\">f</span><span class=\"s2\">&quot;.</span><span
  class=\"si\">{</span><span class=\"n\">tool</span><span class=\"si\">}</span><span
  class=\"s2\">.toml&quot;</span><span class=\"p\">,</span>\n            <span class=\"s2\">&quot;ac_parser&quot;</span><span
  class=\"p\">:</span> <span class=\"s2\">&quot;toml&quot;</span><span class=\"p\">,</span>\n
  \           <span class=\"s2\">&quot;keys&quot;</span><span class=\"p\">:</span>
  <span class=\"p\">[</span><span class=\"n\">tool</span><span class=\"p\">],</span>\n
  \       <span class=\"p\">},</span>\n        <span class=\"p\">{</span>\n            <span
  class=\"s2\">&quot;path_specs&quot;</span><span class=\"p\">:</span> <span class=\"n\">Path</span><span
  class=\"p\">(</span><span class=\"n\">project_home</span><span class=\"p\">)</span>
  <span class=\"o\">/</span> <span class=\"sa\">f</span><span class=\"s2\">&quot;pyproject.toml&quot;</span><span
  class=\"p\">,</span>\n            <span class=\"s2\">&quot;ac_parser&quot;</span><span
  class=\"p\">:</span> <span class=\"s2\">&quot;toml&quot;</span><span class=\"p\">,</span>\n
  \           <span class=\"s2\">&quot;keys&quot;</span><span class=\"p\">:</span>
  <span class=\"p\">[</span><span class=\"s2\">&quot;tool&quot;</span><span class=\"p\">,</span>
  <span class=\"n\">tool</span><span class=\"p\">],</span>\n        <span class=\"p\">},</span>\n
  \       <span class=\"p\">{</span>\n            <span class=\"s2\">&quot;path_specs&quot;</span><span
  class=\"p\">:</span> <span class=\"n\">Path</span><span class=\"p\">(</span><span
  class=\"n\">project_home</span><span class=\"p\">)</span> <span class=\"o\">/</span>
  <span class=\"sa\">f</span><span class=\"s2\">&quot;setup.cfg&quot;</span><span
  class=\"p\">,</span>\n            <span class=\"s2\">&quot;ac_parser&quot;</span><span
  class=\"p\">:</span> <span class=\"s2\">&quot;ini&quot;</span><span class=\"p\">,</span>\n
  \           <span class=\"s2\">&quot;keys&quot;</span><span class=\"p\">:</span>
  <span class=\"p\">[</span><span class=\"sa\">f</span><span class=\"s2\">&quot;tool.</span><span
  class=\"si\">{</span><span class=\"n\">tool</span><span class=\"si\">}</span><span
  class=\"s2\">&quot;</span><span class=\"p\">],</span>\n        <span class=\"p\">},</span>\n
  \   <span class=\"p\">]</span>\n</code></pre></div>\n</details>\n<hr />\n<h2 id=\"_get_attrs-function\">_get_attrs
  <code>function</code></h2>\n<p>Get nested config data from a list of keys.</p>\n<p>specifically
  written for pyproject.toml which needs to get <code>tool</code> then <code>&lt;tool&gt;</code></p>\n<details>\n<summary>_get_attrs
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">_get_attrs</span><span class=\"p\">(</span><span class=\"n\">attrs</span><span
  class=\"p\">:</span> <span class=\"nb\">list</span><span class=\"p\">,</span> <span
  class=\"n\">config</span><span class=\"p\">:</span> <span class=\"n\">Dict</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"n\">Dict</span><span
  class=\"p\">:</span>\n    <span class=\"sd\">&quot;&quot;&quot;Get nested config
  data from a list of keys.</span>\n\n<span class=\"sd\">    specifically written
  for pyproject.toml which needs to get `tool` then `&lt;tool&gt;`</span>\n<span class=\"sd\">
  \   &quot;&quot;&quot;</span>\n    <span class=\"k\">for</span> <span class=\"n\">attr</span>
  <span class=\"ow\">in</span> <span class=\"n\">attrs</span><span class=\"p\">:</span>\n
  \       <span class=\"n\">config</span> <span class=\"o\">=</span> <span class=\"n\">config</span><span
  class=\"p\">[</span><span class=\"n\">attr</span><span class=\"p\">]</span>\n    <span
  class=\"k\">return</span> <span class=\"n\">config</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"_load_files-function\">_load_files <code>function</code></h2>\n<p>Use
  anyconfig to load config files stopping at the first one that exists.</p>\n<p>config_path_specs
  (list): a list of pathspecs and keys to load</p>\n<details>\n<summary>_load_files
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">_load_files</span><span class=\"p\">(</span><span class=\"n\">config_path_specs</span><span
  class=\"p\">:</span> <span class=\"n\">path_spec_type</span><span class=\"p\">)</span>
  <span class=\"o\">-&gt;</span> <span class=\"n\">Dict</span><span class=\"p\">:</span>\n
  \   <span class=\"sd\">&quot;&quot;&quot;Use anyconfig to load config files stopping
  at the first one that exists.</span>\n\n<span class=\"sd\">    config_path_specs
  (list): a list of pathspecs and keys to load</span>\n<span class=\"sd\">    &quot;&quot;&quot;</span>\n
  \   <span class=\"k\">for</span> <span class=\"n\">file</span> <span class=\"ow\">in</span>
  <span class=\"n\">config_path_specs</span><span class=\"p\">:</span>\n\n        <span
  class=\"k\">if</span> <span class=\"n\">file</span><span class=\"p\">[</span><span
  class=\"s2\">&quot;path_specs&quot;</span><span class=\"p\">]</span><span class=\"o\">.</span><span
  class=\"n\">exists</span><span class=\"p\">():</span>\n            <span class=\"n\">config</span>
  <span class=\"o\">=</span> <span class=\"n\">anyconfig</span><span class=\"o\">.</span><span
  class=\"n\">load</span><span class=\"p\">(</span><span class=\"o\">**</span><span
  class=\"n\">file</span><span class=\"p\">)</span>\n        <span class=\"k\">else</span><span
  class=\"p\">:</span>\n            <span class=\"c1\"># ignore missing files</span>\n
  \           <span class=\"k\">continue</span>\n\n        <span class=\"k\">try</span><span
  class=\"p\">:</span>\n            <span class=\"k\">return</span> <span class=\"n\">_get_attrs</span><span
  class=\"p\">(</span><span class=\"n\">file</span><span class=\"p\">[</span><span
  class=\"s2\">&quot;keys&quot;</span><span class=\"p\">],</span> <span class=\"n\">config</span><span
  class=\"p\">)</span>\n        <span class=\"k\">except</span> <span class=\"ne\">KeyError</span><span
  class=\"p\">:</span>\n            <span class=\"c1\"># ignore incorrect keys</span>\n
  \           <span class=\"k\">continue</span>\n\n    <span class=\"k\">return</span>
  <span class=\"p\">{}</span>\n</code></pre></div>\n</details>\n<hr />\n<h2 id=\"_load_env-function\">_load_env
  <code>function</code></h2>\n<p>Load config from environment variables.</p>\n<p>Args:\n
  \   tool (str): name of the tool to configure</p>\n<details>\n<summary>_load_env
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">_load_env</span><span class=\"p\">(</span><span class=\"n\">tool</span><span
  class=\"p\">:</span> <span class=\"nb\">str</span><span class=\"p\">)</span> <span
  class=\"o\">-&gt;</span> <span class=\"n\">Dict</span><span class=\"p\">:</span>\n
  \   <span class=\"sd\">&quot;&quot;&quot;Load config from environment variables.</span>\n\n<span
  class=\"sd\">    Args:</span>\n<span class=\"sd\">        tool (str): name of the
  tool to configure</span>\n<span class=\"sd\">    &quot;&quot;&quot;</span>\n    <span
  class=\"nb\">vars</span> <span class=\"o\">=</span> <span class=\"p\">[</span><span
  class=\"n\">var</span> <span class=\"k\">for</span> <span class=\"n\">var</span>
  <span class=\"ow\">in</span> <span class=\"n\">os</span><span class=\"o\">.</span><span
  class=\"n\">environ</span><span class=\"o\">.</span><span class=\"n\">keys</span><span
  class=\"p\">()</span> <span class=\"k\">if</span> <span class=\"n\">var</span><span
  class=\"o\">.</span><span class=\"n\">startswith</span><span class=\"p\">(</span><span
  class=\"n\">tool</span><span class=\"o\">.</span><span class=\"n\">upper</span><span
  class=\"p\">())]</span>\n    <span class=\"k\">return</span> <span class=\"p\">{</span>\n
  \       <span class=\"n\">var</span><span class=\"o\">.</span><span class=\"n\">lower</span><span
  class=\"p\">()</span><span class=\"o\">.</span><span class=\"n\">strip</span><span
  class=\"p\">(</span><span class=\"n\">tool</span><span class=\"o\">.</span><span
  class=\"n\">lower</span><span class=\"p\">())</span><span class=\"o\">.</span><span
  class=\"n\">strip</span><span class=\"p\">(</span><span class=\"s2\">&quot;_&quot;</span><span
  class=\"p\">)</span><span class=\"o\">.</span><span class=\"n\">strip</span><span
  class=\"p\">(</span><span class=\"s2\">&quot;-&quot;</span><span class=\"p\">):</span>
  <span class=\"n\">os</span><span class=\"o\">.</span><span class=\"n\">environ</span><span
  class=\"p\">[</span><span class=\"n\">var</span><span class=\"p\">]</span>\n        <span
  class=\"k\">for</span> <span class=\"n\">var</span> <span class=\"ow\">in</span>
  <span class=\"nb\">vars</span>\n    <span class=\"p\">}</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"load-function\">load <code>function</code></h2>\n<p>Load tool config
  from standard config files.</p>\n<p>Resolution Order</p>\n<ul>\n<li>First global
  file with a tool key</li>\n<li>First local file with a tool key</li>\n<li>Environment
  variables prefixed with <code>TOOL</code></li>\n<li>Overrides</li>\n</ul>\n<p>Args:\n
  \   tool (str): name of the tool to configure</p>\n<details>\n<summary>load source</summary>\n<div
  class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span> <span class=\"nf\">load</span><span
  class=\"p\">(</span><span class=\"n\">tool</span><span class=\"p\">:</span> <span
  class=\"nb\">str</span><span class=\"p\">,</span> <span class=\"n\">project_home</span><span
  class=\"p\">:</span> <span class=\"n\">Union</span><span class=\"p\">[</span><span
  class=\"n\">Path</span><span class=\"p\">,</span> <span class=\"nb\">str</span><span
  class=\"p\">]</span> <span class=\"o\">=</span> <span class=\"s2\">&quot;.&quot;</span><span
  class=\"p\">,</span> <span class=\"n\">overrides</span><span class=\"p\">:</span>
  <span class=\"n\">Dict</span> <span class=\"o\">=</span> <span class=\"p\">{})</span>
  <span class=\"o\">-&gt;</span> <span class=\"n\">Dict</span><span class=\"p\">:</span>\n
  \   <span class=\"sd\">&quot;&quot;&quot;Load tool config from standard config files.</span>\n\n<span
  class=\"sd\">    Resolution Order</span>\n\n<span class=\"sd\">    * First global
  file with a tool key</span>\n<span class=\"sd\">    * First local file with a tool
  key</span>\n<span class=\"sd\">    * Environment variables prefixed with `TOOL`</span>\n<span
  class=\"sd\">    * Overrides</span>\n\n<span class=\"sd\">    Args:</span>\n<span
  class=\"sd\">        tool (str): name of the tool to configure</span>\n<span class=\"sd\">
  \   &quot;&quot;&quot;</span>\n    <span class=\"n\">global_config</span> <span
  class=\"o\">=</span> <span class=\"n\">_load_files</span><span class=\"p\">(</span><span
  class=\"n\">_get_global_path_specs</span><span class=\"p\">(</span><span class=\"n\">tool</span><span
  class=\"p\">))</span>\n    <span class=\"n\">local_config</span> <span class=\"o\">=</span>
  <span class=\"n\">_load_files</span><span class=\"p\">(</span><span class=\"n\">_get_local_path_specs</span><span
  class=\"p\">(</span><span class=\"n\">tool</span><span class=\"p\">,</span> <span
  class=\"n\">project_home</span><span class=\"p\">))</span>\n    <span class=\"n\">env_config</span>
  <span class=\"o\">=</span> <span class=\"n\">_load_env</span><span class=\"p\">(</span><span
  class=\"n\">tool</span><span class=\"p\">)</span>\n    <span class=\"k\">return</span>
  <span class=\"p\">{</span><span class=\"o\">**</span><span class=\"n\">global_config</span><span
  class=\"p\">,</span> <span class=\"o\">**</span><span class=\"n\">local_config</span><span
  class=\"p\">,</span> <span class=\"o\">**</span><span class=\"n\">env_config</span><span
  class=\"p\">,</span> <span class=\"o\">**</span><span class=\"n\">overrides</span><span
  class=\"p\">}</span>\n</code></pre></div>\n</details>"
datetime: null
description: Docs for standard_config
long_description: ''
now: 2022-02-05 19:38:00.891366
path: standard_config.md
slug: markata/standard_config
status: published
title: standard_config.py
today: 2022-02-05
---

Standard Config.
A module to load tooling config from a users project space.

Inspired from frustrations that some tools have a tool.ini, .tool.ini,
setup.cfg, or pyproject.toml.  Some allow for global configs, some don't.  Some
properly follow the users home directory, others end up in a weird temp
directory.  Windows home directory is only more confusing.  Some will even
respect the users `$XDG_HOME` directory.


This file is for any project that can be configured in plain text such as `ini`
or `toml` and not requiring a .py file.  Just name your tool and let users put
config where it makes sense to them, no need to figure out resolution order.

## Usage:

``` python
from standard_config import load

# Retrieve any overrides from the user
overrides = {'setting': True}
config = load('my_tool', overrides)
```

## Resolution Order

* First global file with a tool key
* First local file with a tool key
* Environment variables prefixed with `TOOL`
* Overrides

### Tool Specific Ini files

Ini file formats must include a `<tool>` key.

``` ini
[my_tool]
setting = True
```

### pyproject.toml

Toml files must include a `tool.<tool>` key

``` toml
[tool.my_tool]
setting = True
```

### setup.cfg

setup.cfg files must include a `tool:<tool>` key

``` ini
[tool:my_tool]
setting = True
```


### global files to consider

* <home>/tool.ini
* <home>/.tool
* <home>/.tool.ini
* <home>/.config/tool.ini
* <home>/.config/.tool
* <home>/.config/.tool.ini

### local files to consider

* <project_home>/tool.ini
* <project_home>/.tool
* <project_home>/.tool.ini
* <project_home>/pyproject.toml
* <project_home>/setup.cfg


---

## _get_global_path_specs `function`

Generate a list of standard pathspecs for global config files.

Args:
    tool (str): name of the tool to configure

??? "_get_global_path_specs source"
    ``` python
    def _get_global_path_specs(tool: str) -> path_spec_type:
        """
        Generate a list of standard pathspecs for global config files.

        Args:
            tool (str): name of the tool to configure
        """
        try:
            home = Path(os.environ["XDG_HOME"])
        except KeyError:
            home = Path.home()

        return [
            {"path_specs": home / f"{tool}.ini", "ac_parser": "ini", "keys": [tool]},
            {"path_specs": home / f".{tool}", "ac_parser": "ini", "keys": [tool]},
            {"path_specs": home / f".{tool}.ini", "ac_parser": "ini", "keys": [tool]},
            {
                "path_specs": home / ".config" / f"{tool}.ini",
                "ac_parser": "ini",
                "keys": [tool],
            },
            {
                "path_specs": home / ".config" / f".{tool}",
                "ac_parser": "ini",
                "keys": [tool],
            },
            {
                "path_specs": home / ".config" / f".{tool}.ini",
                "ac_parser": "ini",
                "keys": [tool],
            },
        ]
    ```


---

## _get_local_path_specs `function`

Generate a list of standard pathspecs for local, project directory config files.

Args:
    tool (str): name of the tool to configure

??? "_get_local_path_specs source"
    ``` python
    def _get_local_path_specs(tool: str, project_home: Union[str, Path]) -> path_spec_type:
        """
        Generate a list of standard pathspecs for local, project directory config files.

        Args:
            tool (str): name of the tool to configure
        """
        return [
            {
                "path_specs": Path(project_home) / f"{tool}.ini",
                "ac_parser": "ini",
                "keys": [tool],
            },
            {
                "path_specs": Path(project_home) / f".{tool}",
                "ac_parser": "ini",
                "keys": [tool],
            },
            {
                "path_specs": Path(project_home) / f".{tool}.ini",
                "ac_parser": "ini",
                "keys": [tool],
            },
            {
                "path_specs": Path(project_home) / f"{tool}.yml",
                "ac_parser": "yaml",
                "keys": [tool],
            },
            {
                "path_specs": Path(project_home) / f".{tool}.yml",
                "ac_parser": "yaml",
                "keys": [tool],
            },
            {
                "path_specs": Path(project_home) / f"{tool}.toml",
                "ac_parser": "toml",
                "keys": [tool],
            },
            {
                "path_specs": Path(project_home) / f".{tool}.toml",
                "ac_parser": "toml",
                "keys": [tool],
            },
            {
                "path_specs": Path(project_home) / f"pyproject.toml",
                "ac_parser": "toml",
                "keys": ["tool", tool],
            },
            {
                "path_specs": Path(project_home) / f"setup.cfg",
                "ac_parser": "ini",
                "keys": [f"tool.{tool}"],
            },
        ]
    ```


---

## _get_attrs `function`

Get nested config data from a list of keys.

specifically written for pyproject.toml which needs to get `tool` then `<tool>`

??? "_get_attrs source"
    ``` python
    def _get_attrs(attrs: list, config: Dict) -> Dict:
        """Get nested config data from a list of keys.

        specifically written for pyproject.toml which needs to get `tool` then `<tool>`
        """
        for attr in attrs:
            config = config[attr]
        return config
    ```


---

## _load_files `function`

Use anyconfig to load config files stopping at the first one that exists.

config_path_specs (list): a list of pathspecs and keys to load

??? "_load_files source"
    ``` python
    def _load_files(config_path_specs: path_spec_type) -> Dict:
        """Use anyconfig to load config files stopping at the first one that exists.

        config_path_specs (list): a list of pathspecs and keys to load
        """
        for file in config_path_specs:

            if file["path_specs"].exists():
                config = anyconfig.load(**file)
            else:
                # ignore missing files
                continue

            try:
                return _get_attrs(file["keys"], config)
            except KeyError:
                # ignore incorrect keys
                continue

        return {}
    ```


---

## _load_env `function`

Load config from environment variables.

Args:
    tool (str): name of the tool to configure

??? "_load_env source"
    ``` python
    def _load_env(tool: str) -> Dict:
        """Load config from environment variables.

        Args:
            tool (str): name of the tool to configure
        """
        vars = [var for var in os.environ.keys() if var.startswith(tool.upper())]
        return {
            var.lower().strip(tool.lower()).strip("_").strip("-"): os.environ[var]
            for var in vars
        }
    ```


---

## load `function`

Load tool config from standard config files.

Resolution Order

* First global file with a tool key
* First local file with a tool key
* Environment variables prefixed with `TOOL`
* Overrides

Args:
    tool (str): name of the tool to configure

??? "load source"
    ``` python
    def load(tool: str, project_home: Union[Path, str] = ".", overrides: Dict = {}) -> Dict:
        """Load tool config from standard config files.

        Resolution Order

        * First global file with a tool key
        * First local file with a tool key
        * Environment variables prefixed with `TOOL`
        * Overrides

        Args:
            tool (str): name of the tool to configure
        """
        global_config = _load_files(_get_global_path_specs(tool))
        local_config = _load_files(_get_local_path_specs(tool, project_home))
        env_config = _load_env(tool)
        return {**global_config, **local_config, **env_config, **overrides}
    ```