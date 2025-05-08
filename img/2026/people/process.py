import numpy as np
from PIL import Image

def downsample_image(path_src, path_dst, scale=4):
    """
    Downsample an image by a given scale factor.
    """
    # Open the image file
    img = Image.open(path_src)
    # Calculate new size
    new_size = (img.width // scale, img.height // scale)
    # Resize the image
    downsampled_img = img.resize(new_size, Image.LANCZOS)
    # Convert to numpy array
    downsampled_img.save(path_dst)

# downsample_image("angjoo.jpg", "angjoo_downsampled.jpg", scale=4)
downsample_image("Arash_Mahdavi-Amiri.jpg", "Arash_Mahdavi-Amiri_downsampled.jpg", scale=4)
# downsample_image("Jiayi.jpg", "Jiayi_downsampled.jpg", scale=4)
# downsample_image("Junho.jpg", "Junho_downsampled.jpg", scale=4)
# downsample_image("ritchie.jpg", "ritchie_downsampled.jpg", scale=4)

