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
	
	lux = suma/3
	return lux
# rgb_to_lum((255,255,255))

def luminance_img(img): 
	"""
	Transforms a RGB image to a L image using luminance
	>>> luminance img((’RGB’, [[(255, 255, 255), (255, 255, 255), (255, 255, 255)], [(255, 255, 255),(255, 255, 255), (255, 255, 255)], [(255, 255, 255), (255, 255, 255), (255, 255, 255)]])) 
	(’L’, [[255, 255, 255], [255, 255, 255], [255, 255, 255]])
	"""
	luminance=[]
	for fila in img:
		nova_fila = []
		for bits in fila:
			nova_fila += [rgb_to_lum(bits)]
		luminance+=[nova_fila]
	print luminance

# luminance_img([[(56,250,180),(134,14,133),(24,25,211)],[(24,255,234),(213,332,333),(411,433,444)],[(57,5776,57),(656,654,62),(712,7333,74)]])

def histogram(img):
	


