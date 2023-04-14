Update:

from PIL import Image

to:

from PIL import Image, ImageOps


def identify_image(image_path):
    try:
        with Image.open(image_path) as im:
            inverted_image = ImageOps.invert(im)
            return f"{image_path} {inverted_image.format} {inverted_image.size[0]}x{inverted_image.size[1]} {inverted_image.mode}"
    except OSError:
        pass
