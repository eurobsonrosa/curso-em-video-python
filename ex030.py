print('='*20+' PAR OU ÍMPAR '+'='*20)

n = int(input('digite um número: '))
if n % 2 == 0:
    print('{} É PAR!'.format(n))
else:
    print('{} É ÍMPAR!'.format(n))
