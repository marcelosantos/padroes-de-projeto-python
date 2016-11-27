class Orcamento(object):

	def __init__(self, valor):

		self.__valor = valor

	#propertie
	@property
	def valor(self):
		
		return self.__valor
