import cv2
import numpy as np
class filters:
    def greyscale(img):
        greyscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return greyscale

    def sharp(img):
        kernel = np.array([[-1, -1, -1], [-1, 9.5, -1], [-1, -1, -1]])
        img_sharpen = cv2.filter2D(img, -1, kernel)
        return img_sharpen

    def sepia(img):
        img_sepia = np.array(img, dtype=np.float64) # converting to float to prevent loss
        img_sepia = cv2.transform(img_sepia, np.matrix([[0.272, 0.534, 0.131],
                                    [0.349, 0.686, 0.168],
                                    [0.393, 0.769, 0.189]])) # multipying image with special sepia matrix
        img_sepia[np.where(img_sepia > 255)] = 255 # normalizing values greater than 255 to 255
        img_sepia = np.array(img_sepia, dtype=np.uint8)
        return img_sepia
    
    def invert(img):
        inv = cv2.bitwise_not(img)
        return inv
    
    def pencil(img):
        #inbuilt function to create sketch effect in colour and greyscale
        sk_gray, sk_color = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.1) 
        return  sk_gray
    