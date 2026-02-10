import os

def test_output_folder_exists():
    assert os.path.exists("output_images"), "output_images folder does not exist"

def test_grayscale_output_exists():
    files = os.listdir("output_images")
    grayscale = [f for f in files if "grayscale" in f.lower()]
    assert len(grayscale) > 0, "No grayscale output found"

def test_pixelated_output_exists():
    files = os.listdir("output_images")
    pixelated = [f for f in files if "pixel" in f.lower()]
    assert len(pixelated) > 0, "No pixelated output found"

def test_sketch_output_exists():
    files = os.listdir("output_images")
    sketch_files = [f for f in files if "sketch" in f.lower()]
    assert len(sketch_files) > 0, "No sketch output found"
