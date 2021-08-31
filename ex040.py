print('='*20+' CÁLCULO DE MPEDIA DO ALUNO '+'='*20)

n1 = float(input('DIGITE SUA PRIMEIRA NOTA:'))
n2 = float(input('DIGITE SUA SEGUNDA NOTA:'))
m=float((n1+n2)/2)

if m < 5:
    print('REPROVADO. MÉDIA {:.2f}'.format(m))
elif 5 <= m <= 6.9:
    print('RECUPERAÇÃO. MÉDIA {:.2f}'.format(m))
elif m >= 7:
    print('APROVADO. MÉDIA {:.2f]'.format(m))