#!/usr/bin/python
# -*- coding: utf-8 -*-

# AUTOR: Adrià Auguets

def rgb_to_bn(img):
	"""
	Retorna una imatge de la mateixa dimensió de img que cont́e la mateixa escena però convertida a blanc i negre.
	
	Transforms a RGB image to a 1 image using luminance, histogram and get threshold
	>>> rgb to bn((’RGB’, [[(255, 255, 255), (255, 255, 255), (255, 255, 255)],[(255, 255, 255),(255, 255, 255), (255, 255, 255)], [(255, 255, 255), (255, 255, 255), (255, 255, 255)]]))
	(’1’, [[255, 255, 255], [255, 255, 255], [255, 255, 255]])
	"""
def rgb_to_lum(pixel):
	"""
	Returns the luminance level off a RGB pixel 
	>>> rgb to lum((255,255,255))
	255
	>>> rgb to lum((255,0,0))
	85
	"""
	suma=0
	for element in pixel:
		suma += element
	
	return suma/3
# rgb_to_lum((255,255,255))

def luminance_img(img): 
	"""
	Transforms a RGB image to a L image using luminance
	>>> luminance img((’RGB’, [[(255, 255, 255), (255, 255, 255), (255, 255, 255)], [(255, 255, 255),(255, 255, 255), (255, 255, 255)], [(255, 255, 255), (255, 255, 255), (255, 255, 255)]])) 
	(’L’, [[255, 255, 255], [255, 255, 255], [255, 255, 255]])
	"""
	luminance = []
	image = img[1:][0]
	for fila in image:
		nova_fila = []
		for colors in fila:
			nova_fila += [rgb_to_lum(colors)]
		luminance += [nova_fila]
	return ("L", luminance)

def histogram(i):
	"""
	Crea una llista de 256 valors i coloca la quantitat de color de cada pixel.
	Histogram of grey values of L image i
	>>> histogram(("L", [[255, 255, 255, 255], [255, 255, 255, 255]]))
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8]
	"""
	
	histograma = 256*[0]
	for fila in range(i[0]):
		print fila
		for pixel in fila:
			histograma[pixel] += 1
	return histograma

def get_threshold(histograma, total):
	"""
	Retorna el valor dels dos maxims elements del histograma fent servir l'algoritme d'Otsu threshold 
	
	>>> get_threshold([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 5)
	170
	"""
	suma = 0
	for i in range(1, 256):
		suma += i*histograma[i]
	sumB = 0
	wB = 0
 	wF =0
	mB = 0
	mF = 0
	maxim = 0
	between = 0
	threshold = 0
	for i in range(256):
		wB += histograma[i]
		if wB == 0:
			continue
		wF = total - wB
		if wF == 0:
			break
		sumB += i * histograma[i]
		mB = sumB / wB
		mF = (suma - sumB) / wF
		between = wB * wF * (mB - mF)**2
		if between > maxim:
			maxim = between
			threshold = i
	return threshold

def to255(hist):
	n_hist=256*[0]
	for i in range(6):
		n_hist[i*51]=hist[i]
	return n_hist
