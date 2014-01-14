#!/usr/bin/python
# -*- coding: utf-8 -*-

# DEV: Jordi Masip

from utiles import *

def mirror_effect(img):
	"""
	Retorna la imatge girada 180º sobre l'eix Y
	"""
	return [row[::-1] for row in img]

def transpose(img):
	"""
	Retorna una matriu amb les files com a columnes i les columnes com a files
	>>> transpose([[255,255,255, 255],[255,255,255, 255],[255,255,255, 255],[0,255,255, 255]])
	[[255,255,255,0],[255,255,255,255],[255,255,255,255],[255,255,255,255]]
	"""
	# Crea tantes files a "transposed_img" com columnes hi ha a "img":
	transposed_img = [[] for x in range(len(img[0]))]

	for row in img:
		i = 0
		for column in row:
			transposed_img[i] += [column]
			i += 1

	return transposed_img

def image_slice_width(image, f, to):
	"""
	Retorna la imatge entre la fila de la posició "f" fins la posició "to" (exclosa)
	>>> image_slice_width([[0,0,0], [0,0,0], [255,255,255]], 1,2)
	[[0], [0], [255]]
	"""
	return [row[f:to] for row in image]

def getPositionOfFirstRowOfColor(color, img):
	"""
	Retorna la posició de la primera fila de la imatge que és tota del color "color"
	>>> getPositionOfFirstRowOfColor(0, [[255,255,255, 255],[255,255,255, 255],[255,255,255, 255],[0,255,255, 255]])
	-1
	>>> getPositionOfFirstRowOfColor(255, [[255,255,255, 255],[255,255,255, 255],[255,255,255, 255],[0,255,255, 255]])
	0
	>>> getPositionOfFirstRowOfColor(255, [[0,255,255, 255],[255,255,255, 255],[255,255,255, 255],[0,255,255, 255]])
	1
	"""
	position = 0
	for row in img:
		all_the_same = True
		for pixel in row:
			if pixel != color:
				all_the_same = False
				break
		if all_the_same:
			return position
		position += 1
	return -1

def getPositionOfFirstColumnOfColor(color, img):
	"""
	Retorna la posició de la primera columna de la imatge que és tota del color "color"
	>>> getPositionOfFirstColumnOfColor(0, [[255,255,255, 255],[255,255,255, 255],[255,255,255, 255],[0,255,255, 255]])
	-1
	>>> getPositionOfFirstColumnOfColor(0, [[255,0,255, 255],[255,0,255, 255],[0,0,0,0],[0,0,255, 255]])
	1
	"""
	return getPositionOfFirstRowOfColor(color, transpose(img))

def getPositionOfFirstRowOfColorDiff(color, img):
	"""
	Retorna la posició de la primera fila de la imatge que és tota d'un color diferent de "color"
	>>> getPositionOfFirstRowOfColorDiff(0, [[0,0,0,0], [255,255,255,255],[255,255,255,255],[0,255,255, 255],[0,0,0,0]])
	1
	>>> getPositionOfFirstRowOfColorDiff(0, [[0,0,0,0], [0,255,255,255],[255,255,255,255],[0,255,255, 255],[0,0,0,0]])
	2
	"""
	position = 0
	for row in img:
		all_the_same = True
		for pixel in row:
			all_the_same *= pixel != color
		if all_the_same:
			return position 
		position += 1
	return -1

def getPositionOfFirstColumnOfColorDiff(color, img):
	"""
	Retorna la posició de la primera columna de la imatge que és tota d'un color diferent de "color"
	>>> getPositionOfFirstColumnOfColorDiff(0, [[0,0,255,0], [255,255,255,255],[255,255,255,255],[0,255,255, 255],[0,0,255,0]])
	2
	"""
	return getPositionOfFirstRowOfColorDiff(color, transpose(img))

def split_digit(img):
	"""
	Aquesta funció rebrà una imatge img en blanc i negre retallada verticalment i retorna una tupla (D,R) en la que D és una
	imatge amb el dígit de més a l’esquerra i R és la resta de la imatge. La imatge corresponent al dígit extret D es retorna
	convenientment retallada en la direcció horitzontal. La resta R esdevé una imatge nul.la quan s’han extret tots els dígits.
	###>>> split_digit([[255,255,255, 0],[255,255,255, 255]])
	"""
	# S'escapça la imatge
	img = vtrim(htrim(img))

	# S'obté la posició de la primera columna on tot és blanc (aquesta serà la cordenada on acaba el primer caràcter)
	pos_end_first_char = getPositionOfFirstColumnOfColor(WHITE, img)

	# Es fa un slice del primer caràcter, des de 0->pos_end_first_char
	img_char = image_slice_width(img, 0, pos_end_first_char)

	# Es fa un slice de la resta de caràcters des de pos_end_first_char->final
	img_restant = image_slice_width(img, pos_end_first_char, len(img) - 1)

	# Es retorna una tupla (img_char, img_restant)
	return (img_char, vtrim(img_restant))

print [[255,255,255, 0],[255,255,255, 255]]
print mirror_efect([[255,255,255, 0],[255,255,255, 255]])