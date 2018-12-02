import matplotlib.image as mpimg
import os
import numpy as np

images = []
folder = '/home/fatema/Pictures/IMAGES/2018-10-15'
for filename in os.listdir(folder):
    try:
        img = mpimg.imread(os.path.join(folder, filename))
        if img is not None:
            images.append(img)
    except:
        print('Cant import ' + filename)
images = np.asarray(images)

print(images)

