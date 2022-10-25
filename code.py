import random
import numpy as np

campo = []
campo_jogador = []
tamanho_campo = input('Tamanho do campo: ')
tamanho_campo2 = int(tamanho_campo)
qtd_bomb = input('Quantidade de bombas no campo: ')
pont = 0

for i in range(int(tamanho_campo)):
    campo.append( [0] * int(tamanho_campo))

campo_jogador = np.zeros(shape = (int(tamanho_campo), int(tamanho_campo)))


for i in range(int(qtd_bomb)):
    random_index = random.randint(0,int(tamanho_campo)-1)
    random_index2 = random.randint(0,int(tamanho_campo)-1)
    campo[random_index][random_index2] = 1

print(str(campo_jogador).replace(' [', '').replace('[', '').replace(']', '').replace('.', ''))
#print(campo)

jogo = True

while jogo == True:
    valor_x = input('Insira o valor de x: ')
    valor_y = input('Insira o valor de y: ')
    if campo[int(valor_x) - 1][int(valor_y) - 1] == 1:
        jogo = False
        print(str(campo_jogador).replace(' [', '').replace('[', '').replace(']', '').replace('.', ''))
        print('Vc perdeu!')
        print('Pontos:', pont)
        break
    else:        
        campo_jogador[int(valor_x) - 1][int(valor_y) - 1] = 1
        pont = pont + 1
        print(str(campo_jogador).replace(' [', '').replace('[', '').replace(']', '').replace('.', ''))
