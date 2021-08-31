print('='*20+' ALUGUEL DE CARRO '+'='*20)
diaria = float(input('Quantos dias o carro foi alugado:'))
km = float(input('Quantos KM foi rodado:'))

total = 60 * diaria + km * 0.15
print('Total a pagar: R${:.2f}'.format(total))
