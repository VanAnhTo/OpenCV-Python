import numpy as np
import cv2
from im_functions import translate

img = cv2.imread("images/wave.png")
cv2.imshow("img",img)
cv2.waitKey(0)
trns = translate(img,-90,-50)
cv2.imshow("transilated img",trns)
cv2.waitKey(0)
