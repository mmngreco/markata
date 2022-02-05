---
article_html: "<p>Icon Resize Plugin</p>\n<hr />\n<h2 id=\"render-function\">render
  <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>render source</summary>\n<div
  class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span> <span class=\"nf\">render</span><span
  class=\"p\">(</span><span class=\"n\">markata</span><span class=\"p\">:</span> <span
  class=\"s2\">&quot;MarkataIcons&quot;</span><span class=\"p\">)</span> <span class=\"o\">-&gt;</span>
  <span class=\"kc\">None</span><span class=\"p\">:</span>\n    <span class=\"k\">if</span>
  <span class=\"s2\">&quot;icon&quot;</span> <span class=\"ow\">not</span> <span class=\"ow\">in</span>
  <span class=\"n\">markata</span><span class=\"o\">.</span><span class=\"n\">config</span><span
  class=\"p\">:</span>\n        <span class=\"k\">return</span>\n    <span class=\"n\">base_out_file</span>
  <span class=\"o\">=</span> <span class=\"n\">Path</span><span class=\"p\">(</span><span
  class=\"n\">markata</span><span class=\"o\">.</span><span class=\"n\">config</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;output_dir&quot;</span><span class=\"p\">])</span>
  <span class=\"o\">/</span> <span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">config</span><span class=\"p\">[</span><span class=\"s2\">&quot;icon&quot;</span><span
  class=\"p\">]</span>\n\n    <span class=\"k\">with</span> <span class=\"n\">Image</span><span
  class=\"o\">.</span><span class=\"n\">open</span><span class=\"p\">(</span><span
  class=\"n\">Path</span><span class=\"p\">(</span><span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">config</span><span class=\"p\">[</span><span
  class=\"s2\">&quot;assets_dir&quot;</span><span class=\"p\">])</span> <span class=\"o\">/</span>
  <span class=\"n\">markata</span><span class=\"o\">.</span><span class=\"n\">config</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;icon&quot;</span><span class=\"p\">])</span>
  <span class=\"k\">as</span> <span class=\"n\">img</span><span class=\"p\">:</span>\n
  \       <span class=\"n\">markata</span><span class=\"o\">.</span><span class=\"n\">icons</span>
  <span class=\"o\">=</span> <span class=\"p\">[]</span>\n        <span class=\"k\">for</span>
  <span class=\"n\">width</span> <span class=\"ow\">in</span> <span class=\"p\">[</span><span
  class=\"mi\">48</span><span class=\"p\">,</span> <span class=\"mi\">72</span><span
  class=\"p\">,</span> <span class=\"mi\">96</span><span class=\"p\">,</span> <span
  class=\"mi\">144</span><span class=\"p\">,</span> <span class=\"mi\">192</span><span
  class=\"p\">,</span> <span class=\"mi\">256</span><span class=\"p\">,</span> <span
  class=\"mi\">384</span><span class=\"p\">,</span> <span class=\"mi\">512</span><span
  class=\"p\">]:</span>\n            <span class=\"n\">height</span> <span class=\"o\">=</span>
  <span class=\"nb\">int</span><span class=\"p\">(</span><span class=\"nb\">float</span><span
  class=\"p\">(</span><span class=\"n\">img</span><span class=\"o\">.</span><span
  class=\"n\">size</span><span class=\"p\">[</span><span class=\"mi\">1</span><span
  class=\"p\">])</span> <span class=\"o\">*</span> <span class=\"nb\">float</span><span
  class=\"p\">(</span><span class=\"n\">width</span> <span class=\"o\">/</span> <span
  class=\"nb\">float</span><span class=\"p\">(</span><span class=\"n\">img</span><span
  class=\"o\">.</span><span class=\"n\">size</span><span class=\"p\">[</span><span
  class=\"mi\">0</span><span class=\"p\">])))</span>\n            <span class=\"n\">filename</span>
  <span class=\"o\">=</span> <span class=\"n\">Path</span><span class=\"p\">(</span>\n
  \               <span class=\"sa\">f</span><span class=\"s2\">&quot;</span><span
  class=\"si\">{</span><span class=\"n\">base_out_file</span><span class=\"o\">.</span><span
  class=\"n\">stem</span><span class=\"si\">}</span><span class=\"s2\">_</span><span
  class=\"si\">{</span><span class=\"n\">width</span><span class=\"si\">}</span><span
  class=\"s2\">x</span><span class=\"si\">{</span><span class=\"n\">height</span><span
  class=\"si\">}{</span><span class=\"n\">base_out_file</span><span class=\"o\">.</span><span
  class=\"n\">suffix</span><span class=\"si\">}</span><span class=\"s2\">&quot;</span>\n
  \           <span class=\"p\">)</span>\n            <span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">icons</span><span class=\"o\">.</span><span
  class=\"n\">append</span><span class=\"p\">(</span>\n                <span class=\"p\">{</span>\n
  \                   <span class=\"s2\">&quot;src&quot;</span><span class=\"p\">:</span>
  <span class=\"nb\">str</span><span class=\"p\">(</span><span class=\"n\">filename</span><span
  class=\"p\">),</span>\n                    <span class=\"s2\">&quot;sizes&quot;</span><span
  class=\"p\">:</span> <span class=\"sa\">f</span><span class=\"s2\">&quot;</span><span
  class=\"si\">{</span><span class=\"n\">width</span><span class=\"si\">}</span><span
  class=\"s2\">x</span><span class=\"si\">{</span><span class=\"n\">width</span><span
  class=\"si\">}</span><span class=\"s2\">&quot;</span><span class=\"p\">,</span>\n
  \                   <span class=\"s2\">&quot;type&quot;</span><span class=\"p\">:</span>
  <span class=\"sa\">f</span><span class=\"s2\">&quot;image/</span><span class=\"si\">{</span><span
  class=\"n\">img</span><span class=\"o\">.</span><span class=\"n\">format</span><span
  class=\"si\">}</span><span class=\"s2\">&quot;</span><span class=\"o\">.</span><span
  class=\"n\">lower</span><span class=\"p\">(),</span>\n                    <span
  class=\"s2\">&quot;purpose&quot;</span><span class=\"p\">:</span> <span class=\"s2\">&quot;any
  maskable&quot;</span><span class=\"p\">,</span>\n                <span class=\"p\">}</span>\n
  \           <span class=\"p\">)</span>\n</code></pre></div>\n</details>\n<hr />\n<h2
  id=\"save-function\">save <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>save
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">save</span><span class=\"p\">(</span><span class=\"n\">markata</span><span
  class=\"p\">:</span> <span class=\"s2\">&quot;MarkataIcons&quot;</span><span class=\"p\">)</span>
  <span class=\"o\">-&gt;</span> <span class=\"kc\">None</span><span class=\"p\">:</span>\n
  \   <span class=\"k\">if</span> <span class=\"s2\">&quot;icon&quot;</span> <span
  class=\"ow\">not</span> <span class=\"ow\">in</span> <span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">config</span><span class=\"p\">:</span>\n
  \       <span class=\"k\">return</span>\n    <span class=\"n\">base_out_file</span>
  <span class=\"o\">=</span> <span class=\"n\">Path</span><span class=\"p\">(</span><span
  class=\"n\">markata</span><span class=\"o\">.</span><span class=\"n\">config</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;output_dir&quot;</span><span class=\"p\">])</span>
  <span class=\"o\">/</span> <span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">config</span><span class=\"p\">[</span><span class=\"s2\">&quot;icon&quot;</span><span
  class=\"p\">]</span>\n    <span class=\"k\">for</span> <span class=\"n\">width</span>
  <span class=\"ow\">in</span> <span class=\"p\">[</span><span class=\"mi\">48</span><span
  class=\"p\">,</span> <span class=\"mi\">72</span><span class=\"p\">,</span> <span
  class=\"mi\">96</span><span class=\"p\">,</span> <span class=\"mi\">144</span><span
  class=\"p\">,</span> <span class=\"mi\">192</span><span class=\"p\">,</span> <span
  class=\"mi\">256</span><span class=\"p\">,</span> <span class=\"mi\">384</span><span
  class=\"p\">,</span> <span class=\"mi\">512</span><span class=\"p\">]:</span>\n
  \       <span class=\"k\">with</span> <span class=\"n\">Image</span><span class=\"o\">.</span><span
  class=\"n\">open</span><span class=\"p\">(</span>\n            <span class=\"n\">Path</span><span
  class=\"p\">(</span><span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">config</span><span class=\"p\">[</span><span class=\"s2\">&quot;assets_dir&quot;</span><span
  class=\"p\">])</span> <span class=\"o\">/</span> <span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">config</span><span class=\"p\">[</span><span
  class=\"s2\">&quot;icon&quot;</span><span class=\"p\">]</span>\n        <span class=\"p\">)</span>
  <span class=\"k\">as</span> <span class=\"n\">img</span><span class=\"p\">:</span>\n
  \           <span class=\"n\">height</span> <span class=\"o\">=</span> <span class=\"nb\">int</span><span
  class=\"p\">(</span><span class=\"nb\">float</span><span class=\"p\">(</span><span
  class=\"n\">img</span><span class=\"o\">.</span><span class=\"n\">size</span><span
  class=\"p\">[</span><span class=\"mi\">1</span><span class=\"p\">])</span> <span
  class=\"o\">*</span> <span class=\"nb\">float</span><span class=\"p\">(</span><span
  class=\"n\">width</span> <span class=\"o\">/</span> <span class=\"nb\">float</span><span
  class=\"p\">(</span><span class=\"n\">img</span><span class=\"o\">.</span><span
  class=\"n\">size</span><span class=\"p\">[</span><span class=\"mi\">0</span><span
  class=\"p\">])))</span>\n            <span class=\"n\">img</span> <span class=\"o\">=</span>
  <span class=\"n\">img</span><span class=\"o\">.</span><span class=\"n\">resize</span><span
  class=\"p\">((</span><span class=\"n\">width</span><span class=\"p\">,</span> <span
  class=\"n\">height</span><span class=\"p\">),</span> <span class=\"n\">Image</span><span
  class=\"o\">.</span><span class=\"n\">ANTIALIAS</span><span class=\"p\">)</span>\n
  \           <span class=\"n\">filename</span> <span class=\"o\">=</span> <span class=\"n\">Path</span><span
  class=\"p\">(</span>\n                <span class=\"sa\">f</span><span class=\"s2\">&quot;</span><span
  class=\"si\">{</span><span class=\"n\">base_out_file</span><span class=\"o\">.</span><span
  class=\"n\">stem</span><span class=\"si\">}</span><span class=\"s2\">_</span><span
  class=\"si\">{</span><span class=\"n\">width</span><span class=\"si\">}</span><span
  class=\"s2\">x</span><span class=\"si\">{</span><span class=\"n\">height</span><span
  class=\"si\">}{</span><span class=\"n\">base_out_file</span><span class=\"o\">.</span><span
  class=\"n\">suffix</span><span class=\"si\">}</span><span class=\"s2\">&quot;</span>\n
  \           <span class=\"p\">)</span>\n            <span class=\"n\">out_file</span>
  <span class=\"o\">=</span> <span class=\"n\">Path</span><span class=\"p\">(</span><span
  class=\"n\">markata</span><span class=\"o\">.</span><span class=\"n\">config</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;output_dir&quot;</span><span class=\"p\">])</span>
  <span class=\"o\">/</span> <span class=\"n\">filename</span>\n            <span
  class=\"n\">img</span><span class=\"o\">.</span><span class=\"n\">save</span><span
  class=\"p\">(</span><span class=\"n\">out_file</span><span class=\"p\">)</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"markataicons-class\">MarkataIcons <code>class</code></h2>\n<p>None</p>\n<details>\n<summary>MarkataIcons
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">class</span>
  <span class=\"nc\">MarkataIcons</span><span class=\"p\">(</span><span class=\"n\">Markata</span><span
  class=\"p\">):</span>\n        <span class=\"n\">icons</span><span class=\"p\">:</span>
  <span class=\"n\">List</span><span class=\"p\">[</span><span class=\"n\">Dict</span><span
  class=\"p\">[</span><span class=\"nb\">str</span><span class=\"p\">,</span> <span
  class=\"nb\">str</span><span class=\"p\">]]</span>\n</code></pre></div>\n</details>"
