---
article_html: "<p>A Markata plugin to create automatic descriptions for markdown documents.
  \ It\ndoes this by grabbing the first <code>{len}</code> number of characters from
  the document\nthat are in a paragraph.</p>\n<h2 id=\"configuration\">Configuration</h2>\n<p>Open
  up your <code>markata.toml</code> file and add new entries for your\nauto_descriptions.
  \ You can have multiple desriptions, each one will be named\nafter the key you give
  it in your config.</p>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">[markata]</span><span
  class=\"w\"></span>\n<span class=\"n\">hooks</span><span class=\"o\">=</span><span
  class=\"p\">[</span><span class=\"w\"></span>\n<span class=\"w\">   </span><span
  class=\"s\">&quot;markata.plugins.auto_description&quot;</span><span class=\"p\">,</span><span
  class=\"w\"></span>\n<span class=\"w\">   </span><span class=\"p\">]</span><span
  class=\"w\"></span>\n\n<span class=\"k\">[markata.auto_description.description]</span><span
  class=\"w\"></span>\n<span class=\"n\">len</span><span class=\"o\">=</span><span
  class=\"mi\">160</span><span class=\"w\"></span>\n<span class=\"k\">[markata.auto_description.long_description]</span><span
  class=\"w\"></span>\n<span class=\"n\">len</span><span class=\"o\">=</span><span
  class=\"mi\">250</span><span class=\"w\"></span>\n<span class=\"k\">[markata.auto_description.super_description]</span><span
  class=\"w\"></span>\n<span class=\"n\">len</span><span class=\"o\">=</span><span
  class=\"mi\">500</span><span class=\"w\"></span>\n</code></pre></div>\n<div class=\"admonition
  note\">\n<p class=\"admonition-title\">Note</p>\n</div>\n<p>Make sure that you have
  the auto_description plugin in your configured hooks.</p>\n<p>In the above we will
  end up with three different descritpions, \n(<code>description</code>, <code>long_description</code>,
  and <code>super_description</code>) each will be the\nfirst number of characters
  from the document as specified in the config.</p>\n<h3 id=\"using-the-description\">Using
  the Description</h3>\n<p>Downstream hooks can now use the description for things
  such as seo, or feeds.\nHere is a simple example that lists all of the descriptions
  in all posts.  This\nis a handy thing you can do right from a repl.</p>\n<div class=\"highlight\"><pre><span></span><code><span
  class=\"kn\">from</span> <span class=\"nn\">markata</span> <span class=\"kn\">import</span>
  <span class=\"n\">Markata</span>\n<span class=\"n\">m</span> <span class=\"o\">=</span>
  <span class=\"n\">Markata</span><span class=\"p\">()</span>\n<span class=\"p\">[</span><span
  class=\"n\">p</span><span class=\"p\">[</span><span class=\"s2\">&quot;description&quot;</span><span
  class=\"p\">]</span> <span class=\"k\">for</span> <span class=\"n\">p</span> <span
  class=\"ow\">in</span> <span class=\"n\">m</span><span class=\"o\">.</span><span
  class=\"n\">articles</span><span class=\"p\">]</span>\n</code></pre></div>\n<hr
  />\n<h2 id=\"get_description-function\">get_description <code>function</code></h2>\n<p>Get
  the full-length description for a single post using the commonmark\nparser.  Only
  paragraph nodes will count as text towards the description.</p>\n<details>\n<summary>get_description
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">get_description</span><span class=\"p\">(</span><span class=\"n\">article</span><span
  class=\"p\">:</span> <span class=\"s2\">&quot;Post&quot;</span><span class=\"p\">)</span>
  <span class=\"o\">-&gt;</span> <span class=\"nb\">str</span><span class=\"p\">:</span>\n
  \   <span class=\"sd\">&quot;&quot;&quot;</span>\n<span class=\"sd\">    Get the
  full-length description for a single post using the commonmark</span>\n<span class=\"sd\">
  \   parser.  Only paragraph nodes will count as text towards the description.</span>\n<span
  class=\"sd\">    &quot;&quot;&quot;</span>\n    <span class=\"n\">ast</span> <span
  class=\"o\">=</span> <span class=\"n\">_parser</span><span class=\"o\">.</span><span
  class=\"n\">parse</span><span class=\"p\">(</span><span class=\"n\">article</span><span
  class=\"o\">.</span><span class=\"n\">content</span><span class=\"p\">)</span>\n
  \   <span class=\"k\">return</span> <span class=\"s2\">&quot; &quot;</span><span
  class=\"o\">.</span><span class=\"n\">join</span><span class=\"p\">(</span>\n        <span
  class=\"p\">[</span>\n            <span class=\"n\">node</span><span class=\"p\">[</span><span
  class=\"mi\">0</span><span class=\"p\">]</span><span class=\"o\">.</span><span class=\"n\">first_child</span><span
  class=\"o\">.</span><span class=\"n\">literal</span>\n            <span class=\"k\">for</span>
  <span class=\"n\">node</span> <span class=\"ow\">in</span> <span class=\"n\">ast</span><span
  class=\"o\">.</span><span class=\"n\">walker</span><span class=\"p\">()</span>\n
  \           <span class=\"k\">if</span> <span class=\"n\">node</span><span class=\"p\">[</span><span
  class=\"mi\">0</span><span class=\"p\">]</span><span class=\"o\">.</span><span class=\"n\">t</span>
  <span class=\"o\">==</span> <span class=\"s2\">&quot;paragraph&quot;</span> <span
  class=\"ow\">and</span> <span class=\"n\">node</span><span class=\"p\">[</span><span
  class=\"mi\">0</span><span class=\"p\">]</span><span class=\"o\">.</span><span class=\"n\">first_child</span><span
  class=\"o\">.</span><span class=\"n\">literal</span> <span class=\"ow\">is</span>
  <span class=\"ow\">not</span> <span class=\"kc\">None</span>\n        <span class=\"p\">]</span>\n
  \   <span class=\"p\">)</span>\n</code></pre></div>\n</details>\n<hr />\n<h2 id=\"set_description-function\">set_description
  <code>function</code></h2>\n<p>For a given <code>article</code>, find the description,
  put it in the cache, and set\nthe configured descriptions for the article.</p>\n<details>\n<summary>set_description
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">set_description</span><span class=\"p\">(</span>\n    <span class=\"n\">markata</span><span
  class=\"p\">:</span> <span class=\"s2\">&quot;Markata&quot;</span><span class=\"p\">,</span>
  <span class=\"n\">article</span><span class=\"p\">:</span> <span class=\"s2\">&quot;Post&quot;</span><span
  class=\"p\">,</span> <span class=\"n\">cache</span><span class=\"p\">:</span> <span
  class=\"s2\">&quot;FanoutCache&quot;</span><span class=\"p\">,</span> <span class=\"n\">config</span><span
  class=\"p\">:</span> <span class=\"n\">Dict</span>\n<span class=\"p\">)</span> <span
  class=\"o\">-&gt;</span> <span class=\"kc\">None</span><span class=\"p\">:</span>\n
  \   <span class=\"sd\">&quot;&quot;&quot;</span>\n<span class=\"sd\">    For a given
  `article`, find the description, put it in the cache, and set</span>\n<span class=\"sd\">
  \   the configured descriptions for the article.</span>\n<span class=\"sd\">    &quot;&quot;&quot;</span>\n
  \   <span class=\"n\">key</span> <span class=\"o\">=</span> <span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">make_hash</span><span class=\"p\">(</span>\n
  \       <span class=\"s2\">&quot;long_description&quot;</span><span class=\"p\">,</span>\n
  \       <span class=\"s2\">&quot;render&quot;</span><span class=\"p\">,</span>\n
  \       <span class=\"n\">Path</span><span class=\"p\">(</span><span class=\"vm\">__file__</span><span
  class=\"p\">)</span><span class=\"o\">.</span><span class=\"n\">read_text</span><span
  class=\"p\">(),</span>\n        <span class=\"n\">article</span><span class=\"o\">.</span><span
  class=\"n\">content</span><span class=\"p\">,</span>\n    <span class=\"p\">)</span>\n\n
  \   <span class=\"n\">description_from_cache</span> <span class=\"o\">=</span> <span
  class=\"n\">cache</span><span class=\"o\">.</span><span class=\"n\">get</span><span
  class=\"p\">(</span><span class=\"n\">key</span><span class=\"p\">)</span>\n    <span
  class=\"k\">if</span> <span class=\"n\">description_from_cache</span> <span class=\"ow\">is</span>
  <span class=\"kc\">None</span><span class=\"p\">:</span>\n        <span class=\"n\">description</span>
  <span class=\"o\">=</span> <span class=\"n\">get_description</span><span class=\"p\">(</span><span
  class=\"n\">article</span><span class=\"p\">)</span>\n        <span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">cache</span><span class=\"o\">.</span><span
  class=\"n\">add</span><span class=\"p\">(</span><span class=\"n\">key</span><span
  class=\"p\">,</span> <span class=\"n\">description</span><span class=\"p\">,</span>
  <span class=\"n\">expire</span><span class=\"o\">=</span><span class=\"n\">config</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;cache_expire&quot;</span><span class=\"p\">])</span>\n
  \   <span class=\"k\">else</span><span class=\"p\">:</span>\n        <span class=\"n\">description</span>
  <span class=\"o\">=</span> <span class=\"n\">description_from_cache</span>\n\n    <span
  class=\"k\">for</span> <span class=\"n\">description_key</span> <span class=\"ow\">in</span>
  <span class=\"n\">config</span><span class=\"p\">:</span>\n        <span class=\"k\">if</span>
  <span class=\"n\">description_key</span> <span class=\"ow\">not</span> <span class=\"ow\">in</span>
  <span class=\"p\">[</span><span class=\"s2\">&quot;cache_expire&quot;</span><span
  class=\"p\">,</span> <span class=\"s2\">&quot;config_key&quot;</span><span class=\"p\">]:</span>\n
  \           <span class=\"k\">if</span> <span class=\"n\">description_key</span>
  <span class=\"ow\">not</span> <span class=\"ow\">in</span> <span class=\"n\">article</span><span
  class=\"o\">.</span><span class=\"n\">metadata</span><span class=\"o\">.</span><span
  class=\"n\">keys</span><span class=\"p\">():</span>\n                <span class=\"n\">article</span><span
  class=\"o\">.</span><span class=\"n\">metadata</span><span class=\"p\">[</span><span
  class=\"n\">description_key</span><span class=\"p\">]</span> <span class=\"o\">=</span>
  <span class=\"n\">description</span><span class=\"p\">[</span>\n                    <span
  class=\"p\">:</span> <span class=\"n\">config</span><span class=\"p\">[</span><span
  class=\"n\">description_key</span><span class=\"p\">][</span><span class=\"s2\">&quot;len&quot;</span><span
  class=\"p\">]</span>\n                <span class=\"p\">]</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"pre_render-function\">pre_render <code>function</code></h2>\n<p>The
  Markata hook that will set descriptions for all posts in the pre-render phase.</p>\n<details>\n<summary>pre_render
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">pre_render</span><span class=\"p\">(</span><span class=\"n\">markata</span><span
  class=\"p\">:</span> <span class=\"s2\">&quot;Markata&quot;</span><span class=\"p\">)</span>
  <span class=\"o\">-&gt;</span> <span class=\"kc\">None</span><span class=\"p\">:</span>\n
  \   <span class=\"sd\">&quot;&quot;&quot;</span>\n<span class=\"sd\">    The Markata
  hook that will set descriptions for all posts in the pre-render phase.</span>\n<span
  class=\"sd\">    &quot;&quot;&quot;</span>\n    <span class=\"n\">config</span>
  <span class=\"o\">=</span> <span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">get_plugin_config</span><span class=\"p\">(</span><span class=\"vm\">__file__</span><span
  class=\"p\">)</span>\n    <span class=\"k\">if</span> <span class=\"s2\">&quot;description&quot;</span>
  <span class=\"ow\">not</span> <span class=\"ow\">in</span> <span class=\"n\">config</span><span
  class=\"o\">.</span><span class=\"n\">keys</span><span class=\"p\">():</span>\n
  \       <span class=\"n\">config</span><span class=\"p\">[</span><span class=\"s2\">&quot;description&quot;</span><span
  class=\"p\">]</span> <span class=\"o\">=</span> <span class=\"p\">{}</span>\n        <span
  class=\"n\">config</span><span class=\"p\">[</span><span class=\"s2\">&quot;description&quot;</span><span
  class=\"p\">][</span><span class=\"s2\">&quot;len&quot;</span><span class=\"p\">]</span>
  <span class=\"o\">=</span> <span class=\"mi\">160</span>\n    <span class=\"k\">with</span>
  <span class=\"n\">markata</span><span class=\"o\">.</span><span class=\"n\">cache</span>
  <span class=\"k\">as</span> <span class=\"n\">cache</span><span class=\"p\">:</span>\n
  \       <span class=\"k\">for</span> <span class=\"n\">article</span> <span class=\"ow\">in</span>
  <span class=\"n\">markata</span><span class=\"o\">.</span><span class=\"n\">iter_articles</span><span
  class=\"p\">(</span><span class=\"s2\">&quot;setting auto description&quot;</span><span
  class=\"p\">):</span>\n            <span class=\"n\">set_description</span><span
  class=\"p\">(</span>\n                <span class=\"n\">markata</span><span class=\"p\">,</span>\n
  \               <span class=\"n\">article</span><span class=\"p\">,</span>\n                <span
  class=\"n\">cache</span><span class=\"p\">,</span>\n                <span class=\"n\">config</span><span
  class=\"p\">,</span>\n            <span class=\"p\">)</span>\n</code></pre></div>\n</details>"
