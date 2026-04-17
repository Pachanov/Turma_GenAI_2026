from universidade.professor import Professor

print("=== CLASSE PROFESSOR ===")

professor = Professor(
    nome="Paulo",
    cpf="12345678901",
    valor_hora=80,
    carga_horaria=20,
)

print(professor.exibir_dados())
print(f"Salário calculado: R$ {professor.salario}")
