#=============================================
#LISTA DE EXERCÍCIOS - PYTHON (TEMA: LISTAS)
#=============================================

# ------------------------
# NÍVEL 2 - INTERMEDIÁRIO
# -----------------------

# 5. MÉDIA E ACIMA
#    Crie um programa que leia as notas de uma turma (quantidade indefinida). 
#    O programa deve parar quando o usuário digitar -1. 
#    Calcule a média da turma e mostre quantos alunos obtiveram nota acima dessa média.

notas_da_turma = []
while True:
    nota = float(input("Digite a nota do aluno (ou -1 para finalizar): "))
    if nota == -1:
        break
    notas_da_turma.append(nota)

if notas_da_turma:
    media = sum(notas_da_turma) / len(notas_da_turma)
    acima_da_media = len([nota for nota in notas_da_turma if nota > media])
    print(f"A média da turma é: {media:.2f}")
    print(f"Quantidade de alunos com nota acima da média: {acima_da_media}")

# 6. REMOVENO DUPLICATAS
#    Desenvolva um programa que receba uma lista de números inteiros (pode ter valores repetidos) 
#    e crie uma nova lista apenas com os valores únicos, mantendo a ordem de primeira aparição.

numeros_com_duplicatas = [1, 2, 3, 2, 4, 1, 5]
numeros_unicos = []
for num in numeros_com_duplicatas:
    if num not in numeros_unicos:
        numeros_unicos.append(num)
print(f"Lista original: {numeros_com_duplicatas}")
print(f"Lista com valores únicos: {numeros_unicos}")

# 7. LISTAS DENTRO DE LISTAS
#    Faça um programa que crie uma matriz 3x3 (3 linhas e 3 colunas) preenchida com números 
#    fornecidos pelo usuário. No final, exiba a matriz na tela e mostre:
#    - A soma de todos os elementos
#    - A soma da primeira linha
#    - A soma da diagonal principal


    
linha = []
coluna = []
for i in range(3):
    for j in range(3):
        num = int(input(f"Digite o número para a posição [{i}][{j}]: "))
        linha.append(num)
    coluna.append(linha)
    linha = []
print("Matriz 3x3:")
for linha in coluna:
    print(linha)
soma_total = sum(sum(linha) for linha in coluna)
soma_primeira_linha = sum(coluna[0])
soma_diagonal_principal = sum(coluna[i][i] for i in range(3))
print(f"Soma de todos os elementos: {soma_total}")
print(f"Soma da primeira linha: {soma_primeira_linha}")
print(f"Soma da diagonal principal: {soma_diagonal_principal}")


# 8. INTERCALANDO LISTAS
#    Escreva um programa que leia duas listas de 5 elementos cada e gere uma terceira lista 
#    com os elementos intercalados (primeiro da lista A, primeiro da lista B, segundo da lista A, etc.)

leitura_lista_a = []
leitura_lista_b = []
for i in range(5):
    leitura_lista_a.append(input(f"Digite o {i+1}º elemento da lista A: "))
for i in range(5):
    leitura_lista_b.append(input(f"Digite o {i+1}º elemento da lista B: "))
lista_intercalada = []
for i in range(5):
    lista_intercalada.append(leitura_lista_a[i])
    lista_intercalada.append(leitura_lista_b[i])
print(f"Lista A: {leitura_lista_a}")
print(f"Lista B: {leitura_lista_b}")
print(f"Lista intercalada: {lista_intercalada}")



