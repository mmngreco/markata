---
article_html: "<hr />\n<h2 id=\"plugins-class\">Plugins <code>class</code></h2>\n<p>None</p>\n<details>\n<summary>Plugins
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">class</span>
  <span class=\"nc\">Plugins</span><span class=\"p\">:</span>\n    <span class=\"k\">def</span>
  <span class=\"fm\">__init__</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">,</span> <span class=\"n\">markata</span><span class=\"p\">:</span>
  <span class=\"s2\">&quot;Markata&quot;</span><span class=\"p\">):</span>\n        <span
  class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">m</span> <span
  class=\"o\">=</span> <span class=\"n\">markata</span>\n\n    <span class=\"k\">def</span>
  <span class=\"nf\">__rich__</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"n\">Panel</span><span
  class=\"p\">:</span>\n        <span class=\"n\">grid</span> <span class=\"o\">=</span>
  <span class=\"n\">Table</span><span class=\"o\">.</span><span class=\"n\">grid</span><span
  class=\"p\">(</span><span class=\"n\">expand</span><span class=\"o\">=</span><span
  class=\"kc\">True</span><span class=\"p\">)</span>\n        <span class=\"n\">grid</span><span
  class=\"o\">.</span><span class=\"n\">add_row</span><span class=\"p\">(</span><span
  class=\"sa\">f</span><span class=\"s2\">&quot;[bright_blue]</span><span class=\"si\">{</span><span
  class=\"nb\">len</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">m</span><span class=\"o\">.</span><span class=\"n\">_pm</span><span
  class=\"o\">.</span><span class=\"n\">get_plugins</span><span class=\"p\">())</span><span
  class=\"si\">}</span><span class=\"s2\">[/] plugins&quot;</span><span class=\"p\">)</span>\n
  \       <span class=\"k\">for</span> <span class=\"n\">plugin</span> <span class=\"ow\">in</span>
  <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">m</span><span
  class=\"o\">.</span><span class=\"n\">_pm</span><span class=\"o\">.</span><span
  class=\"n\">get_plugins</span><span class=\"p\">():</span>\n            <span class=\"n\">grid</span><span
  class=\"o\">.</span><span class=\"n\">add_row</span><span class=\"p\">(</span>\n
  \               <span class=\"s2\">&quot;&quot;</span><span class=\"o\">.</span><span
  class=\"n\">join</span><span class=\"p\">(</span>\n                    <span class=\"p\">[</span>\n
  \                       <span class=\"s2\">&quot;[bright_black]&quot;</span><span
  class=\"p\">,</span>\n                        <span class=\"s2\">&quot;.&quot;</span><span
  class=\"o\">.</span><span class=\"n\">join</span><span class=\"p\">(</span><span
  class=\"n\">plugin</span><span class=\"o\">.</span><span class=\"vm\">__name__</span><span
  class=\"o\">.</span><span class=\"n\">split</span><span class=\"p\">(</span><span
  class=\"s2\">&quot;.&quot;</span><span class=\"p\">)[:</span><span class=\"o\">-</span><span
  class=\"mi\">1</span><span class=\"p\">]),</span>\n                        <span
  class=\"s2\">&quot;.[/]&quot;</span><span class=\"p\">,</span>\n                        <span
  class=\"n\">plugin</span><span class=\"o\">.</span><span class=\"vm\">__name__</span><span
  class=\"o\">.</span><span class=\"n\">split</span><span class=\"p\">(</span><span
  class=\"s2\">&quot;.&quot;</span><span class=\"p\">)[</span><span class=\"o\">-</span><span
  class=\"mi\">1</span><span class=\"p\">],</span>\n                    <span class=\"p\">]</span>\n
  \               <span class=\"p\">)</span>\n            <span class=\"p\">)</span>\n
  \       <span class=\"k\">return</span> <span class=\"n\">Panel</span><span class=\"p\">(</span><span
  class=\"n\">grid</span><span class=\"p\">,</span> <span class=\"n\">title</span><span
  class=\"o\">=</span><span class=\"s2\">&quot;plugins&quot;</span><span class=\"p\">,</span>
  <span class=\"n\">border_style</span><span class=\"o\">=</span><span class=\"s2\">&quot;gold1&quot;</span><span
  class=\"p\">)</span>\n</code></pre></div>\n</details>\n<hr />\n<h2 id=\"init-method\"><strong>init</strong>
  <code>method</code></h2>\n<p>None</p>\n<details>\n<summary><strong>init</strong>
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"fm\">__init__</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">,</span> <span class=\"n\">markata</span><span class=\"p\">:</span>
  <span class=\"s2\">&quot;Markata&quot;</span><span class=\"p\">):</span>\n        <span
  class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">m</span> <span
  class=\"o\">=</span> <span class=\"n\">markata</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"rich-method\"><strong>rich</strong> <code>method</code></h2>\n<p>None</p>\n<details>\n<summary><strong>rich</strong>
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">__rich__</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"n\">Panel</span><span
  class=\"p\">:</span>\n        <span class=\"n\">grid</span> <span class=\"o\">=</span>
  <span class=\"n\">Table</span><span class=\"o\">.</span><span class=\"n\">grid</span><span
  class=\"p\">(</span><span class=\"n\">expand</span><span class=\"o\">=</span><span
  class=\"kc\">True</span><span class=\"p\">)</span>\n        <span class=\"n\">grid</span><span
  class=\"o\">.</span><span class=\"n\">add_row</span><span class=\"p\">(</span><span
  class=\"sa\">f</span><span class=\"s2\">&quot;[bright_blue]</span><span class=\"si\">{</span><span
  class=\"nb\">len</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">m</span><span class=\"o\">.</span><span class=\"n\">_pm</span><span
  class=\"o\">.</span><span class=\"n\">get_plugins</span><span class=\"p\">())</span><span
  class=\"si\">}</span><span class=\"s2\">[/] plugins&quot;</span><span class=\"p\">)</span>\n
  \       <span class=\"k\">for</span> <span class=\"n\">plugin</span> <span class=\"ow\">in</span>
  <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">m</span><span
  class=\"o\">.</span><span class=\"n\">_pm</span><span class=\"o\">.</span><span
  class=\"n\">get_plugins</span><span class=\"p\">():</span>\n            <span class=\"n\">grid</span><span
  class=\"o\">.</span><span class=\"n\">add_row</span><span class=\"p\">(</span>\n
  \               <span class=\"s2\">&quot;&quot;</span><span class=\"o\">.</span><span
  class=\"n\">join</span><span class=\"p\">(</span>\n                    <span class=\"p\">[</span>\n
  \                       <span class=\"s2\">&quot;[bright_black]&quot;</span><span
  class=\"p\">,</span>\n                        <span class=\"s2\">&quot;.&quot;</span><span
  class=\"o\">.</span><span class=\"n\">join</span><span class=\"p\">(</span><span
  class=\"n\">plugin</span><span class=\"o\">.</span><span class=\"vm\">__name__</span><span
  class=\"o\">.</span><span class=\"n\">split</span><span class=\"p\">(</span><span
  class=\"s2\">&quot;.&quot;</span><span class=\"p\">)[:</span><span class=\"o\">-</span><span
  class=\"mi\">1</span><span class=\"p\">]),</span>\n                        <span
  class=\"s2\">&quot;.[/]&quot;</span><span class=\"p\">,</span>\n                        <span
  class=\"n\">plugin</span><span class=\"o\">.</span><span class=\"vm\">__name__</span><span
  class=\"o\">.</span><span class=\"n\">split</span><span class=\"p\">(</span><span
  class=\"s2\">&quot;.&quot;</span><span class=\"p\">)[</span><span class=\"o\">-</span><span
  class=\"mi\">1</span><span class=\"p\">],</span>\n                    <span class=\"p\">]</span>\n
  \               <span class=\"p\">)</span>\n            <span class=\"p\">)</span>\n
  \       <span class=\"k\">return</span> <span class=\"n\">Panel</span><span class=\"p\">(</span><span
  class=\"n\">grid</span><span class=\"p\">,</span> <span class=\"n\">title</span><span
  class=\"o\">=</span><span class=\"s2\">&quot;plugins&quot;</span><span class=\"p\">,</span>
  <span class=\"n\">border_style</span><span class=\"o\">=</span><span class=\"s2\">&quot;gold1&quot;</span><span
  class=\"p\">)</span>\n</code></pre></div>\n</details>"
