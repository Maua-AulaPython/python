#exercicio 3: faca um programa que leia 3 notas e calcule a media delas

def media(a, b, c):
	print "nota1:", a
	print "nota2:", b
	print "nota3:", c
	print "A media do aluno foi:"
	resposta = (a + b + c)/3
	return resposta

print "digite a nota 1"
a = int(raw_input())

print "digite a nota 2"
b = int(raw_input())

print "digite a nota 3"
c = int(raw_input())  

print media(a, b, c)