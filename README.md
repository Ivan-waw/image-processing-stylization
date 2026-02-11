# 🖼️ Image Processing Stylization

## 📌 Overview

This project implements a complete image processing pipeline that applies multiple computer vision techniques to normalized input images.

All images are first standardized using geometric and spatial transformations. After normalization, six core image processing techniques are applied. Each technique produces a separate processed output for comparison with the original image.

The system is designed to ensure:

* Consistent image dimensions
* Reproducibility of results
* Clear comparison between outputs
* Extensibility for future techniques

---

## 🚀 How to Run the Project

### 1️⃣ Activate the Virtual Environment

```bash
venv\Scripts\Activate
```

### 2️⃣ Run the Main Program

```bash
python src\main.py
```

### 3️⃣ Run Unit Tests

```bash
python -m pytest
```

---

## 🛠️ Image Normalization (Preprocessing)

Before applying image processing techniques, all input images are standardized.

### 🔹 Center Square Cropping

* Geometric transformation
* Extracts the centered square portion of the image

### 🔹 Fixed-Size Image Resizing

* Spatial transformation
* Ensures consistent output dimensions

⚠️ These steps are considered preprocessing and are not counted as core image processing techniques.

---

## 🎯 Implemented Image Processing Techniques (6)

The project applies six primary image processing techniques:

### 1️⃣ Grayscale Conversion

* Converts RGB/BGR images into intensity-based images
* Serves as the foundation for many vision algorithms

---

### 2️⃣ Gaussian Blur

* Applies smoothing using a Gaussian kernel
* Reduces image noise
* Used internally within the pencil sketch effect

---

### 3️⃣ Pixelation (Downsampling + Upsampling)

* Reduces spatial resolution
* Enlarges the image back to original size
* Demonstrates resolution manipulation

---

### 4️⃣ Canny Edge Detection

* Detects edges using gradient magnitude and hysteresis
* Classic edge detection algorithm in computer vision

---

### 5️⃣ Binary Thresholding

* Converts grayscale images into black-and-white images
* Demonstrates basic image segmentation

---

### 6️⃣ Pencil Sketch Effect (Non-Linear Blending)

A composite stylization technique combining:

* Grayscale conversion
* Image inversion
* Gaussian blur
* Image division

Although composed of multiple steps, it is considered one technique because it produces a single stylized output.

---

## ❓ Why It’s 6 Techniques (Not 8)

Cropping and resizing may appear as additional techniques, but academically they are classified as preprocessing and normalization steps rather than independent image processing methods.

The project therefore implements **six core image processing techniques**, supported by preprocessing for consistency.

---

## 📊 Output

The final output consists of:

* Multiple processed images
* Each representing a different image processing technique
* Standardized dimensions across all results
* Direct comparison between original and transformed images

The system allows selecting a final technique for comparison against the original image.

---

## 🧠 Project Summary

This project demonstrates a structured and reproducible workflow for image processing. Images are first normalized through cropping and resizing, then processed using six core techniques: grayscale conversion, Gaussian blur, pixelation, Canny edge detection, binary thresholding, and pencil sketch stylization.

The modular pipeline design ensures consistency, clarity in results, and scalability for future incorporation of additional techniques.

---
