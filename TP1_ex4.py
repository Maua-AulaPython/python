#TrabalhoPratico_exercicio4

import math

def triangulo(A, B, C):
	if C < A + B:
		print "(%d, %d, %d) formam um triangulo retangulo" %(A, B, C)
		area = (A * B)/2
		print "area = %d" %area
	else:
		print "(%d, %d, %d) nao formam um triangulo retangulo" %(A, B, C)

print "digite cateto A"
A = int(raw_input())

print "digite cateto B"
B = int(raw_input())

print "digite hipotenuza C"
C = int(raw_input())

print triangulo(A, B, C)