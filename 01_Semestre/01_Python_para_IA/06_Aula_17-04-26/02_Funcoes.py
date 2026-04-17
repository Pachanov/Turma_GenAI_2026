"""Assim como para listas convencionais, a função len() vai retornar o tamanho da
string (o número de caracteres)"""

frase = "Curso de Python"
print("Num caracs", len(frase))

##Acessando itens
"""De maneira similar a vetores, podemos acessar um caractere ou um conjunto de caracteres
por índice
Internamente uma string é um vetor, onde o primeiro caractere está na posição zero
"""

frase = "Curso de Python"
linguagem = frase[9:len(frase)]
print(linguagem)
print("Primeira Letra:", frase[0])


#Replace

"""É possível substituir um trecho de uma frase por outro via replace("texto
antigo", "novo")
A função retorna uma nova string alterada
A string original não é alterada"""

frase = "Esse é o curso de IA Generativa. Você pode criar programas com prompts."
mudanca = frase.replace("prompts", "Python")
print(frase)
print(mudanca)

#É possível especificar o número limite de substituições no replace