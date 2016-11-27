# -*- coding: utf-8 -*-
#author Marcelo Santos

from impostos import ISS, ICMS, IPTU, ICAA, ICBB

class Calculador_de_impostos(object):

    """
    utilizando duck typing, se parece um pato é um pato, se o imposto
    é uma instância com método calcula, então ele calcula um imposto
    """
    def realiza_calculo(self, orcamento, imposto):

        imposto_calculado = imposto.calcula(orcamento)
        print imposto_calculado

if __name__ == '__main__':
    from orcamento import Orcamento, Item

    calculador = Calculador_de_impostos()

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('TENIS',200.0))
    orcamento.adiciona_item(Item('BLUSAO',300.0))
    orcamento.adiciona_item(Item('BIKE',1500.0))
    #orcamento.adiciona_item(Item('LUVAS',70.0))
    #orcamento.adiciona_item(Item('BLUSA',30.0))
    #orcamento.adiciona_item(Item('CUECA',15.0))

    print 'ISS / ICMS / IPTU'

    calculador.realiza_calculo(orcamento, ISS())

    calculador.realiza_calculo(orcamento, ICMS())

    calculador.realiza_calculo(orcamento, IPTU())

    print 'ICAA / ICBB'

    calculador.realiza_calculo(orcamento, ICAA())

    calculador.realiza_calculo(orcamento, ICBB())
