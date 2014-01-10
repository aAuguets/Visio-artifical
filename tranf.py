#!/usr/bin/python
# -*- coding: utf-8 
# AUTOR: Felipe Arango
#Letras Blancas con fondo negro
from utiles import *
from img import *
from PIL import Image
from imgio import *


def escale(src, h):
	"""
	Scale image src taking into account height h preserving ratio aspect
	>>> scale((’RGB’, [[(255, 255, 255), (255, 255, 255), (255, 255, 255)], [(255, 255, 255),
	(255, 255, 255), (255, 255, 255)], [(255, 255, 255), (255, 255, 255), (255, 255, 255)]]),2)
	(’1’, [[(255, 255, 255), (255, 255, 255)], [(255, 255, 255), (255, 255, 255)]])
	>>> scale((’RGB’, [[(0, 0, 0), (255, 255, 255), (255, 0, 0)], [(255, 255, 255), (0, 255, 0),
	(255, 255, 255)], [(0, 0, 255), (255, 255, 255), (255, 255, 255)]]),2)
	(’1’, [[(0, 0, 0), (255, 0, 0)], [(0, 0, 255), (255, 255, 255)]])
	"""
	print "H: ",get_h(src),"  ", "W: ",get_w(src), " ","h: ",h
	Fh=get_h(src)/float(h)
	print "Fh: ",Fh
	show_console(src[1])
	

escale(('RGB', [[(0, 0, 0), (255, 255, 255), (255, 0, 0)], [(255, 255, 255), (0, 255, 0),
	(255, 255, 255)], [(0, 0, 255), (255, 255, 255), (255, 255, 255)]]),2)
