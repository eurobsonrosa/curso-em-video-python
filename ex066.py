print('='*20+'Vários números com FLag'+'='*20)
n = int(input('Digite um número(999 para parar): '))
cont = 0
soma = 0
while True:
    if n == 999:
        break
    cont += 1
    soma += n
    n = int(input('Digite um número (999 para parar): '))

print(f'Total de números digitados foi {cont} e a soma entre eles é de {soma}.\nFIM!')