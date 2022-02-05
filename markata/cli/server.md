---
article_html: "<hr />\n<h2 id=\"find_port-function\">find_port <code>function</code></h2>\n<p>Find
  a port not in ues starting at given port</p>\n<details>\n<summary>find_port source</summary>\n<div
  class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span> <span class=\"nf\">find_port</span><span
  class=\"p\">(</span><span class=\"n\">port</span><span class=\"p\">:</span> <span
  class=\"nb\">int</span> <span class=\"o\">=</span> <span class=\"mi\">8000</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"nb\">int</span><span
  class=\"p\">:</span>\n    <span class=\"sd\">&quot;&quot;&quot;Find a port not in
  ues starting at given port&quot;&quot;&quot;</span>\n    <span class=\"kn\">import</span>
  <span class=\"nn\">socket</span>\n\n    <span class=\"k\">with</span> <span class=\"n\">socket</span><span
  class=\"o\">.</span><span class=\"n\">socket</span><span class=\"p\">(</span><span
  class=\"n\">socket</span><span class=\"o\">.</span><span class=\"n\">AF_INET</span><span
  class=\"p\">,</span> <span class=\"n\">socket</span><span class=\"o\">.</span><span
  class=\"n\">SOCK_STREAM</span><span class=\"p\">)</span> <span class=\"k\">as</span>
  <span class=\"n\">s</span><span class=\"p\">:</span>\n        <span class=\"k\">if</span>
  <span class=\"n\">s</span><span class=\"o\">.</span><span class=\"n\">connect_ex</span><span
  class=\"p\">((</span><span class=\"s2\">&quot;localhost&quot;</span><span class=\"p\">,</span>
  <span class=\"n\">port</span><span class=\"p\">))</span> <span class=\"o\">==</span>
  <span class=\"mi\">0</span><span class=\"p\">:</span>\n            <span class=\"k\">return</span>
  <span class=\"n\">find_port</span><span class=\"p\">(</span><span class=\"n\">port</span><span
  class=\"o\">=</span><span class=\"n\">port</span> <span class=\"o\">+</span> <span
  class=\"mi\">1</span><span class=\"p\">)</span>\n        <span class=\"k\">else</span><span
  class=\"p\">:</span>\n            <span class=\"k\">return</span> <span class=\"n\">port</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"server-class\">Server <code>class</code></h2>\n<p>None</p>\n<details>\n<summary>Server
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">class</span>
  <span class=\"nc\">Server</span><span class=\"p\">:</span>\n    <span class=\"k\">def</span>
  <span class=\"fm\">__init__</span><span class=\"p\">(</span>\n        <span class=\"bp\">self</span><span
  class=\"p\">,</span>\n        <span class=\"n\">auto_restart</span><span class=\"p\">:</span>
  <span class=\"nb\">bool</span> <span class=\"o\">=</span> <span class=\"kc\">True</span><span
  class=\"p\">,</span>\n        <span class=\"n\">directory</span><span class=\"p\">:</span>
  <span class=\"n\">Union</span><span class=\"p\">[</span><span class=\"nb\">str</span><span
  class=\"p\">,</span> <span class=\"s2\">&quot;Path&quot;</span><span class=\"p\">]</span>
  <span class=\"o\">=</span> <span class=\"kc\">None</span><span class=\"p\">,</span>\n
  \       <span class=\"n\">port</span><span class=\"p\">:</span> <span class=\"nb\">int</span>
  <span class=\"o\">=</span> <span class=\"mi\">8000</span><span class=\"p\">,</span>\n
  \   <span class=\"p\">):</span>\n        <span class=\"k\">if</span> <span class=\"n\">directory</span>
  <span class=\"ow\">is</span> <span class=\"kc\">None</span><span class=\"p\">:</span>\n
  \           <span class=\"kn\">from</span> <span class=\"nn\">markata</span> <span
  class=\"kn\">import</span> <span class=\"n\">Markata</span>\n\n            <span
  class=\"n\">m</span> <span class=\"o\">=</span> <span class=\"n\">Markata</span><span
  class=\"p\">()</span>\n            <span class=\"n\">directory</span> <span class=\"o\">=</span>
  <span class=\"n\">Path</span><span class=\"p\">(</span><span class=\"nb\">str</span><span
  class=\"p\">(</span><span class=\"n\">m</span><span class=\"o\">.</span><span class=\"n\">config</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;output_dir&quot;</span><span class=\"p\">]))</span>\n\n
  \       <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">auto_restart</span>
  <span class=\"o\">=</span> <span class=\"n\">auto_restart</span>\n        <span
  class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">directory</span>
  <span class=\"o\">=</span> <span class=\"n\">directory</span>\n        <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">port</span> <span class=\"o\">=</span> <span
  class=\"n\">find_port</span><span class=\"p\">(</span><span class=\"n\">port</span><span
  class=\"o\">=</span><span class=\"n\">port</span><span class=\"p\">)</span>\n        <span
  class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">start_server</span><span
  class=\"p\">()</span>\n        <span class=\"n\">atexit</span><span class=\"o\">.</span><span
  class=\"n\">register</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">kill</span><span class=\"p\">)</span>\n\n
  \   <span class=\"k\">def</span> <span class=\"nf\">start_server</span><span class=\"p\">(</span><span
  class=\"bp\">self</span><span class=\"p\">)</span> <span class=\"o\">-&gt;</span>
  <span class=\"kc\">None</span><span class=\"p\">:</span>\n        <span class=\"kn\">import</span>
  <span class=\"nn\">subprocess</span>\n\n        <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">cmd</span> <span class=\"o\">=</span> <span
  class=\"p\">[</span>\n            <span class=\"s2\">&quot;python&quot;</span><span
  class=\"p\">,</span>\n            <span class=\"s2\">&quot;-m&quot;</span><span
  class=\"p\">,</span>\n            <span class=\"s2\">&quot;http.server&quot;</span><span
  class=\"p\">,</span>\n            <span class=\"nb\">str</span><span class=\"p\">(</span><span
  class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">port</span><span
  class=\"p\">),</span>\n            <span class=\"s2\">&quot;--directory&quot;</span><span
  class=\"p\">,</span>\n            <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">directory</span><span class=\"p\">,</span>\n        <span class=\"p\">]</span>\n\n
  \       <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">proc</span>
  <span class=\"o\">=</span> <span class=\"n\">subprocess</span><span class=\"o\">.</span><span
  class=\"n\">Popen</span><span class=\"p\">(</span>\n            <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">cmd</span><span class=\"p\">,</span>\n            <span
  class=\"n\">stderr</span><span class=\"o\">=</span><span class=\"n\">subprocess</span><span
  class=\"o\">.</span><span class=\"n\">PIPE</span><span class=\"p\">,</span>\n            <span
  class=\"n\">stdout</span><span class=\"o\">=</span><span class=\"n\">subprocess</span><span
  class=\"o\">.</span><span class=\"n\">PIPE</span><span class=\"p\">,</span>\n        <span
  class=\"p\">)</span>\n        <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">start_time</span> <span class=\"o\">=</span> <span class=\"n\">time</span><span
  class=\"o\">.</span><span class=\"n\">time</span><span class=\"p\">()</span>\n\n
  \   <span class=\"nd\">@property</span>\n    <span class=\"k\">def</span> <span
  class=\"nf\">uptime</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"nb\">int</span><span
  class=\"p\">:</span>\n        <span class=\"k\">return</span> <span class=\"nb\">round</span><span
  class=\"p\">(</span><span class=\"n\">time</span><span class=\"o\">.</span><span
  class=\"n\">time</span><span class=\"p\">()</span> <span class=\"o\">-</span> <span
  class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">start_time</span><span
  class=\"p\">)</span>\n\n    <span class=\"k\">def</span> <span class=\"nf\">kill</span><span
  class=\"p\">(</span><span class=\"bp\">self</span><span class=\"p\">)</span> <span
  class=\"o\">-&gt;</span> <span class=\"kc\">None</span><span class=\"p\">:</span>\n
  \       <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">auto_restart</span>
  <span class=\"o\">=</span> <span class=\"kc\">False</span>\n        <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">proc</span><span class=\"o\">.</span><span
  class=\"n\">kill</span><span class=\"p\">()</span>\n\n    <span class=\"k\">def</span>
  <span class=\"nf\">__rich__</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"n\">Panel</span><span
  class=\"p\">:</span>\n        <span class=\"k\">if</span> <span class=\"ow\">not</span>
  <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">proc</span><span
  class=\"o\">.</span><span class=\"n\">poll</span><span class=\"p\">():</span>\n
  \           <span class=\"k\">return</span> <span class=\"n\">Panel</span><span
  class=\"p\">(</span>\n                <span class=\"sa\">f</span><span class=\"s2\">&quot;[green]serving
  on port: [gold1]</span><span class=\"si\">{</span><span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">port</span><span class=\"si\">}</span><span
  class=\"s2\"> [green]using pid: [gold1]</span><span class=\"si\">{</span><span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">proc</span><span class=\"o\">.</span><span
  class=\"n\">pid</span><span class=\"si\">}</span><span class=\"s2\"> [green]uptime:
  [gold1]</span><span class=\"si\">{</span><span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">uptime</span><span class=\"si\">}</span><span class=\"s2\"> [green]link:
  [gold1] http://localhost:</span><span class=\"si\">{</span><span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">port</span><span class=\"si\">}</span><span
  class=\"s2\">[/]&quot;</span><span class=\"p\">,</span>\n                <span class=\"n\">border_style</span><span
  class=\"o\">=</span><span class=\"s2\">&quot;blue&quot;</span><span class=\"p\">,</span>\n
  \               <span class=\"n\">title</span><span class=\"o\">=</span><span class=\"s2\">&quot;server&quot;</span><span
  class=\"p\">,</span>\n            <span class=\"p\">)</span>\n\n        <span class=\"k\">else</span><span
  class=\"p\">:</span>\n\n            <span class=\"k\">return</span> <span class=\"n\">Panel</span><span
  class=\"p\">(</span><span class=\"sa\">f</span><span class=\"s2\">&quot;[red]server
  died&quot;</span><span class=\"p\">,</span> <span class=\"n\">title</span><span
  class=\"o\">=</span><span class=\"s2\">&quot;server&quot;</span><span class=\"p\">,</span>
  <span class=\"n\">border_style</span><span class=\"o\">=</span><span class=\"s2\">&quot;red&quot;</span><span
  class=\"p\">)</span>\n</code></pre></div>\n</details>\n<hr />\n<h2 id=\"init-method\"><strong>init</strong>
  <code>method</code></h2>\n<p>None</p>\n<details>\n<summary><strong>init</strong>
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"fm\">__init__</span><span class=\"p\">(</span>\n        <span class=\"bp\">self</span><span
  class=\"p\">,</span>\n        <span class=\"n\">auto_restart</span><span class=\"p\">:</span>
  <span class=\"nb\">bool</span> <span class=\"o\">=</span> <span class=\"kc\">True</span><span
  class=\"p\">,</span>\n        <span class=\"n\">directory</span><span class=\"p\">:</span>
  <span class=\"n\">Union</span><span class=\"p\">[</span><span class=\"nb\">str</span><span
  class=\"p\">,</span> <span class=\"s2\">&quot;Path&quot;</span><span class=\"p\">]</span>
  <span class=\"o\">=</span> <span class=\"kc\">None</span><span class=\"p\">,</span>\n
  \       <span class=\"n\">port</span><span class=\"p\">:</span> <span class=\"nb\">int</span>
  <span class=\"o\">=</span> <span class=\"mi\">8000</span><span class=\"p\">,</span>\n
  \   <span class=\"p\">):</span>\n        <span class=\"k\">if</span> <span class=\"n\">directory</span>
  <span class=\"ow\">is</span> <span class=\"kc\">None</span><span class=\"p\">:</span>\n
  \           <span class=\"kn\">from</span> <span class=\"nn\">markata</span> <span
  class=\"kn\">import</span> <span class=\"n\">Markata</span>\n\n            <span
  class=\"n\">m</span> <span class=\"o\">=</span> <span class=\"n\">Markata</span><span
  class=\"p\">()</span>\n            <span class=\"n\">directory</span> <span class=\"o\">=</span>
  <span class=\"n\">Path</span><span class=\"p\">(</span><span class=\"nb\">str</span><span
  class=\"p\">(</span><span class=\"n\">m</span><span class=\"o\">.</span><span class=\"n\">config</span><span
  class=\"p\">[</span><span class=\"s2\">&quot;output_dir&quot;</span><span class=\"p\">]))</span>\n\n
  \       <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">auto_restart</span>
  <span class=\"o\">=</span> <span class=\"n\">auto_restart</span>\n        <span
  class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">directory</span>
  <span class=\"o\">=</span> <span class=\"n\">directory</span>\n        <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">port</span> <span class=\"o\">=</span> <span
  class=\"n\">find_port</span><span class=\"p\">(</span><span class=\"n\">port</span><span
  class=\"o\">=</span><span class=\"n\">port</span><span class=\"p\">)</span>\n        <span
  class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">start_server</span><span
  class=\"p\">()</span>\n        <span class=\"n\">atexit</span><span class=\"o\">.</span><span
  class=\"n\">register</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">kill</span><span class=\"p\">)</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"start_server-method\">start_server <code>method</code></h2>\n<p>None</p>\n<details>\n<summary>start_server
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">start_server</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"kc\">None</span><span
  class=\"p\">:</span>\n        <span class=\"kn\">import</span> <span class=\"nn\">subprocess</span>\n\n
  \       <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">cmd</span>
  <span class=\"o\">=</span> <span class=\"p\">[</span>\n            <span class=\"s2\">&quot;python&quot;</span><span
  class=\"p\">,</span>\n            <span class=\"s2\">&quot;-m&quot;</span><span
  class=\"p\">,</span>\n            <span class=\"s2\">&quot;http.server&quot;</span><span
  class=\"p\">,</span>\n            <span class=\"nb\">str</span><span class=\"p\">(</span><span
  class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">port</span><span
  class=\"p\">),</span>\n            <span class=\"s2\">&quot;--directory&quot;</span><span
  class=\"p\">,</span>\n            <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">directory</span><span class=\"p\">,</span>\n        <span class=\"p\">]</span>\n\n
  \       <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">proc</span>
  <span class=\"o\">=</span> <span class=\"n\">subprocess</span><span class=\"o\">.</span><span
  class=\"n\">Popen</span><span class=\"p\">(</span>\n            <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">cmd</span><span class=\"p\">,</span>\n            <span
  class=\"n\">stderr</span><span class=\"o\">=</span><span class=\"n\">subprocess</span><span
  class=\"o\">.</span><span class=\"n\">PIPE</span><span class=\"p\">,</span>\n            <span
  class=\"n\">stdout</span><span class=\"o\">=</span><span class=\"n\">subprocess</span><span
  class=\"o\">.</span><span class=\"n\">PIPE</span><span class=\"p\">,</span>\n        <span
  class=\"p\">)</span>\n        <span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">start_time</span> <span class=\"o\">=</span> <span class=\"n\">time</span><span
  class=\"o\">.</span><span class=\"n\">time</span><span class=\"p\">()</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"uptime-method\">uptime <code>method</code></h2>\n<p>None</p>\n<details>\n<summary>uptime
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">uptime</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"nb\">int</span><span
  class=\"p\">:</span>\n        <span class=\"k\">return</span> <span class=\"nb\">round</span><span
  class=\"p\">(</span><span class=\"n\">time</span><span class=\"o\">.</span><span
  class=\"n\">time</span><span class=\"p\">()</span> <span class=\"o\">-</span> <span
  class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">start_time</span><span
  class=\"p\">)</span>\n</code></pre></div>\n</details>\n<hr />\n<h2 id=\"kill-method\">kill
  <code>method</code></h2>\n<p>None</p>\n<details>\n<summary>kill source</summary>\n<div
  class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span> <span class=\"nf\">kill</span><span
  class=\"p\">(</span><span class=\"bp\">self</span><span class=\"p\">)</span> <span
  class=\"o\">-&gt;</span> <span class=\"kc\">None</span><span class=\"p\">:</span>\n
  \       <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">auto_restart</span>
  <span class=\"o\">=</span> <span class=\"kc\">False</span>\n        <span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">proc</span><span class=\"o\">.</span><span
  class=\"n\">kill</span><span class=\"p\">()</span>\n</code></pre></div>\n</details>\n<hr
  />\n<h2 id=\"rich-method\"><strong>rich</strong> <code>method</code></h2>\n<p>None</p>\n<details>\n<summary><strong>rich</strong>
  source</summary>\n<div class=\"highlight\"><pre><span></span><code><span class=\"k\">def</span>
  <span class=\"nf\">__rich__</span><span class=\"p\">(</span><span class=\"bp\">self</span><span
  class=\"p\">)</span> <span class=\"o\">-&gt;</span> <span class=\"n\">Panel</span><span
  class=\"p\">:</span>\n        <span class=\"k\">if</span> <span class=\"ow\">not</span>
  <span class=\"bp\">self</span><span class=\"o\">.</span><span class=\"n\">proc</span><span
  class=\"o\">.</span><span class=\"n\">poll</span><span class=\"p\">():</span>\n
  \           <span class=\"k\">return</span> <span class=\"n\">Panel</span><span
  class=\"p\">(</span>\n                <span class=\"sa\">f</span><span class=\"s2\">&quot;[green]serving
  on port: [gold1]</span><span class=\"si\">{</span><span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">port</span><span class=\"si\">}</span><span
  class=\"s2\"> [green]using pid: [gold1]</span><span class=\"si\">{</span><span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">proc</span><span class=\"o\">.</span><span
  class=\"n\">pid</span><span class=\"si\">}</span><span class=\"s2\"> [green]uptime:
  [gold1]</span><span class=\"si\">{</span><span class=\"bp\">self</span><span class=\"o\">.</span><span
  class=\"n\">uptime</span><span class=\"si\">}</span><span class=\"s2\"> [green]link:
  [gold1] http://localhost:</span><span class=\"si\">{</span><span class=\"bp\">self</span><span
  class=\"o\">.</span><span class=\"n\">port</span><span class=\"si\">}</span><span
  class=\"s2\">[/]&quot;</span><span class=\"p\">,</span>\n                <span class=\"n\">border_style</span><span
  class=\"o\">=</span><span class=\"s2\">&quot;blue&quot;</span><span class=\"p\">,</span>\n
  \               <span class=\"n\">title</span><span class=\"o\">=</span><span class=\"s2\">&quot;server&quot;</span><span
  class=\"p\">,</span>\n            <span class=\"p\">)</span>\n\n        <span class=\"k\">else</span><span
  class=\"p\">:</span>\n\n            <span class=\"k\">return</span> <span class=\"n\">Panel</span><span
  class=\"p\">(</span><span class=\"sa\">f</span><span class=\"s2\">&quot;[red]server
  died&quot;</span><span class=\"p\">,</span> <span class=\"n\">title</span><span
  class=\"o\">=</span><span class=\"s2\">&quot;server&quot;</span><span class=\"p\">,</span>
  <span class=\"n\">border_style</span><span class=\"o\">=</span><span class=\"s2\">&quot;red&quot;</span><span
  class=\"p\">)</span>\n</code></pre></div>\n</details>"