datetime: null
description: Docs for plugins
long_description: ''
now: 2022-02-05 19:38:00.891453
path: plugins.md
slug: markata/cli/plugins
status: published
title: plugins.py
today: 2022-02-05
---

---

## Plugins `class`

None

??? "Plugins source"
    ``` python
    class Plugins:
        def __init__(self, markata: "Markata"):
            self.m = markata

        def __rich__(self) -> Panel:
            grid = Table.grid(expand=True)
            grid.add_row(f"[bright_blue]{len(self.m._pm.get_plugins())}[/] plugins")
            for plugin in self.m._pm.get_plugins():
                grid.add_row(
                    "".join(
                        [
                            "[bright_black]",
                            ".".join(plugin.__name__.split(".")[:-1]),
                            ".[/]",
                            plugin.__name__.split(".")[-1],
                        ]
                    )
                )
            return Panel(grid, title="plugins", border_style="gold1")
    ```


---

## __init__ `method`

None

??? "__init__ source"
    ``` python
    def __init__(self, markata: "Markata"):
            self.m = markata
    ```


---

## __rich__ `method`

None

??? "__rich__ source"
    ``` python
    def __rich__(self) -> Panel:
            grid = Table.grid(expand=True)
            grid.add_row(f"[bright_blue]{len(self.m._pm.get_plugins())}[/] plugins")
            for plugin in self.m._pm.get_plugins():
                grid.add_row(
                    "".join(
                        [
                            "[bright_black]",
                            ".".join(plugin.__name__.split(".")[:-1]),
                            ".[/]",
                            plugin.__name__.split(".")[-1],
                        ]
                    )
                )
            return Panel(grid, title="plugins", border_style="gold1")
    ```