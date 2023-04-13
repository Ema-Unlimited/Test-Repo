from pathlib import Path
from main.utils import identify_image


def run():
    path = Path("verycool.webp")
    return identify_image(path)


print(run())
