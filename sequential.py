import os
import time
from config import INPUT_FOLDER, OUTPUT_FOLDER
from image_utils import process_image


def run_sequential():
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    files = [
        os.path.join(INPUT_FOLDER, f)
        for f in os.listdir(INPUT_FOLDER)
        if f.endswith(".png")
    ]

    print(f"Total images found: {len(files)}")
    print("Running Sequential Processing...")

    start_time = time.time()

    for image_path in files:
        process_image(image_path)

    end_time = time.time()

    print(f"Sequential Time: {end_time - start_time:.4f} seconds")


if __name__ == "__main__":
    run_sequential()
