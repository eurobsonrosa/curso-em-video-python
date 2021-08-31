print('='*20+'CÁLCULO DE MULTA'+'='*20)

v = int(input('QUAL A VELOCIDADE DO CARRO: '))
if v > 80:
    km = v - 80
    m = km * 7
    print('VALOR DA MULTA É R${},00. VOCÊ EXCEDEU {}KM.'.format(m,km))
