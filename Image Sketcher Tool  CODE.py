#!/usr/bin/env python
# coding: utf-8

# In[9]:


# To install opencv
get_ipython().system('pip install opencv-python')
# To import modules
import cv2
import numpy as np
# Function to convert an image to a sketch effect
def sketch(img):
 # Convert the image to grayscale
 gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 # Apply Gaussian blur to the grayscale image
 gray_blur = cv2.GaussianBlur(gray, (5, 5), 0)
 # Use the Canny edge detector
 canny_edges = cv2.Canny(gray_blur, 10, 70)
 # Invert the edges to get a white sketch on a black background
 r, mask = cv2.threshold(canny_edges, 70, 255, cv2.THRESH_BINARY_INV)
 return mask
# Load an image from a file
image_path = "IMAGE URL.png" # Enter image path
img = cv2.imread(image_path)
# Check if the image was loaded successfully
if img is None:
 print(f"Error: Could not load image from {image_path}")
else:
 # Apply the sketch filter
 sketched_img = sketch(img)
 # Display the sketched image using cv2.imshow
 cv2.imshow("Pencil Sketch", sketched_img)
 # Wait until a key is pressed, then close the displayed window
 cv2.waitKey(0)
 cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




