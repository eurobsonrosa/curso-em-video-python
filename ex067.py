print('='*20+'TABUADA'+'='*20)
n = int(input('Quer ver a tabuada de qual valor?'))
while True:
    if n < 0:
        break
    print('_' * 20)
    for c in range (1,11):
        print(f'{n} x {c:2} = {n*c}')
    print('_' * 20)
    n = int(input('Quer ver a tabuada de qual valor?'))
print('FIM!')