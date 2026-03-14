#  BÔNUS - PROJETO UM POUCO MAIS COMPLEXO
# ----------------------------------------------

# 13. SISTEMA DE GERENCIAMENTO DE ESTOQUE
#     Desenvolva um sistema simples de estoque utilizando listas. O sistema deve:
#     - Armazenar produtos com código, nome, quantidade e preço
#     - Permitir cadastrar, consultar, atualizar e excluir produtos
#     - Gerar relatório de produtos com estoque baixo (menos de 5 unidades)
#     - Calcular o valor total do estoque
#     - Permitir buscar produtos por nome ou código
#     - Implementar um menu interativo para o usuário


sitema_estoque = []
def cadastrar_produto(codigo, nome, quantidade, preco):
    produto = {"codigo": codigo, "nome": nome, "quantidade": quantidade, "preco": preco}
    sitema_estoque.append(produto)
def consultar_produto(codigo):
    for produto in sitema_estoque:
        if produto["codigo"] == codigo:
            return produto
    return None
def atualizar_produto(codigo, nome=None, quantidade=None, preco=None):
    for produto in sitema_estoque:
        if produto["codigo"] == codigo:
            if nome is not None:
                produto["nome"] = nome
            if quantidade is not None:
                produto["quantidade"] = quantidade
            if preco is not None:
                produto["preco"] = preco
            return True
    return False
def excluir_produto(codigo):
    for i, produto in enumerate(sitema_estoque):
        if produto["codigo"] == codigo:
            del sitema_estoque[i]
            return True
    return False
def relatorio_estoque_baixo():
    return [produto for produto in sitema_estoque if produto["quantidade"] < 5]
def valor_total_estoque():
    return sum(produto["quantidade"] * produto["preco"] for produto in sitema_estoque)
def buscar_produto(termo): 
    return [produto for produto in sitema_estoque if termo in produto["nome"] or termo in produto["codigo"]]
def menu():
    while True:
        print("\nMenu de Gerenciamento de Estoque:")
        print("1. Cadastrar Produto")
        print("2. Consultar Produto")
        print("3. Atualizar Produto")
        print("4. Excluir Produto")
        print("5. Relatório de Estoque Baixo")
        print("6. Valor Total do Estoque")
        print("7. Buscar Produto")
        print("0. Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            codigo = input("Código do produto: ")
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade: "))
            preco = float(input("Preço: "))
            cadastrar_produto(codigo, nome, quantidade, preco)
            print("Produto cadastrado com sucesso!")
        elif escolha == "2":
            codigo = input("Código do produto para consulta: ")
            produto = consultar_produto(codigo)
            if produto:
                print(f"Produto encontrado: {produto}")
            else:
                print("Produto não encontrado.")
        elif escolha == "3":
            codigo = input("Código do produto para atualização: ")
            nome = input("Novo nome (deixe em branco para não alterar): ")
            quantidade = input("Nova quantidade (deixe em branco para não alterar): ")
            preco = input("Novo preço (deixe em branco para não alterar): ")
            atualizar_produto(codigo, nome or None, int(quantidade) if quantidade else None, float(preco) if preco else None)
            print("Produto atualizado com sucesso!")
        elif escolha == "4":
            codigo = input("Código do produto para exclusão: ")
            if excluir_produto(codigo):
                print("Produto excluído com sucesso!")
            else:
                print("Produto não encontrado.")
        elif escolha == "5":
            produtos_baixo_estoque = relatorio_estoque_baixo()
            if produtos_baixo_estoque:
                print("Produtos com estoque baixo:")
                for produto in produtos_baixo_estoque:
                    print(produto)
            else:
                print("Nenhum produto com estoque baixo.")
        elif escolha == "6":
            total_estoque = valor_total_estoque()
            print(f"Valor total do estoque: R${total_estoque:.2f}")
        elif escolha == "7":
            termo = input("Digite o nome ou código do produto para busca: ")
            resultados = buscar_produto(termo)
            if resultados:
                print("Produtos encontrados:")
                for produto in resultados:
                    print(produto)
            else:
                print("Nenhum produto encontrado.")
        elif escolha == "0":
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")
menu()  


# DICAS IMPORTANTES:
# ------------------
# - Teste cada exercício com diferentes entradas
# - Tente resolver primeiro sem consultar soluções prontas
# - Para os níveis mais avançados, quebre o problema em partes menores
# - Utilize comentários no código para explicar sua lógica
# - Pratique a manipulação de listas com os métodos: append(), insert(), remove(), pop(), sort()
