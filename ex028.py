import random

print('='*20+'DESAFIO DA ADVINHAÇÃO'+'='*20)
print('ESCOLHENDO NÚMERO...')
print('VAMOS LÁ!! ')
n1 = random.randint(0, 5)

n2 = int(input('TENTE ADVINHAR O NÚMERO QUE ESCOLHI...: '))

if n1 == n2:
    print('PARABÉNS VOCÊ ACERTOU!')
else:
    print('QUE PENA VOCÊ ERROU... O NÚMERO ERA {}'.format(n1))

