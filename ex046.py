from time import sleep
from emoji import emojize

print('=-'*20+' CONTAGEM REGRESSIVA '+'-='*20)
for c in range (10, 0, -1):
    print(c)
    sleep(1)
print(emojize(':sparkles::fireworks: FELIZ ANO NOVO! :fireworks::sparkles:'))