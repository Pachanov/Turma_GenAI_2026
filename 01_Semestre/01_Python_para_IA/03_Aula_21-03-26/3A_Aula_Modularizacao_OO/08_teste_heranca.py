from universidade.professor import Professor
from universidade.aluno import Aluno

print("=== TESTE FINAL DE HERANÇA ===")

professor = Professor("Roberto", "12345678901", valor_hora=100, carga_horaria=10)
aluno = Aluno("Beatriz", "12345678901", "20267777", "Engenharia de Software")

objetos = [professor, aluno]

for obj in objetos:
    print(obj.exibir_dados())
