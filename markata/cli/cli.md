---
article_html: "<hr />\n<h2 id=\"make_layout-function\">make_layout <code>function</code></h2>\n<p>Define
  the layout.</p>\n<details>\n<summary>make_layout source</summary>\n<div class=\"highlight\"><pre><span></span><code><span
  class=\"k\">def</span> <span class=\"nf\">make_layout</span><span class=\"p\">()</span>
  <span class=\"o\">-&gt;</span> <span class=\"n\">Layout</span><span class=\"p\">:</span>\n
  \   <span class=\"sd\">&quot;&quot;&quot;Define the layout.&quot;&quot;&quot;</span>\n
  \   <span class=\"n\">layout</span> <span class=\"o\">=</span> <span class=\"n\">Layout</span><span
  class=\"p\">(</span><span class=\"n\">name</span><span class=\"o\">=</span><span
  class=\"s2\">&quot;root&quot;</span><span class=\"p\">)</span>\n\n    <span class=\"n\">layout</span><span
  class=\"o\">.</span><span class=\"n\">split</span><span class=\"p\">(</span>\n        <span
  class=\"n\">Layout</span><span class=\"p\">(</span><span class=\"n\">name</span><span
  class=\"o\">=</span><span class=\"s2\">&quot;header&quot;</span><span class=\"p\">,</span>
  <span class=\"n\">size</span><span class=\"o\">=</span><span class=\"mi\">3</span><span
  class=\"p\">),</span>\n        <span class=\"n\">Layout</span><span class=\"p\">(</span><span
  class=\"n\">name</span><span class=\"o\">=</span><span class=\"s2\">&quot;main&quot;</span><span
  class=\"p\">),</span>\n    <span class=\"p\">)</span>\n    <span class=\"n\">layout</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;main&quot;</span><span class=\"p\">]</span><span
  class=\"o\">.</span><span class=\"n\">split_row</span><span class=\"p\">(</span>\n
  \       <span class=\"n\">Layout</span><span class=\"p\">(</span><span class=\"n\">name</span><span
  class=\"o\">=</span><span class=\"s2\">&quot;side&quot;</span><span class=\"p\">,</span>
  <span class=\"n\">ratio</span><span class=\"o\">=</span><span class=\"mi\">50</span><span
  class=\"p\">),</span>\n        <span class=\"n\">Layout</span><span class=\"p\">(</span><span
  class=\"n\">name</span><span class=\"o\">=</span><span class=\"s2\">&quot;mid&quot;</span><span
  class=\"p\">,</span> <span class=\"n\">ratio</span><span class=\"o\">=</span><span
  class=\"mi\">30</span><span class=\"p\">),</span>\n        <span class=\"n\">Layout</span><span
  class=\"p\">(</span><span class=\"n\">name</span><span class=\"o\">=</span><span
  class=\"s2\">&quot;describe&quot;</span><span class=\"p\">,</span> <span class=\"n\">ratio</span><span
  class=\"o\">=</span><span class=\"mi\">20</span><span class=\"p\">),</span>\n    <span
  class=\"p\">)</span>\n    <span class=\"n\">layout</span><span class=\"p\">[</span><span
  class=\"s2\">&quot;mid&quot;</span><span class=\"p\">]</span><span class=\"o\">.</span><span
  class=\"n\">split</span><span class=\"p\">(</span>\n        <span class=\"n\">Layout</span><span
  class=\"p\">(</span><span class=\"n\">name</span><span class=\"o\">=</span><span
  class=\"s2\">&quot;server&quot;</span><span class=\"p\">),</span>\n        <span
  class=\"n\">Layout</span><span class=\"p\">(</span><span class=\"n\">name</span><span
  class=\"o\">=</span><span class=\"s2\">&quot;runner&quot;</span><span class=\"p\">),</span>\n
  \   <span class=\"p\">)</span>\n    <span class=\"n\">layout</span><span class=\"p\">[</span><span
  class=\"s2\">&quot;side&quot;</span><span class=\"p\">]</span><span class=\"o\">.</span><span
  class=\"n\">split</span><span class=\"p\">(</span>\n        <span class=\"n\">Layout</span><span
  class=\"p\">(</span><span class=\"n\">name</span><span class=\"o\">=</span><span
  class=\"s2\">&quot;plugins&quot;</span><span class=\"p\">),</span>\n    <span class=\"p\">)</span>\n
  \   <span class=\"k\">return</span> <span class=\"n\">layout</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"run_until_keyboard_interrupt-function\">run_until_keyboard_interrupt
  <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>run_until_keyboard_interrupt
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">run_until_keyboard_interrupt</span><span class=\"p\">()</span>
  <span class=\"o\">-&gt;</span> <span class=\"kc\">None</span><span class=\"p\">:</span>\n
  \   <span class=\"k\">try</span><span class=\"p\">:</span>\n        <span class=\"k\">while</span>
  <span class=\"kc\">True</span><span class=\"p\">:</span>\n            <span class=\"n\">time</span><span
  class=\"o\">.</span><span class=\"n\">sleep</span><span class=\"p\">(</span><span
  class=\"mf\">0.2</span><span class=\"p\">)</span>\n    <span class=\"k\">except</span>
  <span class=\"ne\">KeyboardInterrupt</span><span class=\"p\">:</span>\n        <span
  class=\"k\">pass</span>\n</code></pre></div>\n</details>\n<hr />\n<h2 id=\"version_callback-function\">version_callback
  <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>version_callback source</summary>\n<div
  class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span> <span class=\"nf\">version_callback</span><span
  class=\"p\">(</span><span class=\"n\">value</span><span class=\"p\">:</span> <span
  class=\"nb\">bool</span><span class=\"p\">)</span> <span class=\"o\">-&gt;</span>
  <span class=\"kc\">None</span><span class=\"p\">:</span>\n    <span class=\"k\">if</span>
  <span class=\"n\">value</span><span class=\"p\">:</span>\n        <span class=\"kn\">from</span>
  <span class=\"nn\">markata</span> <span class=\"kn\">import</span> <span class=\"n\">__version__</span>\n\n
  \       <span class=\"n\">typer</span><span class=\"o\">.</span><span class=\"n\">echo</span><span
  class=\"p\">(</span><span class=\"sa\">f</span><span class=\"s2\">&quot;Markata
  CLI Version: </span><span class=\"si\">{</span><span class=\"n\">__version__</span><span
  class=\"si\">}</span><span class=\"s2\">&quot;</span><span class=\"p\">)</span>\n
  \       <span class=\"k\">raise</span> <span class=\"n\">typer</span><span class=\"o\">.</span><span
  class=\"n\">Exit</span><span class=\"p\">()</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"json_callback-function\">json_callback <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>json_callback
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">json_callback</span><span class=\"p\">(</span><span class=\"n\">value</span><span
  class=\"p\">:</span> <span class=\"nb\">bool</span><span class=\"p\">)</span> <span
  class=\"o\">-&gt;</span> <span class=\"kc\">None</span><span class=\"p\">:</span>\n
  \   <span class=\"k\">if</span> <span class=\"n\">value</span><span class=\"p\">:</span>\n
  \       <span class=\"kn\">from</span> <span class=\"nn\">markata</span> <span class=\"kn\">import</span>
  <span class=\"n\">Markata</span>\n\n        <span class=\"n\">typer</span><span
  class=\"o\">.</span><span class=\"n\">echo</span><span class=\"p\">(</span><span
  class=\"n\">Markata</span><span class=\"p\">()</span><span class=\"o\">.</span><span
  class=\"n\">to_json</span><span class=\"p\">())</span>\n        <span class=\"k\">raise</span>
  <span class=\"n\">typer</span><span class=\"o\">.</span><span class=\"n\">Exit</span><span
  class=\"p\">()</span>\n</code></pre></div>\n</details>\n<hr />\n<h2 id=\"main-function\">main
  <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>main source</summary>\n<div
  class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span> <span class=\"nf\">main</span><span
  class=\"p\">(</span>\n    <span class=\"n\">version</span><span class=\"p\">:</span>
  <span class=\"nb\">bool</span> <span class=\"o\">=</span> <span class=\"n\">typer</span><span
  class=\"o\">.</span><span class=\"n\">Option</span><span class=\"p\">(</span>\n
  \       <span class=\"kc\">None</span><span class=\"p\">,</span> <span class=\"s2\">&quot;--version&quot;</span><span
  class=\"p\">,</span> <span class=\"n\">callback</span><span class=\"o\">=</span><span
  class=\"n\">version_callback</span><span class=\"p\">,</span> <span class=\"n\">is_eager</span><span
  class=\"o\">=</span><span class=\"kc\">True</span>\n    <span class=\"p\">),</span>\n
  \   <span class=\"n\">to_json</span><span class=\"p\">:</span> <span class=\"nb\">bool</span>
  <span class=\"o\">=</span> <span class=\"n\">typer</span><span class=\"o\">.</span><span
  class=\"n\">Option</span><span class=\"p\">(</span>\n        <span class=\"kc\">None</span><span
  class=\"p\">,</span> <span class=\"s2\">&quot;--to-json&quot;</span><span class=\"p\">,</span>
  <span class=\"n\">callback</span><span class=\"o\">=</span><span class=\"n\">json_callback</span><span
  class=\"p\">,</span> <span class=\"n\">is_eager</span><span class=\"o\">=</span><span
  class=\"kc\">True</span>\n    <span class=\"p\">),</span>\n<span class=\"p\">)</span>
  <span class=\"o\">-&gt;</span> <span class=\"kc\">None</span><span class=\"p\">:</span>\n
  \   <span class=\"c1\"># Do other global stuff, handle other global options here</span>\n
  \   <span class=\"k\">return</span>\n</code></pre></div>\n</details>\n<hr />\n<h2
  id=\"cli-function\">cli <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>cli
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">cli</span><span class=\"p\">()</span> <span class=\"o\">-&gt;</span>
  <span class=\"kc\">None</span><span class=\"p\">:</span>\n    <span class=\"kn\">from</span>
  <span class=\"nn\">markata</span> <span class=\"kn\">import</span> <span class=\"n\">Markata</span>\n\n
  \   <span class=\"n\">m</span> <span class=\"o\">=</span> <span class=\"n\">Markata</span><span
  class=\"p\">()</span>\n    <span class=\"n\">m</span><span class=\"o\">.</span><span
  class=\"n\">_pm</span><span class=\"o\">.</span><span class=\"n\">hook</span><span
  class=\"o\">.</span><span class=\"n\">cli</span><span class=\"p\">(</span><span
  class=\"n\">markata</span><span class=\"o\">=</span><span class=\"n\">m</span><span
  class=\"p\">,</span> <span class=\"n\">app</span><span class=\"o\">=</span><span
  class=\"n\">app</span><span class=\"p\">)</span>\n    <span class=\"n\">app</span><span
  class=\"p\">()</span>\n</code></pre></div>\n</details>"
