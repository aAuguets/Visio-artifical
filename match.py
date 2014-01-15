#!/usr/bin/python
# -*- coding: utf-8 -*-

# DEV: Jordi Masip

import imgio, tranf, split
from utiles import *
from img import *

def compare_image(img, pttrn):
	"""
	Retorna un real entre 0-1 amb el nivell de coincidència de la imatge amb el patró
	"""	
	total_pixels, coincidence = 0, 0

	print "img dim:", len(img[0]), "-" ,len(img)

	for i in range(len(img)):
		for j in range(len(img[i])):
			if img[i][j] == pttrn[i][j]:
				coincidence += 1
	return coincidence / total_pixels

def load_patterns(prefix):
	"""
	Retorna una llista de tuples on el primer element és el valor que representa el patró i el segon valor és el patró
	"""
	debug("Recordar canviar a load_patterns el range(10)")
	return [(num, imgio.read_bn(str(prefix) + "_" + str(num) + ".jpeg")) for num in [4]] # range(10)

def match(img, patlst):
	"""
	Retorna un número enter entre el 0-9 per indicar la matrícula o -1 si cap dels patros concorda més de 0.5 amb la matrícula
	"""
	# Mida de la imatge
	img_size = (get_w(("", img)), get_h(("", img)))

	# ((int) valor de la imatge, (float) coincidence)
	best_match = (-1, 0.0)

	# Es compara cada pattern:
	for i, pattern in enumerate(patlst):
		# S'escala el patró a la mida del caràcter
		
		pattern = tranf.scale(pattern, img_size[1])
		print "type_pattern", type(pattern)
		#imgio.show(("", pattern))
		show_console(pattern)
		
		# Es desa la nova mida
		pattern_size = (get_w(("", pattern)), get_h(("", pattern)))
		coincidences = []
		print "op", img_size[0] - pattern_size[0] + 1
		for position in range(img_size[0] - pattern_size[0] + 1):
			coincidence = compare_image(split.image_slice_vertical(img, position, img_size[0]+1), pattern)
			coincidences += [(coincidence, i)]
			
			#debug("Coincidence: " + str(coincidence))
			#if coincidence >= best_match[1]:
			#	best_match = (i, coincidence)
	debug("El best_match es " + str(best_match))
	print coincidences
	return best_match[0] if best_match[1] >= 0.5 else -1
