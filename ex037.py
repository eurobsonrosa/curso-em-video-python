print('='*20+'CONVERSOR DE BASES NUMÉRICAS'+'='*20)
num = int(input('DIGITE UM NÚMERO INTEIRO QUALQUER: '))
base = int(input('''PARA QUAL BASE DESEJA CONVERTER:
[ 1 ] - BINÁRIO
[ 2 ] - OCTAL
[ 3 ] - HEXADECIMAL

ESCOLHA SUA OPÇÃO:'''))
if base < 1 or base >3:
    print('OPÇÃO INVÁLIDA. TENTE NOVAMENTE')
else:
    print('O NÚMERO {} CONVERTIDO PARA'.format(num), end=" ")
    if base == 1:
        print('BINÁRIO É {}.'.format(bin(num)[2:]))
    elif base == 2:
        print('OCTAL É {}.'.format(oct(num)[2:]))
    else :
        print('HEXADECIMAL É {}.'.format(hex(num)[2:]))
