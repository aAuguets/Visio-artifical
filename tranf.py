#!/usr/bin/python
# -*- coding: utf-8 

# DEV: Felipe Arango

from utiles import *
from img import *
#from imgio import *
import math, split

# Les funcions htrim() i vtrim() han estat implementades a "split.py"

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