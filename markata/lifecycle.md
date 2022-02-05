---
article_html: "<p>The LifeCycle is a core component for the internal workings of Markata.
  \ It\nsets fourth the hooks available, the methods to run them on the Markata\ninstance,
  and the order they run in.</p>\n<h3 id=\"usage\">Usage</h3>\n<div class=\"highlight\"><pre><span></span><code><span
  class=\"kn\">from</span> <span class=\"nn\">markata</span> <span class=\"kn\">import</span>
  <span class=\"n\">Lifecycle</span>\n\n<span class=\"n\">step</span> <span class=\"o\">=</span>
  <span class=\"n\">Lifecycle</span><span class=\"o\">.</span><span class=\"n\">glob</span>\n</code></pre></div>\n<hr
  />\n<h2 id=\"lifecycle-class\">LifeCycle <code>class</code></h2>\n<p>LifeCycle currently
  supports the following steps.</p>\n<ul>\n<li>configure - load and fix configuration</li>\n<li>glob
  - find files</li>\n<li>load - load files</li>\n<li>pre_render - clean up files/metadata
  before render</li>\n<li>render - render content</li>\n<li>post_render - clean up
  rendered content</li>\n<li>save - store results to disk</li>\n</ul>\n<details>\n<summary>LifeCycle
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">class</span>
  <span class=\"nc\">LifeCycle</span><span class=\"p\">(</span><span class=\"n\">Enum</span><span
  class=\"p\">):</span>\n    <span class=\"sd\">&quot;&quot;&quot;</span>\n<span class=\"sd\">
  \   LifeCycle currently supports the following steps.</span>\n\n<span class=\"sd\">
  \   * configure - load and fix configuration</span>\n<span class=\"sd\">    * glob
  - find files</span>\n<span class=\"sd\">    * load - load files</span>\n<span class=\"sd\">
  \   * pre_render - clean up files/metadata before render</span>\n<span class=\"sd\">
  \   * render - render content</span>\n<span class=\"sd\">    * post_render - clean
  up rendered content</span>\n<span class=\"sd\">    * save - store results to disk</span>\n\n<span
  class=\"sd\">    &quot;&quot;&quot;</span>\n\n    <span class=\"n\">configure</span>
  <span class=\"o\">=</span> <span class=\"n\">auto</span><span class=\"p\">()</span>\n
  \   <span class=\"n\">glob</span> <span class=\"o\">=</span> <span class=\"n\">auto</span><span
  class=\"p\">()</span>\n    <span class=\"n\">load</span> <span class=\"o\">=</span>
  <span class=\"n\">auto</span><span class=\"p\">()</span>\n    <span class=\"n\">pre_render</span>
  <span class=\"o\">=</span> <span class=\"n\">auto</span><span class=\"p\">()</span>\n
  \   <span class=\"n\">render</span> <span class=\"o\">=</span> <span class=\"n\">auto</span><span
  class=\"p\">()</span>\n    <span class=\"n\">post_render</span> <span class=\"o\">=</span>
  <span class=\"n\">auto</span><span class=\"p\">()</span>\n    <span class=\"n\">save</span>
  <span class=\"o\">=</span> <span class=\"n\">auto</span><span class=\"p\">()</span>\n\n
  \   <span class=\"k\">def</span> <span class=\"fm\">__lt__</span><span class=\"p\">(</span><span
  class=\"bp\">self</span><span class=\"p\">,</span> <span class=\"n\">other</span><span
  class=\"p\">:</span> <span class=\"nb\">object</span><span class=\"p\">)</span>
  <span class=\"o\">-&gt;</span> <span class=\"nb\">bool</span><span class=\"p\">:</span>\n
  \       <span class=\"sd\">&quot;&quot;&quot;</span>\n<span class=\"sd\">        Determine
  whether other is less than this instance.</span>\n<span class=\"sd\">        &quot;&quot;&quot;</span>\n
  \       <span class=\"k\">if</span> <span class=\"nb\">isinstance</span><span class=\"p\">(</span><span
  class=\"n\">other</span><span class=\"p\">,</span> <span class=\"n\">LifeCycle</span><span
  class=\"p\">):</span>\n            <span class=\"k\">return</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">value</span> <span class=\"o\">&lt;</span>
  <span class=\"n\">other</span><span class=\"o\">.</span><span class=\"n\">value</span>\n
  \       <span class=\"k\">if</span> <span class=\"nb\">isinstance</span><span class=\"p\">(</span><span
  class=\"n\">other</span><span class=\"p\">,</span> <span class=\"nb\">int</span><span
  class=\"p\">):</span>\n            <span class=\"k\">return</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">value</span> <span class=\"o\">&lt;</span>
  <span class=\"n\">other</span>\n        <span class=\"k\">return</span> <span class=\"bp\">NotImplemented</span>\n\n
  \   <span class=\"k\">def</span> <span class=\"fm\">__eq__</span><span class=\"p\">(</span><span
  class=\"bp\">self</span><span class=\"p\">,</span> <span class=\"n\">other</span><span
  class=\"p\">:</span> <span class=\"nb\">object</span><span class=\"p\">)</span>
  <span class=\"o\">-&gt;</span> <span class=\"nb\">bool</span><span class=\"p\">:</span>\n
  \       <span class=\"sd\">&quot;&quot;&quot;</span>\n<span class=\"sd\">        Determine
  whether other is equal to this instance.</span>\n<span class=\"sd\">        &quot;&quot;&quot;</span>\n
  \       <span class=\"k\">if</span> <span class=\"nb\">isinstance</span><span class=\"p\">(</span><span
  class=\"n\">other</span><span class=\"p\">,</span> <span class=\"n\">LifeCycle</span><span
  class=\"p\">):</span>\n            <span class=\"k\">return</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">value</span> <span class=\"o\">==</span> <span
  class=\"n\">other</span><span class=\"o\">.</span><span class=\"n\">value</span>\n
  \       <span class=\"k\">if</span> <span class=\"nb\">isinstance</span><span class=\"p\">(</span><span
  class=\"n\">other</span><span class=\"p\">,</span> <span class=\"nb\">int</span><span
  class=\"p\">):</span>\n            <span class=\"k\">return</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">value</span> <span class=\"o\">==</span> <span
  class=\"n\">other</span>\n        <span class=\"k\">return</span> <span class=\"bp\">NotImplemented</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"lt-method\"><strong>lt</strong> <code>method</code></h2>\n<p>Determine
  whether other is less than this instance.</p>\n<details>\n<summary><strong>lt</strong>
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"fm\">__lt__</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">,</span> <span class=\"n\">other</span><span class=\"p\">:</span> <span
  class=\"nb\">object</span><span class=\"p\">)</span> <span class=\"o\">-&gt;</span>
  <span class=\"nb\">bool</span><span class=\"p\">:</span>\n        <span class=\"sd\">&quot;&quot;&quot;</span>\n<span
  class=\"sd\">        Determine whether other is less than this instance.</span>\n<span
  class=\"sd\">        &quot;&quot;&quot;</span>\n        <span class=\"k\">if</span>
  <span class=\"nb\">isinstance</span><span class=\"p\">(</span><span class=\"n\">other</span><span
  class=\"p\">,</span> <span class=\"n\">LifeCycle</span><span class=\"p\">):</span>\n
  \           <span class=\"k\">return</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">value</span> <span class=\"o\">&lt;</span>
  <span class=\"n\">other</span><span class=\"o\">.</span><span class=\"n\">value</span>\n
  \       <span class=\"k\">if</span> <span class=\"nb\">isinstance</span><span class=\"p\">(</span><span
  class=\"n\">other</span><span class=\"p\">,</span> <span class=\"nb\">int</span><span
  class=\"p\">):</span>\n            <span class=\"k\">return</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">value</span> <span class=\"o\">&lt;</span>
  <span class=\"n\">other</span>\n        <span class=\"k\">return</span> <span class=\"bp\">NotImplemented</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"eq-method\"><strong>eq</strong> <code>method</code></h2>\n<p>Determine
  whether other is equal to this instance.</p>\n<details>\n<summary><strong>eq</strong>
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"fm\">__eq__</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">,</span> <span class=\"n\">other</span><span class=\"p\">:</span> <span
  class=\"nb\">object</span><span class=\"p\">)</span> <span class=\"o\">-&gt;</span>
  <span class=\"nb\">bool</span><span class=\"p\">:</span>\n        <span class=\"sd\">&quot;&quot;&quot;</span>\n<span
  class=\"sd\">        Determine whether other is equal to this instance.</span>\n<span
  class=\"sd\">        &quot;&quot;&quot;</span>\n        <span class=\"k\">if</span>
  <span class=\"nb\">isinstance</span><span class=\"p\">(</span><span class=\"n\">other</span><span
  class=\"p\">,</span> <span class=\"n\">LifeCycle</span><span class=\"p\">):</span>\n
  \           <span class=\"k\">return</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">value</span> <span class=\"o\">==</span> <span
  class=\"n\">other</span><span class=\"o\">.</span><span class=\"n\">value</span>\n
  \       <span class=\"k\">if</span> <span class=\"nb\">isinstance</span><span class=\"p\">(</span><span
  class=\"n\">other</span><span class=\"p\">,</span> <span class=\"nb\">int</span><span
  class=\"p\">):</span>\n            <span class=\"k\">return</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">value</span> <span class=\"o\">==</span> <span
  class=\"n\">other</span>\n        <span class=\"k\">return</span> <span class=\"bp\">NotImplemented</span>\n</code></pre></div>\n</details>"
