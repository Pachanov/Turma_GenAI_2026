from .pessoa import Pessoa


class Aluno(Pessoa):
    def __init__(self, nome=None, cpf=None, matricula=None, curso=None):
        super().__init__(nome, cpf)
        self.__matricula = matricula
        self.__curso = curso

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    @property
    def curso(self):
        return self.__curso

    @curso.setter
    def curso(self, curso):
        self.__curso = curso

    def exibir_dados(self):
        return (
            f"Aluno: {self.nome} | CPF: {self.cpf} | "
            f"Matrícula: {self.matricula} | Curso: {self.curso}"
        )