datetime: null
description: Docs for icon_resize
long_description: ''
now: 2022-02-05 19:38:00.891421
path: icon_resize.md
slug: markata/plugins/icon_resize
status: published
title: icon_resize.py
today: 2022-02-05
---

Icon Resize Plugin


---

## render `function`

None

??? "render source"
    ``` python
    def render(markata: "MarkataIcons") -> None:
        if "icon" not in markata.config:
            return
        base_out_file = Path(markata.config["output_dir"]) / markata.config["icon"]

        with Image.open(Path(markata.config["assets_dir"]) / markata.config["icon"]) as img:
            markata.icons = []
            for width in [48, 72, 96, 144, 192, 256, 384, 512]:
                height = int(float(img.size[1]) * float(width / float(img.size[0])))
                filename = Path(
                    f"{base_out_file.stem}_{width}x{height}{base_out_file.suffix}"
                )
                markata.icons.append(
                    {
                        "src": str(filename),
                        "sizes": f"{width}x{width}",
                        "type": f"image/{img.format}".lower(),
                        "purpose": "any maskable",
                    }
                )
    ```


---

## save `function`

None

??? "save source"
    ``` python
    def save(markata: "MarkataIcons") -> None:
        if "icon" not in markata.config:
            return
        base_out_file = Path(markata.config["output_dir"]) / markata.config["icon"]
        for width in [48, 72, 96, 144, 192, 256, 384, 512]:
            with Image.open(
                Path(markata.config["assets_dir"]) / markata.config["icon"]
            ) as img:
                height = int(float(img.size[1]) * float(width / float(img.size[0])))
                img = img.resize((width, height), Image.ANTIALIAS)
                filename = Path(
                    f"{base_out_file.stem}_{width}x{height}{base_out_file.suffix}"
                )
                out_file = Path(markata.config["output_dir"]) / filename
                img.save(out_file)
    ```


---

## MarkataIcons `class`

None

??? "MarkataIcons source"
    ``` python
    class MarkataIcons(Markata):
            icons: List[Dict[str, str]]
    ```