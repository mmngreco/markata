---
article_html: "<hr />\n<h2 id=\"configure-function\">configure <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>configure
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">configure</span><span class=\"p\">(</span><span class=\"n\">markata</span><span
  class=\"p\">:</span> <span class=\"s2\">&quot;MarkataMarkdown&quot;</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"kc\">None</span><span
  class=\"p\">:</span>\n    <span class=\"k\">if</span> <span class=\"s2\">&quot;markdown_extensions&quot;</span>
  <span class=\"ow\">not</span> <span class=\"ow\">in</span> <span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">config</span><span class=\"p\">:</span>\n
  \       <span class=\"n\">markdown_extensions</span> <span class=\"o\">=</span>
  <span class=\"p\">[</span><span class=\"s2\">&quot;&quot;</span><span class=\"p\">]</span>\n
  \   <span class=\"k\">if</span> <span class=\"nb\">isinstance</span><span class=\"p\">(</span><span
  class=\"n\">markata</span><span class=\"o\">.</span><span class=\"n\">config</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;markdown_extensions&quot;</span><span
  class=\"p\">],</span> <span class=\"nb\">str</span><span class=\"p\">):</span>\n
  \       <span class=\"n\">markdown_extensions</span> <span class=\"o\">=</span>
  <span class=\"p\">[</span><span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">config</span><span class=\"p\">[</span><span class=\"s2\">&quot;markdown_extensions&quot;</span><span
  class=\"p\">]]</span>\n    <span class=\"k\">if</span> <span class=\"nb\">isinstance</span><span
  class=\"p\">(</span><span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">config</span><span class=\"p\">[</span><span class=\"s2\">&quot;markdown_extensions&quot;</span><span
  class=\"p\">],</span> <span class=\"nb\">list</span><span class=\"p\">):</span>\n
  \       <span class=\"n\">markdown_extensions</span> <span class=\"o\">=</span>
  <span class=\"n\">markata</span><span class=\"o\">.</span><span class=\"n\">config</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;markdown_extensions&quot;</span><span
  class=\"p\">]</span>\n    <span class=\"k\">else</span><span class=\"p\">:</span>\n
  \       <span class=\"k\">raise</span> <span class=\"ne\">TypeError</span><span
  class=\"p\">(</span><span class=\"s2\">&quot;markdown_extensions should be List[str]&quot;</span><span
  class=\"p\">)</span>\n\n    <span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">markdown_extensions</span> <span class=\"o\">=</span> <span class=\"p\">[</span><span
  class=\"o\">*</span><span class=\"n\">DEFAULT_MD_EXTENSIONS</span><span class=\"p\">,</span>
  <span class=\"o\">*</span><span class=\"n\">markdown_extensions</span><span class=\"p\">]</span>\n
  \   <span class=\"n\">markata</span><span class=\"o\">.</span><span class=\"n\">md</span>
  <span class=\"o\">=</span> <span class=\"n\">markdown</span><span class=\"o\">.</span><span
  class=\"n\">Markdown</span><span class=\"p\">(</span><span class=\"n\">extensions</span><span
  class=\"o\">=</span><span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">markdown_extensions</span><span class=\"p\">)</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"render-function\">render <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>render
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">render</span><span class=\"p\">(</span><span class=\"n\">markata</span><span
  class=\"p\">:</span> <span class=\"s2\">&quot;Markata&quot;</span><span class=\"p\">)</span>
  <span class=\"o\">-&gt;</span> <span class=\"kc\">None</span><span class=\"p\">:</span>\n
  \   <span class=\"n\">config</span> <span class=\"o\">=</span> <span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">get_plugin_config</span><span class=\"p\">(</span><span
  class=\"vm\">__file__</span><span class=\"p\">)</span>\n    <span class=\"k\">with</span>
  <span class=\"n\">markata</span><span class=\"o\">.</span><span class=\"n\">cache</span>
  <span class=\"k\">as</span> <span class=\"n\">cache</span><span class=\"p\">:</span>\n
  \       <span class=\"k\">for</span> <span class=\"n\">article</span> <span class=\"ow\">in</span>
  <span class=\"n\">markata</span><span class=\"o\">.</span><span class=\"n\">iter_articles</span><span
  class=\"p\">(</span><span class=\"s2\">&quot;rendering markdown&quot;</span><span
  class=\"p\">):</span>\n            <span class=\"n\">key</span> <span class=\"o\">=</span>
  <span class=\"n\">markata</span><span class=\"o\">.</span><span class=\"n\">make_hash</span><span
  class=\"p\">(</span>\n                <span class=\"s2\">&quot;render_markdown&quot;</span><span
  class=\"p\">,</span>\n                <span class=\"s2\">&quot;render&quot;</span><span
  class=\"p\">,</span>\n                <span class=\"n\">article</span><span class=\"o\">.</span><span
  class=\"n\">content</span><span class=\"p\">,</span>\n            <span class=\"p\">)</span>\n
  \           <span class=\"n\">html_from_cache</span> <span class=\"o\">=</span>
  <span class=\"n\">cache</span><span class=\"o\">.</span><span class=\"n\">get</span><span
  class=\"p\">(</span><span class=\"n\">key</span><span class=\"p\">)</span>\n            <span
  class=\"k\">if</span> <span class=\"n\">html_from_cache</span> <span class=\"ow\">is</span>
  <span class=\"kc\">None</span><span class=\"p\">:</span>\n                <span
  class=\"n\">html</span> <span class=\"o\">=</span> <span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">md</span><span class=\"o\">.</span><span class=\"n\">convert</span><span
  class=\"p\">(</span><span class=\"n\">article</span><span class=\"o\">.</span><span
  class=\"n\">content</span><span class=\"p\">)</span>\n                <span class=\"n\">cache</span><span
  class=\"o\">.</span><span class=\"n\">add</span><span class=\"p\">(</span><span
  class=\"n\">key</span><span class=\"p\">,</span> <span class=\"n\">html</span><span
  class=\"p\">,</span> <span class=\"n\">expire</span><span class=\"o\">=</span><span
  class=\"n\">config</span><span class=\"p\">[</span><span class=\"s2\">&quot;cache_expire&quot;</span><span
  class=\"p\">])</span>\n            <span class=\"k\">else</span><span class=\"p\">:</span>\n
  \               <span class=\"n\">html</span> <span class=\"o\">=</span> <span class=\"n\">html_from_cache</span>\n
  \           <span class=\"n\">article</span><span class=\"o\">.</span><span class=\"n\">html</span>
  <span class=\"o\">=</span> <span class=\"n\">html</span>\n            <span class=\"n\">article</span><span
  class=\"o\">.</span><span class=\"n\">article_html</span> <span class=\"o\">=</span>
  <span class=\"n\">html</span>\n</code></pre></div>\n</details>\n<hr />\n<h2 id=\"markatamarkdown-class\">MarkataMarkdown
  <code>class</code></h2>\n<p>None</p>\n<details>\n<summary>MarkataMarkdown source</summary>\n<div
  class=\"highlight\"><pre><span></span><code><span class=\"k\">class</span> <span
  class=\"nc\">MarkataMarkdown</span><span class=\"p\">(</span><span class=\"n\">Markata</span><span
  class=\"p\">):</span>\n        <span class=\"n\">articles</span><span class=\"p\">:</span>
  <span class=\"n\">List</span> <span class=\"o\">=</span> <span class=\"p\">[]</span>\n
  \       <span class=\"n\">md</span><span class=\"p\">:</span> <span class=\"n\">markdown</span><span
  class=\"o\">.</span><span class=\"n\">Markdown</span> <span class=\"o\">=</span>
  <span class=\"n\">markdown</span><span class=\"o\">.</span><span class=\"n\">Markdown</span><span
  class=\"p\">()</span>\n        <span class=\"n\">markdown_extensions</span><span
  class=\"p\">:</span> <span class=\"n\">List</span> <span class=\"o\">=</span> <span
  class=\"p\">[]</span>\n</code></pre></div>\n</details>"
