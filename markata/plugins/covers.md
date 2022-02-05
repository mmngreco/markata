---
article_html: "<hr />\n<h2 id=\"_load_font-function\">_load_font <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>_load_font
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">_load_font</span><span class=\"p\">(</span><span class=\"n\">path</span><span
  class=\"p\">:</span> <span class=\"n\">Path</span><span class=\"p\">,</span> <span
  class=\"n\">size</span><span class=\"p\">:</span> <span class=\"nb\">int</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"n\">ImageFont</span><span
  class=\"o\">.</span><span class=\"n\">FreeTypeFont</span><span class=\"p\">:</span>\n
  \   <span class=\"k\">return</span> <span class=\"n\">ImageFont</span><span class=\"o\">.</span><span
  class=\"n\">truetype</span><span class=\"p\">(</span><span class=\"n\">path</span><span
  class=\"p\">,</span> <span class=\"n\">size</span><span class=\"o\">=</span><span
  class=\"n\">size</span><span class=\"p\">)</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"get_font-function\">get_font <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>get_font
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">get_font</span><span class=\"p\">(</span>\n    <span class=\"n\">path</span><span
  class=\"p\">:</span> <span class=\"n\">Path</span><span class=\"p\">,</span>\n    <span
  class=\"n\">draw</span><span class=\"p\">:</span> <span class=\"n\">ImageDraw</span><span
  class=\"o\">.</span><span class=\"n\">Draw</span><span class=\"p\">,</span>\n    <span
  class=\"n\">title</span><span class=\"p\">:</span> <span class=\"nb\">str</span><span
  class=\"p\">,</span>\n    <span class=\"n\">size</span><span class=\"p\">:</span>
  <span class=\"nb\">int</span> <span class=\"o\">=</span> <span class=\"mi\">250</span><span
  class=\"p\">,</span>\n    <span class=\"n\">max_size</span><span class=\"p\">:</span>
  <span class=\"nb\">tuple</span> <span class=\"o\">=</span> <span class=\"p\">(</span><span
  class=\"mi\">800</span><span class=\"p\">,</span> <span class=\"mi\">220</span><span
  class=\"p\">),</span>\n<span class=\"p\">)</span> <span class=\"o\">-&gt;</span>
  <span class=\"n\">ImageFont</span><span class=\"o\">.</span><span class=\"n\">FreeTypeFont</span><span
  class=\"p\">:</span>\n    <span class=\"n\">title</span> <span class=\"o\">=</span>
  <span class=\"n\">title</span> <span class=\"ow\">or</span> <span class=\"s2\">&quot;&quot;</span>\n
  \   <span class=\"n\">font</span> <span class=\"o\">=</span> <span class=\"n\">_load_font</span><span
  class=\"p\">(</span><span class=\"n\">path</span><span class=\"p\">,</span> <span
  class=\"n\">size</span><span class=\"p\">)</span>\n    <span class=\"n\">current_size</span>
  <span class=\"o\">=</span> <span class=\"n\">draw</span><span class=\"o\">.</span><span
  class=\"n\">textsize</span><span class=\"p\">(</span><span class=\"n\">title</span><span
  class=\"p\">,</span> <span class=\"n\">font</span><span class=\"o\">=</span><span
  class=\"n\">font</span><span class=\"p\">)</span>\n\n    <span class=\"k\">if</span>
  <span class=\"n\">current_size</span><span class=\"p\">[</span><span class=\"mi\">0</span><span
  class=\"p\">]</span> <span class=\"o\">&gt;</span> <span class=\"n\">max_size</span><span
  class=\"p\">[</span><span class=\"mi\">0</span><span class=\"p\">]</span> <span
  class=\"ow\">or</span> <span class=\"n\">current_size</span><span class=\"p\">[</span><span
  class=\"mi\">1</span><span class=\"p\">]</span> <span class=\"o\">&gt;</span> <span
  class=\"n\">max_size</span><span class=\"p\">[</span><span class=\"mi\">1</span><span
  class=\"p\">]:</span>\n        <span class=\"k\">return</span> <span class=\"n\">get_font</span><span
  class=\"p\">(</span><span class=\"n\">path</span><span class=\"p\">,</span> <span
  class=\"n\">draw</span><span class=\"p\">,</span> <span class=\"n\">title</span><span
  class=\"p\">,</span> <span class=\"n\">size</span> <span class=\"o\">-</span> <span
  class=\"mi\">10</span><span class=\"p\">,</span> <span class=\"n\">max_size</span><span
  class=\"o\">=</span><span class=\"n\">max_size</span><span class=\"p\">)</span>\n
  \   <span class=\"k\">return</span> <span class=\"n\">font</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"paddingerror-class\">PaddingError <code>class</code></h2>\n<p>None</p>\n<details>\n<summary>PaddingError
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">class</span>
  <span class=\"nc\">PaddingError</span><span class=\"p\">(</span><span class=\"ne\">BaseException</span><span
  class=\"p\">):</span>\n    <span class=\"k\">def</span> <span class=\"fm\">__init__</span><span
  class=\"p\">(</span>\n        <span class=\"bp\">self</span><span class=\"p\">,</span>\n
  \       <span class=\"n\">msg</span><span class=\"p\">:</span> <span class=\"nb\">str</span>
  <span class=\"o\">=</span> <span class=\"s2\">&quot;&quot;</span><span class=\"p\">,</span>\n
  \   <span class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"kc\">None</span><span
  class=\"p\">:</span>\n        <span class=\"nb\">super</span><span class=\"p\">()</span><span
  class=\"o\">.</span><span class=\"fm\">__init__</span><span class=\"p\">(</span>\n
  \           <span class=\"s2\">&quot;Padding must be an iterable of length 1, 2,
  3, or 4.</span><span class=\"se\">\\n</span><span class=\"s2\">&quot;</span> <span
  class=\"o\">+</span> <span class=\"n\">msg</span><span class=\"p\">,</span>\n        <span
  class=\"p\">)</span>\n</code></pre></div>\n</details>\n<hr />\n<h2 id=\"draw_text-function\">draw_text
  <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>draw_text source</summary>\n<div
  class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span> <span class=\"nf\">draw_text</span><span
  class=\"p\">(</span>\n    <span class=\"n\">image</span><span class=\"p\">:</span>
  <span class=\"n\">Image</span><span class=\"p\">,</span>\n    <span class=\"n\">font_path</span><span
  class=\"p\">:</span> <span class=\"n\">Path</span><span class=\"p\">,</span>\n    <span
  class=\"n\">text</span><span class=\"p\">:</span> <span class=\"nb\">str</span><span
  class=\"p\">,</span>\n    <span class=\"n\">color</span><span class=\"p\">:</span>
  <span class=\"n\">Union</span><span class=\"p\">[</span><span class=\"nb\">str</span><span
  class=\"p\">,</span> <span class=\"kc\">None</span><span class=\"p\">],</span>\n
  \   <span class=\"n\">padding</span><span class=\"p\">:</span> <span class=\"n\">Tuple</span><span
  class=\"p\">[</span><span class=\"nb\">int</span><span class=\"p\">,</span> <span
  class=\"o\">...</span><span class=\"p\">],</span>\n<span class=\"p\">)</span> <span
  class=\"o\">-&gt;</span> <span class=\"kc\">None</span><span class=\"p\">:</span>\n
  \   <span class=\"n\">text</span> <span class=\"o\">=</span> <span class=\"n\">text</span>
  <span class=\"ow\">or</span> <span class=\"s2\">&quot;&quot;</span>\n    <span class=\"n\">draw</span>
  <span class=\"o\">=</span> <span class=\"n\">ImageDraw</span><span class=\"o\">.</span><span
  class=\"n\">Draw</span><span class=\"p\">(</span><span class=\"n\">image</span><span
  class=\"p\">)</span>\n    <span class=\"n\">padding</span> <span class=\"o\">=</span>
  <span class=\"n\">resolve_padding</span><span class=\"p\">(</span><span class=\"n\">padding</span><span
  class=\"p\">)</span>\n    <span class=\"n\">width</span> <span class=\"o\">=</span>
  <span class=\"n\">image</span><span class=\"o\">.</span><span class=\"n\">size</span><span
  class=\"p\">[</span><span class=\"mi\">0</span><span class=\"p\">]</span>\n    <span
  class=\"n\">height</span> <span class=\"o\">=</span> <span class=\"n\">image</span><span
  class=\"o\">.</span><span class=\"n\">size</span><span class=\"p\">[</span><span
  class=\"mi\">1</span><span class=\"p\">]</span>\n    <span class=\"n\">bounding_box</span>
  <span class=\"o\">=</span> <span class=\"p\">[</span><span class=\"n\">padding</span><span
  class=\"p\">[</span><span class=\"mi\">0</span><span class=\"p\">],</span> <span
  class=\"n\">padding</span><span class=\"p\">[</span><span class=\"mi\">1</span><span
  class=\"p\">],</span> <span class=\"n\">width</span> <span class=\"o\">-</span>
  <span class=\"n\">padding</span><span class=\"p\">[</span><span class=\"mi\">0</span><span
  class=\"p\">],</span> <span class=\"n\">height</span> <span class=\"o\">-</span>
  <span class=\"n\">padding</span><span class=\"p\">[</span><span class=\"mi\">1</span><span
  class=\"p\">]]</span>\n    <span class=\"n\">bounding_box</span> <span class=\"o\">=</span>
  <span class=\"p\">[</span><span class=\"n\">padding</span><span class=\"p\">[</span><span
  class=\"mi\">0</span><span class=\"p\">],</span> <span class=\"n\">padding</span><span
  class=\"p\">[</span><span class=\"mi\">1</span><span class=\"p\">],</span> <span
  class=\"n\">width</span> <span class=\"o\">-</span> <span class=\"n\">padding</span><span
  class=\"p\">[</span><span class=\"mi\">2</span><span class=\"p\">],</span> <span
  class=\"n\">height</span> <span class=\"o\">-</span> <span class=\"n\">padding</span><span
  class=\"p\">[</span><span class=\"mi\">3</span><span class=\"p\">]]</span>\n    <span
  class=\"n\">max_size</span> <span class=\"o\">=</span> <span class=\"p\">(</span><span
  class=\"n\">bounding_box</span><span class=\"p\">[</span><span class=\"mi\">2</span><span
  class=\"p\">]</span> <span class=\"o\">-</span> <span class=\"n\">bounding_box</span><span
  class=\"p\">[</span><span class=\"mi\">0</span><span class=\"p\">],</span> <span
  class=\"n\">bounding_box</span><span class=\"p\">[</span><span class=\"mi\">3</span><span
  class=\"p\">]</span> <span class=\"o\">-</span> <span class=\"n\">bounding_box</span><span
  class=\"p\">[</span><span class=\"mi\">1</span><span class=\"p\">])</span>\n    <span
  class=\"n\">x1</span><span class=\"p\">,</span> <span class=\"n\">y1</span><span
  class=\"p\">,</span> <span class=\"n\">x2</span><span class=\"p\">,</span> <span
  class=\"n\">y2</span> <span class=\"o\">=</span> <span class=\"n\">bounding_box</span>\n
  \   <span class=\"n\">font</span> <span class=\"o\">=</span> <span class=\"n\">get_font</span><span
  class=\"p\">(</span><span class=\"n\">font_path</span><span class=\"p\">,</span>
  <span class=\"n\">draw</span><span class=\"p\">,</span> <span class=\"n\">text</span><span
  class=\"p\">,</span> <span class=\"n\">max_size</span><span class=\"o\">=</span><span
  class=\"n\">max_size</span><span class=\"p\">)</span>\n    <span class=\"n\">w</span><span
  class=\"p\">,</span> <span class=\"n\">h</span> <span class=\"o\">=</span> <span
  class=\"n\">draw</span><span class=\"o\">.</span><span class=\"n\">textsize</span><span
  class=\"p\">(</span><span class=\"n\">text</span><span class=\"p\">,</span> <span
  class=\"n\">font</span><span class=\"o\">=</span><span class=\"n\">font</span><span
  class=\"p\">)</span>\n    <span class=\"n\">x</span> <span class=\"o\">=</span>
  <span class=\"p\">(</span><span class=\"n\">x2</span> <span class=\"o\">-</span>
  <span class=\"n\">x1</span> <span class=\"o\">-</span> <span class=\"n\">w</span><span
  class=\"p\">)</span> <span class=\"o\">/</span> <span class=\"mi\">2</span> <span
  class=\"o\">+</span> <span class=\"n\">x1</span>\n    <span class=\"n\">y</span>
  <span class=\"o\">=</span> <span class=\"p\">(</span><span class=\"n\">y2</span>
  <span class=\"o\">-</span> <span class=\"n\">y1</span> <span class=\"o\">-</span>
  <span class=\"n\">h</span><span class=\"p\">)</span> <span class=\"o\">/</span>
  <span class=\"mi\">2</span> <span class=\"o\">+</span> <span class=\"n\">y1</span>\n
  \   <span class=\"n\">draw</span><span class=\"o\">.</span><span class=\"n\">text</span><span
  class=\"p\">((</span><span class=\"n\">x</span><span class=\"p\">,</span> <span
  class=\"n\">y</span><span class=\"p\">),</span> <span class=\"n\">text</span><span
  class=\"p\">,</span> <span class=\"n\">fill</span><span class=\"o\">=</span><span
  class=\"n\">color</span><span class=\"p\">,</span> <span class=\"n\">font</span><span
  class=\"o\">=</span><span class=\"n\">font</span><span class=\"p\">,</span> <span
  class=\"n\">align</span><span class=\"o\">=</span><span class=\"s2\">&quot;center&quot;</span><span
  class=\"p\">)</span>\n</code></pre></div>\n</details>\n<hr />\n<h2 id=\"resolve_padding-function\">resolve_padding
  <code>function</code></h2>\n<p>Convert padding to a len 4 tuple</p>\n<details>\n<summary>resolve_padding
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">resolve_padding</span><span class=\"p\">(</span><span class=\"n\">padding</span><span
  class=\"p\">:</span> <span class=\"n\">Tuple</span><span class=\"p\">[</span><span
  class=\"nb\">int</span><span class=\"p\">,</span> <span class=\"o\">...</span><span
  class=\"p\">])</span> <span class=\"o\">-&gt;</span> <span class=\"n\">Tuple</span><span
  class=\"p\">[</span><span class=\"nb\">int</span><span class=\"p\">,</span> <span
  class=\"o\">...</span><span class=\"p\">]:</span>\n    <span class=\"sd\">&quot;&quot;&quot;Convert
  padding to a len 4 tuple&quot;&quot;&quot;</span>\n    <span class=\"k\">if</span>
  <span class=\"nb\">len</span><span class=\"p\">(</span><span class=\"n\">padding</span><span
  class=\"p\">)</span> <span class=\"o\">==</span> <span class=\"mi\">4</span><span
  class=\"p\">:</span>\n        <span class=\"k\">return</span> <span class=\"n\">padding</span>\n
  \   <span class=\"k\">if</span> <span class=\"nb\">len</span><span class=\"p\">(</span><span
  class=\"n\">padding</span><span class=\"p\">)</span> <span class=\"o\">==</span>
  <span class=\"mi\">3</span><span class=\"p\">:</span>\n        <span class=\"k\">return</span>
  <span class=\"p\">(</span><span class=\"o\">*</span><span class=\"n\">padding</span><span
  class=\"p\">,</span> <span class=\"n\">padding</span><span class=\"p\">[</span><span
  class=\"mi\">1</span><span class=\"p\">])</span>\n    <span class=\"k\">if</span>
  <span class=\"nb\">len</span><span class=\"p\">(</span><span class=\"n\">padding</span><span
  class=\"p\">)</span> <span class=\"o\">==</span> <span class=\"mi\">2</span><span
  class=\"p\">:</span>\n        <span class=\"k\">return</span> <span class=\"n\">padding</span>
  <span class=\"o\">*</span> <span class=\"mi\">2</span>\n    <span class=\"k\">if</span>
  <span class=\"nb\">len</span><span class=\"p\">(</span><span class=\"n\">padding</span><span
  class=\"p\">)</span> <span class=\"o\">==</span> <span class=\"mi\">1</span><span
  class=\"p\">:</span>\n        <span class=\"k\">return</span> <span class=\"n\">padding</span>
  <span class=\"o\">*</span> <span class=\"mi\">4</span>\n    <span class=\"k\">raise</span>
  <span class=\"n\">PaddingError</span><span class=\"p\">(</span><span class=\"sa\">f</span><span
  class=\"s2\">&quot;recieved padding: </span><span class=\"si\">{</span><span class=\"n\">padding</span><span
  class=\"si\">}</span><span class=\"s2\">&quot;</span><span class=\"p\">)</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"make_cover-function\">make_cover <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>make_cover
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">make_cover</span><span class=\"p\">(</span>\n    <span class=\"n\">title</span><span
  class=\"p\">:</span> <span class=\"nb\">str</span><span class=\"p\">,</span>\n    <span
  class=\"n\">color</span><span class=\"p\">:</span> <span class=\"nb\">str</span><span
  class=\"p\">,</span>\n    <span class=\"n\">output_path</span><span class=\"p\">:</span>
  <span class=\"n\">Path</span><span class=\"p\">,</span>\n    <span class=\"n\">template_path</span><span
  class=\"p\">:</span> <span class=\"n\">Path</span><span class=\"p\">,</span>\n    <span
  class=\"n\">font_path</span><span class=\"p\">:</span> <span class=\"n\">Path</span><span
  class=\"p\">,</span>\n    <span class=\"n\">padding</span><span class=\"p\">:</span>
  <span class=\"n\">Tuple</span><span class=\"p\">[</span><span class=\"nb\">int</span><span
  class=\"p\">,</span> <span class=\"o\">...</span><span class=\"p\">],</span>\n    <span
  class=\"n\">text_font</span><span class=\"p\">:</span> <span class=\"n\">Path</span><span
  class=\"p\">,</span>\n    <span class=\"n\">text</span><span class=\"p\">:</span>
  <span class=\"nb\">str</span> <span class=\"o\">=</span> <span class=\"kc\">None</span><span
  class=\"p\">,</span>\n    <span class=\"n\">text_font_color</span><span class=\"p\">:</span>
  <span class=\"nb\">str</span> <span class=\"o\">=</span> <span class=\"kc\">None</span><span
  class=\"p\">,</span>\n    <span class=\"n\">text_padding</span><span class=\"p\">:</span>
  <span class=\"n\">Tuple</span><span class=\"p\">[</span><span class=\"nb\">int</span><span
  class=\"p\">,</span> <span class=\"o\">...</span><span class=\"p\">]</span> <span
  class=\"o\">=</span> <span class=\"kc\">None</span><span class=\"p\">,</span>\n<span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"kc\">None</span><span
  class=\"p\">:</span>\n    <span class=\"n\">image</span> <span class=\"o\">=</span>
  <span class=\"n\">Image</span><span class=\"o\">.</span><span class=\"n\">open</span><span
  class=\"p\">(</span><span class=\"n\">template_path</span><span class=\"p\">)</span>\n
  \   <span class=\"n\">draw_text</span><span class=\"p\">(</span><span class=\"n\">image</span><span
  class=\"p\">,</span> <span class=\"n\">font_path</span><span class=\"p\">,</span>
  <span class=\"n\">title</span><span class=\"p\">,</span> <span class=\"n\">color</span><span
  class=\"p\">,</span> <span class=\"n\">padding</span><span class=\"p\">)</span>\n
  \   <span class=\"k\">if</span> <span class=\"n\">text</span> <span class=\"ow\">is</span>
  <span class=\"ow\">not</span> <span class=\"kc\">None</span><span class=\"p\">:</span>\n
  \       <span class=\"k\">if</span> <span class=\"n\">text_padding</span> <span
  class=\"ow\">is</span> <span class=\"kc\">None</span><span class=\"p\">:</span>\n
  \           <span class=\"n\">text_padding</span> <span class=\"o\">=</span> <span
  class=\"p\">(</span>\n                <span class=\"n\">image</span><span class=\"o\">.</span><span
  class=\"n\">size</span><span class=\"p\">[</span><span class=\"mi\">1</span><span
  class=\"p\">]</span> <span class=\"o\">-</span> <span class=\"n\">image</span><span
  class=\"o\">.</span><span class=\"n\">size</span><span class=\"p\">[</span><span
  class=\"mi\">1</span><span class=\"p\">]</span> <span class=\"o\">/</span> <span
  class=\"mi\">5</span><span class=\"p\">,</span>\n                <span class=\"n\">image</span><span
  class=\"o\">.</span><span class=\"n\">size</span><span class=\"p\">[</span><span
  class=\"mi\">0</span><span class=\"p\">]</span> <span class=\"o\">/</span> <span
  class=\"mi\">5</span><span class=\"p\">,</span>\n                <span class=\"n\">image</span><span
  class=\"o\">.</span><span class=\"n\">size</span><span class=\"p\">[</span><span
  class=\"mi\">1</span><span class=\"p\">]</span> <span class=\"o\">-</span> <span
  class=\"n\">image</span><span class=\"o\">.</span><span class=\"n\">size</span><span
  class=\"p\">[</span><span class=\"mi\">1</span><span class=\"p\">]</span> <span
  class=\"o\">/</span> <span class=\"mi\">10</span><span class=\"p\">,</span>\n            <span
  class=\"p\">)</span>\n        <span class=\"n\">draw_text</span><span class=\"p\">(</span><span
  class=\"n\">image</span><span class=\"p\">,</span> <span class=\"n\">text_font</span><span
  class=\"p\">,</span> <span class=\"n\">text</span><span class=\"p\">,</span> <span
  class=\"n\">text_font_color</span><span class=\"p\">,</span> <span class=\"n\">text_padding</span><span
  class=\"p\">)</span>\n\n    <span class=\"n\">output_path</span><span class=\"o\">.</span><span
  class=\"n\">parent</span><span class=\"o\">.</span><span class=\"n\">mkdir</span><span
  class=\"p\">(</span><span class=\"n\">exist_ok</span><span class=\"o\">=</span><span
  class=\"kc\">True</span><span class=\"p\">)</span>\n    <span class=\"n\">image</span><span
  class=\"o\">.</span><span class=\"n\">save</span><span class=\"p\">(</span><span
  class=\"n\">output_path</span><span class=\"p\">)</span>\n    <span class=\"n\">ratio</span>
  <span class=\"o\">=</span> <span class=\"n\">image</span><span class=\"o\">.</span><span
  class=\"n\">size</span><span class=\"p\">[</span><span class=\"mi\">1</span><span
  class=\"p\">]</span> <span class=\"o\">/</span> <span class=\"n\">image</span><span
  class=\"o\">.</span><span class=\"n\">size</span><span class=\"p\">[</span><span
  class=\"mi\">0</span><span class=\"p\">]</span>\n\n    <span class=\"n\">covers</span>
  <span class=\"o\">=</span> <span class=\"p\">[]</span>\n    <span class=\"k\">for</span>
  <span class=\"n\">width</span> <span class=\"ow\">in</span> <span class=\"p\">[</span>\n
  \       <span class=\"c1\"># 32,</span>\n        <span class=\"mi\">250</span><span
  class=\"p\">,</span>\n        <span class=\"c1\"># 500,</span>\n    <span class=\"p\">]:</span>\n\n
  \       <span class=\"n\">re_img</span> <span class=\"o\">=</span> <span class=\"n\">image</span><span
  class=\"o\">.</span><span class=\"n\">resize</span><span class=\"p\">((</span><span
  class=\"n\">width</span><span class=\"p\">,</span> <span class=\"nb\">int</span><span
  class=\"p\">(</span><span class=\"n\">width</span> <span class=\"o\">*</span> <span
  class=\"n\">ratio</span><span class=\"p\">)),</span> <span class=\"n\">Image</span><span
  class=\"o\">.</span><span class=\"n\">ANTIALIAS</span><span class=\"p\">)</span>\n
  \       <span class=\"n\">filename</span> <span class=\"o\">=</span> <span class=\"sa\">f</span><span
  class=\"s2\">&quot;</span><span class=\"si\">{</span><span class=\"n\">output_path</span><span
  class=\"o\">.</span><span class=\"n\">stem</span><span class=\"si\">}</span><span
  class=\"s2\">_</span><span class=\"si\">{</span><span class=\"n\">width</span><span
  class=\"si\">}</span><span class=\"s2\">x</span><span class=\"si\">{</span><span
  class=\"nb\">int</span><span class=\"p\">(</span><span class=\"n\">width</span><span
  class=\"o\">*</span><span class=\"n\">ratio</span><span class=\"p\">)</span><span
  class=\"si\">}{</span><span class=\"n\">output_path</span><span class=\"o\">.</span><span
  class=\"n\">suffix</span><span class=\"si\">}</span><span class=\"s2\">&quot;</span>\n
  \       <span class=\"n\">covers</span><span class=\"o\">.</span><span class=\"n\">append</span><span
  class=\"p\">(</span><span class=\"n\">filename</span><span class=\"p\">)</span>\n\n
  \       <span class=\"n\">filepath</span> <span class=\"o\">=</span> <span class=\"n\">Path</span><span
  class=\"p\">(</span><span class=\"n\">output_path</span><span class=\"o\">.</span><span
  class=\"n\">parent</span> <span class=\"o\">/</span> <span class=\"n\">filename</span><span
  class=\"p\">)</span>\n        <span class=\"n\">re_img</span><span class=\"o\">.</span><span
  class=\"n\">save</span><span class=\"p\">(</span><span class=\"n\">filepath</span><span
  class=\"p\">)</span>\n</code></pre></div>\n</details>\n<hr />\n<h2 id=\"save-function\">save
  <code>function</code></h2>\n<p>None</p>\n<details>\n<summary>save source</summary>\n<div
  class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span> <span class=\"nf\">save</span><span
  class=\"p\">(</span><span class=\"n\">markata</span><span class=\"p\">:</span> <span
  class=\"s2\">&quot;Markata&quot;</span><span class=\"p\">)</span> <span class=\"o\">-&gt;</span>
  <span class=\"kc\">None</span><span class=\"p\">:</span>\n    <span class=\"n\">futures</span>
  <span class=\"o\">=</span> <span class=\"p\">[]</span>\n\n    <span class=\"k\">if</span>
  <span class=\"ow\">not</span> <span class=\"nb\">hasattr</span><span class=\"p\">(</span><span
  class=\"n\">markata</span><span class=\"o\">.</span><span class=\"n\">config</span><span
  class=\"p\">,</span> <span class=\"s2\">&quot;covers&quot;</span><span class=\"p\">):</span>\n
  \       <span class=\"k\">return</span>\n\n    <span class=\"k\">for</span> <span
  class=\"n\">article</span> <span class=\"ow\">in</span> <span class=\"n\">markata</span><span
  class=\"o\">.</span><span class=\"n\">articles</span><span class=\"p\">:</span>\n
  \       <span class=\"k\">for</span> <span class=\"n\">cover</span> <span class=\"ow\">in</span>
  <span class=\"n\">markata</span><span class=\"o\">.</span><span class=\"n\">config</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;covers&quot;</span><span class=\"p\">]:</span>\n
  \           <span class=\"k\">try</span><span class=\"p\">:</span>\n                <span
  class=\"n\">padding</span> <span class=\"o\">=</span> <span class=\"n\">cover</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;padding&quot;</span><span class=\"p\">]</span>\n
  \           <span class=\"k\">except</span> <span class=\"ne\">KeyError</span><span
  class=\"p\">:</span>\n                <span class=\"n\">padding</span> <span class=\"o\">=</span>
  <span class=\"p\">(</span>\n                    <span class=\"mi\">200</span><span
  class=\"p\">,</span>\n                    <span class=\"mi\">100</span><span class=\"p\">,</span>\n
  \               <span class=\"p\">)</span>\n            <span class=\"k\">try</span><span
  class=\"p\">:</span>\n                <span class=\"n\">text_padding</span> <span
  class=\"o\">=</span> <span class=\"n\">cover</span><span class=\"p\">[</span><span
  class=\"s2\">&quot;text_padding&quot;</span><span class=\"p\">]</span>\n            <span
  class=\"k\">except</span> <span class=\"ne\">KeyError</span><span class=\"p\">:</span>\n
  \               <span class=\"n\">text_padding</span> <span class=\"o\">=</span>
  <span class=\"p\">(</span>\n                    <span class=\"mi\">200</span><span
  class=\"p\">,</span>\n                    <span class=\"mi\">100</span><span class=\"p\">,</span>\n
  \               <span class=\"p\">)</span>\n            <span class=\"k\">if</span>
  <span class=\"s2\">&quot;text_key&quot;</span> <span class=\"ow\">in</span> <span
  class=\"n\">cover</span><span class=\"p\">:</span>\n                <span class=\"k\">try</span><span
  class=\"p\">:</span>\n                    <span class=\"n\">text</span> <span class=\"o\">=</span>
  <span class=\"n\">article</span><span class=\"o\">.</span><span class=\"n\">metadata</span><span
  class=\"p\">[</span><span class=\"n\">cover</span><span class=\"p\">[</span><span
  class=\"s2\">&quot;text_key&quot;</span><span class=\"p\">]]</span>\n                <span
  class=\"k\">except</span> <span class=\"ne\">AttributeError</span><span class=\"p\">:</span>\n
  \                   <span class=\"n\">text</span> <span class=\"o\">=</span> <span
  class=\"n\">article</span><span class=\"p\">[</span><span class=\"n\">cover</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;text_key&quot;</span><span class=\"p\">]]</span>\n
  \               <span class=\"k\">try</span><span class=\"p\">:</span>\n                    <span
  class=\"n\">text</span> <span class=\"o\">=</span> <span class=\"n\">text</span><span
  class=\"o\">.</span><span class=\"n\">replace</span><span class=\"p\">(</span><span
  class=\"s2\">&quot;</span><span class=\"se\">\\n</span><span class=\"s2\">&quot;</span><span
  class=\"p\">,</span> <span class=\"s2\">&quot;&quot;</span><span class=\"p\">)</span>\n
  \                   <span class=\"kn\">from</span> <span class=\"nn\">more_itertools</span>
  <span class=\"kn\">import</span> <span class=\"n\">chunked</span>\n\n                    <span
  class=\"n\">text</span> <span class=\"o\">=</span> <span class=\"s2\">&quot;</span><span
  class=\"se\">\\n</span><span class=\"s2\">&quot;</span><span class=\"o\">.</span><span
  class=\"n\">join</span><span class=\"p\">([</span><span class=\"s2\">&quot;&quot;</span><span
  class=\"o\">.</span><span class=\"n\">join</span><span class=\"p\">(</span><span
  class=\"n\">c</span><span class=\"p\">)</span> <span class=\"k\">for</span> <span
  class=\"n\">c</span> <span class=\"ow\">in</span> <span class=\"n\">chunked</span><span
  class=\"p\">(</span><span class=\"n\">text</span><span class=\"p\">,</span> <span
  class=\"mi\">60</span><span class=\"p\">)])</span>\n                <span class=\"k\">except</span>
  <span class=\"ne\">AttributeError</span><span class=\"p\">:</span>\n                    <span
  class=\"c1\"># text is likely None</span>\n                    <span class=\"k\">pass</span>\n\n
  \               <span class=\"n\">text_font</span> <span class=\"o\">=</span> <span
  class=\"n\">cover</span><span class=\"p\">[</span><span class=\"s2\">&quot;text_font&quot;</span><span
  class=\"p\">]</span>\n                <span class=\"n\">text_font_color</span> <span
  class=\"o\">=</span> <span class=\"n\">cover</span><span class=\"p\">[</span><span
  class=\"s2\">&quot;text_font_color&quot;</span><span class=\"p\">]</span>\n            <span
  class=\"k\">else</span><span class=\"p\">:</span>\n                <span class=\"n\">text</span>
  <span class=\"o\">=</span> <span class=\"kc\">None</span>\n                <span
  class=\"n\">text_font</span> <span class=\"o\">=</span> <span class=\"kc\">None</span>\n
  \               <span class=\"n\">text_font_color</span> <span class=\"o\">=</span>
  <span class=\"kc\">None</span>\n            <span class=\"k\">try</span><span class=\"p\">:</span>\n
  \               <span class=\"n\">title</span> <span class=\"o\">=</span> <span
  class=\"n\">article</span><span class=\"o\">.</span><span class=\"n\">metadata</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;title&quot;</span><span class=\"p\">]</span>\n
  \           <span class=\"k\">except</span> <span class=\"ne\">AttributeError</span><span
  class=\"p\">:</span>\n                <span class=\"n\">title</span> <span class=\"o\">=</span>
  <span class=\"n\">article</span><span class=\"p\">[</span><span class=\"s2\">&quot;title&quot;</span><span
  class=\"p\">]</span>\n            <span class=\"n\">futures</span><span class=\"o\">.</span><span
  class=\"n\">append</span><span class=\"p\">(</span>\n                <span class=\"n\">make_cover</span><span
  class=\"p\">(</span>\n                    <span class=\"n\">title</span><span class=\"o\">=</span><span
  class=\"n\">title</span><span class=\"p\">,</span>\n                    <span class=\"n\">color</span><span
  class=\"o\">=</span><span class=\"n\">cover</span><span class=\"p\">[</span><span
  class=\"s2\">&quot;font_color&quot;</span><span class=\"p\">],</span>\n                    <span
  class=\"n\">output_path</span><span class=\"o\">=</span><span class=\"n\">Path</span><span
  class=\"p\">(</span><span class=\"n\">markata</span><span class=\"o\">.</span><span
  class=\"n\">config</span><span class=\"p\">[</span><span class=\"s2\">&quot;output_dir&quot;</span><span
  class=\"p\">])</span>\n                    <span class=\"o\">/</span> <span class=\"p\">(</span><span
  class=\"n\">article</span><span class=\"p\">[</span><span class=\"s2\">&quot;slug&quot;</span><span
  class=\"p\">]</span> <span class=\"o\">+</span> <span class=\"n\">cover</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;name&quot;</span><span class=\"p\">]</span>
  <span class=\"o\">+</span> <span class=\"s2\">&quot;.png&quot;</span><span class=\"p\">),</span>\n
  \                   <span class=\"n\">template_path</span><span class=\"o\">=</span><span
  class=\"n\">cover</span><span class=\"p\">[</span><span class=\"s2\">&quot;template&quot;</span><span
  class=\"p\">],</span>\n                    <span class=\"n\">font_path</span><span
  class=\"o\">=</span><span class=\"n\">cover</span><span class=\"p\">[</span><span
  class=\"s2\">&quot;font&quot;</span><span class=\"p\">],</span>\n                    <span
  class=\"n\">padding</span><span class=\"o\">=</span><span class=\"n\">padding</span><span
  class=\"p\">,</span>\n                    <span class=\"n\">text_font</span><span
  class=\"o\">=</span><span class=\"n\">text_font</span><span class=\"p\">,</span>\n
  \                   <span class=\"n\">text</span><span class=\"o\">=</span><span
  class=\"n\">text</span><span class=\"p\">,</span>\n                    <span class=\"n\">text_font_color</span><span
  class=\"o\">=</span><span class=\"n\">text_font_color</span><span class=\"p\">,</span>\n
  \                   <span class=\"n\">text_padding</span><span class=\"o\">=</span><span
  class=\"n\">text_padding</span><span class=\"p\">,</span>\n                <span
  class=\"p\">)</span>\n            <span class=\"p\">)</span>\n\n    <span class=\"n\">progress</span>
  <span class=\"o\">=</span> <span class=\"n\">Progress</span><span class=\"p\">(</span>\n
  \       <span class=\"n\">BarColumn</span><span class=\"p\">(</span><span class=\"n\">bar_width</span><span
  class=\"o\">=</span><span class=\"kc\">None</span><span class=\"p\">),</span> <span
  class=\"n\">transient</span><span class=\"o\">=</span><span class=\"kc\">True</span><span
  class=\"p\">,</span> <span class=\"n\">console</span><span class=\"o\">=</span><span
  class=\"n\">markata</span><span class=\"o\">.</span><span class=\"n\">console</span>\n
  \   <span class=\"p\">)</span>\n    <span class=\"n\">task_id</span> <span class=\"o\">=</span>
  <span class=\"n\">progress</span><span class=\"o\">.</span><span class=\"n\">add_task</span><span
  class=\"p\">(</span><span class=\"s2\">&quot;loading markdown&quot;</span><span
  class=\"p\">)</span>\n    <span class=\"n\">progress</span><span class=\"o\">.</span><span
  class=\"n\">update</span><span class=\"p\">(</span><span class=\"n\">task_id</span><span
  class=\"p\">,</span> <span class=\"n\">total</span><span class=\"o\">=</span><span
  class=\"nb\">len</span><span class=\"p\">(</span><span class=\"n\">futures</span><span
  class=\"p\">))</span>\n    <span class=\"k\">with</span> <span class=\"n\">progress</span><span
  class=\"p\">:</span>\n        <span class=\"k\">while</span> <span class=\"ow\">not</span>
  <span class=\"nb\">all</span><span class=\"p\">([</span><span class=\"n\">f</span><span
  class=\"o\">.</span><span class=\"n\">done</span><span class=\"p\">()</span> <span
  class=\"k\">for</span> <span class=\"n\">f</span> <span class=\"ow\">in</span> <span
  class=\"n\">futures</span><span class=\"p\">]):</span>\n            <span class=\"n\">time</span><span
  class=\"o\">.</span><span class=\"n\">sleep</span><span class=\"p\">(</span><span
  class=\"mf\">0.1</span><span class=\"p\">)</span>\n            <span class=\"n\">progress</span><span
  class=\"o\">.</span><span class=\"n\">update</span><span class=\"p\">(</span><span
  class=\"n\">task_id</span><span class=\"p\">,</span> <span class=\"n\">total</span><span
  class=\"o\">=</span><span class=\"nb\">len</span><span class=\"p\">([</span><span
  class=\"n\">f</span> <span class=\"k\">for</span> <span class=\"n\">f</span> <span
  class=\"ow\">in</span> <span class=\"n\">futures</span> <span class=\"k\">if</span>
  <span class=\"n\">f</span><span class=\"o\">.</span><span class=\"n\">done</span><span
  class=\"p\">()]))</span>\n    <span class=\"p\">[</span><span class=\"n\">f</span><span
  class=\"o\">.</span><span class=\"n\">result</span><span class=\"p\">()</span> <span
  class=\"k\">for</span> <span class=\"n\">f</span> <span class=\"ow\">in</span> <span
  class=\"n\">futures</span><span class=\"p\">]</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"init-method\"><strong>init</strong> <code>method</code></h2>\n<p>None</p>\n<details>\n<summary><strong>init</strong>
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"fm\">__init__</span><span class=\"p\">(</span>\n        <span class=\"bp\">self</span><span
  class=\"p\">,</span>\n        <span class=\"n\">msg</span><span class=\"p\">:</span>
  <span class=\"nb\">str</span> <span class=\"o\">=</span> <span class=\"s2\">&quot;&quot;</span><span
  class=\"p\">,</span>\n    <span class=\"p\">)</span> <span class=\"o\">-&gt;</span>
  <span class=\"kc\">None</span><span class=\"p\">:</span>\n        <span class=\"nb\">super</span><span
  class=\"p\">()</span><span class=\"o\">.</span><span class=\"fm\">__init__</span><span
  class=\"p\">(</span>\n            <span class=\"s2\">&quot;Padding must be an iterable
  of length 1, 2, 3, or 4.</span><span class=\"se\">\\n</span><span class=\"s2\">&quot;</span>
  <span class=\"o\">+</span> <span class=\"n\">msg</span><span class=\"p\">,</span>\n
  \       <span class=\"p\">)</span>\n</code></pre></div>\n</details>"
