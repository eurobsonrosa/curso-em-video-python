print('='*20+' ANO BISSEXTO '+'='*20)
ano = int(input('DIGITE UM ANO: '))
if ano%4 != 0:
    print('{} não é ano Bissexto!'.format(ano))

if ano%4 == 0 and ano%100 == 0 and ano%400 == 0:
    print('{} é ano Bissexto!'.format(ano))

if ano%4 == 0 and ano%100 != 0:
    print('{} é ano bissexto.'.format(ano))

ano2 = int(input('DIGITE UM ANO QUALQUER: '))
j = 0
while j != 1:
    ano2 = ano2 + 1
    if ano2%4 == 0 and ano2%100 != 0:
        j = 1

    if ano2 % 4 == 0 and ano2 % 100 == 0 and ano2 % 400 == 0:
        j = 1

print('PRÓXIMO ANO BISSEXTO É {} !'.format(ano2))
