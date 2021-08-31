print('='*20+'SOMA ÍMPARES MULTIPLOS DE 3'+'='*20)
s = 0
for c in range(1,500):
    if c % 2 != 0:
        if c % 3 == 0:
            print(c)
            s += c
print('Somatório é {}'.format(s))
