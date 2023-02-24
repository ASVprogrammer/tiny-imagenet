import os

MAIN_PATH = os.getcwd()
TRAIN_PATH = (os.path.join(MAIN_PATH, 'data', 'train'))

for folder in os.listdir(TRAIN_PATH):
    IMAGE_FOLDER = os.path.join(TRAIN_PATH, folder, 'image')
    for image in os.listdir(IMAGE_FOLDER):
        IMAGE_PATH = os.path.join(IMAGE_FOLDER, image)

