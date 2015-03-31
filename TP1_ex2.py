#TrabalhoPratico_exercicio2

import math

def distancia(P1x1, P1y1, P2x2, P2y2):
	d = math.sqrt(math.pow((P1x1-P2x2),2) + math.pow((P1y1-P2y2),2))
	print "distancia = %f" %d
	return d

Lista = []
Q = True
while Q:
	print "digite ponto P(x,y) (exemplo: 1,2):"
	Ponto = raw_input().split(",")
	Lista.append((int(Ponto[0]), int(Ponto[1])))
	print "continua? (s/n)"
	Sair = raw_input()
	if Sair == "n":
		Q = False

print Lista

dmaior = 0

for i in xrange(0, len(Lista)-1):
	for l in xrange(i+1,len(Lista)):
		d = distancia(Lista[i][0], Lista[i][1], Lista[l][0],Lista[l][1])
		if d > dmaior:
			dmaior = d

print "a maior distancia eh de: %f" %dmaior