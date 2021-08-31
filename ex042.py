print('=-'*25+'\n \033[1;33m TIPO DO TRIÂNGULO\n\033[m'+'=-'*25)

from math import fabs

r1 = float(input('DIGITE O TAMANHO DO PRIMEIRA SEGMENTO DE RETA: '))
r2 = float(input('DIGITE O TAMANHO DO SEGUNDA SEGMENTO DE RETA: '))
r3 = float(input('DIGITE O TAMANHO DO TERCEIRA RETA: '))

if fabs(r2 - r3) < r1 < r2 + r3 and fabs(r1 - r3) < r2 < r1 + r3 and fabs(r1 - r2) < r3 < r1 + r2:
    print('É POSSÍVEL FORMAR UM TRIÂNGULO', end=" ")
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    elif r1 == r2 != r3 or r1 == r3 != r2 or r2 == r3 != r1: #OU APENAS 'ELSE'
        print('ISÓSCELES!')
else:
    print('NÃO É POSSÍVEL FORMAR UM TRIÂNGULO! :(')