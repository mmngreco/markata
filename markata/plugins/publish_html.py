from pathlib import Path
from typing import TYPE_CHECKING

from markata.hookspec import hook_impl

if TYPE_CHECKING:
    from markata import Markata


@hook_impl
def save(markata: "Markata") -> None:
    output_dir = Path(markata.config["output_dir"])  # type: ignore
    output_dir.mkdir(parents=True, exist_ok=True)

    for article in markata.articles:
        if article["slug"] == "index":
            article_path = output_dir / "index.html"
        else:
            article_path = output_dir / article["slug"] / "index.html"
        article_path.parent.mkdir(parents=True, exist_ok=True)
        with open(article_path, "w+") as f:
            f.write(article.html)
