print('='*20+' NÚMEROS PRIMOS '+'='*20)
n = int(input('Digite um número inteiro: '))
v = 0
for c in range(0, n):
    if n % (c+1) == 0:
        if n != (c+1) and c+1 != 1:
            v = 1
if v == 1:
    print('NÃO é número primo!')
else:
    print('É número primo!')
