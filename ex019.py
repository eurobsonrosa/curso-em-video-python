import random

print('='*20+' SORTEIO '+'='*20)
alunos = []
alunos.append(input('DIGITE O NOME DO PRIMEIRO ALUNO: '))
alunos.append(input('DIGITE O NOME DO SEGUNDO ALUNO: '))
alunos.append(input('DIGITE O NOME DO TERCEIRO ALUNO: '))
alunos.append(input('DIGITE O NOME DO QUARTO ALUNO: '))
aluno =  random.choice(alunos)
print('\n')
print('Aluno Escolhido: {}'.format(aluno))
