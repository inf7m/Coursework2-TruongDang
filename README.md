# Image Processing Parallel Project

## Overview

This project demonstrates the performance difference between **sequential and parallel computing** using an image processing workload.

The program processes a large number of images by applying several transformations:

- Convert image to **grayscale**
- Apply **Gaussian blur**
- Perform **edge detection**

Two implementations are provided:

- **Sequential version** – processes images one by one using a single CPU core.
- **Parallel version** – distributes image processing tasks across multiple CPU processes.

Since each image can be processed independently, the workload is **embarrassingly parallel**, making it ideal for multiprocessing.

---

# Project Structure
project/
│
├── config.py # Configuration settings
├── generate_images.py # Script to generate dataset
├── image_utils.py # Core image processing logic
├── sequential.py # Sequential execution
├── parallel.py # Parallel execution
│
├── input_images/ # Generated dataset
└── output_images/ # Processed images