datetime: null
description: Docs for server
long_description: ''
now: 2022-02-05 19:38:00.891459
path: server.md
slug: markata/cli/server
status: published
title: server.py
today: 2022-02-05
---

---

## find_port `function`

Find a port not in ues starting at given port

??? "find_port source"
    ``` python
    def find_port(port: int = 8000) -> int:
        """Find a port not in ues starting at given port"""
        import socket

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(("localhost", port)) == 0:
                return find_port(port=port + 1)
            else:
                return port
    ```


---

## Server `class`

None

??? "Server source"
    ``` python
    class Server:
        def __init__(
            self,
            auto_restart: bool = True,
            directory: Union[str, "Path"] = None,
            port: int = 8000,
        ):
            if directory is None:
                from markata import Markata

                m = Markata()
                directory = Path(str(m.config["output_dir"]))

            self.auto_restart = auto_restart
            self.directory = directory
            self.port = find_port(port=port)
            self.start_server()
            atexit.register(self.kill)

        def start_server(self) -> None:
            import subprocess

            self.cmd = [
                "python",
                "-m",
                "http.server",
                str(self.port),
                "--directory",
                self.directory,
            ]

            self.proc = subprocess.Popen(
                self.cmd,
                stderr=subprocess.PIPE,
                stdout=subprocess.PIPE,
            )
            self.start_time = time.time()

        @property
        def uptime(self) -> int:
            return round(time.time() - self.start_time)

        def kill(self) -> None:
            self.auto_restart = False
            self.proc.kill()

        def __rich__(self) -> Panel:
            if not self.proc.poll():
                return Panel(
                    f"[green]serving on port: [gold1]{self.port} [green]using pid: [gold1]{self.proc.pid} [green]uptime: [gold1]{self.uptime} [green]link: [gold1] http://localhost:{self.port}[/]",
                    border_style="blue",
                    title="server",
                )

            else:

                return Panel(f"[red]server died", title="server", border_style="red")
    ```


