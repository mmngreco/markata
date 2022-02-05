---
article_html: "<p>Default glob plugin</p>\n<hr />\n<h2 id=\"render-function\">render
  <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>render source</summary>\n<div
  class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span> <span class=\"nf\">render</span><span
  class=\"p\">(</span><span class=\"n\">markata</span><span class=\"p\">:</span> <span
  class=\"s2\">&quot;MarkataRss&quot;</span><span class=\"p\">)</span> <span class=\"o\">-&gt;</span>
  <span class=\"kc\">None</span><span class=\"p\">:</span>\n    <span class=\"n\">fg</span>
  <span class=\"o\">=</span> <span class=\"n\">FeedGenerator</span><span class=\"p\">()</span>\n
  \   <span class=\"n\">url</span> <span class=\"o\">=</span> <span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">get_config</span><span class=\"p\">(</span><span
  class=\"s2\">&quot;url&quot;</span><span class=\"p\">)</span> <span class=\"ow\">or</span>
  <span class=\"s2\">&quot;&quot;</span>\n    <span class=\"n\">title</span> <span
  class=\"o\">=</span> <span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">get_config</span><span class=\"p\">(</span><span class=\"s2\">&quot;title&quot;</span><span
  class=\"p\">)</span> <span class=\"ow\">or</span> <span class=\"s2\">&quot;rss_feed&quot;</span>\n
  \   <span class=\"n\">name</span> <span class=\"o\">=</span> <span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">get_config</span><span class=\"p\">(</span><span
  class=\"s2\">&quot;author_name&quot;</span><span class=\"p\">)</span> <span class=\"ow\">or</span>
  <span class=\"s2\">&quot;&quot;</span>\n    <span class=\"n\">email</span> <span
  class=\"o\">=</span> <span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">get_config</span><span class=\"p\">(</span><span class=\"s2\">&quot;author_email&quot;</span><span
  class=\"p\">)</span> <span class=\"ow\">or</span> <span class=\"s2\">&quot;&quot;</span>\n
  \   <span class=\"n\">icon</span> <span class=\"o\">=</span> <span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">get_config</span><span class=\"p\">(</span><span
  class=\"s2\">&quot;icon&quot;</span><span class=\"p\">)</span> <span class=\"ow\">or</span>
  <span class=\"s2\">&quot;&quot;</span>\n    <span class=\"n\">lang</span> <span
  class=\"o\">=</span> <span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">get_config</span><span class=\"p\">(</span><span class=\"s2\">&quot;lang&quot;</span><span
  class=\"p\">)</span> <span class=\"ow\">or</span> <span class=\"s2\">&quot;&quot;</span>\n
  \   <span class=\"n\">rss_description</span> <span class=\"o\">=</span> <span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">get_config</span><span class=\"p\">(</span><span
  class=\"s2\">&quot;rss_description&quot;</span><span class=\"p\">)</span> <span
  class=\"ow\">or</span> <span class=\"s2\">&quot;rss_feed&quot;</span>\n\n    <span
  class=\"n\">fg</span><span class=\"o\">.</span><span class=\"n\">id</span><span
  class=\"p\">(</span><span class=\"n\">url</span> <span class=\"o\">+</span> <span
  class=\"s2\">&quot;/rss.xml&quot;</span><span class=\"p\">)</span>\n    <span class=\"n\">fg</span><span
  class=\"o\">.</span><span class=\"n\">title</span><span class=\"p\">(</span><span
  class=\"n\">title</span><span class=\"p\">)</span>\n    <span class=\"n\">fg</span><span
  class=\"o\">.</span><span class=\"n\">author</span><span class=\"p\">(</span>\n
  \       <span class=\"p\">{</span>\n            <span class=\"s2\">&quot;name&quot;</span><span
  class=\"p\">:</span> <span class=\"n\">name</span><span class=\"p\">,</span>\n            <span
  class=\"s2\">&quot;email&quot;</span><span class=\"p\">:</span> <span class=\"n\">email</span><span
  class=\"p\">,</span>\n        <span class=\"p\">}</span>\n    <span class=\"p\">)</span>\n
  \   <span class=\"n\">fg</span><span class=\"o\">.</span><span class=\"n\">link</span><span
  class=\"p\">(</span><span class=\"n\">href</span><span class=\"o\">=</span><span
  class=\"n\">url</span><span class=\"p\">,</span> <span class=\"n\">rel</span><span
  class=\"o\">=</span><span class=\"s2\">&quot;alternate&quot;</span><span class=\"p\">)</span>\n
  \   <span class=\"n\">fg</span><span class=\"o\">.</span><span class=\"n\">logo</span><span
  class=\"p\">(</span><span class=\"n\">icon</span><span class=\"p\">)</span>\n    <span
  class=\"n\">fg</span><span class=\"o\">.</span><span class=\"n\">subtitle</span><span
  class=\"p\">(</span><span class=\"n\">rss_description</span><span class=\"p\">)</span>\n
  \   <span class=\"n\">fg</span><span class=\"o\">.</span><span class=\"n\">link</span><span
  class=\"p\">(</span><span class=\"n\">href</span><span class=\"o\">=</span><span
  class=\"n\">url</span> <span class=\"o\">+</span> <span class=\"s2\">&quot;/rss.xml&quot;</span><span
  class=\"p\">,</span> <span class=\"n\">rel</span><span class=\"o\">=</span><span
  class=\"s2\">&quot;self&quot;</span><span class=\"p\">)</span>\n    <span class=\"n\">fg</span><span
  class=\"o\">.</span><span class=\"n\">language</span><span class=\"p\">(</span><span
  class=\"n\">lang</span><span class=\"p\">)</span>\n\n    <span class=\"k\">try</span><span
  class=\"p\">:</span>\n        <span class=\"n\">all_posts</span> <span class=\"o\">=</span>
  <span class=\"nb\">reversed</span><span class=\"p\">(</span><span class=\"nb\">sorted</span><span
  class=\"p\">(</span><span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">articles</span><span class=\"p\">,</span> <span class=\"n\">key</span><span
  class=\"o\">=</span><span class=\"k\">lambda</span> <span class=\"n\">x</span><span
  class=\"p\">:</span> <span class=\"n\">x</span><span class=\"p\">[</span><span class=\"s2\">&quot;date&quot;</span><span
  class=\"p\">]))</span>\n        <span class=\"n\">posts</span> <span class=\"o\">=</span>
  <span class=\"p\">[</span><span class=\"n\">post</span> <span class=\"k\">for</span>
  <span class=\"n\">post</span> <span class=\"ow\">in</span> <span class=\"n\">all_posts</span>
  <span class=\"k\">if</span> <span class=\"n\">post</span><span class=\"p\">[</span><span
  class=\"s2\">&quot;status&quot;</span><span class=\"p\">]</span> <span class=\"o\">==</span>
  <span class=\"s2\">&quot;published&quot;</span><span class=\"p\">]</span>\n    <span
  class=\"k\">except</span> <span class=\"ne\">BaseException</span><span class=\"p\">:</span>\n
  \       <span class=\"n\">posts</span> <span class=\"o\">=</span> <span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">articles</span>\n\n    <span class=\"k\">for</span>
  <span class=\"n\">article</span> <span class=\"ow\">in</span> <span class=\"n\">posts</span><span
  class=\"p\">:</span>\n        <span class=\"n\">fe</span> <span class=\"o\">=</span>
  <span class=\"n\">fg</span><span class=\"o\">.</span><span class=\"n\">add_entry</span><span
  class=\"p\">()</span>\n        <span class=\"n\">fe</span><span class=\"o\">.</span><span
  class=\"n\">id</span><span class=\"p\">(</span><span class=\"n\">url</span> <span
  class=\"o\">+</span> <span class=\"s2\">&quot;/&quot;</span> <span class=\"o\">+</span>
  <span class=\"n\">article</span><span class=\"p\">[</span><span class=\"s2\">&quot;slug&quot;</span><span
  class=\"p\">])</span>\n        <span class=\"n\">fe</span><span class=\"o\">.</span><span
  class=\"n\">title</span><span class=\"p\">(</span><span class=\"n\">article</span><span
  class=\"o\">.</span><span class=\"n\">metadata</span><span class=\"p\">[</span><span
  class=\"s2\">&quot;title&quot;</span><span class=\"p\">])</span>\n        <span
  class=\"n\">fe</span><span class=\"o\">.</span><span class=\"n\">published</span><span
  class=\"p\">(</span><span class=\"n\">article</span><span class=\"o\">.</span><span
  class=\"n\">metadata</span><span class=\"p\">[</span><span class=\"s2\">&quot;datetime&quot;</span><span
  class=\"p\">])</span>\n        <span class=\"n\">fe</span><span class=\"o\">.</span><span
  class=\"n\">description</span><span class=\"p\">(</span><span class=\"n\">article</span><span
  class=\"o\">.</span><span class=\"n\">metadata</span><span class=\"p\">[</span><span
  class=\"s2\">&quot;description&quot;</span><span class=\"p\">])</span>\n        <span
  class=\"n\">fe</span><span class=\"o\">.</span><span class=\"n\">summary</span><span
  class=\"p\">(</span><span class=\"n\">article</span><span class=\"o\">.</span><span
  class=\"n\">metadata</span><span class=\"p\">[</span><span class=\"s2\">&quot;long_description&quot;</span><span
  class=\"p\">])</span>\n        <span class=\"n\">fe</span><span class=\"o\">.</span><span
  class=\"n\">link</span><span class=\"p\">(</span><span class=\"n\">href</span><span
  class=\"o\">=</span><span class=\"n\">url</span> <span class=\"o\">+</span> <span
  class=\"s2\">&quot;/&quot;</span> <span class=\"o\">+</span> <span class=\"n\">article</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;slug&quot;</span><span class=\"p\">])</span>\n
  \       <span class=\"n\">fe</span><span class=\"o\">.</span><span class=\"n\">content</span><span
  class=\"p\">(</span><span class=\"n\">article</span><span class=\"o\">.</span><span
  class=\"n\">article_html</span><span class=\"o\">.</span><span class=\"n\">translate</span><span
  class=\"p\">(</span><span class=\"nb\">dict</span><span class=\"o\">.</span><span
  class=\"n\">fromkeys</span><span class=\"p\">(</span><span class=\"nb\">range</span><span
  class=\"p\">(</span><span class=\"mi\">32</span><span class=\"p\">))))</span>\n\n
  \   <span class=\"n\">markata</span><span class=\"o\">.</span><span class=\"n\">fg</span>
  <span class=\"o\">=</span> <span class=\"n\">fg</span>\n    <span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">rss</span> <span class=\"o\">=</span> <span
  class=\"n\">fg</span><span class=\"o\">.</span><span class=\"n\">rss_str</span><span
  class=\"p\">(</span><span class=\"n\">pretty</span><span class=\"o\">=</span><span
  class=\"kc\">True</span><span class=\"p\">)</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"save-function\">save <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>save
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">save</span><span class=\"p\">(</span><span class=\"n\">markata</span><span
  class=\"p\">:</span> <span class=\"s2\">&quot;MarkataRss&quot;</span><span class=\"p\">)</span>
  <span class=\"o\">-&gt;</span> <span class=\"kc\">None</span><span class=\"p\">:</span>\n
  \   <span class=\"n\">output_dir</span> <span class=\"o\">=</span> <span class=\"n\">Path</span><span
  class=\"p\">(</span><span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">config</span><span class=\"p\">[</span><span class=\"s2\">&quot;output_dir&quot;</span><span
  class=\"p\">])</span>\n    <span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">fg</span><span class=\"o\">.</span><span class=\"n\">rss_file</span><span
  class=\"p\">(</span><span class=\"nb\">str</span><span class=\"p\">(</span><span
  class=\"n\">output_dir</span> <span class=\"o\">/</span> <span class=\"s2\">&quot;rss.xml&quot;</span><span
  class=\"p\">))</span>\n</code></pre></div>\n</details>\n<hr />\n<h2 id=\"markatarss-class\">MarkataRss
  <code>class</code></h2>\n<p>None</p>\n<details>\n<summary>MarkataRss source</summary>\n<div
  class=\"highlight\"><pre><span></span><code><span class=\"k\">class</span> <span
  class=\"nc\">MarkataRss</span><span class=\"p\">(</span><span class=\"n\">Markata</span><span
  class=\"p\">):</span>\n        <span class=\"n\">fg</span><span class=\"p\">:</span>
  <span class=\"s2\">&quot;FeedGenerator&quot;</span>\n        <span class=\"n\">rss</span><span
  class=\"p\">:</span> <span class=\"nb\">str</span>\n</code></pre></div>\n</details>"
