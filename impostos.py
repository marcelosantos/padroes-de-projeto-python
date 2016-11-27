# -*- coding: utf-8 -*-
#author Marcelo Santos

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
