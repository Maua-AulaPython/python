#TrabalhoPratico_exercicio3

import math

def coordenadapolares(x, y):
	r = math.sqrt(math.pow(x,2) + math.pow(y,2))
	angulo = math.degrees(math.atan(y/x))
	print "distancia %f" %r
	print "angulo %f" %angulo
	return (r,angulo)
	
Ponto = []
for i in xrange (0,2):
	print "digite Ponto%d" %(i+1)
	Ponto = raw_input().split(",")
	coord = coordenadapolares(int(Ponto[0]), int(Ponto[1]))
	print Ponto
	print "coordenadas polares"
	print coord