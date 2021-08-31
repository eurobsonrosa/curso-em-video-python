print('='*22+' PALÍNDROMO '+'='*22)
text = input('DIGITE UMA FRASE/PALAVRA: ')
print('='*56)
text = text.strip()
text = text.upper()
text_aux1 = []
text_aux2 = []

for c in range(0, len(text)):
    if text[c] != ' ':
        text_aux1.append(text[c])

for c in range(len(text_aux1), 0, -1):
    j = 1
    text_aux2.append(text_aux1[c-j])
    j -=1

print('SEU TEXTO: {}'.format(text_aux1))
print('INVERTIDO: {}'.format(text_aux2))
print('='*56)
if text_aux1 == text_aux2:
    print('A PALAVRA/FRASE É PALÍNDROMO')
else:
    print('NÃO É PALÍNDROMO')
