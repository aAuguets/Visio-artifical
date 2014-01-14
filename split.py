#!/usr/bin/python
# -*- coding: utf-8 -*-

# DEV: Jordi Masip

from utiles import *

def transpose(img):
	"""
	Retorna una matriu amb les files com a columnes i les columnes com a files
	"""
	# Crea tantes files a transposed_img com columnes hi ha a img:
	transposed_img = [[] for x in range(len(img[0]))]

	for row in img:
		i = 0
		for column in row:
			transposed_img[i] += [column]
			i += 1

	return transposed_img

def getFirstRowOfColor(color, img):
	"""
	Retorna la posició de la última columna de la imatge que és tota blanca abans de trobar una negra (o arribar al final)
	"""
	i, position = 0, -1
	for this in img:
		for pixel in this:
			if pixel == color:
				position = i + 1
				break
		i += 1
	return position

def getFirstColumnOfColor(color, img):
	return getFirstRowOfColor(color, transpose(img))

def split_digit(img):
	"""
	Aquesta funció rebrà una imatge img en blanc i negre retallada verticalment i retorna una tupla (D,R) en la que D és una
	imatge amb el dígit de més a l’esquerra i R és la resta de la imatge. La imatge corresponent al dígit extret D es retorna
	convenientment retallada en la direcció horitzontal. La resta R esdevé una imatge nul.la quan s’han extret tots els dígits.
	"""
	debug("La última columna tota blanca està a la pos: " + str(end_white))
	# Si no s'ha trobat cap columna vertical "blanca"...
	if end_white == -1:
		return (img, [])
		
	i = 0
	img_char, img_restant = [], []
	for row in img:
		if i > end_white:
			img_restant += [row[end_white:]]
		else:
			img_char += [row[:end_white]]
		i += 1
	return (img_char, img_restant)

split_digit([[255,255,255, 0],[255,255,255, 255]])
#print [[255,255,255, 0],[255,255,255, 255]]
#print transpose([[255,255,255, 0],[255,255,255, 255]])