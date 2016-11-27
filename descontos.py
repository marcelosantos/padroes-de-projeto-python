# -*- coding: utf-8 -*-
#author Marcelo Santos

class Desconto_por_dois_itens(object):

    def __init__(self, proximo_desconto):
        self.__proximo_desconto = proximo_desconto

    def calcula(self, orcamento):
        if orcamento.total_itens == 2:
            print 'DESCONTO POR 2 ITENS'
            return orcamento.valor * 0.02
        else:
			return self.__proximo_desconto.calcula(orcamento)

class Desconto_por_cinco_itens(object):

    def __init__(self, proximo_desconto):

		self.__proximo_desconto = proximo_desconto

    def calcula(self, orcamento):

		if orcamento.total_itens > 5:
			print 'DESCONTO POR MAIS DE 5 ITENS'
			return orcamento.valor * 0.1
		else:
			return self.__proximo_desconto.calcula(orcamento)

class Desconto_por_mais_de_quinhentos_reais(object):

    def __init__(self, proximo_desconto):

		self.__proximo_desconto = proximo_desconto

    def calcula(self, orcamento):
		if orcamento.valor > 500.0:
			print 'DESCONTO POR MAIS DE 500 REAIS'
			return orcamento.valor * 0.07
		else:
			return self.__proximo_desconto.calcula(orcamento)

class Sem_desconto(object):

    def calcula(self, orcamento):
		print 'SEM DESCONTO'
		return 0
