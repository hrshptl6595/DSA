import numpy as np
import cv2
from pytesser import *
from espeak import espeak

cap = cv2.VideoCapture(0)

while(True):
	ret, frame = cap.read()

	text = image_to_string(frame)
	espeak.synth(text)

cap.release()
cv2.destroyAllWindows()