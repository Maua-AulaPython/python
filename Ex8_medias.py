#Copie o exercicio Ex3_medias.py que voce fez na aula passada e adicione uma
#funcao que mostre a maior nota da lista. Eh necessario proteger o input do
#usuario com tratamento de excecoes.

#Exemplo de saida esperada:
# >>> Media: 5.8
# >>> Maior nota: 7.7

def media(nota):
	contador = 0
	media = 0
	maiornota = nota
	while nota >= 0:
		while True:
			contador = contador + 1
			media = media + nota
			print "digite uma nota"
			try:
				nota = int(raw_input())
				if nota > maiornota:
					maiornota = nota
				break
			except:
				print "Voce nao digitou um numero valido"
	else:
		mediafinal = media/contador
		return (mediafinal, maiornota)

print "digite uma nota"
try:
	nota = int(raw_input())
except:
	print "Voce nao digitou um numero valido"

med, mai = media(nota)
print "a media final eh: %d" % med
print "a maior nota eh: %d" % mai 


#Nota: 0.8
#Comentario: Bom uso de retorno de tupla na funcao. Boa organizacao do codigo.
#            -0.1 porque Media eh um float e nao um inteiro. -0.1 porque o
#            codigo tem um bug meio serio (o que acontece se eu digitar um
#            caractere invalido no segundo loop?)
