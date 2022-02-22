import glob
import cv2
import os
##Scale Image
def scaleImage(image, scale = 15):
    get_image = cv2.imread(image,-1)
    WIDTH = int(get_image.shape[1] * scale / 100)
    HEIGHT = int(get_image.shape[0] * scale / 100)
    resized_image = cv2.resize(get_image, ( WIDTH, HEIGHT ) )
    return resized_image

images_original_name = glob.glob("*.png")

for index, image in enumerate(images_original_name):
    to_save1 = scaleImage(image, 100)
    cv2.imwrite(f"fish{index+1}_1.png", to_save1)
    to_save2 = scaleImage(image, 75)
    cv2.imwrite(f"{index+1}.png", to_save2)
    #os.remove(image)

