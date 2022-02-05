---
article_html: "<hr />\n<h2 id=\"render-function\">render <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>render
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">render</span><span class=\"p\">(</span><span class=\"n\">markata</span><span
  class=\"p\">:</span> <span class=\"n\">Markata</span><span class=\"p\">)</span>
  <span class=\"o\">-&gt;</span> <span class=\"kc\">None</span><span class=\"p\">:</span>\n
  \   <span class=\"n\">url</span> <span class=\"o\">=</span> <span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">get_config</span><span class=\"p\">(</span><span
  class=\"s2\">&quot;url&quot;</span><span class=\"p\">)</span> <span class=\"ow\">or</span>
  <span class=\"s2\">&quot;&quot;</span>\n\n    <span class=\"n\">sitemap</span> <span
  class=\"o\">=</span> <span class=\"p\">{</span>\n        <span class=\"s2\">&quot;urlset&quot;</span><span
  class=\"p\">:</span> <span class=\"p\">[</span>\n            <span class=\"p\">{</span>\n
  \               <span class=\"s2\">&quot;url&quot;</span><span class=\"p\">:</span>
  <span class=\"p\">{</span>\n                    <span class=\"s2\">&quot;loc&quot;</span><span
  class=\"p\">:</span> <span class=\"n\">url</span> <span class=\"o\">+</span> <span
  class=\"s2\">&quot;/&quot;</span> <span class=\"o\">+</span> <span class=\"n\">article</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;slug&quot;</span><span class=\"p\">]</span>
  <span class=\"o\">+</span> <span class=\"s2\">&quot;/&quot;</span><span class=\"p\">,</span>\n
  \                   <span class=\"s2\">&quot;changefreq&quot;</span><span class=\"p\">:</span>
  <span class=\"s2\">&quot;daily&quot;</span><span class=\"p\">,</span>\n                    <span
  class=\"s2\">&quot;priority&quot;</span><span class=\"p\">:</span> <span class=\"s2\">&quot;0.7&quot;</span><span
  class=\"p\">,</span>\n                <span class=\"p\">}</span>\n            <span
  class=\"p\">}</span>\n            <span class=\"k\">for</span> <span class=\"n\">article</span>
  <span class=\"ow\">in</span> <span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">articles</span>\n            <span class=\"k\">if</span> <span class=\"n\">article</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;status&quot;</span><span class=\"p\">]</span>
  <span class=\"o\">==</span> <span class=\"s2\">&quot;published&quot;</span>\n        <span
  class=\"p\">]</span>\n    <span class=\"p\">}</span>\n\n    <span class=\"n\">sitemap</span>
  <span class=\"o\">=</span> <span class=\"p\">(</span>\n        <span class=\"n\">anyconfig</span><span
  class=\"o\">.</span><span class=\"n\">dumps</span><span class=\"p\">(</span><span
  class=\"n\">sitemap</span><span class=\"p\">,</span> <span class=\"s2\">&quot;xml&quot;</span><span
  class=\"p\">)</span>\n        <span class=\"o\">.</span><span class=\"n\">decode</span><span
  class=\"p\">(</span><span class=\"s2\">&quot;utf-8&quot;</span><span class=\"p\">)</span>\n
  \       <span class=\"o\">.</span><span class=\"n\">replace</span><span class=\"p\">(</span>\n
  \           <span class=\"s2\">&quot;&lt;urlset&gt;&quot;</span><span class=\"p\">,</span>\n
  \           <span class=\"s1\">&#39;&lt;urlset xmlns=&quot;http://www.sitemaps.org/schemas/sitemap/0.9&quot;
  xmlns:news=&quot;http://www.google.com/schemas/sitemap-news/0.9&quot; xmlns:xhtml=&quot;http://www.w3.org/1999/xhtml&quot;
  xmlns:mobile=&quot;http://www.google.com/schemas/sitemap-mobile/1.0&quot; xmlns:image=&quot;http://www.google.com/schemas/sitemap-image/1.1&quot;
  xmlns:video=&quot;http://www.google.com/schemas/sitemap-video/1.1&quot;&gt;&#39;</span><span
  class=\"p\">,</span>\n        <span class=\"p\">)</span>\n        <span class=\"o\">.</span><span
  class=\"n\">replace</span><span class=\"p\">(</span><span class=\"s2\">&quot;&lt;/url&gt;&quot;</span><span
  class=\"p\">,</span> <span class=\"s2\">&quot;&lt;/url&gt;</span><span class=\"se\">\\n</span><span
  class=\"s2\">&quot;</span><span class=\"p\">)</span>\n    <span class=\"p\">)</span>\n
  \   <span class=\"nb\">setattr</span><span class=\"p\">(</span><span class=\"n\">markata</span><span
  class=\"p\">,</span> <span class=\"s2\">&quot;sitemap&quot;</span><span class=\"p\">,</span>
  <span class=\"n\">sitemap</span><span class=\"p\">)</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"save-function\">save <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>save
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">save</span><span class=\"p\">(</span><span class=\"n\">markata</span><span
  class=\"p\">:</span> <span class=\"n\">Markata</span><span class=\"p\">)</span>
  <span class=\"o\">-&gt;</span> <span class=\"kc\">None</span><span class=\"p\">:</span>\n
  \   <span class=\"k\">with</span> <span class=\"nb\">open</span><span class=\"p\">(</span><span
  class=\"n\">Path</span><span class=\"p\">(</span><span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">config</span><span class=\"p\">[</span><span
  class=\"s2\">&quot;output_dir&quot;</span><span class=\"p\">])</span> <span class=\"o\">/</span>
  <span class=\"s2\">&quot;sitemap.xml&quot;</span><span class=\"p\">,</span> <span
  class=\"s2\">&quot;w&quot;</span><span class=\"p\">)</span> <span class=\"k\">as</span>
  <span class=\"n\">f</span><span class=\"p\">:</span>\n        <span class=\"n\">f</span><span
  class=\"o\">.</span><span class=\"n\">write</span><span class=\"p\">(</span><span
  class=\"n\">markata</span><span class=\"o\">.</span><span class=\"n\">sitemap</span><span
  class=\"p\">)</span>\n</code></pre></div>\n</details>"
datetime: null
description: Docs for sitemap
long_description: ''
now: 2022-02-05 19:38:00.891404
path: sitemap.md
slug: markata/plugins/sitemap
status: published
title: sitemap.py
today: 2022-02-05
---

---

## render `function`

None

??? "render source"
    ``` python
    def render(markata: Markata) -> None:
        url = markata.get_config("url") or ""

        sitemap = {
            "urlset": [
                {
                    "url": {
                        "loc": url + "/" + article["slug"] + "/",
                        "changefreq": "daily",
                        "priority": "0.7",
                    }
                }
                for article in markata.articles
                if article["status"] == "published"
            ]
        }

        sitemap = (
            anyconfig.dumps(sitemap, "xml")
            .decode("utf-8")
            .replace(
                "<urlset>",
                '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:news="http://www.google.com/schemas/sitemap-news/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns:mobile="http://www.google.com/schemas/sitemap-mobile/1.0" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1" xmlns:video="http://www.google.com/schemas/sitemap-video/1.1">',
            )
            .replace("</url>", "</url>\n")
        )
        setattr(markata, "sitemap", sitemap)
    ```


---

## save `function`

None

??? "save source"
    ``` python
    def save(markata: Markata) -> None:
        with open(Path(markata.config["output_dir"]) / "sitemap.xml", "w") as f:
            f.write(markata.sitemap)
    ```