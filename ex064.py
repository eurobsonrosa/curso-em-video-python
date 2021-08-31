print('='*20+'CONTAGEM 999'+'='*20)
n = int(input('Digite um valor: '))
c = 0
while n != 999:
    c += 1
    n = int(input('Digite outro valor: '))
print('Você informou {} números antes de 999'.format(c))
