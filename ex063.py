print('='*20+'SEQUENCIA DE FIBONACCI'+'='*20)
n = int(input('QUANTOS ELEMENOS GOSTARIA DE VER: '))
c = 0
fn = []
while c < n:
    if c == 0:
        fn.append(c)
    elif c == 1:
        fn.append(c)
    else:
        f = fn[c-1] + fn[c-2]
        fn.append(f)
    c += 1
print(fn)
z = 0
while z < n:
    print(' → {}'.format(fn[z]), end='')
    z += 1
