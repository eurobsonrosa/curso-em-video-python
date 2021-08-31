frase = input('DIGITE UMA FRASE:')
frase = frase.strip()
frase = frase.upper()
print('A LETRA A APARECE {} VEZES NA FRASE'.format(frase.count('A')))
print('A LETRA A APARECE PRIMEIRO NA POSIÇÃO {} E POR ULTIMO NA POSIÇÃO {} !!'.format(frase.find('A'),frase.rfind('A')))


