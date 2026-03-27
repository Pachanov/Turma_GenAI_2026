def __init__(self, nome, carga_horaria = 60, professor=None):
	self.__nome = nome
	if carga_horaria > 0:
		self.__carga_horaria = carga_horaria
	else:
		self.__carga_horaria = -1 #Carga inválida
	self.__professor = professor

@property
def professor(self):
	return self.__professor

@professor.setter
def professor(self, professor):
	self.__professor = professor