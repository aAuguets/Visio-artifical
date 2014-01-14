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

#patterns

#2-Llegir la imatge de la matricula.modul imgio
img = imgio.read_bn(matricula)
#3-Convertir la matricula en blanc i negre. modul discret
#img = rgb_to_bn(img)
#4-Ajustar l'alçada de la matricula retallant les franjes blanques que puguin existir.  tranf.py
#img = htrim(img)
#img = vtrim(img)
#5-Escalar la matricula a fi i efecte que l'alçada coincideixi amb la dels patrons.+ modul transf

#6-Extreure els digits de la matricula i simultaniament, determinar a quina xifra representen mitjançant el matching. Modul split
#print "Imatge:", img
while True:
	numImg = split_digit(img)
	digits += numImg[0]
	if numImg[1] == []:
		break

#7-Mostrar l'enter que correspon a la matricula.
print "Match", match(img, patlst)

