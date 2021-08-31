from math import hypot

y = float(input('Informe a medida do cateto oposto: '))
x = float(input('Informe a media do cateto adjascente: '))

print('A Hipotenusa mede {:.2f}'.format(hypot(x,y)))
