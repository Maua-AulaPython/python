#exercicio 4: Faca um programa que verifique se um numero e par

def par(a):
	resposta = (a % 2)
	if (resposta == 0):
		return "numero %d e par" %a
	else:
		return "numero %d e impar" %a

print "digite um numero"
a = int(raw_input())

print par(a)

# Nota: 1.0
# Comentario: Muito bom. So tome cuidado com o excesso de outputs