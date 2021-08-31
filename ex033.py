print('='*20+' MAIOR E MENOR '+'='*20)
n1 = int(input('DIGITE O PRIMEIRO NÚMERO:'))
n2 = int(input('DIGITE O SEGUNDO NÚMERO:'))
n3 = int(input('DIGITE O TERCEIRO NÚMERO: '))

if n2 > n1 and n2> n3:
    print('Maior valor: {}'.format(n2))
if n1 > n2 and n1 > n3:
    print('Maior Valor: {}'.format(n1))
if n3 > n1 and n3 > n2:
    print('Maior Valor: {}'.format(n3))

if n2 < n1 and n2 < n3:
    print('Menor valor: {}'.format(n2))
if n1 < n2 and n1 < n3:
    print('Menor Valor: {}'.format(n1))
if n3 < n1 and n3 < n2:
    print('Menor Valor: {}'.format(n3))
