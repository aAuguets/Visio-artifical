#!/usr/bin/python
# -*- coding: utf-8 
# AUTOR: Felipe Arango
#Letras Blancas con fondo negro
from utiles import *
from img import *
import math
#from PIL import Image
#from imgio import *


def scale(src, h):
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
	Fh=get_h(src)/float(h) 	#Factor d'escalat
	new_w=get_w(src)/float(Fh)				#Nova amplada per l'escalada
	print "nova mida:  Alçada",h," Amplada: ",int(new_w),"No int: ",new_w
	print "Fh: ",Fh
	nova_imatge=[]
	src_imatge=src[1]		#retorna només l'imatge src (senre el "RGB")
	print "W----------->",new_w,"    ",int(new_w)
	print "H----------->",h,"    ",int(h)
	for a in range(int(h)):
		for b in range(int(new_w)):
			#print (a*Fh+1),"Int: ",math.ceil(a*Fh+1),",",(b*Fh+1),"Int ",math.ceil(b*Fh+1)
			nova_imatge+=(src_imatge[int(math.ceil(a*Fh))], [int(math.ceil(b*Fh))])
			#print nova_imatge
	print "Resultat: ",nova_imatge
			
			
			
	
	

#Matriu   ([[(0, 0, 0),(255, 255, 255), (255, 0, 0)], 
#	    [(255, 255, 255), (0, 255, 0), (255, 255, 255)], 
#	    [(0, 0, 255), (255, 255, 255), (255, 255, 255)]])
#_________________________________________________
#Resultat   [[(0, 0, 0), (255, 0, 0)],
#	    [(0, 0, 255), (255, 255, 255)]]
####
####
#Matriu [[(255, 255, 255), (255, 255, 255), (255, 255, 255)], 
#	[(255, 255, 255),(255, 255, 255), (255, 255, 255)],
#	[(255, 255, 255), (255, 255, 255), (255, 255, 255)]]
###

print ""
print "Escalat: "
show_console([[(0, 0, 0), (255, 0, 0)], [(0, 0, 255), (255, 255, 255)]])
print ""
show_console([[(255, 255, 255), (255, 255, 255), (255, 255, 255)], [(255, 255, 255),
	(255, 255, 255), (255, 255, 255)], [(255, 255, 255), (255, 255, 255), (255, 255, 255)]])
print ""
print "Escalat: "
show_console([[(255, 255, 255), (255, 255, 255)], [(255, 255, 255), (255, 255, 255)]])
scale(("RGB", [[(0, 0, 0), (255, 255, 255), (255, 0, 0)], [(255, 255, 255), (0, 255, 0),
	(255, 255, 255)], [(0, 0, 255), (255, 255, 255), (255, 255, 255)]]),2)
