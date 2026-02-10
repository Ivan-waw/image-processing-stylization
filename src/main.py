import cv2
import os
import numpy as np

INPUT_DIR = "input_images"
OUTPUT_DIR = "output_images"

os.makedirs(OUTPUT_DIR, exist_ok=True)

for filename in os.listdir(INPUT_DIR):
    if filename.lower().endswith((".jpg", ".png", ".jpeg")):
        img_path = os.path.join(INPUT_DIR, filename)
        image = cv2.imread(img_path)

        if image is None:
            continue

        # --- Grayscale conversion ---
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        gray_filename = "gray_" + filename
        gray_path = os.path.join(OUTPUT_DIR, gray_filename)
        cv2.imwrite(gray_path, gray)

        # --- Pixelation ---
        h, w = gray.shape
        scale = 0.1  # smaller = more pixelated

        small = cv2.resize(gray, (int(w * scale), int(h * scale)),
                        interpolation=cv2.INTER_LINEAR)

        pixelated = cv2.resize(small, (w, h),
                                interpolation=cv2.INTER_NEAREST)

        pixel_filename = "pixel_" + filename
        pixel_path = os.path.join(OUTPUT_DIR, pixel_filename)

        cv2.imwrite(pixel_path, pixelated)



print("Processing complete.")
