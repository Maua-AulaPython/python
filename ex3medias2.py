#exercicio3: a lista termina quando eh digitado um numero negativo

def media(a):
	contador = 0
	media = 0
	while a >= 0:
		contador = contador + 1
		media = media + a
		print "digite uma nota"
		a = int(raw_input())
	else:
		mediafinal = media/contador
		return mediafinal

print "digite uma nota"
a = int(raw_input())

print "a media final eh: %d" %media(a)

# Nota: 1.0
# Comentario: Tome cuidado com o excesso de outputs.