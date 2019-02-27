from skimage.io import imread
from skimage.color import rgb2gray
import matplotlib.pyplot as plt

img = imread('resources/box.jpg')
imggray = rgb2gray(img)

plt.imshow(imggray, cmap="gray")
plt.axis("off")
plt.show()