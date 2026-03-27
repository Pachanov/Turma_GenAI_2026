# NÍVEL 4 - DESAFIO
# ------------------

# 12. GRAFOS COM DICIONÁRIOS
#     Represente um grafo direcionado usando dicionários, onde cada chave é um vértice
#     e cada valor é uma lista de vértices adjacentes (arestas de saída).
    
#     Implemente as seguintes funções:
#     - adicionar_vertice(grafo, vertice)
#     - adicionar_aresta(grafo, origem, destino, peso=1) - use tuplas (destino, peso)
#     - remover_vertice(grafo, vertice)
#     - bfs(grafo, inicio) - busca em largura retornando ordem de visita
#     - dfs(grafo, inicio) - busca em profundidade retornando ordem de visita
#     - menor_caminho(grafo, origem, destino) - usando algoritmo de Dijkstra
#     - detectar_ciclo(grafo) - verifica se existe ciclo no grafo

#     Exemplo de grafo:
#     grafo = {
#         "A": [("B", 4), ("C", 2)],
#         "B": [("C", 1), ("D", 5)],
#         "C": [("D", 8), ("E", 10)],
#         "D": [("E", 2)],
#         "E": []
#     }

# 13. SISTEMA DE RECOMENDAÇÃO (BÔNUS)
#     Crie um sistema simples de recomendação baseado em conteúdo usando dicionários.
    
#     Estrutura de dados:
#     usuarios = {
#         "joao": {"filmes": ["Matrix", "Interestelar"], "livros": ["1984", "Duna"]},
#         "maria": {"filmes": ["Matrix", "Senhor dos Anéis"], "musicas": ["Bohemian Rhapsody"]},
#         # ... mais usuários
#     }
    
#     Itens (filmes, livros, músicas) com tags/categorias:
#     itens = {
#         "Matrix": {"tipo": "filme", "genero": "Ficção Científica", "ano": 1999},
#         "1984": {"tipo": "livro", "genero": "Distopia", "autor": "George Orwell"},
#         # ... mais itens
#     }
    
#     O sistema deve:
#     - Calcular similaridade entre usuários baseado nos itens que consomem
#     - Recomendar itens para um usuário baseado no que usuários similares gostam
#     - Sugerir itens similares a um determinado item baseado nas tags
#     - Permitir que usuário avalie itens (1 a 5 estrelas) e use isso para recomendações

# DICAS IMPORTANTES:
# ------------------
# - Explore métodos de dicionários: keys(), values(), items(), get(), setdefault()
# - Use dicionários aninhados para estruturas mais complexas
# - Lembre-se de tratar erros (KeyError) ao acessar chaves que podem não existir
# - Para ordenar dicionários, use sorted() com parâmetros adequados
# - Combine listas e dicionários para soluções mais eficientes
