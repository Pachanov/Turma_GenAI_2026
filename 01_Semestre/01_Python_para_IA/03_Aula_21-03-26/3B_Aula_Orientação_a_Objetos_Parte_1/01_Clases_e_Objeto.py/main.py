# Pessoa é uma classe.
# Define a estrutura de uma pessoa.
# Agora podemos criar pessoas na memória.
# ● Criar variáveis do tipo Pessoa.
# ● Essas variáveis são chamados de objeto do tipo Pessoa.
# ● Quando criamos um objeto, estamos instanciando um objeto da classe.

from clases_e_objeto import Pessoa
p1 = Pessoa()
p2 = Pessoa()
p1.nome = "João da Silva"
p2.nome = "Maria Oliveira"
print(p1.nome)

print(p1.cpf)