print('='*20+' AUMENTO DE SALÁRIO '+'='*20)
sal = float(input('INFORME AQUI O SEU SALÁRIO:'))
if sal > 1250:
    print('SEU NOVO SALÁRIO É: R$ {:.2f}'.format(sal*1.1))
if sal <= 1250:
    print('SEU NOVO SALÁRIO é: R$ {:.2f}'.format(sal*1.15))
