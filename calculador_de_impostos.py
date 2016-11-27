# -*- coding: utf-8 -*-
#author Marcelo Santos

from impostos import ISS, ICMS, IPTU

class Calculador_de_impostos(object):

    """
    utilizando duck typing, se parece um pato é um pato, se o imposto
    é uma instância com método calcula, então ele calcula um imposto
    """
    def realiza_calculo(self, orcamento, imposto):

        imposto_calculado = imposto.calcula(orcamento)
        print imposto_calculado

if __name__ == '__main__':

	from orcamento import Orcamento

	calculador = Calculador_de_impostos()

	orcamento = Orcamento(600)

	calculador.realiza_calculo(orcamento, ISS())

	calculador.realiza_calculo(orcamento, ICMS())

	calculador.realiza_calculo(orcamento, IPTU())
