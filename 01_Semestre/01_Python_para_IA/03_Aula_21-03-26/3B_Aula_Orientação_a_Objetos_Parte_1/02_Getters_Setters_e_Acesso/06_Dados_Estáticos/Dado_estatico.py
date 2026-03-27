# Os dados que criamos até agora pertencem aos objetos.
# Cada objeto do tipo ConteudoMinistrado criado na memória possui sua própria descrição, carga e id.

class ConteudoMinistrado:
	def __init__(self, descricao, carga_horaria):
		self.__descricao = descricao
		self.__carga_horaria = carga_horaria
		self.__id = 0
  
# Os dados que criamos até agora pertencem aos objetos.
# Cada objeto do tipo ConteudoMinistrado criado na memória possui sua própria descrição, carga e id.
# Uma dado estático não pertence aos objetos, mas sim a classe.
# “Compartilhado” entre todos os objetos do mesmo tipo

class ConteudoMinistrado:
	PROX_ID = 0
	
	def __init__(self, descricao, carga_horaria):
		self.__descricao = descricao
		self.__carga_horaria = carga_horaria
		self.__id = 0
	
	@property
	def descricao(self):
		return self.__descricao
	
	@property
	def carga_horaria(self):
		return self.__carga_horaria
	
	@property
	def id(self):
		return self.__id