---
article_html: "<p>Define hook specs.</p>\n<hr />\n<h2 id=\"markataspecs-class\">MarkataSpecs
  <code>class</code></h2>\n<p>Namespace that defines all specifications for Load hooks.</p>\n<p>configure
  -&gt; glob -&gt; load -&gt; render -&gt; save</p>\n<details>\n<summary>MarkataSpecs
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">class</span>
  <span class=\"nc\">MarkataSpecs</span><span class=\"p\">:</span>\n    <span class=\"sd\">&quot;&quot;&quot;</span>\n<span
  class=\"sd\">    Namespace that defines all specifications for Load hooks.</span>\n\n<span
  class=\"sd\">    configure -&gt; glob -&gt; load -&gt; render -&gt; save</span>\n<span
  class=\"sd\">    &quot;&quot;&quot;</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"generic_lifecycle_method-function\">generic_lifecycle_method <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>generic_lifecycle_method
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">generic_lifecycle_method</span><span class=\"p\">(</span>\n    <span
  class=\"n\">markata</span><span class=\"p\">:</span> <span class=\"s2\">&quot;Markata&quot;</span><span
  class=\"p\">,</span>\n<span class=\"p\">)</span> <span class=\"o\">-&gt;</span>
  <span class=\"n\">Any</span><span class=\"p\">:</span>\n    <span class=\"o\">...</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"cli_lifecycle_method-function\">cli_lifecycle_method <code>function</code></h2>\n<p>A
  Markata lifecycle methos that includes a typer app used for cli's</p>\n<details>\n<summary>cli_lifecycle_method
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">cli_lifecycle_method</span><span class=\"p\">(</span><span class=\"n\">markata</span><span
  class=\"p\">:</span> <span class=\"s2\">&quot;Markata&quot;</span><span class=\"p\">,</span>
  <span class=\"n\">app</span><span class=\"p\">:</span> <span class=\"s2\">&quot;typer.Typer&quot;</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"n\">Any</span><span
  class=\"p\">:</span>\n    <span class=\"s2\">&quot;A Markata lifecycle methos that
  includes a typer app used for cli&#39;s&quot;</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"register_attr-function\">register_attr <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>register_attr
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">register_attr</span><span class=\"p\">(</span><span class=\"o\">*</span><span
  class=\"n\">attrs</span><span class=\"p\">:</span> <span class=\"n\">Any</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"n\">Callable</span><span
  class=\"p\">:</span>\n    <span class=\"k\">def</span> <span class=\"nf\">decorator_register</span><span
  class=\"p\">(</span>\n        <span class=\"n\">func</span><span class=\"p\">:</span>
  <span class=\"n\">Callable</span><span class=\"p\">,</span>\n    <span class=\"p\">)</span>
  <span class=\"o\">-&gt;</span> <span class=\"n\">Callable</span><span class=\"p\">:</span>\n\n
  \       <span class=\"k\">for</span> <span class=\"n\">attr</span> <span class=\"ow\">in</span>
  <span class=\"n\">attrs</span><span class=\"p\">:</span>\n            <span class=\"k\">if</span>
  <span class=\"n\">attr</span> <span class=\"ow\">not</span> <span class=\"ow\">in</span>
  <span class=\"n\">registered_attrs</span><span class=\"p\">:</span>\n                <span
  class=\"n\">registered_attrs</span><span class=\"p\">[</span><span class=\"n\">attr</span><span
  class=\"p\">]</span> <span class=\"o\">=</span> <span class=\"p\">[]</span>\n            <span
  class=\"n\">registered_attrs</span><span class=\"p\">[</span><span class=\"n\">attr</span><span
  class=\"p\">]</span><span class=\"o\">.</span><span class=\"n\">append</span><span
  class=\"p\">(</span>\n                <span class=\"p\">{</span>\n                    <span
  class=\"s2\">&quot;func&quot;</span><span class=\"p\">:</span> <span class=\"n\">func</span><span
  class=\"p\">,</span>\n                    <span class=\"s2\">&quot;funcname&quot;</span><span
  class=\"p\">:</span> <span class=\"n\">func</span><span class=\"o\">.</span><span
  class=\"vm\">__code__</span><span class=\"o\">.</span><span class=\"n\">co_name</span><span
  class=\"p\">,</span>\n                    <span class=\"s2\">&quot;lifecycle&quot;</span><span
  class=\"p\">:</span> <span class=\"nb\">getattr</span><span class=\"p\">(</span><span
  class=\"n\">LifeCycle</span><span class=\"p\">,</span> <span class=\"n\">func</span><span
  class=\"o\">.</span><span class=\"vm\">__code__</span><span class=\"o\">.</span><span
  class=\"n\">co_name</span><span class=\"p\">),</span>\n                <span class=\"p\">}</span>\n
  \           <span class=\"p\">)</span>\n\n        <span class=\"nd\">@functools</span><span
  class=\"o\">.</span><span class=\"n\">wraps</span><span class=\"p\">(</span><span
  class=\"n\">func</span><span class=\"p\">)</span>\n        <span class=\"k\">def</span>
  <span class=\"nf\">wrapper_register</span><span class=\"p\">(</span><span class=\"n\">markata</span><span
  class=\"p\">:</span> <span class=\"s2\">&quot;Markata&quot;</span><span class=\"p\">,</span>
  <span class=\"o\">*</span><span class=\"n\">args</span><span class=\"p\">:</span>
  <span class=\"n\">Any</span><span class=\"p\">,</span> <span class=\"o\">**</span><span
  class=\"n\">kwargs</span><span class=\"p\">:</span> <span class=\"n\">Any</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"n\">Any</span><span
  class=\"p\">:</span>\n            <span class=\"k\">return</span> <span class=\"n\">func</span><span
  class=\"p\">(</span><span class=\"n\">markata</span><span class=\"p\">,</span> <span
  class=\"o\">*</span><span class=\"n\">args</span><span class=\"p\">,</span> <span
  class=\"o\">**</span><span class=\"n\">kwargs</span><span class=\"p\">)</span>\n\n
  \       <span class=\"k\">return</span> <span class=\"n\">wrapper_register</span>\n\n
  \   <span class=\"k\">return</span> <span class=\"n\">decorator_register</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"decorator_register-function\">decorator_register <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>decorator_register
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">decorator_register</span><span class=\"p\">(</span>\n        <span
  class=\"n\">func</span><span class=\"p\">:</span> <span class=\"n\">Callable</span><span
  class=\"p\">,</span>\n    <span class=\"p\">)</span> <span class=\"o\">-&gt;</span>
  <span class=\"n\">Callable</span><span class=\"p\">:</span>\n\n        <span class=\"k\">for</span>
  <span class=\"n\">attr</span> <span class=\"ow\">in</span> <span class=\"n\">attrs</span><span
  class=\"p\">:</span>\n            <span class=\"k\">if</span> <span class=\"n\">attr</span>
  <span class=\"ow\">not</span> <span class=\"ow\">in</span> <span class=\"n\">registered_attrs</span><span
  class=\"p\">:</span>\n                <span class=\"n\">registered_attrs</span><span
  class=\"p\">[</span><span class=\"n\">attr</span><span class=\"p\">]</span> <span
  class=\"o\">=</span> <span class=\"p\">[]</span>\n            <span class=\"n\">registered_attrs</span><span
  class=\"p\">[</span><span class=\"n\">attr</span><span class=\"p\">]</span><span
  class=\"o\">.</span><span class=\"n\">append</span><span class=\"p\">(</span>\n
  \               <span class=\"p\">{</span>\n                    <span class=\"s2\">&quot;func&quot;</span><span
  class=\"p\">:</span> <span class=\"n\">func</span><span class=\"p\">,</span>\n                    <span
  class=\"s2\">&quot;funcname&quot;</span><span class=\"p\">:</span> <span class=\"n\">func</span><span
  class=\"o\">.</span><span class=\"vm\">__code__</span><span class=\"o\">.</span><span
  class=\"n\">co_name</span><span class=\"p\">,</span>\n                    <span
  class=\"s2\">&quot;lifecycle&quot;</span><span class=\"p\">:</span> <span class=\"nb\">getattr</span><span
  class=\"p\">(</span><span class=\"n\">LifeCycle</span><span class=\"p\">,</span>
  <span class=\"n\">func</span><span class=\"o\">.</span><span class=\"vm\">__code__</span><span
  class=\"o\">.</span><span class=\"n\">co_name</span><span class=\"p\">),</span>\n
  \               <span class=\"p\">}</span>\n            <span class=\"p\">)</span>\n\n
  \       <span class=\"nd\">@functools</span><span class=\"o\">.</span><span class=\"n\">wraps</span><span
  class=\"p\">(</span><span class=\"n\">func</span><span class=\"p\">)</span>\n        <span
  class=\"k\">def</span> <span class=\"nf\">wrapper_register</span><span class=\"p\">(</span><span
  class=\"n\">markata</span><span class=\"p\">:</span> <span class=\"s2\">&quot;Markata&quot;</span><span
  class=\"p\">,</span> <span class=\"o\">*</span><span class=\"n\">args</span><span
  class=\"p\">:</span> <span class=\"n\">Any</span><span class=\"p\">,</span> <span
  class=\"o\">**</span><span class=\"n\">kwargs</span><span class=\"p\">:</span> <span
  class=\"n\">Any</span><span class=\"p\">)</span> <span class=\"o\">-&gt;</span>
  <span class=\"n\">Any</span><span class=\"p\">:</span>\n            <span class=\"k\">return</span>
  <span class=\"n\">func</span><span class=\"p\">(</span><span class=\"n\">markata</span><span
  class=\"p\">,</span> <span class=\"o\">*</span><span class=\"n\">args</span><span
  class=\"p\">,</span> <span class=\"o\">**</span><span class=\"n\">kwargs</span><span
  class=\"p\">)</span>\n\n        <span class=\"k\">return</span> <span class=\"n\">wrapper_register</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"wrapper_register-function\">wrapper_register <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>wrapper_register
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">wrapper_register</span><span class=\"p\">(</span><span class=\"n\">markata</span><span
  class=\"p\">:</span> <span class=\"s2\">&quot;Markata&quot;</span><span class=\"p\">,</span>
  <span class=\"o\">*</span><span class=\"n\">args</span><span class=\"p\">:</span>
  <span class=\"n\">Any</span><span class=\"p\">,</span> <span class=\"o\">**</span><span
  class=\"n\">kwargs</span><span class=\"p\">:</span> <span class=\"n\">Any</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"n\">Any</span><span
  class=\"p\">:</span>\n            <span class=\"k\">return</span> <span class=\"n\">func</span><span
  class=\"p\">(</span><span class=\"n\">markata</span><span class=\"p\">,</span> <span
  class=\"o\">*</span><span class=\"n\">args</span><span class=\"p\">,</span> <span
  class=\"o\">**</span><span class=\"n\">kwargs</span><span class=\"p\">)</span>\n</code></pre></div>\n</details>"
