class Pessoa:
    def __init__(self, nome=None, cpf=None):
        self.__nome = nome
        self.__cpf = None

        if cpf is not None:
            self.cpf = cpf

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        if self.__validar_cpf(cpf):
            self.__cpf = str(cpf)
        else:
            raise ValueError("CPF inválido.")

    def __validar_cpf(self, cpf):
        cpf = str(cpf).strip()

        if not cpf.isdigit():
            return False

        if len(cpf) != 11:
            return False

        if cpf == cpf[0] * 11:
            return False

        return True

    def exibir_dados(self):
        return f"Nome: {self.nome} | CPF: {self.cpf}"
