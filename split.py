#!/usr/bin/python
# -*- coding: utf-8 -*-

# AUTOR: Jordi Masip

def split_digit(img):
	"""
	Aquesta funció rebrà una imatge img en blanc i negre retallada verticalment i retorna una tupla (D,R) en la que D és una
	imatge amb el dígit de més a l’esquerra i R és la resta de la imatge. La imatge corresponent al dígit extret D es retorna
	convenientment retallada en la direcció horitzontal. La resta R esdevé una imatge nul.la quan s’han extret tots els dígits.
	"""
	
	column_pos = -1
	i = 0
	for row in img:
		i += 1
		is_vertical = True
		for value in img[column][row]:
			if value == 0:
				is_vertical *= False
		else:
			column_pos = i
			break
	
	print "La primera columna vertical està a la pos:", columns_pos
	
	# Si no s'ha trobat cap columna vertical "blanca"...
	if column_pos == -1:
		return (img, [])
		
	i, j = 0, 0
	nova_imatge = []
	img_restant = []
	for row in img:
		i += 1
		for bit in img[row]:
			j += 1
			if j <= column_pos:
				nova_imatge += [bit]
			else:
				img_restant += [bit]
	return (nova_imatge, img_restant)