datetime: null
description: Docs for covers
long_description: ''
now: 2022-02-05 19:38:00.891385
path: covers.md
slug: markata/plugins/covers
status: published
title: covers.py
today: 2022-02-05
---

---

## _load_font `function`

None

??? "_load_font source"
    ``` python
    def _load_font(path: Path, size: int) -> ImageFont.FreeTypeFont:
        return ImageFont.truetype(path, size=size)
    ```


---

## get_font `function`

None

??? "get_font source"
    ``` python
    def get_font(
        path: Path,
        draw: ImageDraw.Draw,
        title: str,
        size: int = 250,
        max_size: tuple = (800, 220),
    ) -> ImageFont.FreeTypeFont:
        title = title or ""
        font = _load_font(path, size)
        current_size = draw.textsize(title, font=font)

        if current_size[0] > max_size[0] or current_size[1] > max_size[1]:
            return get_font(path, draw, title, size - 10, max_size=max_size)
        return font
    ```


---

## PaddingError `class`

None

??? "PaddingError source"
    ``` python
    class PaddingError(BaseException):
        def __init__(
            self,
            msg: str = "",
        ) -> None:
            super().__init__(
                "Padding must be an iterable of length 1, 2, 3, or 4.\n" + msg,
            )
    ```


---

## draw_text `function`

