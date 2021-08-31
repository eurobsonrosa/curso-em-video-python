print('='*20+' REAL PARA DÓLAR '+'='*20)
real = float(input('Quanto dinheiro você tem em reais:'))
dolar = real//4.15
print('Com R${:.2f} reais você pode comprar US${:.2f}! :D'.format(real,dolar))


