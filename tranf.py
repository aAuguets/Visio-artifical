#!/usr/bin/python
# -*- coding: utf-8 

# DEV: Felipe Arango

from utiles import *
from img import *
#from imgio import *
import math, split


def scale(src, h):
	"""
	Scale image src taking into account height h preserving ratio aspect
	>>> scale(('RGB', [[(255, 255, 255), (255, 255, 255), (255, 255, 255)], [(255, 255, 255),
	(255, 255, 255), (255, 255, 255)], [(255, 255, 255), (255, 255, 255), (255, 255, 255)]]),2)
	('1', [[(255, 255, 255), (255, 255, 255)], [(255, 255, 255), (255, 255, 255)]])
	>>> scale(('RGB', [[(0, 0, 0), (255, 255, 255), (255, 0, 0)], [(255, 255, 255), (0, 255, 0),
	(255, 255, 255)], [(0, 0, 255), (255, 255, 255), (255, 255, 255)]]),2)
	('1', [[(0, 0, 0), (255, 0, 0)], [(0, 0, 255), (255, 255, 255)]])
	"""
	#print "H: ",get_h(src),"  ", "W: ",get_w(src), " ","h: ",h

	# Factor d'escalat
	Fh = get_h(src)/float(h)

	# Nova amplada per l'escalada
	new_w=get_w(src)/float(Fh)
	print "nova mida:  Alçada",h," Amplada: ",int(new_w),"No int: ",new_w
	print "Factor de converció: ",Fh
	
	nova_imatge=[]
	imatge_final=[]
	src_imatge=src[1]		#retorna només l'imatge src (senre el "RGB")
	for a in range(int(h)):
		for b in range(int(new_w)):
			#print (a*Fh+1),"Int: ",math.ceil(a*Fh+1),",",(b*Fh+1),"Int ",math.ceil(b*Fh+1)
			nova_imatge += (src_imatge[int(math.ceil(a*Fh))][int(math.ceil(b*Fh))],)
			#print "nova img: ",nova_imatge
		imatge_final+=[nova_imatge]
		nova_imatge=[]	
	print "Resultat: ", imatge_final

def vtrim(img):
	"""
	Retalla tot el color blanc que hi ha a l'esquerra i a la dreta de la imatge abans de trobar-se un caràcter
	>>> vtrim([[255,255,0],[255,0,0]])
	[[255, 0], [0, 0]]
	>>> vtrim([[255,255,0,255],[255,255,0,255], [0, 255, 0,255]])
	[[255,255,0],[255,255,0], [0, 255, 0]]
	"""
	position = split.getPositionOfFirstColumnOfColorDiff(255, img)
	img = split.image_slice_vertical(img, position+1, len(img[0]))
	img = split.mirror_effect(img)
	position = split.getPositionOfFirstColumnOfColorDiff(0, img, True)

	if position == -1:
		position = len(img[0])
	img = split.image_slice_vertical(img, 0, position)
	return split.mirror_effect(img)

def htrim(img):
	"""
	Retalla tot el color blanc que hi ha a dalt i abaix de la imatge abans de trobar-se un caràcter
	>>> htrim([[255,255,255],[255,0,0]])
	[[255, 0, 0]]
	>>> htrim([[255,255,255],[255,255,255],[255,255,255],[255,0,0], [255,255,255], [255,255,255]])
	[[255, 0, 0]]
	"""
	position = split.getPositionOfFirstRowOfColorDiff(255, img)
	img = split.image_slice_horizontal(img, position, len(img[0]))
	img = img[::-1]
	position = split.getPositionOfFirstRowOfColorDiff(255, img)
	if position == -1:
		position = len(img[0])
	return split.image_slice_horizontal(img[::-1], 0, position)