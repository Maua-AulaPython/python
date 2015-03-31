#TrabalhoPratico_exercicio5
import math

a = 6378160
E = 0.00669454185

def coordenadas(x, y, z):
	P = math.sqrt(math.pow(x,2) + math.pow(y,2))
	N = 1
	h = 0

	longitude = math.atan(y/x)
	print longitude

	for i in range(0,5):
		latitude = math.atan(z / (P * (1 - E * N / (N + h)))) 
		N = a/(math.sqrt(1 - E * math.sin(latitude) ** 2))
		h = P / math.cos(latitude) - N
		return math.degrees(latitude), math.degrees(longitude), h
 
print "digite coordenada cartesiana x"
x = float(raw_input())

print "digite coordenada cartesiana y"
y = float(raw_input())

print "digite coordenada cartesiana z"
z = float(raw_input())

print coordenadas(x, y, z)
