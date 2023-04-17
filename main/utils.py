File changed: main/utils.py

from PIL import Image


def identify_image(image_path):
    try:
        with Image.open(image_path) as im:
            return f"{image_path} {im.format} {im.size}x{im.mode}"
    except OSError:
        pass

