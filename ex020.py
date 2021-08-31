import random

print('='*20+' ORDEM DE APRESENTAÇÃO '+'='*20)
alunos = []
alunos.append(input('DIGITE O NOME DO PRIMEIRO ALUNO: '))
alunos.append(input('DIGITE O NOME DO SEGUNDO ALUNO: '))
alunos.append(input('DIGITE O NOME DO TERCEIRO ALUNO: '))
alunos.append(input('DIGITE O NOME DO QUARTO ALUNO: '))
random.shuffle(alunos)

print('Ordem de apresentação é:\n{}'.format(alunos))