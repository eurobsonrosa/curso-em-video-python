print('='*20+' ANALISADOR COMPLETO '+'='*20)
nome = []
idade = []
sexo = []
somaIdade = 0
somaW = 0
oldman = 0
for c in range(0, 4):
    print('------ {}ª Pessoa ------'.format(c+1))
    nome.append(str(input('NOME: ')))
    idade.append(int(input('IDADE: ')))
    sexo.append(str(input('SEXO [M/F]:')))
print('='*30)
for c in range(0, len(nome)):
    nome[c] = nome[c].upper().strip()
    sexo[c] = sexo[c].upper().strip()
for c in range(0, len(nome)):
    print('Nome:{} Idade: {} Sexo: {}'.format(nome[c], idade[c], sexo[c]))
print('-'*30)
for c in range(0, len(sexo)):
    if sexo[c] == 'M':
        if idade[c] >= oldman:
            oldman = idade[c]
for c in range(0, len(sexo)):
    if sexo[c] == 'F':
        if idade[c] <= 20:
            somaW += 1
for c in range(0, len(idade)):
   somaIdade += idade[c]
print('Média de Idade do grupo: {:.2f}'.format(somaIdade/len(idade)))
print('-' * 30)
print('O homem mais velho do grupo é {} e tem {} anos.'.format(nome[idade.index(oldman)], max(idade)))
print('-' * 30)
print('{} mulheres abaixo dos 20 anos'.format(somaW))
