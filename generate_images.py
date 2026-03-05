import os
import sys
import shutil
import random
from PIL import Image
from config import INPUT_FOLDER, OUTPUT_FOLDER


def generate_images(num_images, width, height):
    # Remove old folders
    if os.path.exists(INPUT_FOLDER):
        shutil.rmtree(INPUT_FOLDER)

    if os.path.exists(OUTPUT_FOLDER):
        shutil.rmtree(OUTPUT_FOLDER)

    os.makedirs(INPUT_FOLDER)
    os.makedirs(OUTPUT_FOLDER)

    print(f"Generating {num_images} images of size {width}x{height}...")

    for i in range(num_images):
        # Create random RGB image
        img = Image.new("RGB", (width, height))

        pixels = [
            (random.randint(0, 255),
             random.randint(0, 255),
             random.randint(0, 255))
            for _ in range(width * height)
        ]

        img.putdata(pixels)

        img.save(os.path.join(INPUT_FOLDER, f"image_{i}.png"))

    print("Dataset generation completed.")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python generate_images.py <num_images> <width> <height>")
        sys.exit(1)

    num_images = int(sys.argv[1])
    width = int(sys.argv[2])
    height = int(sys.argv[3])

    generate_images(num_images, width, height)
