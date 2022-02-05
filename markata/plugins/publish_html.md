---
article_html: "<hr />\n<h2 id=\"save-function\">save <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>save
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">save</span><span class=\"p\">(</span><span class=\"n\">markata</span><span
  class=\"p\">:</span> <span class=\"s2\">&quot;Markata&quot;</span><span class=\"p\">)</span>
  <span class=\"o\">-&gt;</span> <span class=\"kc\">None</span><span class=\"p\">:</span>\n
  \   <span class=\"n\">output_dir</span> <span class=\"o\">=</span> <span class=\"n\">Path</span><span
  class=\"p\">(</span><span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">config</span><span class=\"p\">[</span><span class=\"s2\">&quot;output_dir&quot;</span><span
  class=\"p\">])</span>  <span class=\"c1\"># type: ignore</span>\n    <span class=\"n\">output_dir</span><span
  class=\"o\">.</span><span class=\"n\">mkdir</span><span class=\"p\">(</span><span
  class=\"n\">parents</span><span class=\"o\">=</span><span class=\"kc\">True</span><span
  class=\"p\">,</span> <span class=\"n\">exist_ok</span><span class=\"o\">=</span><span
  class=\"kc\">True</span><span class=\"p\">)</span>\n\n    <span class=\"k\">for</span>
  <span class=\"n\">article</span> <span class=\"ow\">in</span> <span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">articles</span><span class=\"p\">:</span>\n
  \       <span class=\"k\">if</span> <span class=\"n\">article</span><span class=\"p\">[</span><span
  class=\"s2\">&quot;slug&quot;</span><span class=\"p\">]</span> <span class=\"o\">==</span>
  <span class=\"s2\">&quot;index&quot;</span><span class=\"p\">:</span>\n            <span
  class=\"n\">article_path</span> <span class=\"o\">=</span> <span class=\"n\">output_dir</span>
  <span class=\"o\">/</span> <span class=\"s2\">&quot;index.html&quot;</span>\n        <span
  class=\"k\">else</span><span class=\"p\">:</span>\n            <span class=\"n\">article_path</span>
  <span class=\"o\">=</span> <span class=\"n\">output_dir</span> <span class=\"o\">/</span>
  <span class=\"n\">article</span><span class=\"p\">[</span><span class=\"s2\">&quot;slug&quot;</span><span
  class=\"p\">]</span> <span class=\"o\">/</span> <span class=\"s2\">&quot;index.html&quot;</span>\n
  \       <span class=\"n\">article_path</span><span class=\"o\">.</span><span class=\"n\">parent</span><span
  class=\"o\">.</span><span class=\"n\">mkdir</span><span class=\"p\">(</span><span
  class=\"n\">parents</span><span class=\"o\">=</span><span class=\"kc\">True</span><span
  class=\"p\">,</span> <span class=\"n\">exist_ok</span><span class=\"o\">=</span><span
  class=\"kc\">True</span><span class=\"p\">)</span>\n        <span class=\"k\">with</span>
  <span class=\"nb\">open</span><span class=\"p\">(</span><span class=\"n\">article_path</span><span
  class=\"p\">,</span> <span class=\"s2\">&quot;w+&quot;</span><span class=\"p\">)</span>
  <span class=\"k\">as</span> <span class=\"n\">f</span><span class=\"p\">:</span>\n
  \           <span class=\"n\">f</span><span class=\"o\">.</span><span class=\"n\">write</span><span
  class=\"p\">(</span><span class=\"n\">article</span><span class=\"o\">.</span><span
  class=\"n\">html</span><span class=\"p\">)</span>\n</code></pre></div>\n</details>"
datetime: null
description: Docs for publish_html
long_description: ''
now: 2022-02-05 19:38:00.891418
path: publish_html.md
slug: markata/plugins/publish_html
status: published
title: publish_html.py
today: 2022-02-05
---

---

## save `function`

None

??? "save source"
    ``` python
    def save(markata: "Markata") -> None:
        output_dir = Path(markata.config["output_dir"])  # type: ignore
        output_dir.mkdir(parents=True, exist_ok=True)

        for article in markata.articles:
            if article["slug"] == "index":
                article_path = output_dir / "index.html"
            else:
                article_path = output_dir / article["slug"] / "index.html"
            article_path.parent.mkdir(parents=True, exist_ok=True)
            with open(article_path, "w+") as f:
                f.write(article.html)
    ```