None

??? "draw_text source"
    ``` python
    def draw_text(
        image: Image,
        font_path: Path,
        text: str,
        color: Union[str, None],
        padding: Tuple[int, ...],
    ) -> None:
        text = text or ""
        draw = ImageDraw.Draw(image)
        padding = resolve_padding(padding)
        width = image.size[0]
        height = image.size[1]
        bounding_box = [padding[0], padding[1], width - padding[0], height - padding[1]]
        bounding_box = [padding[0], padding[1], width - padding[2], height - padding[3]]
        max_size = (bounding_box[2] - bounding_box[0], bounding_box[3] - bounding_box[1])
        x1, y1, x2, y2 = bounding_box
        font = get_font(font_path, draw, text, max_size=max_size)
        w, h = draw.textsize(text, font=font)
        x = (x2 - x1 - w) / 2 + x1
        y = (y2 - y1 - h) / 2 + y1
        draw.text((x, y), text, fill=color, font=font, align="center")
    ```


---

## resolve_padding `function`

Convert padding to a len 4 tuple

??? "resolve_padding source"
    ``` python
    def resolve_padding(padding: Tuple[int, ...]) -> Tuple[int, ...]:
        """Convert padding to a len 4 tuple"""
        if len(padding) == 4:
            return padding
        if len(padding) == 3:
            return (*padding, padding[1])
        if len(padding) == 2:
            return padding * 2
        if len(padding) == 1:
            return padding * 4
        raise PaddingError(f"recieved padding: {padding}")
    ```


