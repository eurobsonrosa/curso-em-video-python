print('='*20+'FATORIAL'+'='*20)
n1 = int(input('DIGITE UM VALOR: '))
nAux = n1
n2 = n1
while n1 > 1:
    n2 *= (n1 - 1)
    n1 -= 1
print('{}! = {}'.format(nAux, n2))
