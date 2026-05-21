#=============================================
#LISTA DE EXERCÍCIOS - PYTHON (TEMA: LISTAS)
#=============================================

#NÍVEL 1 - INICIANTE
#-------------------


# 1. SOMA DOS ELEMENTOS
#    Escreva um programa que crie uma lista com 5 números inteiros fornecidos pelo usuário e exiba a soma de todos os elementos.

"""soma_de_elementos = 0
numeros = []
for i in range(5):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(numero)
    soma_de_elementos += numero

print(f"A soma dos elementos é: {soma_de_elementos}") """

# 2. MAIOR E MENOR VALOR
#    Crie um programa que leia 7 números inteiros, armazene-os em uma lista e mostre o maior e o menor valor digitados, juntamente com suas respectivas posições.

"""numeros = []
for i in range(7):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(numero)
    maior = max(numeros)
    menor = min(numeros)
    print(f"O maior número é: {maior} e o menor número é: {menor}") """


# 3. CONTAGEM DE PARES
#    Faça um programa que gere uma lista com 10 números aleatórios entre 1 e 100 e mostre quantos deles são pares.

"""import random 
numeros = []

numeros_aleatorios = []
for i in range(10):
    numero = random.randint(1,100)
    numeros_aleatorios.append(numeros)
contador_pares = 0
for numero in numeros_aleatorios:
    if numeros % 2 == 0:
        contador_pares += 1
print(f"Quantidade de números pares: {contador_pares}") """
    
    


# 4. INVERTENDO A LISTA
#    Escreva um programa que leia 6 palavras e as armazene em uma lista. Em seguida, exiba a lista na ordem inversa sem usar o método reverse() ou fatiamento [::-1].

# Lê as 6 palavras e armazena na lista
palavras = []

for i in range(6):
    palavra = input(f"Digite a {i+1}ª palavra: ")
    palavras.append(palavra)

# Exibe na ordem inversa
print("\nLista na ordem inversa:")

for i in range(len(palavras) - 1, -1, -1):
    print(palavras[i])
