# 🧪 QA Checklist – Image Processing Stylization

## 1️⃣ Environment Setup
- [ ] Python installed
- [ ] Virtual environment activated (`venv\Scripts\Activate`)
- [ ] Dependencies installed (`pip install -r requirements.txt`)

## 2️⃣ Input Images
- [ ] Sample images added for testing
- [ ] System handles invalid or missing files gracefully

## 3️⃣ Output Verification
- [ ] Grayscale image generated
- [ ] Pencil sketch image generated
- [ ] Duotone image generated
- [ ] Pixelated image generated
- [ ] Soft glow image generated
- [ ] All output images saved in correct folder
- [ ] Output images have correct dimensions

## 4️⃣ Technique Verification

### Grayscale Conversion
- [ ] Image is truly black & white
- [ ] Pixel intensity values correctly represent brightness

### Pencil Sketch Effect
- [ ] Edges are clearly visible
- [ ] Image resembles a sketch drawing
- [ ] No excessive noise or artifacts

### Duotone Color Mapping
- [ ] Only two dominant colors present
- [ ] Color mapping follows grayscale intensity

### Pixelation
- [ ] Visible block/mosaic effect
- [ ] Fine details reduced
- [ ] Output image retains original dimensions after upsampling

### Soft Glow Effect
- [ ] Highlights enhanced
- [ ] Blending is smooth (not overexposed)
- [ ] Output image retains correct resolution

## 5️⃣ Preprocessing Verification
- [ ] Center square cropping applied
- [ ] Fixed-size resizing applied
- [ ] No distortion or unexpected scaling

## 6️⃣ Program Stability
- [ ] Program runs without crashing
- [ ] Handles multiple images correctly
- [ ] Optional: All pytest tests pass (if available)

## 7️⃣ Optional Extras
- [ ] Add screenshots of outputs for reference
- [ ] Record any bugs or inconsistencies in outputs

### 🐞 Bugs / Notes
- [ ] …
