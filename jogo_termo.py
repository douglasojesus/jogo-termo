'''
Autor: Douglas Oliveira de Jesus
'''

from random import *

#Uma lista de palavras que podem ser sorteadas para ser escolhida no jogo.
lista_de_palavras=['livro', 'lindo', 'lapis', 'casa', 'amor', 'vida', 'dedo', 'pesca', 'pato', 'peixe', 'mesa', 'feio', 'jogo', 'jeito', 'adeus', 'cracha']

num=randint(0, len(lista_de_palavras)-1)

palavra=lista_de_palavras[num]

print("*"*27, '\n\t\tJOGO TERMO\n', "*"*27, sep='')
print(f"\nA PALAVRA TEM {len(palavra)} LETRAS.")

for i in range(len(palavra)):
	print("[ ]", end=' ')

qntd_tentativas=input("\n\nQuantas tentativas haverá: ")
while (not qntd_tentativas.isdigit()) or int(qntd_tentativas)<=0:
	qntd_tentativas=input("Coloque um número inteiro válido: ")
qntd_tentativas=int(qntd_tentativas)

for i in range(qntd_tentativas, 0, -1):
	letras_descobertas=[]
	posicao_descoberta=[]
	print(f"\nTentativas restantes: {i}")
	tentativa=input('Tentativa: ').lower()
	if tentativa == palavra:
		print("PARABÉNS! Acertou a palavra!")
		break
	while len(tentativa) != len(palavra):
		tentativa=input(f"Escreva uma palavra com {len(palavra)} letras: ")
	else:
		for j in range(len(palavra)):
			for k in range(len(palavra)):
				if palavra[j] == tentativa[k]:
					letras_descobertas.append(tentativa[k])
					posicao_descoberta.append(k+1)

	print("Letras descobertas e suas posições na palavra: ")
	for j in range(len(letras_descobertas)):
		print(f"Letra: {letras_descobertas[j]}\tPosição: {posicao_descoberta[j]}")
	
if tentativa != palavra: print("Não foi dessa vez!")