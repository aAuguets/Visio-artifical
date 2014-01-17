#!/usr/bin/python
# -*- coding: utf-8 -*-

from split import *
from discret import *
from match import *
from img import *
import sys, imgio

# Per processar la matricula cal:

if len(sys.argv) >= 2:
	matricula = sys.argv[1]
else:
	print "No està especificat el nom de la imatge"
	sys.exit(0)

# 1-Obtenir la llista de patrons que seran imatges en format blanc i negre.
print "Carregant patrons..."
patterns = load_patterns("patterns/patro_")

# 2-Llegir la imatge de la matricula.modul imgio
# 3-Convertir la matricula en blanc i negre. modul discret
img = rgb_to_bn(imgio.read_rgb(matricula))
img = vtrim(htrim(img[1]))

print "Detectant els digits..."
img_digits = []
numImg = (img, img)
while True:
	numImg = split_digit(numImg[1])
	img_digits += [numImg[0]]
	if numImg[1] == []:
		break
	numImg = ([], numImg[1])

total_dig = len(img_digits)
digits = []
for i, digit in enumerate(img_digits):
	dig = str(match(digit, patterns))
	if dig == "-1":
		continue
	digits += [dig]
	print "Completat", (i+1) / float(total_dig) * 100, "%"

# 7-Mostrar l'enter que correspon a la matricula.
print "\nMatrícula:",
for i, num in enumerate(digits):
	print num,
	if i == 3 and total_dig > 4:
		print "-",
