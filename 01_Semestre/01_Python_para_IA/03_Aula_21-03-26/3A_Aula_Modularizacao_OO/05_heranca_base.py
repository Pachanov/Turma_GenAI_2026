from universidade.pessoa import Pessoa
from universidade.professor import Professor
from universidade.aluno import Aluno

print("=== HERANÇA: EXEMPLO BASE ===")

pessoa = Pessoa("Carlos", "12345678901")
professor = Professor("Paulo", "12345678901")
aluno = Aluno("Julia", "12345678901", "2026001", "ADS")

print(pessoa.exibir_dados())
print(professor.exibir_dados())
print(aluno.exibir_dados())
