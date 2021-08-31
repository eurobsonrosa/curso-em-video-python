print('='*20+' PROGRESSÃO ARITIMÉTICA '+'='*20)
pn = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))

for c in range(1, 11):
    a = pn +(c-1)*r
    print('Termo {}: {}'.format(c, a))