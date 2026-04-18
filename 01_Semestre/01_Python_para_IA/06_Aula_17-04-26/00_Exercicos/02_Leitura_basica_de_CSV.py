"""1. Leitura básica de CSV
Escreva um programa que leia um arquivo CSV chamado `dados.csv` com as colunas `nome,
idade, cidade` e exiba cada linha no formato:
`"Nome: X, Idade: Y, Cidade: Z"`.
Ignore a linha de cabeçalho (use `next(reader)`).
2. Escrita de CSV a partir de uma lista de dicionários
Dada a seguinte lista de dicionários:
pessoas = [
{"nome": "Ana", "idade": 25, "cidade": "São Paulo"},
{"nome": "Bruno", "idade": 30, "cidade": "Rio de Janeiro"},
{"nome": "Carla", "idade": 22, "cidade": "Belo Horizonte"}
]
Escreva esses dados em um arquivo `pessoas.csv` com cabeçalho e vírgula como delimitador.
3. Leitura seletiva (apenas colunas específicas)
Leia o arquivo `vendas.csv` que possui as colunas: `produto, quantidade, preco_unitario, data`.
Calcule o valor total de cada venda (`quantidade * preco_unitario`) e escreva um novo CSV
chamado `total_vendas.csv` com as colunas: `produto, data, valor_total`.
4. Manipulação de diferentes delimitadores
O arquivo `dados_ponto_e_virgula.csv` usa ponto e vírgula (`;`) como delimitador e vírgula
decimal nos números.
Exemplo de linha: `"João;35;1.750,50"` (idade 35, salário 1750,50).
Leia o arquivo, converta o salário para float (trate a vírgula decimal) e escreva um novo CSV
com delimitador vírgula e ponto decimal.
5. Tratamento de valores ausentes
Dado o arquivo `clientes.csv` que pode ter campos vazios, leia‑o e substitua os valores
ausentes:
- Na coluna `email`, preencha com `"sem_email"`
- Na coluna `telefone`, preencha com `"0000-0000"`
- Nas colunas numéricas, preencha com `0`
Salve o resultado em `clientes_limpo.csv`.
6. Filtragem de linhas por condição
Leia o arquivo `funcionarios.csv` com colunas `nome, departamento, salario`.
Crie um novo arquivo `alta_renda.csv` contendo apenas os funcionários com salário maior que
5000.
Ordene o resultado por salário decrescente.
7. Agregação simples (contagem por categoria)
O arquivo `produtos.csv` tem as colunas `categoria, produto, vendas`.
Calcule o total de vendas por categoria e grave um novo CSV com `categoria, total_vendas`.
8. Mesclagem de dois CSVs (inner join manual)
Você tem dois arquivos:
- `alunos.csv`: `id_aluno, nome, turma`
- `notas.csv`: `id_aluno, disciplina, nota`
Crie um terceiro CSV `alunos_notas.csv` que combine as informações, incluindo apenas os
alunos que possuem pelo menos uma nota. O resultado deve ter as colunas: `nome, turma,
disciplina, nota`.
9. Divisão de um CSV grande em vários menores
Dado um arquivo `dados_1000_linhas.csv` (você mesmo pode gerar), escreva um programa
que divida esse arquivo em múltiplos CSVs, cada um com no máximo 100 linhas (exceto o
último). Os arquivos devem se chamar `parte_1.csv`, `parte_2.csv`, etc., e manter o cabeçalho
original.
10. Pequeno projeto: conversor de formato com validação
Crie um programa que:
- Solicita ao usuário o caminho de um arquivo CSV de entrada.
- Lê o arquivo e verifica se ele contém pelo menos as colunas `id` (inteiro), `nome` (texto) e
`valor` (float).
- Se alguma linha tiver erro de tipo (ex.: `valor` não numérico), o programa deve pular essa
linha e registrar o erro em um arquivo `log_erros.txt` (número da linha e motivo).
- Por fim, escreve um arquivo `dados_validados.csv` apenas com as linhas válidas,
convertendo os tipos corretamente."""