---
article_html: "<p>manifest plugin</p>\n<hr />\n<h2 id=\"render-function\">render <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>render
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">render</span><span class=\"p\">(</span><span class=\"n\">markata</span><span
  class=\"p\">:</span> <span class=\"s2\">&quot;MarkataIcons&quot;</span><span class=\"p\">)</span>
  <span class=\"o\">-&gt;</span> <span class=\"kc\">None</span><span class=\"p\">:</span>\n
  \   <span class=\"k\">if</span> <span class=\"s2\">&quot;icons&quot;</span> <span
  class=\"ow\">in</span> <span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"vm\">__dict__</span><span class=\"o\">.</span><span class=\"n\">keys</span><span
  class=\"p\">():</span>\n        <span class=\"n\">icons</span> <span class=\"o\">=</span>
  <span class=\"n\">markata</span><span class=\"o\">.</span><span class=\"n\">icons</span>\n
  \   <span class=\"k\">else</span><span class=\"p\">:</span>\n        <span class=\"n\">icons</span>
  <span class=\"o\">=</span> <span class=\"p\">[]</span>\n    <span class=\"n\">manifest</span>
  <span class=\"o\">=</span> <span class=\"p\">{</span>\n        <span class=\"s2\">&quot;name&quot;</span><span
  class=\"p\">:</span> <span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">get_config</span><span class=\"p\">(</span><span class=\"s2\">&quot;site_name&quot;</span><span
  class=\"p\">)</span> <span class=\"ow\">or</span> <span class=\"s2\">&quot;&quot;</span><span
  class=\"p\">,</span>\n        <span class=\"s2\">&quot;short_name&quot;</span><span
  class=\"p\">:</span> <span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">get_config</span><span class=\"p\">(</span><span class=\"s2\">&quot;short_name&quot;</span><span
  class=\"p\">)</span> <span class=\"ow\">or</span> <span class=\"s2\">&quot;&quot;</span><span
  class=\"p\">,</span>\n        <span class=\"s2\">&quot;start_url&quot;</span><span
  class=\"p\">:</span> <span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">get_config</span><span class=\"p\">(</span><span class=\"s2\">&quot;start_url&quot;</span><span
  class=\"p\">)</span> <span class=\"ow\">or</span> <span class=\"s2\">&quot;&quot;</span><span
  class=\"p\">,</span>\n        <span class=\"s2\">&quot;display&quot;</span><span
  class=\"p\">:</span> <span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">get_config</span><span class=\"p\">(</span><span class=\"s2\">&quot;display&quot;</span><span
  class=\"p\">)</span> <span class=\"ow\">or</span> <span class=\"s2\">&quot;&quot;</span><span
  class=\"p\">,</span>\n        <span class=\"s2\">&quot;background_color&quot;</span><span
  class=\"p\">:</span> <span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">get_config</span><span class=\"p\">(</span><span class=\"s2\">&quot;background_color&quot;</span><span
  class=\"p\">)</span> <span class=\"ow\">or</span> <span class=\"s2\">&quot;&quot;</span><span
  class=\"p\">,</span>\n        <span class=\"s2\">&quot;theme_color&quot;</span><span
  class=\"p\">:</span> <span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">get_config</span><span class=\"p\">(</span><span class=\"s2\">&quot;theme_color&quot;</span><span
  class=\"p\">)</span> <span class=\"ow\">or</span> <span class=\"s2\">&quot;&quot;</span><span
  class=\"p\">,</span>\n        <span class=\"s2\">&quot;description&quot;</span><span
  class=\"p\">:</span> <span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">get_config</span><span class=\"p\">(</span><span class=\"s2\">&quot;description&quot;</span><span
  class=\"p\">)</span> <span class=\"ow\">or</span> <span class=\"s2\">&quot;&quot;</span><span
  class=\"p\">,</span>\n        <span class=\"s2\">&quot;icons&quot;</span><span class=\"p\">:</span>
  <span class=\"n\">icons</span><span class=\"p\">,</span>\n    <span class=\"p\">}</span>\n
  \   <span class=\"n\">filepath</span> <span class=\"o\">=</span> <span class=\"n\">Path</span><span
  class=\"p\">(</span><span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">config</span><span class=\"p\">[</span><span class=\"s2\">&quot;output_dir&quot;</span><span
  class=\"p\">])</span> <span class=\"o\">/</span> <span class=\"s2\">&quot;manifest.json&quot;</span>\n
  \   <span class=\"n\">filepath</span><span class=\"o\">.</span><span class=\"n\">parent</span><span
  class=\"o\">.</span><span class=\"n\">mkdir</span><span class=\"p\">(</span><span
  class=\"n\">parents</span><span class=\"o\">=</span><span class=\"kc\">True</span><span
  class=\"p\">,</span> <span class=\"n\">exist_ok</span><span class=\"o\">=</span><span
  class=\"kc\">True</span><span class=\"p\">)</span>\n    <span class=\"n\">filepath</span><span
  class=\"o\">.</span><span class=\"n\">touch</span><span class=\"p\">(</span><span
  class=\"n\">exist_ok</span><span class=\"o\">=</span><span class=\"kc\">True</span><span
  class=\"p\">)</span>\n    <span class=\"k\">with</span> <span class=\"nb\">open</span><span
  class=\"p\">(</span><span class=\"n\">filepath</span><span class=\"p\">,</span>
  <span class=\"s2\">&quot;w+&quot;</span><span class=\"p\">)</span> <span class=\"k\">as</span>
  <span class=\"n\">f</span><span class=\"p\">:</span>\n        <span class=\"n\">json</span><span
  class=\"o\">.</span><span class=\"n\">dump</span><span class=\"p\">(</span><span
  class=\"n\">manifest</span><span class=\"p\">,</span> <span class=\"n\">f</span><span
  class=\"p\">,</span> <span class=\"n\">ensure_ascii</span><span class=\"o\">=</span><span
  class=\"kc\">True</span><span class=\"p\">,</span> <span class=\"n\">indent</span><span
  class=\"o\">=</span><span class=\"mi\">4</span><span class=\"p\">)</span>\n    <span
  class=\"n\">config</span> <span class=\"o\">=</span> <span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">get_plugin_config</span><span class=\"p\">(</span><span
  class=\"vm\">__file__</span><span class=\"p\">)</span>\n    <span class=\"k\">with</span>
  <span class=\"n\">markata</span><span class=\"o\">.</span><span class=\"n\">cache</span>
  <span class=\"k\">as</span> <span class=\"n\">cache</span><span class=\"p\">:</span>\n
  \       <span class=\"k\">for</span> <span class=\"n\">article</span> <span class=\"ow\">in</span>
  <span class=\"n\">markata</span><span class=\"o\">.</span><span class=\"n\">iter_articles</span><span
  class=\"p\">(</span><span class=\"s2\">&quot;add manifest link&quot;</span><span
  class=\"p\">):</span>\n            <span class=\"n\">key</span> <span class=\"o\">=</span>
  <span class=\"n\">markata</span><span class=\"o\">.</span><span class=\"n\">make_hash</span><span
  class=\"p\">(</span>\n                <span class=\"s2\">&quot;seo&quot;</span><span
  class=\"p\">,</span>\n                <span class=\"s2\">&quot;manifest&quot;</span><span
  class=\"p\">,</span>\n                <span class=\"n\">article</span><span class=\"o\">.</span><span
  class=\"n\">content</span><span class=\"p\">,</span>\n                <span class=\"n\">article</span><span
  class=\"o\">.</span><span class=\"n\">html</span><span class=\"p\">,</span>\n            <span
  class=\"p\">)</span>\n            <span class=\"n\">html_from_cache</span> <span
  class=\"o\">=</span> <span class=\"n\">cache</span><span class=\"o\">.</span><span
  class=\"n\">get</span><span class=\"p\">(</span><span class=\"n\">key</span><span
  class=\"p\">)</span>\n\n            <span class=\"k\">if</span> <span class=\"n\">html_from_cache</span>
  <span class=\"ow\">is</span> <span class=\"kc\">None</span><span class=\"p\">:</span>\n
  \               <span class=\"n\">soup</span> <span class=\"o\">=</span> <span class=\"n\">BeautifulSoup</span><span
  class=\"p\">(</span><span class=\"n\">article</span><span class=\"o\">.</span><span
  class=\"n\">html</span><span class=\"p\">,</span> <span class=\"n\">features</span><span
  class=\"o\">=</span><span class=\"s2\">&quot;lxml&quot;</span><span class=\"p\">)</span>\n
  \               <span class=\"n\">link</span> <span class=\"o\">=</span> <span class=\"n\">soup</span><span
  class=\"o\">.</span><span class=\"n\">new_tag</span><span class=\"p\">(</span><span
  class=\"s2\">&quot;link&quot;</span><span class=\"p\">)</span>\n                <span
  class=\"n\">link</span><span class=\"o\">.</span><span class=\"n\">attrs</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;rel&quot;</span><span class=\"p\">]</span>
  <span class=\"o\">=</span> <span class=\"s2\">&quot;manifest&quot;</span>\n                <span
  class=\"n\">link</span><span class=\"o\">.</span><span class=\"n\">attrs</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;href&quot;</span><span class=\"p\">]</span>
  <span class=\"o\">=</span> <span class=\"s2\">&quot;/manifest.json&quot;</span>\n
  \               <span class=\"n\">soup</span><span class=\"o\">.</span><span class=\"n\">head</span><span
  class=\"o\">.</span><span class=\"n\">append</span><span class=\"p\">(</span><span
  class=\"n\">link</span><span class=\"p\">)</span>\n\n                <span class=\"n\">html</span>
  <span class=\"o\">=</span> <span class=\"n\">soup</span><span class=\"o\">.</span><span
  class=\"n\">prettify</span><span class=\"p\">()</span>\n                <span class=\"n\">cache</span><span
  class=\"o\">.</span><span class=\"n\">add</span><span class=\"p\">(</span><span
  class=\"n\">key</span><span class=\"p\">,</span> <span class=\"n\">html</span><span
  class=\"p\">,</span> <span class=\"n\">expire</span><span class=\"o\">=</span><span
  class=\"n\">config</span><span class=\"p\">[</span><span class=\"s2\">&quot;cache_expire&quot;</span><span
  class=\"p\">])</span>\n            <span class=\"k\">else</span><span class=\"p\">:</span>\n
  \               <span class=\"n\">html</span> <span class=\"o\">=</span> <span class=\"n\">html_from_cache</span>\n
  \           <span class=\"n\">article</span><span class=\"o\">.</span><span class=\"n\">html</span>
  <span class=\"o\">=</span> <span class=\"n\">html</span>\n</code></pre></div>\n</details>"
