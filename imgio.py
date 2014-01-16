#!/usr/bin/python
# -*- coding: utf-8 -*-

# DEV: Adrià Auguets i Felipe Arango

from img import *
from PIL import Image

def read_rgb(nomf):
    """
    Donat un nom de fitxer corresponent a una imatge RGB la llegeix
    i torna la imatge corresponent
    """
    image = Image.open(nomf)
    pix = image.load()
    X, Y = image.size[0], image.size[1]
    data = [[pix[x,y] for x in range(X)] for y in range(Y)]    
    return img(data, 'RGB')


def read_bn(nomf):
    """
    Donat un nom d'arxiu corresponent a una imatge en blanc i negre, 
    retorna la matriu d'imatge. Cada pixel serà 0 o 255. 
    """
    image = Image.open(nomf).convert('1')
    pix = image.load()
    X = image.size[0]
    Y = image.size[1]
    return [[pix[x,y] for x in range(X)] for y in range(Y)]

def show(i):
    """
    Donada una imatge, la mostra en un visualitzador. Principalment serveix per a depurar el projecte.
    """
    print get_w(i)
    image = Image.new(format(i),(get_w(i),get_h(i)))
    image.putdata([pixel for F in matrix(i) for pixel in F])
    image.show()

def save(img,nomf):
    """
    Donada una imatge i un nom de fitxer, crea el fitxer imatge a
    partir de la matriu.
   
 """
    image = Image.new(format(img),(get_w(img),get_h(img)))
    image.putdata([pixel for F in matrix(img) for pixel in F])
    image.save(nomf)

#showl=("RGB", [[(0, 0, 0), (255, 255, 255), (255, 0, 0)], [(255, 255, 255), (0, 255, 0), (255, 255, 255)], [(0, 0, 255), (255, 255, 255), (255, 255, 255)]])
#show(showl)
