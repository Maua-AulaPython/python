#exercicio3: a lista termina quando eh digitado um numero negativo

def media(a):
	contador = 0
	media = 0
	while a >= 0:
		contador = contador + 1
		media = media + a
		print a
		print media
		print "digite uma nota"
		a = int(raw_input())
	else:
		mediafinal = media/contador
		print "a media final eh"
		print mediafinal

print "digite uma nota"
a = int(raw_input())

print media(a)