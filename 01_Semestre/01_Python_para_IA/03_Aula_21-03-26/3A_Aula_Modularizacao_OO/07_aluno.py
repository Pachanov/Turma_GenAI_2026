from universidade.aluno import Aluno

print("=== CLASSE ALUNO ===")

aluno = Aluno(
    nome="Marina",
    cpf="12345678901",
    matricula="20261234",
    curso="Análise e Desenvolvimento de Sistemas",
)

print(aluno.exibir_dados())
