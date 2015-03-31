#TrabalhoPratico_exercicio1

import math

def distancia(P1x1, P1y1, P2x2, P2y2):
	d = math.sqrt(math.pow((P1x1-P2x2),2) + math.pow((P1y1-P2y2),2))
	print "distancia = %f" %d

print "digite P1x1"
P1x1 = int(raw_input())

print "digite P1y1"
P1y1 = int(raw_input())

print "digite P2x2"
P2x2 = int(raw_input())

print "digite P2y2"
P2y2 = int(raw_input())

print distancia(P1x1, P1y1, P2x2, P2y2)