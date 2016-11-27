# -*- coding: utf-8 -*-
#author Marcelo Santos

from abc import ABCMeta, abstractmethod

class Imposto(object):

    def __init__(self, outro_imposto = None):
        self.__outro_imposto = outro_imposto

    def calculo_do_outro_imposto(self, orcamento):
		if self.__outro_imposto is None:
			return 0

		return self.__outro_imposto.calcula(orcamento)

    def calcula(self, orcamento):
        pass

class Template_de_imposto_condicional(Imposto):

    __metaclass__ = ABCMeta

    def calcula(self, orcamento):
		if self.deve_usar_max_taxacao(orcamento):
			return self.max_taxacao(orcamento) + self.calculo_do_outro_imposto(orcamento)
		else:
			return self.min_taxacao(orcamento) + self.calculo_do_outro_imposto(orcamento)
    @abstractmethod
    def deve_usar_max_taxacao(self, orcamento):
		pass
    @abstractmethod
    def max_taxacao(self, orcamento):
		pass
    @abstractmethod
    def min_taxacao(self, orcamento):
		pass

def IPVO(metodo_ou_funcao):
	def wrapper(self, orcamento):
		return metodo_ou_funcao(self, orcamento) + 50.0
	return wrapper

#estratégia para calcular ISS
class ISS(Imposto):
    @IPVO
    def calcula(self, orcamento):
		return orcamento.valor * 0.1 + self.calculo_do_outro_imposto(orcamento)

#estratégia para calcular ICMS
class ICMS(Imposto):
	def calcula(self, orcamento):
		return orcamento.valor * 0.06 + self.calculo_do_outro_imposto(orcamento)

#estratégia para calcular IPTU
class IPTU(Imposto):
	def calcula(self, orcamento):
		return orcamento.valor * 0.15 + self.calculo_do_outro_imposto(orcamento)

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
