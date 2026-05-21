# NÍVEL 2 - INTERMEDIÁRIO
# -----------------------

# 5. OPERAÇÕES COM PONTOS
#    Crie um conjunto de funções para trabalhar com pontos no plano cartesiano,
#    onde cada ponto é representado por uma tupla (x, y):
   
#    - `distancia(p1, p2)`: calcula a distância entre dois pontos
#    - `ponto_medio(p1, p2)`: retorna o ponto médio como uma tupla
#    - `inclinacao(p1, p2)`: calcula a inclinação da reta (se possível)
#    - `quadrante(p)`: retorna o quadrante do ponto (1, 2, 3, 4 ou 0 se estiver sobre um eixo)
   
#    Teste as funções com diferentes pontos.

# 6. ESTATÍSTICAS DE TURMA
#    Uma turma tem vários alunos. Cada aluno é representado por uma tupla contendo:
#    (nome, nota1, nota2, nota3)
   
#    Escreva funções para:
#    - `media_aluno(aluno)`: calcula a média de um aluno
#    - `melhor_aluno(turma)`: retorna o nome e a média do aluno com melhor desempenho
#    - `aprovados(turma)`: retorna uma lista de tuplas apenas dos alunos aprovados (média >= 7)
#    - `estatisticas_gerais(turma)`: retorna uma tupla com (média_da_turma, desvio_padrão, maior_nota, menor_nota)
   
#    Utilize a turma: [("Ana", 8.5, 7.0, 9.0), ("Carlos", 6.0, 5.5, 7.5), ("Mariana", 9.0, 9.5, 8.0)]

# 7. CONVERSOR DE UNIDADES
#    Implemente um conversor de unidades usando funções que retornam tuplas.
#    Cada função de conversão deve retornar uma tupla com o valor convertido e a unidade de destino.
   
#    Funções a implementar:
#    - `celsius_para_fahrenheit(c)`: retorna (temperatura, "F")
#    - `fahrenheit_para_celsius(f)`: retorna (temperatura, "C")
#    - `km_para_milhas(km)`: retorna (distância, "milhas")
#    - `milhas_para_km(milhas)`: retorna (distância, "km")
#    - `kg_para_libras(kg)`: retorna (peso, "lb")
#    - `libras_para_kg(lb)`: retorna (peso, "kg")
   
#    Crie um menu interativo para o usuário escolher as conversões.

# 8. ORDENAÇÃO PERSONALIZADA
#    Crie uma função `ordenar_pessoas` que recebe uma lista de tuplas no formato
#    (nome, idade, altura) e retorna uma nova lista ordenada de acordo com um critério
#    especificado por parâmetro:
#    - Critério 1: ordenar por nome
#    - Critério 2: ordenar por idade (crescente)
#    - Critério 3: ordenar por altura (decrescente)
#    - Critério 4: ordenar por idade e depois por altura
   
#    Utilize a função sorted() com parâmetro key personalizado.