---

## __init__ `method`

None

??? "__init__ source"
    ``` python
    def __init__(
            self,
            auto_restart: bool = True,
            directory: Union[str, "Path"] = None,
            port: int = 8000,
        ):
            if directory is None:
                from markata import Markata

                m = Markata()
                directory = Path(str(m.config["output_dir"]))

            self.auto_restart = auto_restart
            self.directory = directory
            self.port = find_port(port=port)
            self.start_server()
            atexit.register(self.kill)
    ```


---

## start_server `method`

None

??? "start_server source"
    ``` python
    def start_server(self) -> None:
            import subprocess

            self.cmd = [
                "python",
                "-m",
                "http.server",
                str(self.port),
                "--directory",
                self.directory,
            ]

            self.proc = subprocess.Popen(
                self.cmd,
                stderr=subprocess.PIPE,
                stdout=subprocess.PIPE,
            )
            self.start_time = time.time()
    ```


---

## uptime `method`

None

??? "uptime source"
    ``` python
    def uptime(self) -> int:
            return round(time.time() - self.start_time)
    ```


---

## kill `method`

None

??? "kill source"
    ``` python
    def kill(self) -> None:
            self.auto_restart = False
            self.proc.kill()
    ```


---

## __rich__ `method`

None

??? "__rich__ source"
    ``` python
    def __rich__(self) -> Panel:
            if not self.proc.poll():
                return Panel(
                    f"[green]serving on port: [gold1]{self.port} [green]using pid: [gold1]{self.proc.pid} [green]uptime: [gold1]{self.uptime} [green]link: [gold1] http://localhost:{self.port}[/]",
                    border_style="blue",
                    title="server",
                )

            else:

                return Panel(f"[red]server died", title="server", border_style="red")
    ```