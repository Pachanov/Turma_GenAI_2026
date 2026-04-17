""" 1. Comprimento da string
Escreva uma função que receba uma string e retorne o número de caracteres (incluindo
espaços).
Exemplo: `"Olá mundo"` → `9` """



# def comprimento_string(s):
#     return len(s)

# # Testando a função
# print(comprimento_string("Olá mundo"))  # Deve retornar 9


"""2. Inversão de string
Crie uma função que inverta uma string sem usar fatiamento `[::-1]` (use um loop).
Exemplo: `"Python"` → `"nohtyP"` """


# def funcao_invertida(s):
#     invertida = ""
#     for i in range(len(s)-1, -1, -1):
#         invertida += s[i]
#     return invertida

# input_string = "Python"
# resultado = funcao_invertida(input_string)
# print(resultado)  # Deve imprimir "nohtyP"




"""3. Contagem de vogais e consoantes
Dada uma string, conte quantas vogais (a, e, i, o, u) e quantas consoantes ela possui. Ignore
maiúsculas/minúsculas.
Exemplo: `"GenAI"` → Vogais: 3, Consoantes: 2"""

# def contar_vogais_consoantes(s):
#     contar_vogais_consoantes = {"vogais": 0, "consoantes": 0}
#     for char in s.lower():
#         if char in "aeiou":
#             contar_vogais_consoantes["vogais"] += 1
#         elif char.isalpha():  # Verifica se é uma letra (consoante)
#             contar_vogais_consoantes["consoantes"] += 1
#     return contar_vogais_consoantes

# # Testando a função
# resultado = contar_vogais_consoantes("GenAI")
# print(f"Vogais: {resultado['vogais']}, Consoantes: {resultado['consoantes']}")  # Deve imprimir "Vogais: 3, Consoantes: 2"




"""4. Remoção de espaços extras
Escreva uma função que remova espaços desnecessários: espaços no início/fim e múltiplos
espaços entre palavras (deixe apenas um).
Exemplo: `" Olá mundo da IA "` → `"Olá mundo da IA"` """

# def remover_espacos_extras(s):
#     #remover espaços no início e fim
#     s = s.strip()
#     #remover múltiplos espaços entre palavras
#     while "  " in s:
#         s = s.replace("  ", " ")
#     return s

# # Testando a função
# input_string = "  Olá  mundo da  IA    "
# resultado = remover_espacos_extras(input_string)
# print(f'"{resultado}"')  # Deve imprimir "Olá mundo da IA"




"""5. Verificador de palíndromo
Verifique se uma string é um palíndromo (ignorando maiúsculas, acentos e espaços).
Exemplo: `"A man a plan a canal panama"` → `True` """




"""6. Tokenização simples
Divida uma frase em uma lista de palavras (separador = espaço). Depois, transforme cada
palavra em minúscula e remova pontuação (`. , ! ? ; :`).
Exemplo: `"Olá, como você está?"` → `["olá", "como", "você", "está"]` """




"""7. Substituição de caracteres
Substitua todas as ocorrências de um caractere por outro em uma string. Faça manualmente
(sem `replace`).
Exemplo: `"banana", 'a', 'o'` → `"bonono"` """



"""8. Extração de iniciais
Dado um nome completo, retorne as iniciais em maiúsculo, separadas por ponto.
Exemplo: `"ana maria silva"` → `"A.M.S"`"""




"""9. Chunking de texto para LLM
Divida um longo texto em pedaços (chunks) de no máximo N caracteres, sem cortar palavras
no meio (quebre no último espaço antes do limite).
Exemplo: Texto = `"Este é um exemplo de chunking para modelos generativos"`, N = 20 →
`["Este é um exemplo", "de chunking para", "modelos generativos"]`"""




"""10. Contagem de frequência de palavras
Conte quantas vezes cada palavra aparece em uma string (ignore maiúsculas/minúsculas e
pontuação). Retorne um dicionário.
Exemplo: `"O rato roeu a roupa do rei de Roma. O rei ficou bravo."` → `{'o': 3, 'rato': 1, 'roeu': 1,
'a': 1, 'roupa': 1, 'do': 1, 'rei': 2, 'de': 1, 'roma': 1, 'ficou': 1, 'bravo': 1}"""



