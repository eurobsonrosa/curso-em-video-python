from datetime import date
print('='*20+'GRUPO DA MAIORIDADE'+'='*20)
m = 0
n = 0
for c in range(0, 7):
    nasc = int(input('Digite o ano do seu nascimento: '))
    if date.today().year - nasc >= 21:
        m += 1
    else:
        n += 1
print('=='*20)
print('{} pessoas atingiram a maioridade e {} ainda não atingiram a maioridade'.format(m, n))
