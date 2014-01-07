#!/usr/bin/python
# -*- coding: utf-8 -*-

from PIL import Image, ImageColor, ImageDraw
from imgio import *

def format(im):
	"""
	Donada imatge retorna format: RGB, 1 (blanc i negre), L (escala de grisos)
	"""
	return im[0]

def get_w(im):
	"""
	Donada imatge retorna l'amplada
	"""
	return len(im[1][0])
def get_h(im):
	"""
	Donada imatge retorna l'alcada
	"""
	return len(im[1])
def white_rgb(w, h):
	"""
	Retorna image en format RGB amb tamany w, h de color blanc
	"""
	fila = [(255, 255, 255) for i in range(w)]
	img = [fila for i in range(h)]
	return ("RGB", img)

def white_grey(w, h):
	fila = [255 for i in range(w)]
	img = [fila for i in range(h)]
	return ("L", img)

def white_bn(w, h):
	fila = [255 for i in range(w)]
	img = [fila for i in range(h)]
	return ("1", img)
	
def matrix(img):
	return img[1]
	
def subimg(img, ow, oh, w, h):
	"""
	subimg(image,column,row,widthColumns,heightRows)
	Returns a subimage from img with origin coordinates ow,oh and size w x h
	>>> subimg(('L', [[0, 0, 255], [255, 255, 255], [255, 255, 255]]),0,0,2,1)
	('L', [[0, 0]])
	>>> subimg(('1', [[255, 255], [255, 255], [255, 255]]),0,1,2,1)
	('1', [[255, 255]])
	>>> subimg(('1', [[255, 255], [255, 255], [0, 255]]),0,1,2,2)
	('1', [[255, 255], [0, 255]])
	"""
	imatge=img[1]
	imatge=imatge[oh:h+1][ow:w+1]
	print imatge

def img(m, model='DISCOVER'):
	"""
	Returns the image representation format (T,m)
	>>> img([[255,255,0],[255,128,255],[191,255,255]],’DISCOVER’)
	(’L’, [[255, 255, 0], [255, 128, 255], [191, 255, 255]])
	>>> img([[255,255,0],[255,0,255],[0,255,255]],’DISCOVER’)
	(’1’, [[255, 255, 0], [255, 0, 255], [0, 255, 255]])
	"""
	if isinstance(m[0][0], tuple): # RGB
			return ("RGB", m)
	for a in m: #NO RGB
		for b in a:
			if b != 255 and b != 0: 
				return ("L", m)
			else:
				return ("1", m)
