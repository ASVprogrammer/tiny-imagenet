import os
from matplotlib import image as mt
import numpy as np

MAIN_PATH = os.getcwd()
TRAIN_PATH = (os.path.join(MAIN_PATH, 'data', 'train'))
def read_txt(path, batch):
    arr = []
    for folder in os.listdir(path):
        txt = os.path.join(path, folder, folder + '_boxes.txt')
        a = open(txt)
        arr.append(a.readlines())

    file_names = []
    bounding_box = []
    for x in arr:
        for y in x:
            i = y.split('\t')
            file_names.append(i[0])
            bounding_box.append([i[1], i[2], i[3], i[4].rstrip('\n')])
    return np.asarray(file_names)[batch], np.asarray(bounding_box)[batch]

def read_image(image_list, path):
    images = []
    for image in image_list:
        IMAGE_PATH = os.path.join(path, image.split('_')[0], 'images', image)
        images.append(mt.imread(IMAGE_PATH))
        return np.asarray(images)


def set_label(file_name):
    l = []
    for i in file_name:
        x = i.split('_')[0]
        l.append(x)
    return l



#image_list = read_image(read_txt(...)[0],)


