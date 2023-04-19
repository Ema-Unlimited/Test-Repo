from PIL import Image


def identify_image(image_path):
    try:
        with Image.open(image_path) as im:
            return f"{image_path} {im.format} {im.size[0]}x{im.size[1]} {im.mode}"
    except OSError:
        pass

