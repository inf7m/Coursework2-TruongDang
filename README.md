# Image Processing Project

## Overview
This project demonstrates image processing using both **sequential** and **parallel** approaches.  
It loads images from an input folder, processes them (resize, grayscale, blur), and saves the results to an output folder.

The project is designed to compare performance between normal execution and parallel processing.

## Project Structure
```
project
│
├── config.py
├── generate_images.py
├── image_utils.py
├── sequential.py
├── parallel.py
│
├── input_images/
└── output_images/
```

## Main Libraries Used
- **Pillow (PIL)** – image loading and processing  
- **NumPy** – image array manipulation  
- **Multiprocessing** – parallel execution  
- **Time** – performance measurement  

## How to Run

### 1. Install dependencies
```
pip install pillow numpy
```

### 2. Generate sample images (optional)
```
python generate_images.py <number_of_image> <width> <height>
```

### 3. Run sequential processing
```
python sequential.py
```

### 4. Run parallel processing
```
python parallel.py
```

Processed images will be saved in the `output_images/` folder.

## Goal
Compare execution time between sequential and parallel processing when handling multiple images.
