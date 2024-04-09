import math

x_origem = int(input('Digite a coordenada X do ponto de origem A do robô: '))
y_origem = int(input('Digite a coordenada Y do ponto de origem A do robô: '))

segundos = int(input('Digite por quanto tempo o robô irá caminhar: '))

passo_cima = 0
passo_direita = 0

#o algoritmo segue sendo cima-direita-direita. Sendo assim, é um algoritmo de 3 passos

x_final = 0
y_final = 0

# Ao dividir os segundos/passos por 3, é possível determinar, a partir do resto da divisão, quantos
#movimentos para cima e para direita foram efetuados

if (segundos % 3) == 0:

    passo_cima = (segundos/3)
    passo_direita = segundos - passo_cima

    x_final = x_origem + passo_direita
    y_final = y_origem + passo_cima
elif (segundos % 3) == 1:

    passo_cima = ((segundos-1)/3) + 1
    passo_direita = segundos - passo_cima

    x_final = x_origem + passo_direita
    y_final = y_origem + passo_cima

elif (segundos % 3) == 2:

    passo_cima = ((segundos-2)/3) + 1
    passo_direita = segundos - passo_cima

    x_final = x_origem + passo_direita
    y_final = y_origem + passo_cima

print(f'Ao final da caminhada o robô estará no ponto ({x_final}, {y_final}) do plano cartesiano')