class Disciplina:
    def __init__(self, nome, carga_horaria=60):
        self.__nome = nome
        if carga_horaria > 0:
            self.__carga_horaria = carga_horaria
        else:
            self.__carga_horaria = -1  # Carga inválida

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def carga_horaria(self):
        return self.__carga_horaria

    @carga_horaria.setter
    def carga_horaria(self, carga_horaria):
        if carga_horaria > 0:
            self.__carga_horaria = carga_horaria
        else:
            self.__carga_horaria = -1