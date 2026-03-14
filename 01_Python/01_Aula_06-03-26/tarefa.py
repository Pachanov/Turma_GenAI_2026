# Exercício 1 - Variáveis e Atribuição

"""1. Considere os seguintes comandos executados no interpretador Python, e indique qual o
valor armazenado nas variáveis depois de todos os comandos terem sido executados."""


#a) variavel1 possui 10 e variavel2 possui 10
#b) variavel1 possui 12 e variavel2 possui 22
#c) variavel1 possui 22 e variavel2 possui 21
#d) variavel1 possui 10 e variavel2 possui -1
#e) variavel1 possui 12 e variavel2 possui 12


variavel1 = 10
variavel1 = variavel1 + 2
variavel2 = variavel1 - 1
variavel1 = variavel1 + 10
variavel1 + 10
variavel2 + 1 

print(variavel1)
print(variavel2)

# Exercício 2 - Tipos de Variáveis
"""2. Considere os seguintes comandos executados no interpretador Python, e indique qual o
tipo das variáveis depois de todos os comandos terem sido executados."""

var1 = 1
var2 = 3
var2 = 2.5
var3 = 4
var1 = "Var2"

print(type(var1))
print(type(var2))
print(type(var3))
print(var1)

# a) var1 é string, var2 é ponto flutuante e var3 é inteiro
# b) var1 é ponto flutuante, var2 é ponto flutuante e var3 é inteiro
# c) var1 é string, var2 é inteiro e var3 é inteiro
# d) var1 é inteiro, var2 é inteiro e var3 é inteiro
# e) var1 é ponto flutuante, var2 é inteiro e var3 é inteiro

# Exercício 3 - Impressão de Variáveis
"""3. Considere o seguinte script Python. Ao executar o script, o que exatamente é exibido na
tela?"""

import math 

nome = "Maria"
sobrenome = "Silva"
calculo = math.sqrt(36)
print("nome", nome, "sobrenome",sobrenome,calculo)

