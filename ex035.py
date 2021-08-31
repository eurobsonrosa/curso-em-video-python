from math import fabs
print('=-'*15+'\n \033[1;33m FORMAÇÃO DE UM TRIÂNGULO \n \033[m'+'=-'*15)
r1 = float(input('DIGITE O TAMANHO DO PRIMEIRA SEGMENTO DE RETA: '))
r2 = float(input('DIGITE O TAMANHO DO SEGUNDA SEGMENTO DE RETA: '))
r3 = float(input('DIGITE O TAMANHO DO TERCEIRA RETA: '))

if fabs(r2 - r3) < r1 < r2 + r3 and fabs(r1 - r3) < r2 < r1 + r3 and fabs(r1 - r2) < r3 < r1 + r2:
    print('É POSSÍVEL FORMAR UM TRIÂNGULO!!')
else:
    print('NÃO É POSSÍVEL FORMAR UM TRIÂNGULO! :(')
