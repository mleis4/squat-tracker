# Statistics/Plotting
import math
import matplotlib.pyplot as plt
import numpy as np


# Computer Vision
import cv2 as cv

def findPlate(img):
	'''
	Detects AruCo tag within given frame based on provided AruCo dictionary.
	Returns all AruCo tag candidates, but for our purposes should only be one tag.
	** Change to: Find the plate **
 	'''
    
    # Convert frame to grayscale
	gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
	
	# Looks for appropriate parameters of a circle
	circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, dp=1, minDist=20, param1=50, param2=30, minRadius=0, maxRadius=0)
 
	# Draw detected circles
	if circles is not None:
		circles = np.uint16(np.around(circles))
		for i in circles[0, :]:
			# Draw outer circle
			cv.circle(img, (i[0], i[1]), i[2], (255, 0, 255), 3)
			# Draw center of circle
			cv.circle(img, (i[0], i[1]), 2, (0, 100, 100), 3)
			# Display results
			cv.imshow('Detected circles', img)
			cv.waitKey(0)
	cv.destroyAllWindows()

img = cv.imread('BlackCircle.jpg')

if img is None:
    raise FileNotFoundError("Could not load image '3.png'")

findPlate(img)