datetime: null
description: Docs for hookspec
long_description: ''
now: 2022-02-05 19:38:00.891360
path: hookspec.md
slug: markata/hookspec
status: published
title: hookspec.py
today: 2022-02-05
---

Define hook specs.


---

## MarkataSpecs `class`

Namespace that defines all specifications for Load hooks.

configure -> glob -> load -> render -> save

??? "MarkataSpecs source"
    ``` python
    class MarkataSpecs:
        """
        Namespace that defines all specifications for Load hooks.

        configure -> glob -> load -> render -> save
        """
    ```


---

## generic_lifecycle_method `function`

None

??? "generic_lifecycle_method source"
    ``` python
    def generic_lifecycle_method(
        markata: "Markata",
    ) -> Any:
        ...
    ```


---

## cli_lifecycle_method `function`

A Markata lifecycle methos that includes a typer app used for cli's

??? "cli_lifecycle_method source"
    ``` python
    def cli_lifecycle_method(markata: "Markata", app: "typer.Typer") -> Any:
        "A Markata lifecycle methos that includes a typer app used for cli's"
    ```


---

## register_attr `function`

None

??? "register_attr source"
    ``` python
    def register_attr(*attrs: Any) -> Callable:
        def decorator_register(
            func: Callable,
        ) -> Callable:

            for attr in attrs:
                if attr not in registered_attrs:
                    registered_attrs[attr] = []
                registered_attrs[attr].append(
                    {
                        "func": func,
                        "funcname": func.__code__.co_name,
                        "lifecycle": getattr(LifeCycle, func.__code__.co_name),
                    }
                )

            @functools.wraps(func)
            def wrapper_register(markata: "Markata", *args: Any, **kwargs: Any) -> Any:
                return func(markata, *args, **kwargs)

            return wrapper_register

        return decorator_register
    ```


---

## decorator_register `function`

None

??? "decorator_register source"
    ``` python
    def decorator_register(
            func: Callable,
        ) -> Callable:

            for attr in attrs:
                if attr not in registered_attrs:
                    registered_attrs[attr] = []
                registered_attrs[attr].append(
                    {
                        "func": func,
                        "funcname": func.__code__.co_name,
                        "lifecycle": getattr(LifeCycle, func.__code__.co_name),
                    }
                )

            @functools.wraps(func)
            def wrapper_register(markata: "Markata", *args: Any, **kwargs: Any) -> Any:
                return func(markata, *args, **kwargs)

            return wrapper_register
    ```


---

## wrapper_register `function`

None

??? "wrapper_register source"
    ``` python
    def wrapper_register(markata: "Markata", *args: Any, **kwargs: Any) -> Any:
                return func(markata, *args, **kwargs)
    ```