class Pessoa:
 def __init__(self, nome=None, cpf=-1):
    self.nome = nome
    self.cpf = cpf
    
    
# Vamos usar o modificador de acesso privado nos atributos da classe.
# Significa que o item pode ser acessado apenas internamente na classe.
# Um membro privado em Python deve iniciar com dois underscores __.

class Pessoa:
    def __init__(self, nome=None, cpf=-1):
        self.__nome = nome
        self.__cpf = cpf