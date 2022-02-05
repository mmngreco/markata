---
article_html: "<hr />\n<h2 id=\"save-function\">save <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>save
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">save</span><span class=\"p\">(</span><span class=\"n\">markata</span><span
  class=\"p\">:</span> <span class=\"s2\">&quot;Markata&quot;</span><span class=\"p\">)</span>
  <span class=\"o\">-&gt;</span> <span class=\"kc\">None</span><span class=\"p\">:</span>\n
  \   <span class=\"k\">try</span><span class=\"p\">:</span>\n        <span class=\"n\">output_dir</span>
  <span class=\"o\">=</span> <span class=\"n\">Path</span><span class=\"p\">(</span><span
  class=\"nb\">str</span><span class=\"p\">(</span><span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">config</span><span class=\"p\">[</span><span
  class=\"s2\">&quot;output_dir&quot;</span><span class=\"p\">]))</span>\n        <span
  class=\"n\">assets_dir</span> <span class=\"o\">=</span> <span class=\"n\">Path</span><span
  class=\"p\">(</span><span class=\"nb\">str</span><span class=\"p\">(</span><span
  class=\"n\">markata</span><span class=\"o\">.</span><span class=\"n\">config</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;assets_dir&quot;</span><span class=\"p\">]))</span>\n
  \   <span class=\"k\">except</span> <span class=\"ne\">KeyError</span><span class=\"p\">:</span>\n
  \       <span class=\"k\">return</span>\n\n    <span class=\"k\">with</span> <span
  class=\"n\">markata</span><span class=\"o\">.</span><span class=\"n\">console</span><span
  class=\"o\">.</span><span class=\"n\">status</span><span class=\"p\">(</span><span
  class=\"s2\">&quot;copying assets&quot;</span><span class=\"p\">,</span> <span class=\"n\">spinner</span><span
  class=\"o\">=</span><span class=\"s2\">&quot;aesthetic&quot;</span><span class=\"p\">,</span>
  <span class=\"n\">speed</span><span class=\"o\">=</span><span class=\"mf\">0.2</span><span
  class=\"p\">):</span>\n        <span class=\"k\">if</span> <span class=\"n\">assets_dir</span><span
  class=\"o\">.</span><span class=\"n\">exists</span><span class=\"p\">():</span>\n
  \           <span class=\"n\">shutil</span><span class=\"o\">.</span><span class=\"n\">copytree</span><span
  class=\"p\">(</span><span class=\"n\">assets_dir</span><span class=\"p\">,</span>
  <span class=\"n\">output_dir</span><span class=\"p\">,</span> <span class=\"n\">dirs_exist_ok</span><span
  class=\"o\">=</span><span class=\"kc\">True</span><span class=\"p\">)</span>\n</code></pre></div>\n</details>"
datetime: null
description: Docs for copy_assets
long_description: ''
now: 2022-02-05 19:38:00.891377
path: copy_assets.md
slug: markata/plugins/copy_assets
status: published
title: copy_assets.py
today: 2022-02-05
---

---

## save `function`

None

??? "save source"
    ``` python
    def save(markata: "Markata") -> None:
        try:
            output_dir = Path(str(markata.config["output_dir"]))
            assets_dir = Path(str(markata.config["assets_dir"]))
        except KeyError:
            return

        with markata.console.status("copying assets", spinner="aesthetic", speed=0.2):
            if assets_dir.exists():
                shutil.copytree(assets_dir, output_dir, dirs_exist_ok=True)
    ```