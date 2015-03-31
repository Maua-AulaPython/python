#exercicio 4: Faca um programa que verifique se um numero e par

def media(a):
	print "numero:", a
	resposta = (a % 2)
	if (resposta == 0):
		return "numero e par"
	else:
		return "numero e impar"

print "digite um numero"
a = int(raw_input())

print media(a)

# Nota: 1.0
# Comentario: Muito bom. So tome cuidado com o excesso de outputs
