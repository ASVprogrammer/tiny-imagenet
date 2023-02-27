import os
from matplotlib import image as mt
def read_txt(path):
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
            return file_names, bounding_box

def read_image(image_list, path):
    images = []
    for image in image_list:
        IMAGE_PATH = os.path.join(path, image.split('_')[0], 'images', image)
        images.append(mt.imread(IMAGE_PATH))
        return images




