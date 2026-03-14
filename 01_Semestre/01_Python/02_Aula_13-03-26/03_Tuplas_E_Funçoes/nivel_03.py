# NÍVEL 3 - AVANÇADO
# -------------------

# 9. PROCESSAMENTO DE MATRIZES
#    Implemente funções para manipular matrizes representadas como tuplas de tuplas
#    (imutáveis, como se fossem matrizes reais):
   
#    - `criar_matriz(linhas, colunas, valor_inicial=0)`: retorna uma matriz com dimensões especificadas
#    - `somar_matrizes(m1, m2)`: retorna a soma de duas matrizes (tupla de tuplas)
#    - `multiplicar_matrizes(m1, m2)`: retorna o produto de duas matrizes (se possível)
#    - `transpor_matriz(m)`: retorna a matriz transposta
#    - `diagonal_principal(m)`: retorna uma tupla com os elementos da diagonal principal
#    - `traco(m)`: retorna a soma dos elementos da diagonal principal (se matriz quadrada)
#    - `menor_elemento(m)`: retorna uma tupla (valor, linha, coluna) do menor elemento
   
#    Lembre-se: como são tuplas, você precisará criar novas estruturas em vez de modificar as existentes.

# 10. ANÁLISE DE TEXTOS AVANÇADA
#     Desenvolva funções para análise de textos utilizando tuplas como estruturas de retorno:
    
#     - `estatisticas_texto(texto)`: retorna uma tupla com (total_palavras, total_caracteres, total_linhas, palavras_unicas)
#     - `palavras_frequentes(texto, n=5)`: retorna uma tupla com as n palavras mais frequentes e suas contagens
#     - `indices_por_palavra(texto, palavra)`: retorna uma tupla com os índices (posições) onde a palavra aparece
#     - `analisar_frase(frase)`: retorna uma tupla aninhada com (palavras, numero_palavras, tamanho_medio, palindromos)
    
#     Teste com um parágrafo ou arquivo de texto fornecido pelo usuário.

# 11. SISTEMA DE FUNCIONÁRIOS
#     Modele um sistema de funcionários onde cada funcionário é representado por uma tupla:
#     (id, nome, cargo, salario, data_admissao)
    
#     Implemente funções para:
    
#     - `cadastrar_funcionario(funcionarios, id, nome, cargo, salario, data)`: adiciona novo funcionário (retorna nova tupla)
#     - `buscar_por_cargo(funcionarios, cargo)`: retorna uma tupla com todos os funcionários de determinado cargo
#     - `aumento_salarial(funcionarios, percentual, cargo=None)`: retorna nova tupla com salários atualizados
#     - `media_salarial(funcionarios, cargo=None)`: retorna a média salarial (geral ou por cargo)
#     - `funcionario_mais_antigo(funcionarios)`: retorna o funcionário com mais tempo de casa
#     - `folha_pagamento(funcionarios)`: retorna o total gasto com salários
    
#     Utilize funções de alta ordem (map, filter, reduce) quando apropriado.

# 12. EXPRESSÕES MATEMÁTICAS (DESAFIO)
#     Crie um sistema para avaliar expressões matemáticas simples representadas como tuplas.
#     Uma expressão é representada por uma tupla aninhada no formato:
#     (operador, operando1, operando2)
    
#     Onde operador é uma string ('+', '-', '*', '/', '^') e operandos podem ser números
#     ou outras expressões (tuplas).
    
#     Exemplo:
#     expressao = ('*', ('+', 3, 4), ('-', 10, 2))  # Representa (3+4) * (10-2)
    
#     Implemente funções para:
    
#     - `avaliar(expressao)`: avalia a expressão recursivamente e retorna o resultado
#     - `to_string(expressao)`: converte a expressão para string (ex: "(3 + 4) * (10 - 2)")
#     - `simplificar(expressao)`: simplifica expressões com operandos constantes
#     - `derivar(expressao, var)`: deriva a expressão em relação a uma variável (bônus)
    
#     Exemplo de uso:
#     expr = ('*', ('+', 'x', 3), ('-', 'x', 1))
#     print(avaliar(expr, {'x': 5}))  # Deve retornar (5+3)*(5-1) = 32

# 13. SISTEMA DE ESTOQUE COM TUPLAS (BÔNUS)
#     Desenvolva um sistema de estoque onde cada produto é uma tupla imutável:
#     (codigo, nome, preco, quantidade, categoria)
    
#     Implemente um módulo com funções para gerenciar o estoque:
    
#     - `adicionar_produto(estoque, produto)`: adiciona produto (retorna novo estoque)
#     - `remover_produto(estoque, codigo)`: remove produto (retorna novo estoque)
#     - `atualizar_quantidade(estoque, codigo, nova_quantidade)`: atualiza (retorna novo estoque)
#     - `buscar_por_categoria(estoque, categoria)`: retorna tupla de produtos da categoria
#     - `valor_total_estoque(estoque)`: retorna o valor total em estoque
#     - `produtos_abaixo_estoque(estoque, limite)`: retorna produtos com quantidade abaixo do limite
#     - `relatorio_por_faixa_preco(estoque, min, max)`: retorna produtos na faixa de preço
#     - `ordenar_produtos(estoque, criterio)`: retorna estoque ordenado por nome, preço ou quantidade
    
#     Utilize tuplas para garantir que os dados não sejam modificados acidentalmente,
#     sempre retornando novas tuplas para as alterações.

# DICAS IMPORTANTES:
# ------------------
# - Tuplas são imutáveis: lembre-se de sempre criar novas tuplas em vez de modificar
# - Use retorno múltiplo de funções para devolver várias informações relacionadas
# - Explore o desempacotamento de tuplas: a, b, c = minha_tupla
# - Utilize tuplas como chaves de dicionários quando necessário
# - Combine listas de tuplas para estruturas de dados mais complexas
# - Funções podem retornar tuplas para agrupar resultados relacionados
# - Use type hints para documentar os tipos esperados e retornados
