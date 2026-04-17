"""1. Faça um programa que pergunta o peso (em kg) e a altura (em metros) do usuário. O
programa deve calcular o Índice de Massa Corpórea (IMC) do usuário, que é dado por
peso/(altura*altura) e exibir o valor de IMC na tela.
Dica: use float para ler o input. Para separar as casas decimais quando estiver digitando,
utilize ponto (e.g., digite 1.8 para uma altura de um e oitenta). Isso pode ser diferente em
alguns sistemas. Por exemplo, alguns terminais de sistemas Mac utilizam vírgula para
separar as casas decimais."""


######################################################
###CALCULADORA DE IMC#################################
######################################################


peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
imc = peso / (altura * altura)
print("Seu IMC é: ", imc)





"""2. Escreva um programa que solicita o raio de um círculo, e exibe o perímetro e a área
desse círculo. Para calcular a área, utilize o operador de exponenciação **."""


radio = float(input("Digite o raio do círculo: "))
perimetro = 2 * 3.14 * radio
area = 3.14 * radio ** 2
print("O perímetro do círculo é: ", perimetro)
print("A área do círculo é: ", area)


"""3. Faça um programa que leia os coeficientes a, b e c de uma equação de segundo grau. O
programa deve calcular por Bhaskara as raízes dessa equação. Para esse problema,
assuma que a equação sempre vai ter raízes reais (o usuário não vai digitar valores a, b e c
que levam a uma equação que não possui raízes). Caso a equação possua apenas uma raiz, como a equação x2
, repita a raiz na resposta duas vezes.
Exemplo de execução do programa:
Digite a: 2
Digite b: 0
Digite c: 0
Raíz 1: 0
Raíz 2: 0 """


lendo_a = float(input("Digite o coeficiente a: "))
lendo_b = float(input("Digite o coeficiente b: "))
lendo_c = float(input("Digite o coeficiente c: "))
delta = lendo_b ** 2 - 4 * lendo_a * lendo_c
raiz1 = (-lendo_b + delta ** 0.5) / (2 * lendo_a)
raiz2 = (-lendo_b - delta ** 0.5) / (2 * lendo_a)
print("Raíz 1: ", raiz1)
print("Raíz 2: ", raiz2)

