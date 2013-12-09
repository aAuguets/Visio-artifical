#!/usr/bin/python
# -*- coding: utf-8 -*-

# AUTOR: Jordi Masip

from utiles import *
from imgio import *

def load_patterns(prefix):
	patrons = []
	for num in range(10):
		name = prefix + "_" + num + ".jpeg"
		debug("Carregant '" + name + "'")
		patrons += [read_bn(name)]
	return patrons

def match(img, patlst):
	for pattern in patlst:
		pass
	return []