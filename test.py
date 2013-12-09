#!/usr/bin/python
# -*- coding: utf-8 -*-

from imgio import *

img = read_bn("images/matricula2.jpeg")
for line in img:
	new_line = []
	for val in line:
		if val == 255:
			val = "▓"
		else:
			val = "░"
		new_line += [val]
	print "".join(new_line)
