print('='*20+' CUSTO DA VIAGEM '+'='*20)
km = float(input('A QUANTOS KM ESTÁ O SEU DESTINO? '))
if km <= 200:
    print('SUA VIAGEM CUSTARÁ R${:.2f}'.format(km*0.50))
elif km > 200:
    print('SUA VIAGEM CUSTARÁ R${:.2f}'.format(km*0.45))
