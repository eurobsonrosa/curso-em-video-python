print('='*20+'MAIOR E MENOR DA SEQUÊNCIA'+'='*20)
peso = []
for c in range(0, 5):
    peso.append(float(input('DIGITE SEU PESO: ')))
print('=='*20)
print('Maior peso é {}Kg.'.format(max(peso)))
print('Menor peso é {}Kg.'.format(min(peso)))
