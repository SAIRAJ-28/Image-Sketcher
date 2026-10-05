# ✏️ IMAGE SKETCHER TOOL as Pencil Sketch Using OpenCV

A simple **Python computer vision project** that converts a normal image into a pencil-sketch style image using **OpenCV**.

The project demonstrates basic image processing techniques such as **grayscale conversion, Gaussian Blur, Canny Edge Detection, and thresholding**.

---

## 📌 Project Overview

This project takes an input image and applies a series of image-processing operations to create a pencil sketch effect.

### Image Processing Pipeline

```text
Original Image
      ↓
Convert to Grayscale
      ↓
Gaussian Blur
      ↓
Canny Edge Detection
      ↓
Binary Threshold
      ↓
Pencil Sketch
```

---

## ✨ Features

- Convert a color image into a pencil sketch
- Convert image to grayscale
- Reduce image noise using Gaussian Blur
- Detect edges using Canny Edge Detection
- Invert detected edges using thresholding
- Display the final sketch using OpenCV

---

## 🛠️ Technologies Used

- **Python**
- **OpenCV**
- **NumPy**

### Libraries

```python
import cv2
import numpy as np
```

---

## 📦 Installation

First, install OpenCV:

```bash
pip install opencv-python
```

NumPy can be installed using:

```bash
pip install numpy
```

Or install both together:

```bash
pip install opencv-python numpy
```

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/SAIRAJ_28/pencil-sketch-opencv.git
```

### 2. Navigate to the Project

```bash
cd pencil-sketch-opencv
```

### 3. Install Dependencies

```bash
pip install opencv-python numpy
```

### 4. Add Your Image

Place your image inside the project folder.

For example:

```text
pencil-sketch-opencv/
│
├── pencil_sketch.py
├── input_image.png
└── README.md
```

### 5. Update the Image Path

Change:

```python
image_path = "IMAGE URL.png"
```

to:

```python
image_path = "input_image.png"
```

### 6. Run the Program

```bash
python pencil_sketch.py
```

The processed sketch will open in an OpenCV window.

---

## 🔍 How the Code Works

### 1. Read the Image

```python
img = cv2.imread(image_path)
```

`cv2.imread()` loads the image from the specified file path.

---

### 2. Convert to Grayscale

```python
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
```

The original image contains three color channels: **Blue, Green, and Red**.

Converting it to grayscale simplifies the image to intensity values, which makes edge detection easier.

---

### 3. Apply Gaussian Blur

```python
gray_blur = cv2.GaussianBlur(gray, (5, 5), 0)
```

Gaussian Blur reduces small details and noise from the image before edge detection.

The `(5, 5)` represents the Gaussian kernel size.

---

### 4. Detect Edges

```python
canny_edges = cv2.Canny(gray_blur, 10, 70)
```

The **Canny Edge Detector** identifies strong changes in image intensity and produces the major edges of the image.

The values:

```text
10 → Lower threshold
70 → Upper threshold
```

control the sensitivity of edge detection.

---

### 5. Apply Thresholding

```python
r, mask = cv2.threshold(
    canny_edges,
    70,
    255,
    cv2.THRESH_BINARY_INV
)
```

The detected edges are inverted to produce the sketch-like appearance.

---

### 6. Display the Sketch

```python
cv2.imshow("Pencil Sketch", sketched_img)
```

The resulting image is displayed in a separate OpenCV window.

The program waits for a key press:

```python
cv2.waitKey(0)
```

and then closes the window:

```python
cv2.destroyAllWindows()
```

---

## 🧠 Concepts Learned

This project helped me understand:

| Concept | Application |
|---|---|
| OpenCV | Image processing |
| Image Reading | `cv2.imread()` |
| Color Conversion | BGR → Grayscale |
| Gaussian Blur | Noise reduction |
| Canny Edge Detection | Finding image edges |
| Thresholding | Creating the sketch effect |
| NumPy | Numerical/image data processing |
| Functions | Reusable image-processing logic |
| Error Handling | Checking whether image loaded successfully |

---

## 📂 Project Structure

```text
Pencil-Sketch-OpenCV/
│
├── pencil_sketch.py
├── input_image.png
├── output/
│   └── sketch.png
└── README.md
```

---

## 📸 Example

### Input

A normal color image is provided as input.

### Output

The program converts the image into a black-and-white pencil sketch.

> Add your own **before/after screenshots** to the repository to make the project more attractive.

---

## 🎯 Learning Objective

The goal of this project is to understand the fundamentals of **computer vision and image processing using Python and OpenCV** by building a simple practical application.

---

## ⭐ If You Like This Project

If you found this project useful, consider giving the repository a ⭐.



It's My First Python Internship Project 

It converted image into pencil art which can easily drawable and understand Image outline for Sketch Artists.

By using this Tool it becomes easy to draw in less time without any effort and difficulty
