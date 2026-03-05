from PIL import Image, ImageFilter
import os
from config import OUTPUT_FOLDER, BLUR_RADIUS


def process_image(image_path):
    """
    Perform heavy image processing:
    - Convert to grayscale
    - Apply blur
    - Apply edge detection
    - Save result
    """

    img = Image.open(image_path)

    # Convert to grayscale
    img = img.convert("L")

    # Apply blur
    img = img.filter(ImageFilter.GaussianBlur(BLUR_RADIUS))

    # Edge detection
    img = img.filter(ImageFilter.FIND_EDGES)

    # Save processed image
    filename = os.path.basename(image_path)
    output_path = os.path.join(OUTPUT_FOLDER, filename)

    img.save(output_path)

    return filename
