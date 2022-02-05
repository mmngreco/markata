---
article_html: "<hr />\n<h2 id=\"get_font-function\">get_font <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>get_font
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">get_font</span><span class=\"p\">(</span>\n    <span class=\"n\">path</span><span
  class=\"p\">:</span> <span class=\"n\">Path</span><span class=\"p\">,</span> <span
  class=\"n\">draw</span><span class=\"p\">:</span> <span class=\"n\">ImageDraw</span><span
  class=\"o\">.</span><span class=\"n\">Draw</span><span class=\"p\">,</span> <span
  class=\"n\">title</span><span class=\"p\">:</span> <span class=\"nb\">str</span><span
  class=\"p\">,</span> <span class=\"n\">size</span><span class=\"p\">:</span> <span
  class=\"nb\">int</span> <span class=\"o\">=</span> <span class=\"mi\">250</span>\n<span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"n\">ImageFont</span><span
  class=\"o\">.</span><span class=\"n\">FreeTypeFont</span><span class=\"p\">:</span>\n
  \   <span class=\"n\">font</span> <span class=\"o\">=</span> <span class=\"n\">ImageFont</span><span
  class=\"o\">.</span><span class=\"n\">truetype</span><span class=\"p\">(</span><span
  class=\"n\">path</span><span class=\"p\">,</span> <span class=\"n\">size</span><span
  class=\"o\">=</span><span class=\"n\">size</span><span class=\"p\">)</span>\n    <span
  class=\"k\">if</span> <span class=\"n\">draw</span><span class=\"o\">.</span><span
  class=\"n\">textsize</span><span class=\"p\">(</span><span class=\"n\">title</span><span
  class=\"p\">,</span> <span class=\"n\">font</span><span class=\"o\">=</span><span
  class=\"n\">font</span><span class=\"p\">)[</span><span class=\"mi\">0</span><span
  class=\"p\">]</span> <span class=\"o\">&gt;</span> <span class=\"mi\">800</span><span
  class=\"p\">:</span>\n        <span class=\"k\">return</span> <span class=\"n\">get_font</span><span
  class=\"p\">(</span><span class=\"n\">path</span><span class=\"p\">,</span> <span
  class=\"n\">draw</span><span class=\"p\">,</span> <span class=\"n\">title</span><span
  class=\"p\">,</span> <span class=\"n\">size</span> <span class=\"o\">-</span> <span
  class=\"mi\">10</span><span class=\"p\">)</span>\n    <span class=\"k\">return</span>
  <span class=\"n\">font</span>\n</code></pre></div>\n</details>\n<hr />\n<h2 id=\"make_cover-function\">make_cover
  <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>make_cover source</summary>\n<div
  class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span> <span class=\"nf\">make_cover</span><span
  class=\"p\">(</span>\n    <span class=\"n\">title</span><span class=\"p\">:</span>
  <span class=\"nb\">str</span><span class=\"p\">,</span> <span class=\"n\">color</span><span
  class=\"p\">:</span> <span class=\"nb\">str</span><span class=\"p\">,</span> <span
  class=\"n\">output_path</span><span class=\"p\">:</span> <span class=\"n\">Path</span><span
  class=\"p\">,</span> <span class=\"n\">template_path</span><span class=\"p\">:</span>
  <span class=\"n\">Path</span><span class=\"p\">,</span> <span class=\"n\">font_path</span><span
  class=\"p\">:</span> <span class=\"n\">Path</span>\n<span class=\"p\">)</span> <span
  class=\"o\">-&gt;</span> <span class=\"kc\">None</span><span class=\"p\">:</span>\n
  \   <span class=\"n\">image</span> <span class=\"o\">=</span> <span class=\"n\">Image</span><span
  class=\"o\">.</span><span class=\"n\">open</span><span class=\"p\">(</span><span
  class=\"n\">template_path</span><span class=\"p\">)</span>\n\n    <span class=\"n\">draw</span>
  <span class=\"o\">=</span> <span class=\"n\">ImageDraw</span><span class=\"o\">.</span><span
  class=\"n\">Draw</span><span class=\"p\">(</span><span class=\"n\">image</span><span
  class=\"p\">)</span>\n\n    <span class=\"n\">font</span> <span class=\"o\">=</span>
  <span class=\"n\">get_font</span><span class=\"p\">(</span><span class=\"n\">font_path</span><span
  class=\"p\">,</span> <span class=\"n\">draw</span><span class=\"p\">,</span> <span
  class=\"n\">title</span><span class=\"p\">)</span>\n\n    <span class=\"n\">color</span>
  <span class=\"o\">=</span> <span class=\"s2\">&quot;rgb(255,255,255)&quot;</span>\n
  \   <span class=\"n\">padding</span> <span class=\"o\">=</span> <span class=\"p\">(</span><span
  class=\"mi\">200</span><span class=\"p\">,</span> <span class=\"mi\">100</span><span
  class=\"p\">)</span>\n    <span class=\"n\">bounding_box</span> <span class=\"o\">=</span>
  <span class=\"p\">[</span><span class=\"n\">padding</span><span class=\"p\">[</span><span
  class=\"mi\">0</span><span class=\"p\">],</span> <span class=\"n\">padding</span><span
  class=\"p\">[</span><span class=\"mi\">1</span><span class=\"p\">],</span> <span
  class=\"mi\">1000</span> <span class=\"o\">-</span> <span class=\"n\">padding</span><span
  class=\"p\">[</span><span class=\"mi\">0</span><span class=\"p\">],</span> <span
  class=\"mi\">420</span> <span class=\"o\">-</span> <span class=\"n\">padding</span><span
  class=\"p\">[</span><span class=\"mi\">1</span><span class=\"p\">]]</span>\n    <span
  class=\"n\">x1</span><span class=\"p\">,</span> <span class=\"n\">y1</span><span
  class=\"p\">,</span> <span class=\"n\">x2</span><span class=\"p\">,</span> <span
  class=\"n\">y2</span> <span class=\"o\">=</span> <span class=\"n\">bounding_box</span>\n
  \   <span class=\"n\">w</span><span class=\"p\">,</span> <span class=\"n\">h</span>
  <span class=\"o\">=</span> <span class=\"n\">draw</span><span class=\"o\">.</span><span
  class=\"n\">textsize</span><span class=\"p\">(</span><span class=\"n\">title</span><span
  class=\"p\">,</span> <span class=\"n\">font</span><span class=\"o\">=</span><span
  class=\"n\">font</span><span class=\"p\">)</span>\n    <span class=\"n\">x</span>
  <span class=\"o\">=</span> <span class=\"p\">(</span><span class=\"n\">x2</span>
  <span class=\"o\">-</span> <span class=\"n\">x1</span> <span class=\"o\">-</span>
  <span class=\"n\">w</span><span class=\"p\">)</span> <span class=\"o\">/</span>
  <span class=\"mi\">2</span> <span class=\"o\">+</span> <span class=\"n\">x1</span>\n
  \   <span class=\"n\">y</span> <span class=\"o\">=</span> <span class=\"p\">(</span><span
  class=\"n\">y2</span> <span class=\"o\">-</span> <span class=\"n\">y1</span> <span
  class=\"o\">-</span> <span class=\"n\">h</span><span class=\"p\">)</span> <span
  class=\"o\">/</span> <span class=\"mi\">2</span> <span class=\"o\">+</span> <span
  class=\"n\">y1</span>\n    <span class=\"n\">draw</span><span class=\"o\">.</span><span
  class=\"n\">text</span><span class=\"p\">((</span><span class=\"n\">x</span><span
  class=\"p\">,</span> <span class=\"n\">y</span><span class=\"p\">),</span> <span
  class=\"n\">title</span><span class=\"p\">,</span> <span class=\"n\">fill</span><span
  class=\"o\">=</span><span class=\"n\">color</span><span class=\"p\">,</span> <span
  class=\"n\">font</span><span class=\"o\">=</span><span class=\"n\">font</span><span
  class=\"p\">,</span> <span class=\"n\">align</span><span class=\"o\">=</span><span
  class=\"s2\">&quot;center&quot;</span><span class=\"p\">)</span>\n    <span class=\"n\">image</span><span
  class=\"o\">.</span><span class=\"n\">save</span><span class=\"p\">(</span><span
  class=\"n\">output_path</span><span class=\"p\">)</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"save-function\">save <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>save
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">save</span><span class=\"p\">(</span><span class=\"n\">markata</span><span
  class=\"p\">:</span> <span class=\"s2\">&quot;Markata&quot;</span><span class=\"p\">)</span>
  <span class=\"o\">-&gt;</span> <span class=\"kc\">None</span><span class=\"p\">:</span>\n
  \   <span class=\"k\">for</span> <span class=\"n\">article</span> <span class=\"ow\">in</span>
  <span class=\"n\">markata</span><span class=\"o\">.</span><span class=\"n\">articles</span><span
  class=\"p\">:</span>\n        <span class=\"n\">output_path</span> <span class=\"o\">=</span>
  <span class=\"n\">Path</span><span class=\"p\">(</span><span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">output_dir</span><span class=\"p\">)</span>
  <span class=\"o\">/</span> <span class=\"p\">(</span>\n            <span class=\"n\">Path</span><span
  class=\"p\">(</span><span class=\"n\">article</span><span class=\"o\">.</span><span
  class=\"n\">metadata</span><span class=\"p\">[</span><span class=\"s2\">&quot;path&quot;</span><span
  class=\"p\">])</span><span class=\"o\">.</span><span class=\"n\">stem</span> <span
  class=\"o\">+</span> <span class=\"s2\">&quot;.png&quot;</span>\n        <span class=\"p\">)</span>\n\n
  \       <span class=\"n\">make_cover</span><span class=\"p\">(</span>\n            <span
  class=\"n\">article</span><span class=\"o\">.</span><span class=\"n\">metadata</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;title&quot;</span><span class=\"p\">],</span>\n
  \           <span class=\"n\">markata</span><span class=\"o\">.</span><span class=\"n\">config</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;cover_font_color&quot;</span><span
  class=\"p\">],</span>\n            <span class=\"n\">output_path</span><span class=\"p\">,</span>\n
  \           <span class=\"n\">markata</span><span class=\"o\">.</span><span class=\"n\">config</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;cover_template&quot;</span><span class=\"p\">],</span>\n
  \           <span class=\"n\">markata</span><span class=\"o\">.</span><span class=\"n\">config</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;cover_font&quot;</span><span class=\"p\">],</span>\n
  \       <span class=\"p\">)</span>\n</code></pre></div>\n</details>"
