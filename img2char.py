#!/usr/bin/python
# -*- coding: utf-8 -*-

from split import *
from discret import *
#from transf import *
from match import *
from img import *
import sys,imgio


if len(sys.argv) >= 2:
	matricula = sys.argv[1]
else:
	print "No està especificat el nom de la imatge"
#Per processar la matricula cal:

#1-Obtenir la llista de patrons que seran imatges en format blanc i negre.

patterns = load_patterns("images/patro")

#2-Llegir la imatge de la matricula.modul imgio
img = rgb_to_bn(imgio.read_rgb(matricula))
imgio.show(img)

#3-Convertir la matricula en blanc i negre. modul discret

#4-Ajustar l'alçada de la matricula retallant les franjes blanques que puguin existir.  tranf.py
#img = htrim(img)
#img = vtrim(img)
#5-Escalar la matricula a fi i efecte que l'alçada coincideixi amb la dels patrons.+ modul transf

#6-Extreure els digits de la matricula i simultaniament, determinar a quina xifra representen mitjançant el matching. Modul split
#print "Imatge:", img
digits = []
numImg = (img[1], img[1])
while numImg[1] != []:
	numImg = split_digit(numImg[0])
	imgio.show(("1", numImg[1]))
	match(numImg[0], patterns)
	digits += [numImg[0]]
	if numImg[1] == []:
		break

#7-Mostrar l'enter que correspon a la matricula.
#print "Match", match(img, patterns)

