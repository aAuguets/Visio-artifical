#!/usr/bin/python
# -*- coding: utf-8 -*-

# AUTOR: Jordi Masip

DEBUG = True

BLACK = 0
WHITE = 255

def debug(msg):
	if DEBUG:
		print "[DEBUG]", msg
def show_console(img):
	for line in img:
		new_line = []
		for val in line:
			if isinstance(val, tuple):
				val = (val[0] + val[1] + val[2])/3
			if val >= 128:
				val = " "
			else:
				val = "▓"
			new_line += [val]
		print "".join(new_line)
