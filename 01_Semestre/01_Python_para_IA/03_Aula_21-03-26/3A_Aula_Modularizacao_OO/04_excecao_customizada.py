from universidade.pessoa_customizada import PessoaCustomizada
from universidade.excecoes import CPFInvalidoException

print("=== EXCEÇÃO CUSTOMIZADA ===")

try:
    pessoa = PessoaCustomizada("Ana", "123")
    print(pessoa.exibir_dados())
except CPFInvalidoException as erro:
    print("Erro tratado com exceção customizada.")
    print(f"Mensagem: {erro}")
