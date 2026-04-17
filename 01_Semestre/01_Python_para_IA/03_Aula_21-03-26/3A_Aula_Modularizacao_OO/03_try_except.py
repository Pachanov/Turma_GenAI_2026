from universidade.pessoa import Pessoa

print("=== EXEMPLO DE TRY / EXCEPT ===")

try:
    pessoa = Pessoa("João", "12345678901")
    print(pessoa.exibir_dados())

    pessoa.cpf = "999"
except ValueError as erro:
    print("Ocorreu um erro ao definir o CPF.")
    print(f"Mensagem: {erro}")
