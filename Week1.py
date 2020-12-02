#!/usr/bin/env python3
from PIL import Image
import glob
import os

def crear_folder():
    if not os.path.exists('/opt/icons/'):
        os.makedirs('/opt/icons/')

def guardar(imagen, filename):
    save_path = '/opt/icons/' + filename
    imagen.save(save_path, 'JPEG')
    print(imagen.format, imagen.size)

def rotate_resize(imagen):
    new_image  = imagen.rotate(-90).resize((128,128))
    return new_image

def main():
    # Script on images/ dir
    crear_folder()
    for filename in glob.glob("ic_*"):
        imagen = Image.open(filename).convert('RGB')
        
        new_image = rotate_resize(imagen)
        guardar(new_image, filename)
        
    print("Done!")

if __name__ == "__main__":
    main()