datetime: null
description: Docs for auto_description
long_description: ''
now: 2022-02-05 19:38:00.891374
path: auto_description.md
slug: markata/plugins/auto_description
status: published
title: auto_description.py
today: 2022-02-05
---

A Markata plugin to create automatic descriptions for markdown documents.  It
does this by grabbing the first `{len}` number of characters from the document
that are in a paragraph.

## Configuration

Open up your `markata.toml` file and add new entries for your
auto_descriptions.  You can have multiple desriptions, each one will be named
after the key you give it in your config.

``` toml
[markata]
hooks=[
   "markata.plugins.auto_description",
   ]

[markata.auto_description.description]
len=160
[markata.auto_description.long_description]
len=250
[markata.auto_description.super_description]
len=500
```

!!! note
   Make sure that you have the auto_description plugin in your configured hooks.

In the above we will end up with three different descritpions, 
(`description`, `long_description`, and `super_description`) each will be the
first number of characters from the document as specified in the config.

### Using the Description

Downstream hooks can now use the description for things such as seo, or feeds.
Here is a simple example that lists all of the descriptions in all posts.  This
is a handy thing you can do right from a repl.

``` python
from markata import Markata
m = Markata()
[p["description"] for p in m.articles]
```


---

## get_description `function`

Get the full-length description for a single post using the commonmark
parser.  Only paragraph nodes will count as text towards the description.