datetime: null
description: Docs for lifecycle
long_description: ''
now: 2022-02-05 19:38:00.891363
path: lifecycle.md
slug: markata/lifecycle
status: published
title: lifecycle.py
today: 2022-02-05
---

The LifeCycle is a core component for the internal workings of Markata.  It
sets fourth the hooks available, the methods to run them on the Markata
instance, and the order they run in.

### Usage

``` python
from markata import Lifecycle

step = Lifecycle.glob
```


---

## LifeCycle `class`

LifeCycle currently supports the following steps.

* configure - load and fix configuration
* glob - find files
* load - load files
* pre_render - clean up files/metadata before render
* render - render content
* post_render - clean up rendered content
* save - store results to disk

??? "LifeCycle source"
    ``` python
    class LifeCycle(Enum):
        """
        LifeCycle currently supports the following steps.

        * configure - load and fix configuration
        * glob - find files
        * load - load files
        * pre_render - clean up files/metadata before render
        * render - render content
        * post_render - clean up rendered content
        * save - store results to disk

        """

        configure = auto()
        glob = auto()
        load = auto()
        pre_render = auto()
        render = auto()
        post_render = auto()
        save = auto()

        def __lt__(self, other: object) -> bool:
            """
            Determine whether other is less than this instance.
            """
            if isinstance(other, LifeCycle):
                return self.value < other.value
            if isinstance(other, int):
                return self.value < other
            return NotImplemented

        def __eq__(self, other: object) -> bool:
            """
            Determine whether other is equal to this instance.
            """
            if isinstance(other, LifeCycle):
                return self.value == other.value
            if isinstance(other, int):
                return self.value == other
            return NotImplemented
    ```


---

## __lt__ `method`

Determine whether other is less than this instance.

??? "__lt__ source"
    ``` python
    def __lt__(self, other: object) -> bool:
            """
            Determine whether other is less than this instance.
            """
            if isinstance(other, LifeCycle):
                return self.value < other.value
            if isinstance(other, int):
                return self.value < other
            return NotImplemented
    ```


---

## __eq__ `method`

Determine whether other is equal to this instance.

??? "__eq__ source"
    ``` python
    def __eq__(self, other: object) -> bool:
            """
            Determine whether other is equal to this instance.
            """
            if isinstance(other, LifeCycle):
                return self.value == other.value
            if isinstance(other, int):
                return self.value == other
            return NotImplemented
    ```