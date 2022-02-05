---
article_html: "<hr />\n<h2 id=\"render-function\">render <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>render
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">render</span><span class=\"p\">(</span><span class=\"n\">markata</span><span
  class=\"p\">:</span> <span class=\"s2\">&quot;Markata&quot;</span><span class=\"p\">)</span>
  <span class=\"o\">-&gt;</span> <span class=\"kc\">None</span><span class=\"p\">:</span>\n
  \   <span class=\"k\">if</span> <span class=\"s2\">&quot;post_template&quot;</span>
  <span class=\"ow\">in</span> <span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">config</span><span class=\"p\">:</span>\n        <span class=\"n\">template_file</span>
  <span class=\"o\">=</span> <span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">config</span><span class=\"p\">[</span><span class=\"s2\">&quot;post_template&quot;</span><span
  class=\"p\">]</span>\n    <span class=\"k\">else</span><span class=\"p\">:</span>\n
  \       <span class=\"n\">template_file</span> <span class=\"o\">=</span> <span
  class=\"n\">Path</span><span class=\"p\">(</span><span class=\"vm\">__file__</span><span
  class=\"p\">)</span><span class=\"o\">.</span><span class=\"n\">parent</span> <span
  class=\"o\">/</span> <span class=\"s2\">&quot;default_post_template.html&quot;</span>\n
  \   <span class=\"k\">with</span> <span class=\"nb\">open</span><span class=\"p\">(</span><span
  class=\"n\">template_file</span><span class=\"p\">)</span> <span class=\"k\">as</span>
  <span class=\"n\">f</span><span class=\"p\">:</span>\n        <span class=\"n\">template</span>
  <span class=\"o\">=</span> <span class=\"n\">Template</span><span class=\"p\">(</span><span
  class=\"n\">f</span><span class=\"o\">.</span><span class=\"n\">read</span><span
  class=\"p\">())</span>\n    <span class=\"k\">for</span> <span class=\"n\">article</span>
  <span class=\"ow\">in</span> <span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">iter_articles</span><span class=\"p\">(</span><span class=\"s2\">&quot;apply
  template&quot;</span><span class=\"p\">):</span>\n\n        <span class=\"n\">article</span><span
  class=\"o\">.</span><span class=\"n\">html</span> <span class=\"o\">=</span> <span
  class=\"n\">template</span><span class=\"o\">.</span><span class=\"n\">render</span><span
  class=\"p\">(</span>\n            <span class=\"n\">body</span><span class=\"o\">=</span><span
  class=\"n\">article</span><span class=\"o\">.</span><span class=\"n\">html</span><span
  class=\"p\">,</span>\n            <span class=\"n\">toc</span><span class=\"o\">=</span><span
  class=\"n\">markata</span><span class=\"o\">.</span><span class=\"n\">md</span><span
  class=\"o\">.</span><span class=\"n\">toc</span><span class=\"p\">,</span>  <span
  class=\"c1\"># type: ignore</span>\n            <span class=\"o\">**</span><span
  class=\"n\">article</span><span class=\"p\">,</span>\n        <span class=\"p\">)</span>\n</code></pre></div>\n</details>"
datetime: null
description: Docs for post_template
long_description: ''
now: 2022-02-05 19:38:00.891426
path: post_template.md
slug: markata/plugins/post_template
status: published
title: post_template.py
today: 2022-02-05
---

---

## render `function`

None

??? "render source"
    ``` python
    def render(markata: "Markata") -> None:
        if "post_template" in markata.config:
            template_file = markata.config["post_template"]
        else:
            template_file = Path(__file__).parent / "default_post_template.html"
        with open(template_file) as f:
            template = Template(f.read())
        for article in markata.iter_articles("apply template"):

            article.html = template.render(
                body=article.html,
                toc=markata.md.toc,  # type: ignore
                **article,
            )
    ```