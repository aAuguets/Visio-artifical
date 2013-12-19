#!/usr/bin/python
# -*- coding: utf-8 -*-

# AUTOR: Jordi Masip

def split digit(img):
	"""
	Aquesta funció rebrà una imatge img en blanc i negre retallada verticalment i retorna una tupla (D,R) en la que D és una
	imatge amb el dígit de més a l’esquerra i R és la resta de la imatge. La imatge corresponent al dígit extret D es retorna
	convenientment retallada en la direcció horitzontal. La resta R esdevé una imatge nul.la quan s’han extret tots els dígits.
	"""
	start_pos = ()
	i, j = 0, 0
	for row in img:
		i += 1
		for bit in img[row]:
			j += 1
			if bit == 255 and start_pos != (0,0):
				start_pos = (i, j)
			
