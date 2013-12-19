#!/usr/bin/python
# -*- coding: utf-8 -*-

# AUTOR: Jordi Masip

def split_digit(img):
	"""
	Aquesta funció rebrà una imatge img en blanc i negre retallada verticalment i retorna una tupla (D,R) en la que D és una
	imatge amb el dígit de més a l’esquerra i R és la resta de la imatge. La imatge corresponent al dígit extret D es retorna
	convenientment retallada en la direcció horitzontal. La resta R esdevé una imatge nul.la quan s’han extret tots els dígits.
	"""
	width = len(img)
	start_white = -1
	end_white = width + 1
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
			if start_white == -1:
				start_white = i
			elif end_white == width + 1:
				end_white = i
			
	
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
			if j <= start_white:
				nova_imatge += [bit]
			elif j 
				img_restant += [bit]
	return (nova_imatge, img_restant)
