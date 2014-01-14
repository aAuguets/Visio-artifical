#!/usr/bin/python
# -*- coding: utf-8 -*-

# DEV: Jordi Masip

from utiles import *

def transpose(img):
	"""
	Retorna una matriu amb les files com a columnes i les columnes com a files
	"""
	# Crea tantes files a "transposed_img" com columnes hi ha a "img":
	transposed_img = [[] for x in range(len(img[0]))]

	for row in img:
		i = 0
		for column in row:
			transposed_img[i] += [column]
			i += 1

	return transposed_img

def getPositionOfLastRowOfColor(color, img):
	"""
	Retorna la posició de la última fila de la imatge que és tota del color "color" abans de trobar una d'un altre color (o arribar al final)
	>>> getPositionOfLastRowOfColor(0, [[255,255,255, 255],[255,255,255, 255],[255,255,255, 255],[0,255,255, 255]])
	2
	"""
	position = 0
	for row in img:
		for pixel in row:
			if pixel == color:
				return position - 1
		position += 1
	return position

def getPositionOfLastColumnOfColor(color, img):
	"""
	Retorna la posició de la última columna de la imatge que és tota del color "color" abans de trobar una d'un altre color (o arribar al final)
	>>> getPositionOfLastColumnOfColor(0, [[255,255,255, 255],[255,255,255, 255],[255,255,255, 255],[0,255,255, 255]])
	-1
	"""
	return getPositionOfLastRowOfColor(color, transpose(img))

def split_digit(img):
	"""
	Aquesta funció rebrà una imatge img en blanc i negre retallada verticalment i retorna una tupla (D,R) en la que D és una
	imatge amb el dígit de més a l’esquerra i R és la resta de la imatge. La imatge corresponent al dígit extret D es retorna
	convenientment retallada en la direcció horitzontal. La resta R esdevé una imatge nul.la quan s’han extret tots els dígits.
	###>>> split_digit([[255,255,255, 0],[255,255,255, 255]])
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