from markata.hookspec import hook_impl
from pathlib import Path

import shutil

from tqdm import tqdm


@hook_impl
def save(markata):
    try:
        output_dir = Path(markata.config["output_dir"])
        assets_dir = Path(markata.config["assets_dir"])
    except KeyError:
        return

    with tqdm(
        total=len(markata.articles),
        desc="copying assets",
        leave=False,
        colour="yellow",
    ) as pbar:
        shutil.copytree(assets_dir, output_dir, dirs_exist_ok=True)