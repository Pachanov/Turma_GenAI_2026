from .pessoa import Pessoa


class Professor(Pessoa):
    def __init__(self, nome=None, cpf=None, valor_hora=60, carga_horaria=40):
        super().__init__(nome, cpf)
        self.__valor_hora = valor_hora
        self.__carga_horaria = carga_horaria

    @property
    def valor_hora(self):
        return self.__valor_hora

    @valor_hora.setter
    def valor_hora(self, valor_hora):
        self.__valor_hora = valor_hora

    @property
    def carga_horaria(self):
        return self.__carga_horaria

    @carga_horaria.setter
    def carga_horaria(self, carga_horaria):
        self.__carga_horaria = carga_horaria

    @property
    def salario(self):
        return int(self.__valor_hora * self.__carga_horaria * 4.5)

    def exibir_dados(self):
        return (
            f"Professor: {self.nome} | CPF: {self.cpf} | "
            f"Valor/Hora: R$ {self.valor_hora} | "
            f"Carga Horária: {self.carga_horaria}h | "
            f"Salário: R$ {self.salario}"
        )
