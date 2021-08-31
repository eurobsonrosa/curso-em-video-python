print('='*20+'CÁLCULO PREÇO FINAL DO PRODUTO'+'='*20)
pn = float(input('DIGITE O VALOR DO PRODUTO: '))
cond = int(input('CONDIÇÃO DE PAGAMENTO:'
                 '\n1 - À VISTA DINHEIRO/CHEQUE'
                 '\n2 - À VISTA NO CARTÃO'
                 '\n3 - ATÉ 2X NO CARTÃO'
                 '\n4 - 3X OU MAIS NO CARTÃO'
                 '\nINFORME O NÚMERO CORRESPONDENTE:'))
print('PREÇO FINAL É R$', end="")
if cond == 1:
    pf = pn*0.9
    print('{:.2f}. Você ganhou 10% de desconto!'.format(pf))
elif cond == 2:
    pf = pn*0.95
    print('{:.2f}. Você ganhou 5% d desconto!'.format(pf))
elif cond == 3:
    parcela = pn/2
    print('{:.2f}. Em 2 x R${:.2f}'.format(pn,parcela))
elif cond == 4:
    pf = pn*1.2
    print('{:.2f}'.format(pf))
    n = int(input('DIGITE O NÚMERO DE PARCELAS:'))
    parcela = pf/n
    print('Em {} x R${:.2f}'.format(n,parcela))
