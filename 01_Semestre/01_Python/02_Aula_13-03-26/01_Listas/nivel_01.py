#=============================================
#LISTA DE EXERCÍCIOS - PYTHON (TEMA: LISTAS)
#=============================================

#NÍVEL 1 - INICIANTE
#-------------------

# 1. SOMA DOS ELEMENTOS
#    Escreva um programa que crie uma lista com 5 números inteiros fornecidos pelo usuário e exiba a soma de todos os elementos.

lista_elementos = []
for i in range(5):
    num = int(input(f"Digite o {i+1}º número inteiro: "))
    lista_elementos.append(num)
print(f"A soma dos elementos é: {sum(lista_elementos)}")

# 2. MAIOR E MENOR VALOR
#    Crie um programa que leia 7 números inteiros, armazene-os em uma lista e mostre o maior e o menor valor digitados, juntamente com suas respectivas posições.

lista_7_elementos = ["1", "2", "3", "4", "5", "6", "7"]
maior = max(lista_7_elementos)
menor = min(lista_7_elementos)
cada_posicao = []
print(f"O maior valor é: {maior} e está na posição: {lista_7_elementos.index(maior)}")
print(f"O menor valor é: {menor} e está na posição: {lista_7_elementos.index(menor)}")


# 3. CONTAGEM DE PARES
#    Faça um programa que gere uma lista com 10 números aleatórios entre 1 e 100 e mostre quantos deles são pares.
Contagem_pares = 0
import random
lista_10_elementos = []
for i in range(10):
    num = random.randint(1, 100)
    lista_10_elementos.append(num)
    if num % 2 == 0:
        Contagem_pares += 1
print(f"A lista gerada é: {lista_10_elementos}")
print(f"A quantidade de números pares na lista é: {Contagem_pares}")


# 4. INVERTENDO A LISTA
#    Escreva um programa que leia 6 palavras e as armazene em uma lista. Em seguida, exiba a lista na ordem inversa sem usar o método reverse() ou fatiamento [::-1].

Lista_6_palavras = []
for i in range(6):
    Lista_6_palavras.append(input(f"Digite a {i+1}º palavra: "))
print("A lista na ordem inversa é:")
for i in range(len(Lista_6_palavras)-1, -1, -1):
    print(Lista_6_palavras[i])
