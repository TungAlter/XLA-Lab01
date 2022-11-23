import cv2
import numpy as np


def linear1(img, b):
    img_new = np.asarray(img + b, dtype=int)  # cast pixel values to int
    img_new[img_new > 255] = 255
    img_new[img_new < 0] = 0
    return img_new

def linear2(img, a):
    img_new = np.asarray(a * img, dtype=int)  # cast pixel values to int
    img_new[img_new > 255] = 255
    img_new[img_new < 0] = 0
    return img_new

def linear3(img, a, b):
    img_new = np.asarray(a * img + b, dtype=int)  # cast pixel values to int
    img_new[img_new > 255] = 255
    img_new[img_new < 0] = 0
    return img_new

if __name__ == "__main__":
    a = 1.5
    b = 35
    img = cv2.imread('Lenna.jpg')  # [height, width, channel]
    #!g(x,y) = f(x,y) + b
    img_new = linear1(img,b)
    cv2.imwrite('linear1.jpg', img_new)
    #!g(x,y) = a*f(x,y)
    img_new = linear2(img, a)
    cv2.imwrite('linear2.jpg', img_new)
    #!g(x,y) = a*f(x,y) + b
    img_new = linear3(img, a, b)
    cv2.imwrite('linear3.jpg', img_new)

    
