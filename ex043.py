print('='*20+' CÁLCULO IMC '+'='*20)
peso = float(input('DIGITE SEU PESO EM Kg: '))
altura = float(input('DIGITE DUA ALTURA EM METROS: '))

imc = float(peso/(altura**2))
print('IMC {:.2f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso!')
elif imc < 25:
    print('Você está no peso ideal!')
elif imc < 30:
    print('Você está em sobrepeso!')
elif imc < 40:
    print('Você está com obesidade!')
else:
    print('Você está com obesidade mórbida!')