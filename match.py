#!/usr/bin/python
# -*- coding: utf-8 -*-

# AUTOR: Jordi Masip

from utiles import *
from img import *
from tranf import *

def load_patterns(prefix):
	patrons = []
	for num in range(10):
		name = prefix + "_" + num + ".jpeg"
		debug("Carregant '" + name + "'")
		patrons += [read_bn(name)]
	return patrons

def match(img, patlst):
	img_size = (get_w(img), get_h(img))
	for i, pattern in enumerate(patlst):
		pattern = scale(pattern, img_size[1])
		patter_size = (get_w(pattern), get_h(pattern))
		if img_size[0] != pattern[0]:
			for each in 
	return []
