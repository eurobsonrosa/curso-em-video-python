print('='*20+' COMPARAR NÚMEROS '+'='*20)

n1 = int(input('DIGITE O PRIMEIRO VALOR:'))
n2 = int(input('DIGITE O SEGUNDO VALOR:'))

if n1 > n2:
    print('O primeiro número é maior!')
elif n2 > n1:
    print('O segundo número é maior!')
else:
    print(' Os números são iguais!')