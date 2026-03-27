class Pessoa:
	def __init__(self, nome=None, cpf=-1):
		self.__nome = nome
		if cpf != -1 and self.__validar_cpf(cpf):
			self.__cpf = cpf
		else:
			self.__cpf = -1  # CPF inválido

	@property
	def cpf(self):
		return self.__cpf

	@cpf.setter
	def cpf(self, cpf):
		if self.__validar_cpf(cpf):
			self.__cpf = cpf
		else:
			self.__cpf = -1

	def __validar_cpf(self, cpf):
		# Add your CPF validation logic here
		return isinstance(cpf, int) and cpf > 0