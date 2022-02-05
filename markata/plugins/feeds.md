---
article_html: "<hr />\n<h2 id=\"markatafiltererror-class\">MarkataFilterError <code>class</code></h2>\n<p>None</p>\n<details>\n<summary>MarkataFilterError
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">class</span>
  <span class=\"nc\">MarkataFilterError</span><span class=\"p\">(</span><span class=\"ne\">RuntimeError</span><span
  class=\"p\">):</span>\n    <span class=\"o\">...</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"save-function\">save <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>save
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">save</span><span class=\"p\">(</span><span class=\"n\">markata</span><span
  class=\"p\">):</span>\n    <span class=\"n\">config</span> <span class=\"o\">=</span>
  <span class=\"n\">markata</span><span class=\"o\">.</span><span class=\"n\">get_plugin_config</span><span
  class=\"p\">(</span><span class=\"s2\">&quot;feeds&quot;</span><span class=\"p\">)</span>\n
  \   <span class=\"k\">if</span> <span class=\"n\">config</span> <span class=\"ow\">is</span>
  <span class=\"kc\">None</span><span class=\"p\">:</span>\n        <span class=\"n\">config</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;feeds&quot;</span><span class=\"p\">]</span>
  <span class=\"o\">=</span> <span class=\"nb\">dict</span><span class=\"p\">()</span>\n
  \   <span class=\"k\">if</span> <span class=\"s2\">&quot;archive&quot;</span> <span
  class=\"ow\">not</span> <span class=\"ow\">in</span> <span class=\"n\">config</span><span
  class=\"o\">.</span><span class=\"n\">keys</span><span class=\"p\">():</span>\n
  \       <span class=\"n\">config</span><span class=\"p\">[</span><span class=\"s2\">&quot;archive&quot;</span><span
  class=\"p\">]</span> <span class=\"o\">=</span> <span class=\"nb\">dict</span><span
  class=\"p\">()</span>\n        <span class=\"n\">config</span><span class=\"p\">[</span><span
  class=\"s2\">&quot;archive&quot;</span><span class=\"p\">][</span><span class=\"s2\">&quot;filter&quot;</span><span
  class=\"p\">]</span> <span class=\"o\">=</span> <span class=\"s2\">&quot;True&quot;</span>\n\n
  \   <span class=\"n\">description</span> <span class=\"o\">=</span> <span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">get_config</span><span class=\"p\">(</span><span
  class=\"s2\">&quot;description&quot;</span><span class=\"p\">)</span> <span class=\"ow\">or</span>
  <span class=\"s2\">&quot;&quot;</span>\n    <span class=\"n\">url</span> <span class=\"o\">=</span>
  <span class=\"n\">markata</span><span class=\"o\">.</span><span class=\"n\">get_config</span><span
  class=\"p\">(</span><span class=\"s2\">&quot;url&quot;</span><span class=\"p\">)</span>
  <span class=\"ow\">or</span> <span class=\"s2\">&quot;&quot;</span>\n\n    <span
  class=\"n\">template</span> <span class=\"o\">=</span> <span class=\"n\">Path</span><span
  class=\"p\">(</span><span class=\"vm\">__file__</span><span class=\"p\">)</span><span
  class=\"o\">.</span><span class=\"n\">parent</span> <span class=\"o\">/</span> <span
  class=\"s2\">&quot;default_post_template.html&quot;</span>\n\n    <span class=\"k\">for</span>
  <span class=\"n\">page</span><span class=\"p\">,</span> <span class=\"n\">page_conf</span>
  <span class=\"ow\">in</span> <span class=\"n\">config</span><span class=\"o\">.</span><span
  class=\"n\">items</span><span class=\"p\">():</span>\n        <span class=\"k\">if</span>
  <span class=\"n\">page</span> <span class=\"ow\">not</span> <span class=\"ow\">in</span>
  <span class=\"p\">[</span><span class=\"s2\">&quot;cache_expire&quot;</span><span
  class=\"p\">,</span> <span class=\"s2\">&quot;config_key&quot;</span><span class=\"p\">]:</span>\n
  \           <span class=\"n\">create_page</span><span class=\"p\">(</span>\n                <span
  class=\"n\">markata</span><span class=\"p\">,</span>\n                <span class=\"n\">page</span><span
  class=\"p\">,</span>\n                <span class=\"n\">description</span><span
  class=\"o\">=</span><span class=\"n\">description</span><span class=\"p\">,</span>\n
  \               <span class=\"n\">url</span><span class=\"o\">=</span><span class=\"n\">url</span><span
  class=\"p\">,</span>\n                <span class=\"n\">template</span><span class=\"o\">=</span><span
  class=\"n\">template</span><span class=\"p\">,</span>\n                <span class=\"o\">**</span><span
  class=\"n\">page_conf</span><span class=\"p\">,</span>\n            <span class=\"p\">)</span>\n\n
  \   <span class=\"n\">home</span> <span class=\"o\">=</span> <span class=\"n\">Path</span><span
  class=\"p\">(</span><span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">config</span><span class=\"p\">[</span><span class=\"s2\">&quot;output_dir&quot;</span><span
  class=\"p\">])</span> <span class=\"o\">/</span> <span class=\"s2\">&quot;index.html&quot;</span>\n
  \   <span class=\"n\">archive</span> <span class=\"o\">=</span> <span class=\"n\">Path</span><span
  class=\"p\">(</span><span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">config</span><span class=\"p\">[</span><span class=\"s2\">&quot;output_dir&quot;</span><span
  class=\"p\">])</span> <span class=\"o\">/</span> <span class=\"s2\">&quot;archive&quot;</span>
  <span class=\"o\">/</span> <span class=\"s2\">&quot;index.html&quot;</span>\n    <span
  class=\"k\">if</span> <span class=\"ow\">not</span> <span class=\"n\">home</span><span
  class=\"o\">.</span><span class=\"n\">exists</span><span class=\"p\">()</span> <span
  class=\"ow\">and</span> <span class=\"n\">archive</span><span class=\"o\">.</span><span
  class=\"n\">exists</span><span class=\"p\">():</span>\n        <span class=\"n\">shutil</span><span
  class=\"o\">.</span><span class=\"n\">copy</span><span class=\"p\">(</span><span
  class=\"nb\">str</span><span class=\"p\">(</span><span class=\"n\">archive</span><span
  class=\"p\">),</span> <span class=\"nb\">str</span><span class=\"p\">(</span><span
  class=\"n\">home</span><span class=\"p\">))</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"create_page-function\">create_page <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>create_page
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">create_page</span><span class=\"p\">(</span>\n    <span class=\"n\">markata</span><span
  class=\"p\">,</span>\n    <span class=\"n\">page</span><span class=\"p\">,</span>\n
  \   <span class=\"n\">tags</span><span class=\"o\">=</span><span class=\"kc\">None</span><span
  class=\"p\">,</span>\n    <span class=\"n\">status</span><span class=\"o\">=</span><span
  class=\"s2\">&quot;published&quot;</span><span class=\"p\">,</span>\n    <span class=\"n\">template</span><span
  class=\"o\">=</span><span class=\"kc\">None</span><span class=\"p\">,</span>\n    <span
  class=\"n\">card_template</span><span class=\"o\">=</span><span class=\"kc\">None</span><span
  class=\"p\">,</span>\n    <span class=\"nb\">filter</span><span class=\"o\">=</span><span
  class=\"kc\">None</span><span class=\"p\">,</span>\n    <span class=\"n\">description</span><span
  class=\"o\">=</span><span class=\"kc\">None</span><span class=\"p\">,</span>\n    <span
  class=\"n\">url</span><span class=\"o\">=</span><span class=\"kc\">None</span><span
  class=\"p\">,</span>\n    <span class=\"n\">title</span><span class=\"o\">=</span><span
  class=\"s2\">&quot;feed&quot;</span><span class=\"p\">,</span>\n<span class=\"p\">):</span>\n
  \   <span class=\"k\">def</span> <span class=\"nf\">try_filter_date</span><span
  class=\"p\">(</span><span class=\"n\">x</span><span class=\"p\">):</span>\n        <span
  class=\"k\">try</span><span class=\"p\">:</span>\n            <span class=\"k\">return</span>
  <span class=\"n\">x</span><span class=\"p\">[</span><span class=\"s2\">&quot;date&quot;</span><span
  class=\"p\">]</span>\n        <span class=\"k\">except</span> <span class=\"ne\">KeyError</span><span
  class=\"p\">:</span>\n            <span class=\"k\">return</span> <span class=\"o\">-</span><span
  class=\"mi\">1</span>\n\n    <span class=\"k\">if</span> <span class=\"nb\">filter</span>
  <span class=\"ow\">is</span> <span class=\"ow\">not</span> <span class=\"kc\">None</span><span
  class=\"p\">:</span>\n        <span class=\"n\">posts</span> <span class=\"o\">=</span>
  <span class=\"nb\">reversed</span><span class=\"p\">(</span><span class=\"nb\">sorted</span><span
  class=\"p\">(</span><span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">articles</span><span class=\"p\">,</span> <span class=\"n\">key</span><span
  class=\"o\">=</span><span class=\"n\">try_filter_date</span><span class=\"p\">))</span>\n
  \       <span class=\"k\">try</span><span class=\"p\">:</span>\n            <span
  class=\"n\">posts</span> <span class=\"o\">=</span> <span class=\"p\">[</span><span
  class=\"n\">post</span> <span class=\"k\">for</span> <span class=\"n\">post</span>
  <span class=\"ow\">in</span> <span class=\"n\">posts</span> <span class=\"k\">if</span>
  <span class=\"nb\">eval</span><span class=\"p\">(</span><span class=\"nb\">filter</span><span
  class=\"p\">,</span> <span class=\"n\">post</span><span class=\"o\">.</span><span
  class=\"n\">to_dict</span><span class=\"p\">(),</span> <span class=\"p\">{})]</span>\n
  \       <span class=\"k\">except</span> <span class=\"ne\">BaseException</span>
  <span class=\"k\">as</span> <span class=\"n\">e</span><span class=\"p\">:</span>\n
  \           <span class=\"n\">msg</span> <span class=\"o\">=</span> <span class=\"n\">textwrap</span><span
  class=\"o\">.</span><span class=\"n\">dedent</span><span class=\"p\">(</span>\n
  \               <span class=\"sa\">f</span><span class=\"s2\">&quot;&quot;&quot;</span>\n<span
  class=\"s2\">                    While processing page=&#39;</span><span class=\"si\">{</span><span
  class=\"n\">page</span><span class=\"si\">}</span><span class=\"s2\">&#39; markata
  hit the following exception</span>\n<span class=\"s2\">                    during
  filter=&#39;</span><span class=\"si\">{</span><span class=\"nb\">filter</span><span
  class=\"si\">}</span><span class=\"s2\">&#39;</span>\n<span class=\"s2\">                    </span><span
  class=\"si\">{</span><span class=\"n\">e</span><span class=\"si\">}</span><span
  class=\"s2\"></span>\n<span class=\"s2\">                    &quot;&quot;&quot;</span>\n
  \           <span class=\"p\">)</span>\n            <span class=\"k\">raise</span>
  <span class=\"n\">MarkataFilterError</span><span class=\"p\">(</span><span class=\"n\">msg</span><span
  class=\"p\">)</span>\n\n    <span class=\"n\">cards</span> <span class=\"o\">=</span>
  <span class=\"p\">[</span><span class=\"n\">create_card</span><span class=\"p\">(</span><span
  class=\"n\">post</span><span class=\"p\">,</span> <span class=\"n\">card_template</span><span
  class=\"p\">)</span> <span class=\"k\">for</span> <span class=\"n\">post</span>
  <span class=\"ow\">in</span> <span class=\"n\">posts</span><span class=\"p\">]</span>\n
  \   <span class=\"n\">cards</span><span class=\"o\">.</span><span class=\"n\">insert</span><span
  class=\"p\">(</span><span class=\"mi\">0</span><span class=\"p\">,</span> <span
  class=\"s2\">&quot;&lt;ul&gt;&quot;</span><span class=\"p\">)</span>\n    <span
  class=\"n\">cards</span><span class=\"o\">.</span><span class=\"n\">append</span><span
  class=\"p\">(</span><span class=\"s2\">&quot;&lt;/ul&gt;&quot;</span><span class=\"p\">)</span>\n\n
  \   <span class=\"k\">with</span> <span class=\"nb\">open</span><span class=\"p\">(</span><span
  class=\"n\">template</span><span class=\"p\">)</span> <span class=\"k\">as</span>
  <span class=\"n\">f</span><span class=\"p\">:</span>\n        <span class=\"n\">template</span>
  <span class=\"o\">=</span> <span class=\"n\">Template</span><span class=\"p\">(</span><span
  class=\"n\">f</span><span class=\"o\">.</span><span class=\"n\">read</span><span
  class=\"p\">())</span>\n    <span class=\"n\">output_file</span> <span class=\"o\">=</span>
  <span class=\"n\">Path</span><span class=\"p\">(</span><span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">config</span><span class=\"p\">[</span><span
  class=\"s2\">&quot;output_dir&quot;</span><span class=\"p\">])</span> <span class=\"o\">/</span>
  <span class=\"n\">page</span> <span class=\"o\">/</span> <span class=\"s2\">&quot;index.html&quot;</span>\n
  \   <span class=\"n\">canonical_url</span> <span class=\"o\">=</span> <span class=\"sa\">f</span><span
  class=\"s2\">&quot;</span><span class=\"si\">{</span><span class=\"n\">url</span><span
  class=\"si\">}</span><span class=\"s2\">/</span><span class=\"si\">{</span><span
  class=\"n\">page</span><span class=\"si\">}</span><span class=\"s2\">/&quot;</span>\n
  \   <span class=\"n\">output_file</span><span class=\"o\">.</span><span class=\"n\">parent</span><span
  class=\"o\">.</span><span class=\"n\">mkdir</span><span class=\"p\">(</span><span
  class=\"n\">exist_ok</span><span class=\"o\">=</span><span class=\"kc\">True</span><span
  class=\"p\">,</span> <span class=\"n\">parents</span><span class=\"o\">=</span><span
  class=\"kc\">True</span><span class=\"p\">)</span>\n\n    <span class=\"k\">with</span>
  <span class=\"nb\">open</span><span class=\"p\">(</span><span class=\"n\">output_file</span><span
  class=\"p\">,</span> <span class=\"s2\">&quot;w+&quot;</span><span class=\"p\">)</span>
  <span class=\"k\">as</span> <span class=\"n\">f</span><span class=\"p\">:</span>\n
  \       <span class=\"n\">f</span><span class=\"o\">.</span><span class=\"n\">write</span><span
  class=\"p\">(</span>\n            <span class=\"n\">template</span><span class=\"o\">.</span><span
  class=\"n\">render</span><span class=\"p\">(</span>\n                <span class=\"n\">body</span><span
  class=\"o\">=</span><span class=\"s2\">&quot;&quot;</span><span class=\"o\">.</span><span
  class=\"n\">join</span><span class=\"p\">(</span><span class=\"n\">cards</span><span
  class=\"p\">),</span>\n                <span class=\"n\">url</span><span class=\"o\">=</span><span
  class=\"n\">url</span><span class=\"p\">,</span>\n                <span class=\"n\">description</span><span
  class=\"o\">=</span><span class=\"n\">description</span><span class=\"p\">,</span>\n
  \               <span class=\"n\">title</span><span class=\"o\">=</span><span class=\"n\">title</span><span
  class=\"p\">,</span>\n                <span class=\"n\">canonical_url</span><span
  class=\"o\">=</span><span class=\"n\">canonical_url</span><span class=\"p\">,</span>\n
  \               <span class=\"n\">today</span><span class=\"o\">=</span><span class=\"n\">datetime</span><span
  class=\"o\">.</span><span class=\"n\">datetime</span><span class=\"o\">.</span><span
  class=\"n\">today</span><span class=\"p\">(),</span>\n            <span class=\"p\">)</span>\n
  \       <span class=\"p\">)</span>\n</code></pre></div>\n</details>\n<hr />\n<h2
  id=\"create_card-function\">create_card <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>create_card
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">create_card</span><span class=\"p\">(</span><span class=\"n\">post</span><span
  class=\"p\">,</span> <span class=\"n\">template</span><span class=\"o\">=</span><span
  class=\"kc\">None</span><span class=\"p\">):</span>\n    <span class=\"k\">if</span>
  <span class=\"n\">template</span> <span class=\"ow\">is</span> <span class=\"kc\">None</span><span
  class=\"p\">:</span>\n        <span class=\"k\">if</span> <span class=\"s2\">&quot;date&quot;</span>
  <span class=\"ow\">in</span> <span class=\"n\">post</span><span class=\"o\">.</span><span
  class=\"n\">keys</span><span class=\"p\">():</span>\n            <span class=\"k\">return</span>
  <span class=\"n\">textwrap</span><span class=\"o\">.</span><span class=\"n\">dedent</span><span
  class=\"p\">(</span>\n                <span class=\"sa\">f</span><span class=\"s2\">&quot;&quot;&quot;</span>\n<span
  class=\"s2\">                &lt;li class=&#39;post&#39;&gt;</span>\n<span class=\"s2\">
  \               &lt;a href=&quot;/</span><span class=\"si\">{</span><span class=\"n\">post</span><span
  class=\"p\">[</span><span class=\"s1\">&#39;slug&#39;</span><span class=\"p\">]</span><span
  class=\"si\">}</span><span class=\"s2\">/&quot;&gt;</span>\n<span class=\"s2\">
  \                   </span><span class=\"si\">{</span><span class=\"n\">post</span><span
  class=\"p\">[</span><span class=\"s1\">&#39;title&#39;</span><span class=\"p\">]</span><span
  class=\"si\">}</span><span class=\"s2\"> </span><span class=\"si\">{</span><span
  class=\"n\">post</span><span class=\"p\">[</span><span class=\"s1\">&#39;date&#39;</span><span
  class=\"p\">]</span><span class=\"o\">.</span><span class=\"n\">year</span><span
  class=\"si\">}</span><span class=\"s2\">-</span><span class=\"si\">{</span><span
  class=\"n\">post</span><span class=\"p\">[</span><span class=\"s1\">&#39;date&#39;</span><span
  class=\"p\">]</span><span class=\"o\">.</span><span class=\"n\">month</span><span
  class=\"si\">}</span><span class=\"s2\">-</span><span class=\"si\">{</span><span
  class=\"n\">post</span><span class=\"p\">[</span><span class=\"s1\">&#39;date&#39;</span><span
  class=\"p\">]</span><span class=\"o\">.</span><span class=\"n\">day</span><span
  class=\"si\">}</span><span class=\"s2\"></span>\n<span class=\"s2\">                &lt;/a&gt;</span>\n<span
  class=\"s2\">                &lt;/li&gt;</span>\n<span class=\"s2\">                &quot;&quot;&quot;</span>\n
  \           <span class=\"p\">)</span>\n        <span class=\"k\">else</span><span
  class=\"p\">:</span>\n            <span class=\"k\">return</span> <span class=\"n\">textwrap</span><span
  class=\"o\">.</span><span class=\"n\">dedent</span><span class=\"p\">(</span>\n
  \               <span class=\"sa\">f</span><span class=\"s2\">&quot;&quot;&quot;</span>\n<span
  class=\"s2\">                &lt;li class=&#39;post&#39;&gt;</span>\n<span class=\"s2\">
  \               &lt;a href=&quot;/</span><span class=\"si\">{</span><span class=\"n\">post</span><span
  class=\"p\">[</span><span class=\"s1\">&#39;slug&#39;</span><span class=\"p\">]</span><span
  class=\"si\">}</span><span class=\"s2\">/&quot;&gt;</span>\n<span class=\"s2\">
  \                   </span><span class=\"si\">{</span><span class=\"n\">post</span><span
  class=\"p\">[</span><span class=\"s1\">&#39;title&#39;</span><span class=\"p\">]</span><span
  class=\"si\">}</span><span class=\"s2\"></span>\n<span class=\"s2\">                &lt;/a&gt;</span>\n<span
  class=\"s2\">                &lt;/li&gt;</span>\n<span class=\"s2\">                &quot;&quot;&quot;</span>\n
  \           <span class=\"p\">)</span>\n    <span class=\"k\">try</span><span class=\"p\">:</span>\n
  \       <span class=\"k\">with</span> <span class=\"nb\">open</span><span class=\"p\">(</span><span
  class=\"n\">template</span><span class=\"p\">)</span> <span class=\"k\">as</span>
  <span class=\"n\">f</span><span class=\"p\">:</span>\n            <span class=\"n\">template</span>
  <span class=\"o\">=</span> <span class=\"n\">Template</span><span class=\"p\">(</span><span
  class=\"n\">f</span><span class=\"o\">.</span><span class=\"n\">read</span><span
  class=\"p\">())</span>\n    <span class=\"k\">except</span> <span class=\"ne\">FileNotFoundError</span><span
  class=\"p\">:</span>\n        <span class=\"n\">template</span> <span class=\"o\">=</span>
  <span class=\"n\">Template</span><span class=\"p\">(</span><span class=\"n\">template</span><span
  class=\"p\">)</span>\n    <span class=\"n\">post</span><span class=\"p\">[</span><span
  class=\"s2\">&quot;article_html&quot;</span><span class=\"p\">]</span> <span class=\"o\">=</span>
  <span class=\"n\">post</span><span class=\"o\">.</span><span class=\"n\">article_html</span>\n\n
  \   <span class=\"k\">return</span> <span class=\"n\">template</span><span class=\"o\">.</span><span
  class=\"n\">render</span><span class=\"p\">(</span><span class=\"o\">**</span><span
  class=\"n\">post</span><span class=\"o\">.</span><span class=\"n\">to_dict</span><span
  class=\"p\">())</span>\n</code></pre></div>\n</details>\n<hr />\n<h2 id=\"try_filter_date-function\">try_filter_date
  <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>try_filter_date source</summary>\n<div
  class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span> <span class=\"nf\">try_filter_date</span><span
  class=\"p\">(</span><span class=\"n\">x</span><span class=\"p\">):</span>\n        <span
  class=\"k\">try</span><span class=\"p\">:</span>\n            <span class=\"k\">return</span>
  <span class=\"n\">x</span><span class=\"p\">[</span><span class=\"s2\">&quot;date&quot;</span><span
  class=\"p\">]</span>\n        <span class=\"k\">except</span> <span class=\"ne\">KeyError</span><span
  class=\"p\">:</span>\n            <span class=\"k\">return</span> <span class=\"o\">-</span><span
  class=\"mi\">1</span>\n</code></pre></div>\n</details>"
