#!/usr/bin/python
# -*- coding: utf-8 -*-

# AUTOR: Jordi Masip

from utiles import *
from imgio import *
from imgio import *

def load_patterns(prefix):
	patrons = []
	for num in range(10):
		name = prefix + "_" + num + ".jpeg"
		debug("Carregant '" + name + "'")
		patrons += [read_bn(name)]
	return patrons

def match(img, patlst):
	img_height = len(img)
	for pattern in patlst:
		#if img_height != 
	return []