#!/usr/bin/python
# -*- coding: utf-8 -*-

# AUTOR: Adrià Auguets

def rgb_to_bn(img):
	"""Retorna una imatge de la mateixa dimensio ́ de img que cont ́e la mateixa escena per`o convertida a blanc i negre."""

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
	histograma = 256*[0]
	img = i[1]
	for fila in img:
		print fila
		for pixel in fila:
			histograma[pixel] += 1
	return histograma

def get_threshold(histograma,total):
    """
    No funciona
    """
	sum = 0
	for i in range(1, 256):
		sum += i*histograma[i]
	sumB = 0
	wB = 0
 	wF =0
	mB = 0
	mF = 0
	max = 0
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
		mF = (sum - sumB) / wF
		between = wB * wF * (mB - mF)**2
		if between > max:
			max = between
			threshold = i
	print wB/51.
	print mB/51., wF/51., mF/51.
	return threshold

def to255(hist):
    """
    Mòdul addiciional
    """
	n_hist=256*[0]
	for i in range(6):
		n_hist[i*51]=hist[i]
	return n_hist

#print "histo", to255([8,7,2,6,9,4])
#print get_threshold(to255([8,7,2,6,9,4]), 36)