datetime: null
description: Docs for rss
long_description: ''
now: 2022-02-05 19:38:00.891442
path: rss.md
slug: markata/plugins/rss
status: published
title: rss.py
today: 2022-02-05
---

Default glob plugin


---

## render `function`

None

??? "render source"
    ``` python
    def render(markata: "MarkataRss") -> None:
        fg = FeedGenerator()
        url = markata.get_config("url") or ""
        title = markata.get_config("title") or "rss_feed"
        name = markata.get_config("author_name") or ""
        email = markata.get_config("author_email") or ""
        icon = markata.get_config("icon") or ""
        lang = markata.get_config("lang") or ""
        rss_description = markata.get_config("rss_description") or "rss_feed"

        fg.id(url + "/rss.xml")
        fg.title(title)
        fg.author(
            {
                "name": name,
                "email": email,
            }
        )
        fg.link(href=url, rel="alternate")
        fg.logo(icon)
        fg.subtitle(rss_description)
        fg.link(href=url + "/rss.xml", rel="self")
        fg.language(lang)

        try:
            all_posts = reversed(sorted(markata.articles, key=lambda x: x["date"]))
            posts = [post for post in all_posts if post["status"] == "published"]
        except BaseException:
            posts = markata.articles

        for article in posts:
            fe = fg.add_entry()
            fe.id(url + "/" + article["slug"])
            fe.title(article.metadata["title"])
            fe.published(article.metadata["datetime"])
            fe.description(article.metadata["description"])
            fe.summary(article.metadata["long_description"])
            fe.link(href=url + "/" + article["slug"])
            fe.content(article.article_html.translate(dict.fromkeys(range(32))))

        markata.fg = fg
        markata.rss = fg.rss_str(pretty=True)
    ```


---

## save `function`

None

??? "save source"
    ``` python
    def save(markata: "MarkataRss") -> None:
        output_dir = Path(markata.config["output_dir"])
        markata.fg.rss_file(str(output_dir / "rss.xml"))
    ```


---

## MarkataRss `class`

None

??? "MarkataRss source"
    ``` python
    class MarkataRss(Markata):
            fg: "FeedGenerator"
            rss: str
    ```