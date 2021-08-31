from random import randint
from time import sleep
print('='*20+' JOKENPÔ '+'='*20)
j1 = int(input('''FAÇA SUA ESCOLHA:
0 - PEDRA
1 - PAPEL
2 - TESOURA
DIGITE O NÚMERO CORRESPONDENTE: '''))
print('='*40)

jkp = ['PEDRA', 'PAPEL', 'TESOURA']
machine = randint(0, 2)

if j1 < 0 or j1 > 2:
    print('JOGADA INVÁLIDA!')
else:
    print('JO',end="")
    sleep(1)
    print('KEN',end="")
    sleep(1)
    print('PÔ!!')
    sleep(1)
    print('=' * 40)
    print('Você:{}\nComputador: {}'.format(jkp[j1], jkp[machine]))
    print('='*40)
    if j1 == 0 and machine == 2:
        print('VOCÊ GANHOU!!')
    elif j1 == 2 and machine == 1:
     print('VOCÊ GANHOU!!')
    elif j1 == 1 and machine == 0:
        print('VOCÊ GANHOU!!')
    elif j1 == machine:
        print('EMPATE!')
    else:
        print('COMPUTADOR GANHOU!!')
