import cv2
import numpy as np
import matplotlib.pyplot as plt

def notLinear1(img,c):
    log_image = pow(c * (np.log(img + 1)))
    # float value will be converted to int
    log_image = np.array(log_image, dtype = np.uint8)
    return log_image


if __name__ == "__main__":
    img = cv2.imread('Lenna.jpg')  # [height, width, channel]
    c = 255 / np.log(1 + np.max(img))
    #!g(x,y) = c.logf(x,y)
    img_new = notLinear1(img,c)
    cv2.imwrite('nonLinear1.jpg', img_new)