---

## make_cover `function`

None

??? "make_cover source"
    ``` python
    def make_cover(
        title: str,
        color: str,
        output_path: Path,
        template_path: Path,
        font_path: Path,
        padding: Tuple[int, ...],
        text_font: Path,
        text: str = None,
        text_font_color: str = None,
        text_padding: Tuple[int, ...] = None,
    ) -> None:
        image = Image.open(template_path)
        draw_text(image, font_path, title, color, padding)
        if text is not None:
            if text_padding is None:
                text_padding = (
                    image.size[1] - image.size[1] / 5,
                    image.size[0] / 5,
                    image.size[1] - image.size[1] / 10,
                )
            draw_text(image, text_font, text, text_font_color, text_padding)

        output_path.parent.mkdir(exist_ok=True)
        image.save(output_path)
        ratio = image.size[1] / image.size[0]

        covers = []
        for width in [
            # 32,
            250,
            # 500,
        ]:

            re_img = image.resize((width, int(width * ratio)), Image.ANTIALIAS)
            filename = f"{output_path.stem}_{width}x{int(width*ratio)}{output_path.suffix}"
            covers.append(filename)

            filepath = Path(output_path.parent / filename)
            re_img.save(filepath)
    ```


---

## save `function`

None

??? "save source"
    ``` python
    def save(markata: "Markata") -> None:
        futures = []

        if not hasattr(markata.config, "covers"):
            return

        for article in markata.articles:
            for cover in markata.config["covers"]:
                try:
                    padding = cover["padding"]
                except KeyError:
                    padding = (
                        200,
                        100,
                    )
                try:
                    text_padding = cover["text_padding"]
                except KeyError:
                    text_padding = (
                        200,
                        100,
                    )
                if "text_key" in cover:
                    try:
                        text = article.metadata[cover["text_key"]]
                    except AttributeError:
                        text = article[cover["text_key"]]
                    try:
                        text = text.replace("\n", "")
                        from more_itertools import chunked

                        text = "\n".join(["".join(c) for c in chunked(text, 60)])
                    except AttributeError:
                        # text is likely None
                        pass

                    text_font = cover["text_font"]
                    text_font_color = cover["text_font_color"]
                else:
                    text = None
                    text_font = None
                    text_font_color = None
                try:
                    title = article.metadata["title"]
                except AttributeError:
                    title = article["title"]
                futures.append(
                    make_cover(
                        title=title,
                        color=cover["font_color"],
                        output_path=Path(markata.config["output_dir"])
                        / (article["slug"] + cover["name"] + ".png"),
                        template_path=cover["template"],
                        font_path=cover["font"],
                        padding=padding,
                        text_font=text_font,
                        text=text,
                        text_font_color=text_font_color,
                        text_padding=text_padding,
                    )
                )

        progress = Progress(
            BarColumn(bar_width=None), transient=True, console=markata.console
        )
        task_id = progress.add_task("loading markdown")
        progress.update(task_id, total=len(futures))
        with progress:
            while not all([f.done() for f in futures]):
                time.sleep(0.1)
                progress.update(task_id, total=len([f for f in futures if f.done()]))
        [f.result() for f in futures]
    ```


---

## __init__ `method`

None

??? "__init__ source"
    ``` python
    def __init__(
            self,
            msg: str = "",
        ) -> None:
            super().__init__(
                "Padding must be an iterable of length 1, 2, 3, or 4.\n" + msg,
            )
    ```