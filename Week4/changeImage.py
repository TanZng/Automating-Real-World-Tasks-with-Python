#!/usr/bin/env python3
from PIL import Image
import glob
import os

PATH_IMG = "supplier-data/images/"

def guardar(imagen, filename):
    name = filename.split('.')
    save_path = PATH_IMG + name[0] + '.jpeg'
    imagen.save(save_path, 'JPEG')
    print(imagen.format, imagen.size)

def rotate_resize(imagen):
    new_image  = imagen.resize((600, 400))
    return new_image

def main():
    images = PATH_IMG
    print(images)
    for filename in os.listdir(images):
        if '.tiff' in filename:
            imagen = Image.open(PATH_IMG + filename).convert('RGB')
            new_image = rotate_resize(imagen)
            guardar(new_image, filename)
        
    print("Done!")

if __name__ == "__main__":
    main()

