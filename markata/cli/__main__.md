---
article_html: "<hr />\n<h2 id=\"markatawidget-class\">MarkataWidget <code>class</code></h2>\n<p>None</p>\n<details>\n<summary>MarkataWidget
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">class</span>
  <span class=\"nc\">MarkataWidget</span><span class=\"p\">(</span><span class=\"n\">Widget</span><span
  class=\"p\">):</span>\n    <span class=\"k\">def</span> <span class=\"fm\">__init__</span><span
  class=\"p\">(</span><span class=\"bp\">self</span><span class=\"p\">,</span> <span
  class=\"n\">markata</span><span class=\"p\">:</span> <span class=\"n\">Markata</span><span
  class=\"p\">,</span> <span class=\"n\">widget</span><span class=\"p\">:</span> <span
  class=\"nb\">str</span> <span class=\"o\">=</span> <span class=\"s2\">&quot;server&quot;</span><span
  class=\"p\">):</span>\n        <span class=\"nb\">super</span><span class=\"p\">()</span><span
  class=\"o\">.</span><span class=\"fm\">__init__</span><span class=\"p\">(</span><span
  class=\"n\">widget</span><span class=\"p\">)</span>\n        <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">m</span> <span class=\"o\">=</span> <span
  class=\"n\">markata</span>\n        <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">widget</span> <span class=\"o\">=</span> <span class=\"n\">widget</span>\n
  \       <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">renderable</span>
  <span class=\"o\">=</span> <span class=\"nb\">getattr</span><span class=\"p\">(</span><span
  class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">m</span><span
  class=\"p\">,</span> <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">widget</span><span class=\"p\">)</span>\n\n    <span class=\"k\">def</span>
  <span class=\"nf\">render</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">):</span>\n        <span class=\"k\">return</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">renderable</span>\n\n    <span class=\"k\">async</span>
  <span class=\"k\">def</span> <span class=\"nf\">update</span><span class=\"p\">(</span><span
  class=\"bp\">self</span><span class=\"p\">,</span> <span class=\"n\">renderable</span><span
  class=\"p\">:</span> <span class=\"n\">RenderableType</span><span class=\"p\">)</span>
  <span class=\"o\">-&gt;</span> <span class=\"kc\">None</span><span class=\"p\">:</span>\n
  \       <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">renderable</span>
  <span class=\"o\">=</span> <span class=\"n\">renderable</span>\n        <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">refresh</span><span class=\"p\">()</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"markataapp-class\">MarkataApp <code>class</code></h2>\n<p>None</p>\n<details>\n<summary>MarkataApp
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">class</span>
  <span class=\"nc\">MarkataApp</span><span class=\"p\">(</span><span class=\"n\">App</span><span
  class=\"p\">):</span>\n    <span class=\"k\">async</span> <span class=\"k\">def</span>
  <span class=\"nf\">on_mount</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"kc\">None</span><span
  class=\"p\">:</span>\n        <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">m</span> <span class=\"o\">=</span> <span class=\"n\">Markata</span><span
  class=\"p\">()</span>\n        <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">server</span> <span class=\"o\">=</span> <span class=\"n\">MarkataWidget</span><span
  class=\"p\">(</span><span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">m</span><span class=\"p\">,</span> <span class=\"s2\">&quot;server&quot;</span><span
  class=\"p\">)</span>\n        <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">runner</span> <span class=\"o\">=</span> <span class=\"n\">MarkataWidget</span><span
  class=\"p\">(</span><span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">m</span><span class=\"p\">,</span> <span class=\"s2\">&quot;runner&quot;</span><span
  class=\"p\">)</span>\n        <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">plugins</span> <span class=\"o\">=</span> <span class=\"n\">MarkataWidget</span><span
  class=\"p\">(</span><span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">m</span><span class=\"p\">,</span> <span class=\"s2\">&quot;plugins&quot;</span><span
  class=\"p\">)</span>\n        <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">summary</span> <span class=\"o\">=</span> <span class=\"n\">MarkataWidget</span><span
  class=\"p\">(</span><span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">m</span><span class=\"p\">,</span> <span class=\"s2\">&quot;summary&quot;</span><span
  class=\"p\">)</span>\n        <span class=\"k\">await</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">view</span><span class=\"o\">.</span><span
  class=\"n\">dock</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">plugins</span><span class=\"p\">,</span> <span
  class=\"n\">edge</span><span class=\"o\">=</span><span class=\"s2\">&quot;left&quot;</span><span
  class=\"p\">,</span> <span class=\"n\">size</span><span class=\"o\">=</span><span
  class=\"mi\">30</span><span class=\"p\">,</span> <span class=\"n\">name</span><span
  class=\"o\">=</span><span class=\"s2\">&quot;plugins&quot;</span><span class=\"p\">)</span>\n
  \       <span class=\"k\">await</span> <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">view</span><span class=\"o\">.</span><span class=\"n\">dock</span><span
  class=\"p\">(</span><span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">summary</span><span class=\"p\">,</span> <span class=\"n\">edge</span><span
  class=\"o\">=</span><span class=\"s2\">&quot;right&quot;</span><span class=\"p\">,</span>
  <span class=\"n\">size</span><span class=\"o\">=</span><span class=\"mi\">30</span><span
  class=\"p\">,</span> <span class=\"n\">name</span><span class=\"o\">=</span><span
  class=\"s2\">&quot;summary&quot;</span><span class=\"p\">)</span>\n        <span
  class=\"k\">await</span> <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">view</span><span class=\"o\">.</span><span class=\"n\">dock</span><span
  class=\"p\">(</span><span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">server</span><span class=\"p\">,</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">runner</span><span class=\"p\">,</span> <span
  class=\"n\">edge</span><span class=\"o\">=</span><span class=\"s2\">&quot;top&quot;</span><span
  class=\"p\">)</span>\n        <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">set_interval</span><span class=\"p\">(</span><span class=\"mi\">1</span><span
  class=\"p\">,</span> <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">action_refresh</span><span class=\"p\">)</span>\n\n    <span class=\"k\">async</span>
  <span class=\"k\">def</span> <span class=\"nf\">on_load</span><span class=\"p\">(</span><span
  class=\"bp\">self</span><span class=\"p\">,</span> <span class=\"n\">event</span><span
  class=\"p\">):</span>\n        <span class=\"k\">await</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">bind</span><span class=\"p\">(</span><span
  class=\"s2\">&quot;q&quot;</span><span class=\"p\">,</span> <span class=\"s2\">&quot;my_quit&quot;</span><span
  class=\"p\">)</span>\n        <span class=\"k\">await</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">bind</span><span class=\"p\">(</span><span
  class=\"s2\">&quot;r&quot;</span><span class=\"p\">,</span> <span class=\"s2\">&quot;refresh&quot;</span><span
  class=\"p\">)</span>\n\n    <span class=\"k\">async</span> <span class=\"k\">def</span>
  <span class=\"nf\">action_my_quit</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"kc\">None</span><span
  class=\"p\">:</span>\n        <span class=\"k\">await</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">action_quit</span><span class=\"p\">()</span>\n\n
  \   <span class=\"k\">async</span> <span class=\"k\">def</span> <span class=\"nf\">action_refresh</span><span
  class=\"p\">(</span><span class=\"bp\">self</span><span class=\"p\">)</span> <span
  class=\"o\">-&gt;</span> <span class=\"kc\">None</span><span class=\"p\">:</span>\n
  \       <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">refresh</span><span
  class=\"p\">()</span>\n        <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">runner</span><span class=\"o\">.</span><span class=\"n\">refresh</span><span
  class=\"p\">()</span>\n        <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">server</span><span class=\"o\">.</span><span class=\"n\">refresh</span><span
  class=\"p\">()</span>\n        <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">plugins</span><span class=\"o\">.</span><span class=\"n\">refresh</span><span
  class=\"p\">()</span>\n        <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">summary</span><span class=\"o\">.</span><span class=\"n\">refresh</span><span
  class=\"p\">()</span>\n</code></pre></div>\n</details>\n<hr />\n<h2 id=\"init-method\"><strong>init</strong>
  <code>method</code></h2>\n<p>None</p>\n<details>\n<summary><strong>init</strong>
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"fm\">__init__</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">,</span> <span class=\"n\">markata</span><span class=\"p\">:</span>
  <span class=\"n\">Markata</span><span class=\"p\">,</span> <span class=\"n\">widget</span><span
  class=\"p\">:</span> <span class=\"nb\">str</span> <span class=\"o\">=</span> <span
  class=\"s2\">&quot;server&quot;</span><span class=\"p\">):</span>\n        <span
  class=\"nb\">super</span><span class=\"p\">()</span><span class=\"o\">.</span><span
  class=\"fm\">__init__</span><span class=\"p\">(</span><span class=\"n\">widget</span><span
  class=\"p\">)</span>\n        <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">m</span> <span class=\"o\">=</span> <span class=\"n\">markata</span>\n
  \       <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">widget</span>
  <span class=\"o\">=</span> <span class=\"n\">widget</span>\n        <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">renderable</span> <span class=\"o\">=</span>
  <span class=\"nb\">getattr</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">m</span><span class=\"p\">,</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">widget</span><span class=\"p\">)</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"render-method\">render <code>method</code></h2>\n<p>None</p>\n<details>\n<summary>render
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">render</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">):</span>\n        <span class=\"k\">return</span> <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">renderable</span>\n</code></pre></div>\n</details>"
datetime: null
description: Docs for __main__
long_description: ''
now: 2022-02-05 19:38:00.891461
path: __main__.md
slug: markata/cli/__main__
status: published
title: __main__.py
today: 2022-02-05
---

