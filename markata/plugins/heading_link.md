---
article_html: "<p>Creates links next to all heading tags to make it easier for users
  to share a\nspecific heading.</p>\n<hr />\n<h2 id=\"post_render-function\">post_render
  <code>function</code></h2>\n<p>This plugin creates a link svg next to all headings.</p>\n<details>\n<summary>post_render
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">post_render</span><span class=\"p\">(</span><span class=\"n\">markata</span><span
  class=\"p\">:</span> <span class=\"n\">Markata</span><span class=\"p\">)</span>
  <span class=\"o\">-&gt;</span> <span class=\"kc\">None</span><span class=\"p\">:</span>\n
  \   <span class=\"sd\">&quot;&quot;&quot;</span>\n<span class=\"sd\">    This plugin
  creates a link svg next to all headings.</span>\n<span class=\"sd\">    &quot;&quot;&quot;</span>\n\n
  \   <span class=\"n\">config</span> <span class=\"o\">=</span> <span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">get_plugin_config</span><span class=\"p\">(</span><span
  class=\"vm\">__file__</span><span class=\"p\">)</span>\n    <span class=\"k\">with</span>
  <span class=\"n\">markata</span><span class=\"o\">.</span><span class=\"n\">cache</span>
  <span class=\"k\">as</span> <span class=\"n\">cache</span><span class=\"p\">:</span>\n
  \       <span class=\"k\">for</span> <span class=\"n\">article</span> <span class=\"ow\">in</span>
  <span class=\"n\">markata</span><span class=\"o\">.</span><span class=\"n\">iter_articles</span><span
  class=\"p\">(</span><span class=\"s2\">&quot;link headers&quot;</span><span class=\"p\">):</span>\n\n
  \           <span class=\"n\">key</span> <span class=\"o\">=</span> <span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">make_hash</span><span class=\"p\">(</span>\n
  \               <span class=\"s2\">&quot;heading_link&quot;</span><span class=\"p\">,</span>\n
  \               <span class=\"s2\">&quot;post_render&quot;</span><span class=\"p\">,</span>\n
  \               <span class=\"n\">Path</span><span class=\"p\">(</span><span class=\"vm\">__file__</span><span
  class=\"p\">)</span><span class=\"o\">.</span><span class=\"n\">read_text</span><span
  class=\"p\">(),</span>\n                <span class=\"n\">article</span><span class=\"o\">.</span><span
  class=\"n\">content</span><span class=\"p\">,</span>\n                <span class=\"n\">article</span><span
  class=\"o\">.</span><span class=\"n\">html</span><span class=\"p\">,</span>\n            <span
  class=\"p\">)</span>\n\n            <span class=\"n\">html_from_cache</span> <span
  class=\"o\">=</span> <span class=\"n\">cache</span><span class=\"o\">.</span><span
  class=\"n\">get</span><span class=\"p\">(</span><span class=\"n\">key</span><span
  class=\"p\">)</span>\n\n            <span class=\"k\">if</span> <span class=\"n\">html_from_cache</span>
  <span class=\"ow\">is</span> <span class=\"kc\">None</span><span class=\"p\">:</span>\n
  \               <span class=\"n\">html</span> <span class=\"o\">=</span> <span class=\"n\">link_headings</span><span
  class=\"p\">(</span><span class=\"n\">article</span><span class=\"p\">)</span>\n
  \               <span class=\"n\">cache</span><span class=\"o\">.</span><span class=\"n\">add</span><span
  class=\"p\">(</span><span class=\"n\">key</span><span class=\"p\">,</span> <span
  class=\"n\">html</span><span class=\"p\">,</span> <span class=\"n\">expire</span><span
  class=\"o\">=</span><span class=\"n\">config</span><span class=\"p\">[</span><span
  class=\"s2\">&quot;cache_expire&quot;</span><span class=\"p\">])</span>\n            <span
  class=\"k\">else</span><span class=\"p\">:</span>\n                <span class=\"n\">html</span>
  <span class=\"o\">=</span> <span class=\"n\">html_from_cache</span>\n            <span
  class=\"n\">article</span><span class=\"o\">.</span><span class=\"n\">html</span>
  <span class=\"o\">=</span> <span class=\"n\">html</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"link_headings-function\">link_headings <code>function</code></h2>\n<p>Use
  BeautifulSoup to find all headings and run link_heading on them.</p>\n<details>\n<summary>link_headings
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">link_headings</span><span class=\"p\">(</span><span class=\"n\">article</span><span
  class=\"p\">:</span> <span class=\"s2\">&quot;Post&quot;</span><span class=\"p\">)</span>
  <span class=\"o\">-&gt;</span> <span class=\"n\">Any</span><span class=\"p\">:</span>\n
  \   <span class=\"sd\">&quot;&quot;&quot;</span>\n<span class=\"sd\">    Use BeautifulSoup
  to find all headings and run link_heading on them.</span>\n<span class=\"sd\">    &quot;&quot;&quot;</span>\n
  \   <span class=\"n\">soup</span> <span class=\"o\">=</span> <span class=\"n\">BeautifulSoup</span><span
  class=\"p\">(</span><span class=\"n\">article</span><span class=\"o\">.</span><span
  class=\"n\">html</span><span class=\"p\">,</span> <span class=\"n\">features</span><span
  class=\"o\">=</span><span class=\"s2\">&quot;lxml&quot;</span><span class=\"p\">)</span>\n
  \   <span class=\"k\">for</span> <span class=\"n\">heading</span> <span class=\"ow\">in</span>
  <span class=\"n\">soup</span><span class=\"o\">.</span><span class=\"n\">find_all</span><span
  class=\"p\">(</span><span class=\"n\">re</span><span class=\"o\">.</span><span class=\"n\">compile</span><span
  class=\"p\">(</span><span class=\"s2\">&quot;^h[1-6]$&quot;</span><span class=\"p\">)):</span>\n
  \       <span class=\"k\">if</span> <span class=\"ow\">not</span> <span class=\"n\">heading</span><span
  class=\"o\">.</span><span class=\"n\">find</span><span class=\"p\">(</span><span
  class=\"s2\">&quot;a&quot;</span><span class=\"p\">,</span> <span class=\"p\">{</span><span
  class=\"s2\">&quot;class&quot;</span><span class=\"p\">:</span> <span class=\"s2\">&quot;heading-permalink&quot;</span><span
  class=\"p\">}):</span>\n            <span class=\"n\">link_heading</span><span class=\"p\">(</span><span
  class=\"n\">soup</span><span class=\"p\">,</span> <span class=\"n\">heading</span><span
  class=\"p\">)</span>\n    <span class=\"n\">html</span> <span class=\"o\">=</span>
  <span class=\"n\">soup</span><span class=\"o\">.</span><span class=\"n\">prettify</span><span
  class=\"p\">()</span>\n    <span class=\"k\">return</span> <span class=\"n\">html</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"link_heading-function\">link_heading <code>function</code></h2>\n<p>Mutate
  soup to include an svg link at the heading passed in.</p>\n<details>\n<summary>link_heading
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">link_heading</span><span class=\"p\">(</span><span class=\"n\">soup</span><span
  class=\"p\">:</span> <span class=\"s2\">&quot;bs4.BeautifulSoup&quot;</span><span
  class=\"p\">,</span> <span class=\"n\">heading</span><span class=\"p\">:</span>
  <span class=\"s2\">&quot;bs4.element.Tag&quot;</span><span class=\"p\">)</span>
  <span class=\"o\">-&gt;</span> <span class=\"kc\">None</span><span class=\"p\">:</span>\n
  \   <span class=\"sd\">&quot;&quot;&quot;</span>\n<span class=\"sd\">    Mutate
  soup to include an svg link at the heading passed in.</span>\n<span class=\"sd\">
  \   &quot;&quot;&quot;</span>\n    <span class=\"nb\">id</span> <span class=\"o\">=</span>
  <span class=\"n\">heading</span><span class=\"o\">.</span><span class=\"n\">get</span><span
  class=\"p\">(</span><span class=\"s2\">&quot;id&quot;</span><span class=\"p\">)</span>\n\n
  \   <span class=\"n\">link</span> <span class=\"o\">=</span> <span class=\"n\">soup</span><span
  class=\"o\">.</span><span class=\"n\">new_tag</span><span class=\"p\">(</span><span
  class=\"s2\">&quot;a&quot;</span><span class=\"p\">,</span> <span class=\"n\">href</span><span
  class=\"o\">=</span><span class=\"sa\">f</span><span class=\"s2\">&quot;#</span><span
  class=\"si\">{</span><span class=\"nb\">id</span><span class=\"si\">}</span><span
  class=\"s2\">&quot;</span><span class=\"p\">,</span> <span class=\"o\">**</span><span
  class=\"p\">{</span><span class=\"s2\">&quot;class&quot;</span><span class=\"p\">:</span>
  <span class=\"s2\">&quot;heading-permalink&quot;</span><span class=\"p\">})</span>\n
  \   <span class=\"n\">span</span> <span class=\"o\">=</span> <span class=\"n\">soup</span><span
  class=\"o\">.</span><span class=\"n\">new_tag</span><span class=\"p\">(</span><span
  class=\"s2\">&quot;span&quot;</span><span class=\"p\">,</span> <span class=\"o\">**</span><span
  class=\"p\">{</span><span class=\"s2\">&quot;class&quot;</span><span class=\"p\">:</span>
  <span class=\"s2\">&quot;visually-hidden&quot;</span><span class=\"p\">})</span>\n
  \   <span class=\"n\">svg</span> <span class=\"o\">=</span> <span class=\"n\">soup</span><span
  class=\"o\">.</span><span class=\"n\">new_tag</span><span class=\"p\">(</span>\n
  \       <span class=\"s2\">&quot;svg&quot;</span><span class=\"p\">,</span>\n        <span
  class=\"n\">fill</span><span class=\"o\">=</span><span class=\"s2\">&quot;currentColor&quot;</span><span
  class=\"p\">,</span>\n        <span class=\"n\">focusable</span><span class=\"o\">=</span><span
  class=\"s2\">&quot;false&quot;</span><span class=\"p\">,</span>\n        <span class=\"n\">width</span><span
  class=\"o\">=</span><span class=\"s2\">&quot;1em&quot;</span><span class=\"p\">,</span>\n
  \       <span class=\"n\">height</span><span class=\"o\">=</span><span class=\"s2\">&quot;1em&quot;</span><span
  class=\"p\">,</span>\n        <span class=\"n\">xmlns</span><span class=\"o\">=</span><span
  class=\"s2\">&quot;http://www.w3.org/2000/svg&quot;</span><span class=\"p\">,</span>\n
  \       <span class=\"n\">viewBox</span><span class=\"o\">=</span><span class=\"s2\">&quot;0
  0 24 24&quot;</span><span class=\"p\">,</span>\n        <span class=\"o\">**</span><span
  class=\"p\">{</span>\n            <span class=\"s2\">&quot;aria-hidden&quot;</span><span
  class=\"p\">:</span> <span class=\"s2\">&quot;true&quot;</span><span class=\"p\">,</span>\n
  \       <span class=\"p\">},</span>\n    <span class=\"p\">)</span>\n\n    <span
  class=\"n\">path</span> <span class=\"o\">=</span> <span class=\"n\">soup</span><span
  class=\"o\">.</span><span class=\"n\">new_tag</span><span class=\"p\">(</span>\n
  \       <span class=\"s2\">&quot;path&quot;</span><span class=\"p\">,</span>\n        <span
  class=\"n\">d</span><span class=\"o\">=</span><span class=\"s2\">&quot;M9.199 13.599a5.99
  5.99 0 0 0 3.949 2.345 5.987 5.987 0 0 0 5.105-1.702l2.995-2.994a5.992 5.992 0 0
  0 1.695-4.285 5.976 5.976 0 0 0-1.831-4.211 5.99 5.99 0 0 0-6.431-1.242 6.003 6.003
  0 0 0-1.905 1.24l-1.731 1.721a.999.999 0 1 0 1.41 1.418l1.709-1.699a3.985 3.985
  0 0 1 2.761-1.123 3.975 3.975 0 0 1 2.799 1.122 3.997 3.997 0 0 1 .111 5.644l-3.005
  3.006a3.982 3.982 0 0 1-3.395 1.126 3.987 3.987 0 0 1-2.632-1.563A1 1 0 0 0 9.201
  13.6zm5.602-3.198a5.99 5.99 0 0 0-3.949-2.345 5.987 5.987 0 0 0-5.105 1.702l-2.995
  2.994a5.992 5.992 0 0 0-1.695 4.285 5.976 5.976 0 0 0 1.831 4.211 5.99 5.99 0 0
  0 6.431 1.242 6.003 6.003 0 0 0 1.905-1.24l1.723-1.723a.999.999 0 1 0-1.414-1.414L9.836
  19.81a3.985 3.985 0 0 1-2.761 1.123 3.975 3.975 0 0 1-2.799-1.122 3.997 3.997 0
  0 1-.111-5.644l3.005-3.006a3.982 3.982 0 0 1 3.395-1.126 3.987 3.987 0 0 1 2.632
  1.563 1 1 0 0 0 1.602-1.198z&quot;</span><span class=\"p\">,</span>\n    <span class=\"p\">)</span>\n
  \   <span class=\"n\">svg</span><span class=\"o\">.</span><span class=\"n\">append</span><span
  class=\"p\">(</span><span class=\"n\">path</span><span class=\"p\">)</span>\n    <span
  class=\"n\">link</span><span class=\"o\">.</span><span class=\"n\">append</span><span
  class=\"p\">(</span><span class=\"n\">span</span><span class=\"p\">)</span>\n    <span
  class=\"n\">link</span><span class=\"o\">.</span><span class=\"n\">append</span><span
  class=\"p\">(</span><span class=\"n\">svg</span><span class=\"p\">)</span>\n    <span
  class=\"n\">heading</span><span class=\"o\">.</span><span class=\"n\">append</span><span
  class=\"p\">(</span><span class=\"n\">link</span><span class=\"p\">)</span>\n</code></pre></div>\n</details>"
