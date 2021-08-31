print('='*20+'Maior e Menor valor'+'='*20)
l = []
n = int(input('Digite um valor: '))
l.append(n)
r = 0
soma = 0

v = int(input('Quer informar outro valor?\n[0] NÃO\n[1] SIM\n = '))

while v != 0:
    n = int(input('Digite um valor: '))
    l.append(n)
    v = int(input('Quer informar outro valor?\n[0] NÃO\n[1] SIM\n = '))

while r < len(l):
    soma += l[r]
    r += 1

print('Média = {}'.format(soma/len(l)))
print('Maior Valor = {}'.format(max(l)))
print('Menor valor = {}'.format(min(l)))
