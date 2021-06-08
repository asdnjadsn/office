import os
import cv2
import random

img = cv2.imread('img.jpg')
mask = cv2.imread('mask.png')
mask = mask[..., 0]

fg_mask = mask > 0
bg_mask = mask <= 0

b_channel, g_channel, r_channel = cv2.split(img)
r_channel[fg_mask] = 255
img_BGRA = cv2.merge((b_channel, g_channel, r_channel))

cv2.imwrite('combine.jpg', img_BGRA)
