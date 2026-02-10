import cv2
import os
import numpy as np

INPUT_DIR = "input_images"
OUTPUT_DIR = "output_images"
FIXED_SIZE = (512, 512)

# ============================
# Safety checks
# ============================
if not os.path.exists(INPUT_DIR):
    raise FileNotFoundError("input_images folder not found")

os.makedirs(OUTPUT_DIR, exist_ok=True)

# ============================
# ❌ OLD CROPPING (kept for progress)
# ============================
"""
def center_crop(image, crop_ratio=0.8):
    h, w = image.shape[:2]
    new_h = int(h * crop_ratio)
    new_w = int(w * crop_ratio)
    start_y = (h - new_h) // 2
    start_x = (w - new_w) // 2
    return image[start_y:start_y + new_h, start_x:start_x + new_w]
"""

# ============================
# ✅ FINAL CROPPING STRATEGY
# Square crop for consistency
# ============================
def center_crop_square(image):
    h, w = image.shape[:2]
    side = min(h, w)
    start_y = (h - side) // 2
    start_x = (w - side) // 2
    return image[start_y:start_y + side, start_x:start_x + side]

# ============================
# ❌ OLD RESIZE-TO-MATCH (kept)
# ============================
"""
def resize_to_match(image, target_shape):
    return cv2.resize(image, (target_shape[1], target_shape[0]))
"""

# ============================
# ✅ FINAL RESIZE STRATEGY
# Fixed size guarantees pytest consistency
# ============================
def resize_fixed(image, size=FIXED_SIZE):
    return cv2.resize(image, size)

# ============================
# Pencil Sketch Technique
# ============================
def pencil_sketch(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverted = cv2.bitwise_not(gray)
    blurred = cv2.GaussianBlur(inverted, (21, 21), 0)
    return cv2.divide(gray, 255 - blurred, scale=256)

# ============================
# MAIN PIPELINE
# ============================
for filename in os.listdir(INPUT_DIR):
    if not filename.lower().endswith((".jpg", ".png", ".jpeg")):
        continue

    img_path = os.path.join(INPUT_DIR, filename)
    image = cv2.imread(img_path)

    if image is None:
        continue

    # ============================
    # Normalize original image
    # ============================
    image = center_crop_square(image)
    image = resize_fixed(image)

    original_normalized = image.copy()

    # Save normalized image
    cv2.imwrite(os.path.join(OUTPUT_DIR, f"cropped_{filename}"), image)

    # ============================
    # IMAGE PROCESSING TECHNIQUES
    # ============================

    # 1️⃣ Grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(os.path.join(OUTPUT_DIR, f"grayscale_{filename}"), gray)

    # 2️⃣ Pixelation
    h, w = gray.shape
    scale = 0.1
    small = cv2.resize(gray, (int(w * scale), int(h * scale)),
                       interpolation=cv2.INTER_LINEAR)
    pixelated = cv2.resize(small, (w, h),
                            interpolation=cv2.INTER_NEAREST)
    cv2.imwrite(os.path.join(OUTPUT_DIR, f"pixel_{filename}"), pixelated)

    # 3️⃣ Pencil Sketch
    sketch = pencil_sketch(image)
    cv2.imwrite(os.path.join(OUTPUT_DIR, f"sketch_{filename}"), sketch)

    # 4️⃣ Edge Detection
    edges = cv2.Canny(gray, 50, 150)
    cv2.imwrite(os.path.join(OUTPUT_DIR, f"edges_{filename}"), edges)

    # 5️⃣ Binary Threshold
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    cv2.imwrite(os.path.join(OUTPUT_DIR, f"threshold_{filename}"), thresh)

    # ============================
    # FINAL OUTPUT SELECTION
    # ============================

    FINAL_TECHNIQUE = " "

    if FINAL_TECHNIQUE == "sketch":
        final = sketch
    elif FINAL_TECHNIQUE == "threshold":
        final = thresh
    elif FINAL_TECHNIQUE == "edges":
        final = edges
    elif FINAL_TECHNIQUE == "pixel":
        final = pixelated

    else:
        final = thresh  # fallback safety

    # Convert grayscale final to BGR
    final_bgr = cv2.cvtColor(final, cv2.COLOR_GRAY2BGR)

    # ============================
    # SIDE-BY-SIDE COMPARISON
    # ============================
    comparison = np.hstack((original_normalized, final_bgr))
    comparison = resize_fixed(comparison)

    cv2.imwrite(os.path.join(OUTPUT_DIR, f"compare_{filename}"), comparison)

print("Processing complete.")
