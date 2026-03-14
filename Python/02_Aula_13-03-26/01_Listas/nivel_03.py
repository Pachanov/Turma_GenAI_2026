#=============================================
#LISTA DE EXERCÍCIOS - PYTHON (TEMA: LISTAS)
#=============================================


# ------------------
# NÍVEL 3 - AVANÇADO
# ------------------

# 9. ANÁLISE DE VENDAS
#    Uma loja registra suas vendas diárias em uma lista. Cada venda é representada por uma 
#    sublista contendo [nome_produto, quantidade, preco_unitario]. 
#    Crie um programa que:
#    - Calcule o faturamento total
#    - Encontre o produto mais vendido (em quantidade)
#    - Crie uma lista apenas com os produtos que tiveram faturamento acima de R$100,00
#    - Mostre a média de preço dos produtos vendidos

# Vendas = [
#     ["Camiseta", 10, 29.90],
#     ["Calça", 5, 79.90],
#     ["Tênis", 3, 199.90],
#     ["Boné", 20, 15.90],
#     ["Meias", 50, 5.90]
# ]
# faturamento_total = sum(quantidade * preco for _, quantidade, preco in Vendas)
# produto_mais_vendido = max(Vendas, key=lambda x: x[1])[0]
# produtos_acima_100 = [produto for produto, quantidade, preco in Vendas if quantidade * preco > 100]
# media_preco = sum(preco for _, _, preco in Vendas) / len(Vendas)
# print(f"Faturamento total: R${faturamento_total:.2f}")
# print(f"Produto mais vendido: {produto_mais_vendido}")
# print(f"Produtos com faturamento acima de R$100,00: {produtos_acima_100}")
# print(f"Média de preço dos produtos vendidos: R${media_preco:.2f}")



# 10. PESQUISA EM LISTA ORDENADA
#     Implemente uma função chamada pesquisa_binaria que receba uma lista ordenada 
#     e um valor alvo. A função deve retornar a posição do valor na lista ou -1 se não existir.
#     Não utilize funções prontas como index() ou in.

lista_ordenada = [1, 3, 5, 7, 9, 11, 13, 15]
def pesquisa_binaria(lista, alvo):
    esquerda, direita = 0, len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1
alvo = 7
posicao = pesquisa_binaria(lista_ordenada, alvo)
if posicao != -1:
    print(f"Valor {alvo} encontrado na posição {posicao}.")
else:    print(f"Valor {alvo} não encontrado na lista.")
