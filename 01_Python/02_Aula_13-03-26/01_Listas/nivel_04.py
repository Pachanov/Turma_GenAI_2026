#=============================================
#LISTA DE EXERCÍCIOS - PYTHON (TEMA: LISTAS)
#=============================================


# -----------------
# NÍVEL 4 - DESAFIO
#-----------------

# 11. LISTA ESPIRAL
#     Crie um programa que gere uma matriz quadrada de tamanho N (fornecido pelo usuário) 
#     preenchida com números em ordem crescente no formato espiral, começando do canto 
#     superior esquerdo e girando no sentido horário.
    
#     Exemplo para N=4:
#     1   2   3   4
#     12 13  14   5
#     11 16  15   6
#     10  9   8   7

lista_espiral = []
N = int(input("Digite o tamanho da matriz quadrada (N): "))
num = 1
for i in range(N):
    lista_espiral.append([0] * N)
top, bottom, left, right = 0, N - 1, 0, N - 1
while num <= N * N:
    for i in range(left, right + 1):
        lista_espiral[top][i] = num
        num += 1
    top += 1
    for i in range(top, bottom + 1):
        lista_espiral[i][right] = num
        num += 1
    right -= 1
    for i in range(right, left - 1, -1):
        lista_espiral[bottom][i] = num
        num += 1
    bottom -= 1
    for i in range(bottom, top - 1, -1):
        lista_espiral[i][left] = num
        num += 1
    left += 1
print("Matriz em formato espiral:")
for row in lista_espiral:
    print("\t".join(map(str, row)))

# 12. COMBINAÇÕES E PERMUTAÇÕES
#     Escreva uma função recursiva que receba uma lista de elementos (sem repetição) 
#     e retorne uma lista contendo todas as permutações possíveis desses elementos.
    
#     Exemplo: Entrada = [1, 2, 3]
#     Saída = [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]

funcao_recursiva = []
def permutacoes(lista):
    if len(lista) == 0:
        return [[]]
    resultado = []
    for i in range(len(lista)):
        elemento_atual = lista[i]
        restante = lista[:i] + lista[i+1:]
        for p in permutacoes(restante):
            resultado.append([elemento_atual] + p)
    return resultado   
entrada = [1, 2, 3]
saida = permutacoes(entrada)
print(f"Permutações de {entrada}: {saida}")


