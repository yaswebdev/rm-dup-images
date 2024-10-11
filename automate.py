import os
import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from skimage.metrics import structural_similarity as ssim

def calculate_similarity(image1, image2):
    """Calculate similarity between two images using SSIM."""
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    
    # Calculate Structural Similarity Index (SSI)
    score, _ = ssim(gray1, gray2, full=True)
    return score

def find_and_remove_duplicates(image_dir, similarity_threshold=0.95):
    """Find and remove duplicate images in the specified directory."""
    images = {}
    removed_images = []

    # Iterate through files in the specified directory
    for filename in os.listdir(image_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            filepath = os.path.join(image_dir, filename)
            image = cv2.imread(filepath)
            
            if image is None:
                print(f"Warning: Unable to read image {filepath}. Skipping...")
                continue

            # Compare with previously stored images
            duplicate_found = False
            for stored_filename, stored_image in images.items():
                similarity = calculate_similarity(stored_image, image)

                if similarity >= similarity_threshold:
                    print(f"Removing duplicate: {filepath} (similar to {stored_filename})")
                    os.remove(filepath)
                    removed_images.append(filepath)
                    duplicate_found = True
                    break
            if not duplicate_found:
                # Store the image if no duplicates were found
                images[filename] = image

    if not removed_images:
        messagebox.showinfo("Result", "No duplicate images found.")
    else:
        messagebox.showinfo("Result", f"Removed {len(removed_images)} duplicate images.")

def select_folder():
    """Open a dialog to select a folder."""
    folder_path = filedialog.askdirectory()
    if folder_path:
        find_and_remove_duplicates(folder_path)

if __name__ == "__main__":
    # Create a simple GUI window
    root = tk.Tk()
    root.title("Duplicate Image Remover")
    root.geometry("300x100")

    # Add a button to select a folder
    select_button = tk.Button(root, text="Select Image Folder", command=select_folder)
    select_button.pack(expand=True)

    # Run the GUI loop
    root.mainloop()
