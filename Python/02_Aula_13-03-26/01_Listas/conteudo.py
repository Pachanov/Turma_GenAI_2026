#constructores de dados
#construtor_de_dados = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
#print(construtor_de_dados)



#listas

#lista1= []
# #print(type(lista1))

# """uma lista e uma coleçao de alementos em uma ordem particular
# os itens vao ser manter na ordem que voce definir
# execeptp se voce explicitamente pedir para que a ordem seja alterada"""

# lista_de_compras = ["leite", "pão", "queijo", "frutas"]
# #print(lista_de_compras)
# #listas podem conter qualquer tipo de dado

# """ Existem varias forma para acessar os itens de uma lista, a mais comum e usando o indice do item
# o indice e a posicao do item na lista, comecando do 0 para o"""

# #print(lista_de_compras[0]) #acessa o primeiro item da lista
# #print(lista_de_compras[1]) #acessa o segundo item da lista
# #print(lista_de_compras[2]) #acessa o terceiro item da lista
# #print(lista_de_compras[3]) #acessa o quarto item da lista

# #for elemento in lista_de_compras:
# #    print(elemento)

# """uma lista nada mais e do que um vetor indexado
# E um nome melhor para as listas do Python talvez fosse vetor"""

# print(lista_de_compras[2])

# """Toda lista e indexada
#     O primeiro elemnto e leite
#     O segundo elemento e pao
    
# """

# #Funcao len() - retorna o numero de itens em uma lista
# print(len(lista_de_compras)) #retorna o numero de itens na lista de compras



#Dessa forma, podemos iterar tambem de outras formas em uma lista:

# for i in range(len(lista_de_compras)):
#         print("o elemento na posicao", i, "e", lista_de_compras[i])

#Ou suando um loop while

# i= 0
# while i < len(lista_de_compras):
#     print("o elemento na posicao", i, "e", lista_de_compras[i])
#     i += 1
    
#Intervalor de indice
#podemos acessar um intervalo de itens em uma lista usando a sintaxe de fatiamento (slicing)

# print(lista_de_compras[1:3]) #acessa os itens do indice 1 ao 2 (o indice 3 nao e incluido)
# print(lista_de_compras[:2]) #acessa os itens do inicio da lista ate o

# #Alterando itens em uma lista
# lista_de_compras[0] = "leite desnatado" #altera o primeiro item da lista para "leite desnatado"
# lista_de_compras[1] = "pão integral" #altera o segundo item da lista para "pão integral"
# print(lista_de_compras)

# #Indices e Contagens
# lista_de_compras_1 = ["leite", "pão", "queijo", "frutas"]
# qtde_vezes = lista_de_compras_1.count("pão integral") #conta quantas vezes o item "pão integral" aparece na lista

# print(qtde_vezes) #imprime a quantidade de vezes que o item "pão integral" aparece na lista

# #Ordenado
# """Voce pode ordenar os elementos da lista usando sort() ou sorted()"""

# lista_de_compras_2 = ["leite", "pão", "queijo", "frutas"]
# for item in sorted(lista_de_compras_2):
#     print(item)
    
# print("Ordenado")
# lista_de_compras_2.sort() #ordena a lista de compras 2
# for item in lista_de_compras_2:
#     print(item)

# print("Ordenado Descrescente")
# lista_de_compras_2.sort(reverse=True) #ordena a lista de compras 2 em ordem decrescente
# for item in lista_de_compras_2:
#     print(item)


# #Excluindo por indice
# """Para excluir um elemento da lista por indice, utiize
#    del nome_lista[idx]
# """

# lista_de_compras = ["leite", "pão", "queijo", "frutas"]
# del lista_de_compras[1] #exclui o item no indice 1 ("pão") da lista de compras
# for item in lista_de_compras:
#     print(item)
    
    
# #Excluindo por valor
# """A funcao romeve conteudo remove o primeir elemento com o conteudo especifico
#     A fuçao pop() remove o elemento no indice especifico e retorna o valor do elemento removido
# """
# lista_de_compras = ["leite", "pão", "queijo", "frutas"]
# lista_de_compras.remove("pão") #remove o item "pão" da lista
# for item in lista_de_compras:
#     print(item)
    
# # #Inserindo itens em uma lista
# """inser (idx, item) insere o item na posicao
# #     append(item) adiciona o item no final da lista
# """
# lista_de_compras = ["leite", "pão", "queijo", "frutas"]
# lista_de_compras.insert(1, "pão integral") #insere o item "pão integral" na posicao 1 da lista de compras
# for item in lista_de_compras:
#     print(item)

# #falta exemplo completo aqui    
    
# #Lista sao heterogeneas

# """Pode misturar todo tipo de item
#     ter inteiros,strings,outras listas"""
    
# #exemplo
# lista_inteiros = [1, 2, 3, 4, 5]
# lista_strings = ["um", "dois", "tres", "quatro", "cinco"]
# lista_mista = [1, "dois", 3.0, ["quatro", "cinco"]]
# print(lista_inteiros)

# #Arrays 
# """Python prove arrays(vetores) homogeneos
#     Operam de maneira similar a lista mas em um array todos elementos precisam ser do mesmo tipo
#     (muito) mais eficiente para armazenar grandes quantidades de dados do mesmo tipo
#     Requer a importacao do modulo array
# """

#Tuplas
"""Tuplas sao similares a listas, mas sao imutaveis
    Ou seja, uma vez criada, sua conteudo nao pode ser alterado
"""
tupla_compra = ("leite", "pão", "queijo", "frutas")
for item in tupla_compra:
    print(item)
print("O intem 1 e", tupla_compra[0]) #acessa o primeiro item da tupla

tupla_compra[0] = "leite desnatado" #tenta alterar o primeiro item da tupla (isso vai gerar um erro, pois as tuplas sao imutaveis)

#Quando usar 
"""
    
"""
    
#por curiosidade
    
import sys 
lista = ["maça", "banana", "laranja"]
tupla = ("maça", "banana", "laranja")
print("Tamanho da lista:", sys.getsizeof(lista)) #tamanho da lista em bytes
print("Tamanho da tupla:", sys.getsizeof(tupla)) #tamanho da tupla em bytes

#Dicionarios