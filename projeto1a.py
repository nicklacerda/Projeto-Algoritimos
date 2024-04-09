import math


origem_x = int(input("Digite o valor X da origem: "))
origem_y = int(input("Digite o valor Y da origem: "))
N_pontos = int(input("Quantos pontos serão no total?: "))

contador = 0

quadrante1 = 0
quadrante2 = 0
quadrante3 = 0
quadrante4 = 0

ponto_mais_distante = ''
ponto_mais_proximo = ''

maior_distancia = 0
menor_distancia = 10000

# quando o contador for igual ao número de pontos, todos os pontos já terão sido escritos
while contador < N_pontos:
    x_ponto = int(input("Digite o valor X do ponto: "))
    y_ponto = int(input("Digite o valor Y do ponto: "))


#após passarem pelas condicionais os pontos são adicionados ou não a um quadrante.
# EX: se o ponto está no quadrante 1 quadrante1 += 1    
    
    if x_ponto == 0 and y_ponto == 0:
        print(f"O ponto ({x_ponto, y_ponto}) está no ponto de origem do plano cartesiano")
    elif y_ponto == origem_y:
        print(f"O ponto ({x_ponto, y_ponto}) está no eixo de coordenadas")
    elif x_ponto == origem_x:
        print(f"O ponto ({x_ponto, y_ponto}) está no eixo de coordenadas")
    elif x_ponto >= 0 and y_ponto >= 0:
        print(f"O ponto ({x_ponto, y_ponto}) está no primeiro quadrante")
        quadrante1 += 1
    elif x_ponto <= 0 and y_ponto >= 0:
        print(f"O ponto ({x_ponto, y_ponto}) está no segundo quadrante")
        quadrante2 += 1
    elif x_ponto <= 0 and y_ponto <= 0:
        print(f"O ponto ({x_ponto, y_ponto}) está no terceiro quadrante")
        quadrante3 += 1
    elif x_ponto >= 0 and y_ponto <= 0:
        print(f"O ponto ({x_ponto, y_ponto}) está no quarto quadrante")
        quadrante4 += 1
    
    
    
    distancia = math.sqrt((x_ponto - origem_x)**2 + (y_ponto - origem_y)**2)


#armazena sempre os dados atualizados do loop das distâncias e seus respectivos pontos 

    if distancia < menor_distancia:
        menor_distancia = distancia
        ponto_mais_proximo = str(f'({x_ponto}, {y_ponto})')
    
    if distancia > maior_distancia:
        maior_distancia = distancia
        ponto_mais_distante = str(f'({x_ponto}, {y_ponto})')


    contador += 1

print(f'Existe(m) {quadrante1} ponto(s) no 1º quadrante; {quadrante2} no 2º quadrante; {quadrante3} no 3º quadrante e {quadrante4} no 4º quadrante.')
print(f'A menor distância é {menor_distancia:.4f} do ponto {ponto_mais_proximo}')
print(f'A maior distância é {maior_distancia:.4f} do ponto {ponto_mais_distante}')