#!/usr/bin/python
# -*- coding: utf-8 -*-

# AUTOR: Jordi Masip

from utiles import *

def split_digit(img):
	"""
	Aquesta funció rebrà una imatge img en blanc i negre retallada verticalment i retorna una tupla (D,R) en la que D és una
	imatge amb el dígit de més a l’esquerra i R és la resta de la imatge. La imatge corresponent al dígit extret D es retorna
	convenientment retallada en la direcció horitzontal. La resta R esdevé una imatge nul.la quan s’han extret tots els dígits.
	"""
	end_white = -1
	i = 0
	for row in img:
		i += 1
		is_vertical = True
		# Per element de la columna...
		for value in img[column][row]:
			# Si troba un caràcter zero, salta a la següent columna
			if value == 0:
				is_vertical = False
				break
		else:
			if end_white == -1:
				end_white = i
	
	debug("La primera columna vertical està a la pos:", end_white)
	
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