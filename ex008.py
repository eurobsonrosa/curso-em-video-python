print('='*20+' CONVERSÃO '+'='*20)

m = float(input('Digite uma distância em metros:'))
cm = m*100
mm = m*1000

print('{} metro(s) tem {:.1f}cm e {.1f}mm'.format(m,cm,mm))
