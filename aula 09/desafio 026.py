frase = str(input('Digite uma frase: ').upper())
#frase = frase.split()
#print('A palavra começa com a letra a?\n{}'.format('a' in frase[0].lower()))
print('A letra A aparece {} vez(es) na palavra {}'.format(frase.count('A'), frase))
print('A primeira letra A aparece na posição {} na palavra {}'.format(frase.find('A'), frase))
print('A ultima posição de A na frase {} é {}'.format(frase, frase.rfind('A')))