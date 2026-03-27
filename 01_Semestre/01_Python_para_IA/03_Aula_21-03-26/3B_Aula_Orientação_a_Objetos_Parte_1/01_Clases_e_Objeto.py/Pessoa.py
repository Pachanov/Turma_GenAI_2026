# De acordo com o PEP 8, os nomes de classes devem serguir o padrão Upper Camel Case (PEP 8 chama de CapWords).
# Exemplos de nome de classes:
# Pessoa
# Professor
# SalaAula

# Cada classe deve ser salva em seu próprio arquivo .py
# O arquivo deve ter o mesmo nome da classe mas, de acordo com o PEP 8, o nome do arquivo deve seguir o padrão
# snake case (argh!!!).



# def __init__(self):
# 	self.nome = None
# 	self.cpf = -1
 


#### INTANCEANDO A CLASSE PESSOA

# Pessoa é uma classe.
# Define a estrutura de uma pessoa.
# Agora podemos criar pessoas na memória.
# ● Criar variáveis do tipo Pessoa.
# ● Essas variáveis são chamados de objeto do tipo Pessoa.
# ● Quando criamos um objeto, estamos instanciando um objeto da classe.


class Pessoa:
	def __init__(self):
		self.nome = None
		self.cpf = -1