print('='*20+' PROGRESSÃO ARITIMÉTICA 3'+'='*20)
pn = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
c = 1
while c < 11:
    a = pn + (c - 1) * r
    print('Termo {} = {}'.format(c, a))
    c += 1
t = int(input('GOSTARIA DE VER MAIS TERMOS: '))
while t > 0:
    c1 = c + t
    while c < c1:
        a = pn + (c - 1) * r
        print('Termo {} = {}'.format(c, a))
        c += 1
    t = int(input('GOSTARIA DE VER MAIS TERMOS: '))
print('FIM!')