datetime: null
description: Docs for create_covers
long_description: ''
now: 2022-02-05 19:38:00.891429
path: create_covers.md
slug: markata/plugins/create_covers
status: published
title: create_covers.py
today: 2022-02-05
---

---

## get_font `function`

None

??? "get_font source"
    ``` python
    def get_font(
        path: Path, draw: ImageDraw.Draw, title: str, size: int = 250
    ) -> ImageFont.FreeTypeFont:
        font = ImageFont.truetype(path, size=size)
        if draw.textsize(title, font=font)[0] > 800:
            return get_font(path, draw, title, size - 10)
        return font
    ```


---

## make_cover `function`

None

??? "make_cover source"
    ``` python
    def make_cover(
        title: str, color: str, output_path: Path, template_path: Path, font_path: Path
    ) -> None:
        image = Image.open(template_path)

        draw = ImageDraw.Draw(image)

        font = get_font(font_path, draw, title)

        color = "rgb(255,255,255)"
        padding = (200, 100)
        bounding_box = [padding[0], padding[1], 1000 - padding[0], 420 - padding[1]]
        x1, y1, x2, y2 = bounding_box
        w, h = draw.textsize(title, font=font)
        x = (x2 - x1 - w) / 2 + x1
        y = (y2 - y1 - h) / 2 + y1
        draw.text((x, y), title, fill=color, font=font, align="center")
        image.save(output_path)
    ```


---

## save `function`

None

??? "save source"
    ``` python
    def save(markata: "Markata") -> None:
        for article in markata.articles:
            output_path = Path(markata.output_dir) / (
                Path(article.metadata["path"]).stem + ".png"
            )

            make_cover(
                article.metadata["title"],
                markata.config["cover_font_color"],
                output_path,
                markata.config["cover_template"],
                markata.config["cover_font"],
            )
    ```