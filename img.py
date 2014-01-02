#!/usr/bin/python
# -*- coding: utf-8 -*-

from PIL import Image,ImageColor, ImageDraw
from imgio import *


im = Image.open("test2.jpeg")

def format(im):
	"""
	Donada imatge retorna format: RGB, 1 (blanc i negre), L (escala de grisos)
	"""
	return im.mode

def get_w(im):
	"""
	Donada imatge retorna l'amplada
	"""
	return im.size[0]

def get_h(im):
	"""
	Donada imatge retorna l'alcada
	"""
	return im.size[1]
	
def white_rgb(w, h):
	"""
	Retorna image en format RGB amb tamany w, h de color blanc
	"""
	return Image.new("RGB", (w, h), (255, 255, 255))
		
#ima=Image.open("matricula1.jpeg")
#print get_h(ima)

def white_grey(w, h):
	return Image.new("L", (w, h), (255))

def white_bn(w, h):
	return Image.new("1", (w, h), (255))
	
def matrix(img):
	pix = img.load()
	X, Y = img.size
	data = [[pix[x,y] for x in range(X)] for y in range(Y)]
	#nova = []    
	#for row in data:
	#	r = []
	#	for bit in row:
	#		if bit > 125:
	#			r+=[255]
	#		else:
	#			r+=[0]
	#	nova+=[r]
	return data
    
def subimg(img, ow, oh, w, h):
	img.crop()
	
#m=white_grey(421, 420)
#print matrix(white_bn(400, 400))

#im.show()
#print "Alcada: ",get_h(m)," ","Amplada: ",get_w(m)," ","
#print "Format: ",format(im)
#m.show()


