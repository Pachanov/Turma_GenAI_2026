from universidade.pessoa import Pessoa

print("=== EXEMPLO DE RAISE COM CPF ===")

pessoa = Pessoa("Maria", "12345678901")
print("Pessoa criada com sucesso:")
print(pessoa.exibir_dados())

print("\nAgora vamos tentar atribuir um CPF inválido...")

pessoa.cpf = "123"
