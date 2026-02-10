import cv2
import os
import numpy as np

INPUT_DIR = "input_images"
OUTPUT_DIR = "output_images"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def pencil_sketch(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverted = cv2.bitwise_not(gray)
    blurred = cv2.GaussianBlur(inverted, (21, 21), 0)

    def dodge(front, back):
        return cv2.divide(front, 255 - back, scale=256)

    sketch = dodge(gray, blurred)
    return sketch

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
        output_path = os.path.join("output_images", f"grayscale_{filename}")
        cv2.imwrite(output_path, gray)


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
        
        sketch = pencil_sketch(image)
        sketch_path = os.path.join("output_images", f"sketch_{filename}")
        cv2.imwrite(sketch_path, sketch)



print("Processing complete.")
