import math

short_edge = 100

def glob_var():
	short_edge = 400
	print(short_edge)

def change_glob_var():
	global short_edge
	short_edge = 400
	print(short_edge)

glob_var()
change_glob_var()

print(short_edge)