datetime: null
description: Docs for cli
long_description: ''
now: 2022-02-05 19:38:00.891472
path: cli.md
slug: markata/cli/cli
status: published
title: cli.py
today: 2022-02-05
---

---

## make_layout `function`

Define the layout.

??? "make_layout source"
    ``` python
    def make_layout() -> Layout:
        """Define the layout."""
        layout = Layout(name="root")

        layout.split(
            Layout(name="header", size=3),
            Layout(name="main"),
        )
        layout["main"].split_row(
            Layout(name="side", ratio=50),
            Layout(name="mid", ratio=30),
            Layout(name="describe", ratio=20),
        )
        layout["mid"].split(
            Layout(name="server"),
            Layout(name="runner"),
        )
        layout["side"].split(
            Layout(name="plugins"),
        )
        return layout
    ```


---

## run_until_keyboard_interrupt `function`

None

??? "run_until_keyboard_interrupt source"
    ``` python
    def run_until_keyboard_interrupt() -> None:
        try:
            while True:
                time.sleep(0.2)
        except KeyboardInterrupt:
            pass
    ```


---

## version_callback `function`

None

??? "version_callback source"
    ``` python
    def version_callback(value: bool) -> None:
        if value:
            from markata import __version__

            typer.echo(f"Markata CLI Version: {__version__}")
            raise typer.Exit()
    ```


---

## json_callback `function`

None

??? "json_callback source"
    ``` python
    def json_callback(value: bool) -> None:
        if value:
            from markata import Markata

            typer.echo(Markata().to_json())
            raise typer.Exit()
    ```


---

## main `function`

None

??? "main source"
    ``` python
    def main(
        version: bool = typer.Option(
            None, "--version", callback=version_callback, is_eager=True
        ),
        to_json: bool = typer.Option(
            None, "--to-json", callback=json_callback, is_eager=True
        ),
    ) -> None:
        # Do other global stuff, handle other global options here
        return
    ```


---

## cli `function`

None

??? "cli source"
    ``` python
    def cli() -> None:
        from markata import Markata

        m = Markata()
        m._pm.hook.cli(markata=m, app=app)
        app()
    ```