datetime: null
description: Docs for heading_link
long_description: ''
now: 2022-02-05 19:38:00.891415
path: heading_link.md
slug: markata/plugins/heading_link
status: published
title: heading_link.py
today: 2022-02-05
---

Creates links next to all heading tags to make it easier for users to share a
specific heading.


---

## post_render `function`

This plugin creates a link svg next to all headings.

??? "post_render source"
    ``` python
    def post_render(markata: Markata) -> None:
        """
        This plugin creates a link svg next to all headings.
        """

        config = markata.get_plugin_config(__file__)
        with markata.cache as cache:
            for article in markata.iter_articles("link headers"):

                key = markata.make_hash(
                    "heading_link",
                    "post_render",
                    Path(__file__).read_text(),
                    article.content,
                    article.html,
                )

                html_from_cache = cache.get(key)

                if html_from_cache is None:
                    html = link_headings(article)
                    cache.add(key, html, expire=config["cache_expire"])
                else:
                    html = html_from_cache
                article.html = html
    ```


---

## link_headings `function`

Use BeautifulSoup to find all headings and run link_heading on them.

??? "link_headings source"
    ``` python
    def link_headings(article: "Post") -> Any:
        """
        Use BeautifulSoup to find all headings and run link_heading on them.
        """
        soup = BeautifulSoup(article.html, features="lxml")
        for heading in soup.find_all(re.compile("^h[1-6]$")):
            if not heading.find("a", {"class": "heading-permalink"}):
                link_heading(soup, heading)
        html = soup.prettify()
        return html
    ```