??? "get_description source"
    ``` python
    def get_description(article: "Post") -> str:
        """
        Get the full-length description for a single post using the commonmark
        parser.  Only paragraph nodes will count as text towards the description.
        """
        ast = _parser.parse(article.content)
        return " ".join(
            [
                node[0].first_child.literal
                for node in ast.walker()
                if node[0].t == "paragraph" and node[0].first_child.literal is not None
            ]
        )
    ```


---

## set_description `function`

For a given `article`, find the description, put it in the cache, and set
the configured descriptions for the article.

??? "set_description source"
    ``` python
    def set_description(
        markata: "Markata", article: "Post", cache: "FanoutCache", config: Dict
    ) -> None:
        """
        For a given `article`, find the description, put it in the cache, and set
        the configured descriptions for the article.
        """
        key = markata.make_hash(
            "long_description",
            "render",
            Path(__file__).read_text(),
            article.content,
        )

        description_from_cache = cache.get(key)
        if description_from_cache is None:
            description = get_description(article)
            markata.cache.add(key, description, expire=config["cache_expire"])
        else:
            description = description_from_cache

        for description_key in config:
            if description_key not in ["cache_expire", "config_key"]:
                if description_key not in article.metadata.keys():
                    article.metadata[description_key] = description[
                        : config[description_key]["len"]
                    ]
    ```


---

## pre_render `function`

The Markata hook that will set descriptions for all posts in the pre-render phase.

??? "pre_render source"
    ``` python
    def pre_render(markata: "Markata") -> None:
        """
        The Markata hook that will set descriptions for all posts in the pre-render phase.
        """
        config = markata.get_plugin_config(__file__)
        if "description" not in config.keys():
            config["description"] = {}
            config["description"]["len"] = 160
        with markata.cache as cache:
            for article in markata.iter_articles("setting auto description"):
                set_description(
                    markata,
                    article,
                    cache,
                    config,
                )
    ```