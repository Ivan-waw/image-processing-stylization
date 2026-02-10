import cv2
import os

OUTPUT_DIR = "output_images"

def test_all_outputs_same_dimensions():
    files = [f for f in os.listdir(OUTPUT_DIR) if f.endswith((".jpg", ".png"))]

    assert len(files) > 0, "No output images found"

    base_image = cv2.imread(os.path.join(OUTPUT_DIR, files[0]))
    base_shape = base_image.shape[:2]

    for f in files:
        img = cv2.imread(os.path.join(OUTPUT_DIR, f))
        assert img is not None, f"{f} could not be read"
        assert img.shape[:2] == base_shape, f"{f} has different dimensions"
