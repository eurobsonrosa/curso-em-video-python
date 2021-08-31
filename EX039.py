from datetime import date


print('='*20+' ALISTAMENTO MILITAR '+'='*20)

ano = date.today().year

nasc = int(input('Digite o ano do seu nascimento:'))
idade = ano - nasc
dif = 18 - idade

if dif > 0:
    print('Faltam {} ano(s) para você se alistar'.format(dif.__abs__()))
elif dif < 0:
    print('Já passou {} ano(s) do tempo de alistamento'.format(dif.__abs__()))
else:
    print('Já está na hora de se alistar!')