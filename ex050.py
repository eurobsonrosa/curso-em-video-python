print('='*20+' SOMA DOS PARES '+'='*20)
s = 0
for c in range(0, 6):
    n = int(input('DIGITE UM VALOR QUALQUER:'))
    if n % 2 == 0:
        s += n
print('Total da soma é {}'.format(s))