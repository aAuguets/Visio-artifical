#!/usr/bin/python
# -*- coding: utf-8 -*-

# DEV: Adrià Auguets

def rgb_to_bn(img):
	"""
	Retorna una imatge de la mateixa dimensio ́ de img que cont ́e la mateixa escena però convertida a blanc i negre.
	"""
	pass

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

def luminance_img(img): 
	"""
	Transforms a RGB image to a L image using luminance
	>>> luminance img(('RGB', [[(255, 255, 255), (255, 255, 255), (255, 255, 255)], [(255, 255, 255),(255, 255, 255), (255, 255, 255)], [(255, 255, 255), (255, 255, 255), (255, 255, 255)]])) 
	('L', [[255, 255, 255], [255, 255, 255], [255, 255, 255]])
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
	histograma = 256*[0]
	img = i[1]
	for fila in img:
		print fila
		for pixel in fila:
			histograma[pixel] += 1
	return histograma

def get_threshold(histograma, total):
	"""
	Retorna el llindar de l'Otsu a partir d'un histograma
	>>> get_threshold([8,7,2,6,9,4], 36)
	3
	"""
	profunditat = len(histograma)
	suma, sumB, wB = 0, 0.0, 0.0
	
	for i in range(profunditat):
		suma += i * histograma[i]
	
	for i in range(profunditat):
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