nome = input('DIGITE SEU NOME COMPLETO:')
nome = nome.upper().strip().split()
tamanho = len(nome)
print('PRIMEIRO NOME: {}'.format(nome[0]))
print('ULTIMO NOME: {}'.format(nome[tamanho-1]))