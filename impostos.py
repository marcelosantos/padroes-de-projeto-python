# -*- coding: utf-8 -*-
#author Marcelo Santos

from abc import ABCMeta, abstractmethod

class Template_de_imposto_condicional(object):

    __metaclass__ = ABCMeta

    def calcula(self, orcamento):
		if self.deve_usar_max_taxacao(orcamento):
			return self.max_taxacao(orcamento)
		else:
			return self.min_taxacao(orcamento)
    @abstractmethod
    def deve_usar_max_taxacao(self, orcamento):
		pass
    @abstractmethod
    def max_taxacao(self, orcamento):
		pass
    @abstractmethod
    def min_taxacao(self, orcamento):
		pass

#estratégia para calcular ISS
class ISS(object):

	def calcula(self, orcamento):
		return orcamento.valor * 0.1

#estratégia para calcular ICMS
class ICMS(object):

	def calcula(self, orcamento):
		return orcamento.valor * 0.06

#estratégia para calcular IPTU
class IPTU(object):

	def calcula(self, orcamento):
		return orcamento.valor * 0.15

#estratégia para calcular ICAA
class ICAA(Template_de_imposto_condicional):

    def deve_usar_max_taxacao(self, orcamento):
        return orcamento.valor > 300

    def max_taxacao(self, orcamento):
		return orcamento.valor * 0.06

    def min_taxacao(self, orcamento):
		return orcamento.valor * 0.03

#estratégia para calcular ICBB
class ICBB(Template_de_imposto_condicional):

    def __tem_item_maior_que_150_reais(self, orcamento):
        for item in orcamento.obter_itens():
			if item.valor > 150:
				return True
			return False

    def deve_usar_max_taxacao(self, orcamento):
        return orcamento.valor > 300 and self.__tem_item_maior_que_150_reais(orcamento)

    def max_taxacao(self, orcamento):
	    return orcamento.valor * 0.2

    def min_taxacao(self, orcamento):
	    return orcamento.valor * 0.1