datetime: null
description: Docs for manifest
long_description: ''
now: 2022-02-05 19:38:00.891431
path: manifest.md
slug: markata/plugins/manifest
status: published
title: manifest.py
today: 2022-02-05
---

manifest plugin


---

## render `function`

None

??? "render source"
    ``` python
    def render(markata: "MarkataIcons") -> None:
        if "icons" in markata.__dict__.keys():
            icons = markata.icons
        else:
            icons = []
        manifest = {
            "name": markata.get_config("site_name") or "",
            "short_name": markata.get_config("short_name") or "",
            "start_url": markata.get_config("start_url") or "",
            "display": markata.get_config("display") or "",
            "background_color": markata.get_config("background_color") or "",
            "theme_color": markata.get_config("theme_color") or "",
            "description": markata.get_config("description") or "",
            "icons": icons,
        }
        filepath = Path(markata.config["output_dir"]) / "manifest.json"
        filepath.parent.mkdir(parents=True, exist_ok=True)
        filepath.touch(exist_ok=True)
        with open(filepath, "w+") as f:
            json.dump(manifest, f, ensure_ascii=True, indent=4)
        config = markata.get_plugin_config(__file__)
        with markata.cache as cache:
            for article in markata.iter_articles("add manifest link"):
                key = markata.make_hash(
                    "seo",
                    "manifest",
                    article.content,
                    article.html,
                )
                html_from_cache = cache.get(key)

                if html_from_cache is None:
                    soup = BeautifulSoup(article.html, features="lxml")
                    link = soup.new_tag("link")
                    link.attrs["rel"] = "manifest"
                    link.attrs["href"] = "/manifest.json"
                    soup.head.append(link)

                    html = soup.prettify()
                    cache.add(key, html, expire=config["cache_expire"])
                else:
                    html = html_from_cache
                article.html = html
    ```