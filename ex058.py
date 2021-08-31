import random
print('='*20+'DESAFIO DA ADVINHAÇÃO 2'+'='*20)
n1 = random.randint(0, 10)
n2 = int(input("TENTE ADIVINHAR O NÚMERO: "))
tentativas = 0
while n2 != n1:
    n2 = int(input('VOCÊ ERROU. TENTE NOVAMENTE: '))
    tentativas += 1
tentativas += 1
print('VOCÊ ACERTOU! O NÚMERO ERA {} E FORAM NECESSÁRIAS {} TENTATTIVAS'.format(n1, tentativas))
