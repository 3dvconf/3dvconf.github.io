import numpy as np
from PIL import Image
from PIL import ImageOps

def downsample_image(path_src, path_dst, scale=4):
    """
    Downsample an image by a given scale factor, preserving original rotation.
    """
    # Open the image file
    img = Image.open(path_src)
    # Apply EXIF orientation (if present) to preserve original rotation
    img = ImageOps.exif_transpose(img)
    # Calculate new size
    new_size = (img.width // scale, img.height // scale)
    # Resize the image
    downsampled_img = img.resize(new_size, Image.LANCZOS)
    # Save the image, preserving EXIF data if possible
    if "exif" in img.info:
        downsampled_img.save(path_dst, exif=img.info["exif"])
    else:
        downsampled_img.save(path_dst)

# downsample_image("angjoo_hd.jpg", "angjoo.jpg", scale=8)
# downsample_image("Christian_Theobalt_hd.jpg", "Christian_Theobalt.jpg", scale=2)
# downsample_image("Arash_Mahdavi-Amiri.jpg", "Arash_Mahdavi-Amiri_downsampled.jpg", scale=4)
# downsample_image("Jiayi.jpg", "Jiayi_downsampled.jpg", scale=4)
# downsample_image("Junho.jpg", "Junho_downsampled.jpg", scale=4)
# downsample_image("ritchie_hd.jpg", "ritchie.jpg", scale=8)
# downsample_image("alec.jpg", "alec_downsampled.jpg", scale=4)
# downsample_image("jitendra.jpg", "jitendra_downsampled.jpg", scale=4)
# downsample_image("Arash_Mahdavi-Amiri_hd.jpg", "Arash_Mahdavi-Amiri.jpg", scale=16)
downsample_image("ericyi_hd.jpg", "ericyi.jpg", scale=2)