datetime: null
description: Docs for render_markdown
long_description: ''
now: 2022-02-05 19:38:00.891393
path: render_markdown.md
slug: markata/plugins/render_markdown
status: published
title: render_markdown.py
today: 2022-02-05
---

---

## configure `function`

None

??? "configure source"
    ``` python
    def configure(markata: "MarkataMarkdown") -> None:
        if "markdown_extensions" not in markata.config:
            markdown_extensions = [""]
        if isinstance(markata.config["markdown_extensions"], str):
            markdown_extensions = [markata.config["markdown_extensions"]]
        if isinstance(markata.config["markdown_extensions"], list):
            markdown_extensions = markata.config["markdown_extensions"]
        else:
            raise TypeError("markdown_extensions should be List[str]")

        markata.markdown_extensions = [*DEFAULT_MD_EXTENSIONS, *markdown_extensions]
        markata.md = markdown.Markdown(extensions=markata.markdown_extensions)
    ```


---

## render `function`

None

??? "render source"
    ``` python
    def render(markata: "Markata") -> None:
        config = markata.get_plugin_config(__file__)
        with markata.cache as cache:
            for article in markata.iter_articles("rendering markdown"):
                key = markata.make_hash(
                    "render_markdown",
                    "render",
                    article.content,
                )
                html_from_cache = cache.get(key)
                if html_from_cache is None:
                    html = markata.md.convert(article.content)
                    cache.add(key, html, expire=config["cache_expire"])
                else:
                    html = html_from_cache
                article.html = html
                article.article_html = html
    ```


---

## MarkataMarkdown `class`

None

??? "MarkataMarkdown source"
    ``` python
    class MarkataMarkdown(Markata):
            articles: List = []
            md: markdown.Markdown = markdown.Markdown()
            markdown_extensions: List = []
    ```