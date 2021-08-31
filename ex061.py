print('='*20+' PROGRESSÃO ARITIMÉTICA 2'+'='*20)
pn = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
c = 1
while c < 11:
    a = pn + (c - 1) * r
    print('Termo {} = {}'.format(c, a))
    c += 1
