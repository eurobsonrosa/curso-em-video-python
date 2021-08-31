print('=' * 20 + ' VALIDADOR DE SEXO ' + '=' * 20)
sexo = str(input('Qual seu sexo? [M/F]:')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Valor inválido! Qual seu sexo? M - Para masculino. F - Feminimo:')).strip().upper()[0]
print('Sexo {} registrado!'.format(sexo))
