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
	total_pixels, coincidence = len(img[0]) * len(img), 0
	print "total_pixels", total_pixels
	print "img dim:", len(img[0]), "x" ,len(img)
	#print "Ptnr dim:", get_w(("1",pttrn)), "x",get_h(("1",pttrn))
	
	for i in range(len(img)):
		for j in range(len(img[i])):
			#print img[i][j], "==", pttrn[i][j], img[i][j] == pttrn[i][j]
			if img[i][j] == pttrn[i][j]:
				coincidence += 1
	return coincidence / float(total_pixels)

def load_patterns(prefix):
	"""
	Retorna una llista de tuples on el primer element és el valor que representa el patró i el segon valor és el patró
	"""
	debug("Recordar canviar a load_patterns el range(10)")
	#print imgio.read_bn("images/matricula.png")
	return [(num, imgio.read_bn(str(prefix) + str(num) + ".jpeg")) for num in range(10)] # range(10)

def match(img, patlst):
	"""
	Retorna un número enter entre el 0-9 per indicar la matrícula o -1 si cap dels patros concorda més de 0.5 amb la matrícula
	"""
	# Mida de la imatge
	img_size = (len(img[0]), len(img))

	# ((int) valor de la imatge, (float) coincidence)
	best_match = (-1, 0.0)

	# Es compara cada pattern:
	print "n. patrons: ", len(patlst)

	for i, pattern in enumerate(patlst):
		print "-------------------------------------------------------------\nPattern n:", i
		pattern = ("1", split.vtrim(split.htrim(pattern[1])))
		#imgio.show(pattern)
		# S'escala el patró a la mida del caràcter
		debug("img_size " + str(img_size))
		pattern_size = (get_w(pattern), get_h(pattern))
		debug("pattern_size " + str(pattern_size))

		#pattern = tranf.scale(pattern, img_size[1])#"1"
		#pattern = split.htrim(split.vtrim(pattern))
		
		if img_size[1] >= pattern_size[1]:
			print "img >= pattern"
			img = tranf.scale(("1", img), pattern_size[1])
			img_size = (get_w(("", img)), get_h(("", img)))
		else:
			print "pattern > img"
			pattern = tranf.scale(pattern, img_size[1])
			pattern_size = (get_w(("1", pattern)), get_h(("1", pattern)))

		if img_size[0] >= pattern_size[0]:
			scroll = img_size[0] - pattern_size[0]
			big_size = img_size[0]
			small_size = pattern_size[0]
			big_image = img
			small_image = pattern[1]
		else:
			scroll = pattern_size[0] - img_size[0]
			big_size = pattern_size[0]
			small_size = img_size[0]
			big_image = pattern[1]
			small_image = img

		print "big_img:", type(big_image)
		print "pattern:", type(pattern)

		#imgio.show(("1", pattern))
		#imgio.show(("1", img))

		debug("Scroll: " + str(scroll))
		
		# Es desa la nova mida
		debug("pattern_size_scalated " + str(pattern_size))
		coincidences = []
		
		for position in range(scroll+1):
			#imgio.show(("1", split.image_slice_vertical(img, position, img_size[0]+1)))
			#print "tipus", type(big_image)
			#print "before v_slice", position, big_size + position
			croped_img = split.image_slice_vertical(big_image, position, small_size + position)
			#print "img", len(img[0]), "x", len(img)
			print "cropped_img", len(croped_img[0]), "x", len(croped_img)
			#print small_image
			#print "cropped_type", type(croped_img)
			#print "small_type", type(small_image)
			coincidence = compare_image(croped_img, small_image)
			print i, "-", coincidence
			#coincidences += [(coincidence, i)]
			
			debug("Coincidence: " + str(coincidence))
			if coincidence >= best_match[1]:
				best_match = (i, coincidence)
	debug("El best_match es " + str(best_match))
	print coincidences
	return best_match[0] if best_match[1] >= 0.5 else -1
