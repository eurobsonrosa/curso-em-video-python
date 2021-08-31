print('='*20+' QUANTO DE TINTA IREI PRECISAR '+'='*20)
h = float(input('Altura da parede:'))
w = float(input('Largura da parede:'))

print('Sua parede tem tem {}x{} = {}m²'.format(h,w,h*w))
if (h*w)%2 == 0:
    print('Necessário {}lde tinta'.format((h*w)/2))
if (h*w)%2 != 0:
    print('Necessário {}l de tinta'.format((h*w)//2+1))