---

## link_heading `function`

Mutate soup to include an svg link at the heading passed in.

??? "link_heading source"
    ``` python
    def link_heading(soup: "bs4.BeautifulSoup", heading: "bs4.element.Tag") -> None:
        """
        Mutate soup to include an svg link at the heading passed in.
        """
        id = heading.get("id")

        link = soup.new_tag("a", href=f"#{id}", **{"class": "heading-permalink"})
        span = soup.new_tag("span", **{"class": "visually-hidden"})
        svg = soup.new_tag(
            "svg",
            fill="currentColor",
            focusable="false",
            width="1em",
            height="1em",
            xmlns="http://www.w3.org/2000/svg",
            viewBox="0 0 24 24",
            **{
                "aria-hidden": "true",
            },
        )

        path = soup.new_tag(
            "path",
            d="M9.199 13.599a5.99 5.99 0 0 0 3.949 2.345 5.987 5.987 0 0 0 5.105-1.702l2.995-2.994a5.992 5.992 0 0 0 1.695-4.285 5.976 5.976 0 0 0-1.831-4.211 5.99 5.99 0 0 0-6.431-1.242 6.003 6.003 0 0 0-1.905 1.24l-1.731 1.721a.999.999 0 1 0 1.41 1.418l1.709-1.699a3.985 3.985 0 0 1 2.761-1.123 3.975 3.975 0 0 1 2.799 1.122 3.997 3.997 0 0 1 .111 5.644l-3.005 3.006a3.982 3.982 0 0 1-3.395 1.126 3.987 3.987 0 0 1-2.632-1.563A1 1 0 0 0 9.201 13.6zm5.602-3.198a5.99 5.99 0 0 0-3.949-2.345 5.987 5.987 0 0 0-5.105 1.702l-2.995 2.994a5.992 5.992 0 0 0-1.695 4.285 5.976 5.976 0 0 0 1.831 4.211 5.99 5.99 0 0 0 6.431 1.242 6.003 6.003 0 0 0 1.905-1.24l1.723-1.723a.999.999 0 1 0-1.414-1.414L9.836 19.81a3.985 3.985 0 0 1-2.761 1.123 3.975 3.975 0 0 1-2.799-1.122 3.997 3.997 0 0 1-.111-5.644l3.005-3.006a3.982 3.982 0 0 1 3.395-1.126 3.987 3.987 0 0 1 2.632 1.563 1 1 0 0 0 1.602-1.198z",
        )
        svg.append(path)
        link.append(span)
        link.append(svg)
        heading.append(link)
    ```