datetime: null
description: Docs for feeds
long_description: ''
now: 2022-02-05 19:38:00.891445
path: feeds.md
slug: markata/plugins/feeds
status: published
title: feeds.py
today: 2022-02-05
---

---

## MarkataFilterError `class`

None

??? "MarkataFilterError source"
    ``` python
    class MarkataFilterError(RuntimeError):
        ...
    ```


---

## save `function`

None

??? "save source"
    ``` python
    def save(markata):
        config = markata.get_plugin_config("feeds")
        if config is None:
            config["feeds"] = dict()
        if "archive" not in config.keys():
            config["archive"] = dict()
            config["archive"]["filter"] = "True"

        description = markata.get_config("description") or ""
        url = markata.get_config("url") or ""

        template = Path(__file__).parent / "default_post_template.html"

        for page, page_conf in config.items():
            if page not in ["cache_expire", "config_key"]:
                create_page(
                    markata,
                    page,
                    description=description,
                    url=url,
                    template=template,
                    **page_conf,
                )

        home = Path(markata.config["output_dir"]) / "index.html"
        archive = Path(markata.config["output_dir"]) / "archive" / "index.html"
        if not home.exists() and archive.exists():
            shutil.copy(str(archive), str(home))
    ```


---

## create_page `function`

None

??? "create_page source"
    ``` python
    def create_page(
        markata,
        page,
        tags=None,
        status="published",
        template=None,
        card_template=None,
        filter=None,
        description=None,
        url=None,
        title="feed",
    ):
        def try_filter_date(x):
            try:
                return x["date"]
            except KeyError:
                return -1

        if filter is not None:
            posts = reversed(sorted(markata.articles, key=try_filter_date))
            try:
                posts = [post for post in posts if eval(filter, post.to_dict(), {})]
            except BaseException as e:
                msg = textwrap.dedent(
                    f"""
                        While processing page='{page}' markata hit the following exception
                        during filter='{filter}'
                        {e}
                        """
                )
                raise MarkataFilterError(msg)

        cards = [create_card(post, card_template) for post in posts]
        cards.insert(0, "<ul>")
        cards.append("</ul>")

        with open(template) as f:
            template = Template(f.read())
        output_file = Path(markata.config["output_dir"]) / page / "index.html"
        canonical_url = f"{url}/{page}/"
        output_file.parent.mkdir(exist_ok=True, parents=True)

        with open(output_file, "w+") as f:
            f.write(
                template.render(
                    body="".join(cards),
                    url=url,
                    description=description,
                    title=title,
                    canonical_url=canonical_url,
                    today=datetime.datetime.today(),
                )
            )
    ```


---

## create_card `function`

None

??? "create_card source"
    ``` python
    def create_card(post, template=None):
        if template is None:
            if "date" in post.keys():
                return textwrap.dedent(
                    f"""
                    <li class='post'>
                    <a href="/{post['slug']}/">
                        {post['title']} {post['date'].year}-{post['date'].month}-{post['date'].day}
                    </a>
                    </li>
                    """
                )
            else:
                return textwrap.dedent(
                    f"""
                    <li class='post'>
                    <a href="/{post['slug']}/">
                        {post['title']}
                    </a>
                    </li>
                    """
                )
        try:
            with open(template) as f:
                template = Template(f.read())
        except FileNotFoundError:
            template = Template(template)
        post["article_html"] = post.article_html

        return template.render(**post.to_dict())
    ```


---

## try_filter_date `function`

None

??? "try_filter_date source"
    ``` python
    def try_filter_date(x):
            try:
                return x["date"]
            except KeyError:
                return -1
    ```