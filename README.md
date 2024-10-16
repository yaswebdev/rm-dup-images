# Duplicate Image Remover Project

## Overview
As a response to a common challenge faced by photographers—managing and organizing large volumes of images—I developed a **Duplicate Image Remover** tool. This project aims to streamline the workflow for photographers by automatically identifying and removing duplicate images from their collections.

## Project Description
Photographers often accumulate thousands of photos from shoots, leading to a cluttered library filled with duplicates. This not only consumes storage space but also hinders the editing process. My Duplicate Image Remover utilizes advanced image similarity algorithms to analyze and compare images, effectively detecting duplicates based on their visual content.

## Key Features
- **User-Friendly Interface**: The application provides an intuitive GUI, allowing photographers to easily select the folder containing their images.
- **Automated Duplicate Detection**: Leveraging algorithms such as the Structural Similarity Index (SSIM) from the `scikit-image` library, the tool accurately identifies duplicates, even when they are not identical.
- **Efficient Image Processing**: The project uses `OpenCV` for image manipulation and `NumPy` for efficient numerical operations, ensuring quick and reliable performance.
- **Time and Effort Savings**: By automating the duplicate removal process, photographers can focus on what matters most—editing unique images and delivering high-quality work to their clients.

## Purpose
Through this project, I aim to enhance photographers' productivity, helping them manage their digital assets more effectively and allocate more time to creativity and client satisfaction.

## Technologies Used
- **Python**: The primary programming language used for development.
- **OpenCV**: For image manipulation and processing.
- **NumPy**: For efficient numerical operations.
- **scikit-image**: To implement the Structural Similarity Index (SSIM) for duplicate detection.
- **Tkinter**: For creating a user-friendly graphical user interface (GUI).

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>

2. Install the required libraries:
   ```bash
   pip install numpy opencv-python scikit-image

3. Run the application:
   ```bash
   python automate.py

Feel free to replace `<repository-url>` and `<repository-folder>` with your actual repository URL and folder name. Let me know if you need further assistance!