#!/usr/bin/python
# -*- coding: utf-8 -*-

# DEV: Jordi Masip

import imgio, tranf, split, sys, os
from utiles import *
from img import *

def compare_image(img, pttrn):
	"""
	Retorna un real entre 0-1 amb el nivell de coincidència de la imatge amb el patró
	"""
	total_pixels, coincidence = len(img[0]) * len(img), 0
	
	for i in range(len(img)):
		for j in range(len(img[i])):
			if img[i][j] == pttrn[i][j]:
				coincidence += 1
	if total_pixels != 0:
		return coincidence / float(total_pixels)
	return 0

def load_patterns(prefix): #prefix
	"""
	Retorna una llista de tuples on el primer element és el valor que representa el patró i el segon valor és el patró
	"""
	debug("Recordar canviar a load_patterns el range(10)")
	return [(num, imgio.read_bn(str(prefix) + str(num) + ".jpeg")) for num in range(10)]

def match(img, patlst):
	"""
	Retorna un número enter entre el 0-9 per indicar la matrícula o -1 si cap dels patros concorda més de 0.5 amb la matrícula
	"""
	# Mida de la imatge
	img_size = (len(img[0]), len(img))

	#print "img_size", img_size

	# ((int) valor de la imatge, (float) coincidence)
	best_match = (-1, 0.0)

	for i, pattern in enumerate(patlst):
		#print "-------------------------------------------------------------\nPattern n:", i
		#imgio.show(("1", pattern))
		pattern = ("1", pattern[1]) # split.vtrim(split.htrim(
		#print pattern		
		#imgio.show(pattern)

		debug("img_size " + str(img_size))
		pattern_size = (get_w(pattern), get_h(pattern))
		debug("pattern_size " + str(pattern_size))

		#pattern = tranf.scale(pattern, img_size[1])#"1"
		#pattern = split.htrim(split.vtrim(pattern))
		
		if img_size[1] >= pattern_size[1]:
			#print "img >= pattern"
			img = tranf.scale(("1", img), pattern_size[1])[1]
			img_size = (get_w(("", img)), get_h(("", img)))
			
		else:
			#print "pattern > img"
			
			pattern = tranf.scale(pattern, img_size[1])[1]

			pattern_size = (get_w(("1", pattern)), get_h(("1", pattern)))
			#print "pattern_size", pattern_size

		#print "pattern de los huevos", img[1]
		#print "pattern de los huevos", pattern[1]

		if img_size[0] >= pattern_size[0]:
			scroll = img_size[0] - pattern_size[0]
			
			big_size = img_size[0]
			small_size = pattern_size[0]
			
			big_image = img
			if isinstance(pattern, tuple):
				small_image = pattern[1]
			else:
				small_image = pattern

			#print "heeey", small_image			
			#imgio.show(("1", small_image))			
		else:
			scroll = pattern_size[0] - img_size[0]

			big_size = pattern_size[0]
			small_size = img_size[0]
			#print "solving..", type(pattern)
			if isinstance(pattern, tuple):
				big_image = pattern[1]
			else:
				big_image = pattern
			small_image = img

		#print "bs:", big_size, "\nss:", small_size

		#print "big_img:", type(big_image[0])
		#print "small_img:", type(small_image[0])

		#print len(big_image), len(big_image[0])
		#print len(small_image), len(small_image[0])
		#a = raw_input("...")

		debug("Scroll: " + str(scroll))
		
		# Es desa la nova mida
		debug("pattern_size_scalated " + str(pattern_size))
		last_coincidence = -1
		
		for position in range(scroll+1):
			croped_img = split.image_slice_vertical(big_image, position, small_size + position)
			
			#imgio.show(("1", big_image))
			#imgio.show(("1", small_image))

			#if len(croped_img) == 1:
			#	imgio.show(("1", croped_img))
			#	sys.exit(0)

			#print "cropped_img", len(croped_img[0]), "x", len(croped_img)
			#print small_image
			#print "cropped_type", type(croped_img)
			#print "small_type", type(small_image)
			coincidence = compare_image(croped_img, small_image)
			#print i, ":", coincidence
			#coincidences += [(coincidence, i)]
			#debug("Coincidence: " + str(coincidence))
			if coincidence > last_coincidence:
				last_coincidence = coincidence
		
		if best_match[1] < last_coincidence:
			best_match = (i, last_coincidence)

	debug("El best_match es " + str(best_match))
	return best_match[0] if best_match[1] >= 0.6 else -1
