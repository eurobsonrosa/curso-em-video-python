print('='*20+'OPERAÇÕES ENTRE VALORES'+'='*20)
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('1Digite o segundo valor: '))

n3 = int(input('Escolha qual operação deseja fazer: \n[1] SOMAR \n[2] MULTIPLICAR \n'
               '[3] MAIOR \n[4] NOVOS NÚMEROS \n[5] SAIR DO PROGRAMA'))
while n3 != 5:
    if n3 == 1:
        print('='*20 + '\n {} + {} = {} \n'.format(n1, n2, n1+n2) + '='*20)
    if n3 == 2:
        print('='*20 +'\n {} x {} = {} \n'.format(n1, n2, n1*n2)+ '='*20)
    if n3 == 3:
        print('='*20 +'\n O maior número é: {} \n'.format(max(n1, n2))+'='*20)
    if n3 == 4:
        n1 = int(input('='*20 + '\nDigite o primeiro valor: '))
        n2 = int(input('1Digite o segundo valor: '))
        print('='*20)
    n3 = int(input('Escolha qual operação deseja fazer: \n[1] SOMAR \n[2] MULTIPLICAR \n'
                   '[3] MAIOR \n[4] NOVOS NÚMEROS \n[5] SAIR DO PROGRAMA'))
print('='*20 + '\nFIM!\n'+ '='*20)
