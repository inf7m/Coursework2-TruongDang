import os
import sys
import time
from concurrent.futures import ProcessPoolExecutor
from config import INPUT_FOLDER, OUTPUT_FOLDER, DEFAULT_WORKERS
from image_utils import process_image


def run_parallel(num_workers):
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    files = [
        os.path.join(INPUT_FOLDER, f)
        for f in os.listdir(INPUT_FOLDER)
        if f.endswith(".png")
    ]

    print(f"Total images found: {len(files)}")
    print(f"Running Parallel Processing with {num_workers} processes...")

    start_time = time.time()

    with ProcessPoolExecutor(max_workers=num_workers) as executor:
        executor.map(process_image, files)

    end_time = time.time()

    print(f"Parallel Time: {end_time - start_time:.4f} seconds")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        workers = int(sys.argv[1])
    else:
        workers = DEFAULT_WORKERS

    run_parallel(workers)