---

## MarkataWidget `class`

None

??? "MarkataWidget source"
    ``` python
    class MarkataWidget(Widget):
        def __init__(self, markata: Markata, widget: str = "server"):
            super().__init__(widget)
            self.m = markata
            self.widget = widget
            self.renderable = getattr(self.m, self.widget)

        def render(self):
            return self.renderable

        async def update(self, renderable: RenderableType) -> None:
            self.renderable = renderable
            self.refresh()
    ```


---

## MarkataApp `class`

None

??? "MarkataApp source"
    ``` python
    class MarkataApp(App):
        async def on_mount(self) -> None:
            self.m = Markata()
            self.server = MarkataWidget(self.m, "server")
            self.runner = MarkataWidget(self.m, "runner")
            self.plugins = MarkataWidget(self.m, "plugins")
            self.summary = MarkataWidget(self.m, "summary")
            await self.view.dock(self.plugins, edge="left", size=30, name="plugins")
            await self.view.dock(self.summary, edge="right", size=30, name="summary")
            await self.view.dock(self.server, self.runner, edge="top")
            self.set_interval(1, self.action_refresh)

        async def on_load(self, event):
            await self.bind("q", "my_quit")
            await self.bind("r", "refresh")

        async def action_my_quit(self) -> None:
            await self.action_quit()

        async def action_refresh(self) -> None:
            self.refresh()
            self.runner.refresh()
            self.server.refresh()
            self.plugins.refresh()
            self.summary.refresh()
    ```


---

## __init__ `method`

None

??? "__init__ source"
    ``` python
    def __init__(self, markata: Markata, widget: str = "server"):
            super().__init__(widget)
            self.m = markata
            self.widget = widget
            self.renderable = getattr(self.m, self.widget)
    ```


---

## render `method`

None

??? "render source"
    ``` python
    def render(self):
            return self.renderable
    ```