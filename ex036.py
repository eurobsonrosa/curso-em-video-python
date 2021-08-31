print('='*20+' APROVAÇÃO DE EMPRÉSTIMO '+'='*20)

casa = float(input('Qual o valor da casa que desesa comprar?'))
sal  = float(input('Qual o seu salário?'))
anos = float(input('Em quantos anos deseja pagar a casa?'))

prestacao = casa/(anos*12)
print('Valor da prestação: R${:.2f}'.format(prestacao))
perc = float(prestacao/sal)

if perc <= 0.3:
    print('Empréstimo aprovado!')
else:
    print('Empréstimo negado. Valor da prestação superior a 30% do salário')
    print ('Prestação corresponde a {:.2f}% do salário'.format(perc*100))

