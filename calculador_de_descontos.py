# -*- coding: utf-8 -*-
#author Marcelo Santos

from descontos import Desconto_por_dois_itens, Desconto_por_cinco_itens, Desconto_por_mais_de_quinhentos_reais, Sem_desconto

class Calculador_de_descontos(object):

	def calcula(self, orcamento):

		desconto = Desconto_por_dois_itens(
			Desconto_por_cinco_itens(
				Desconto_por_mais_de_quinhentos_reais(
					Sem_desconto()
				)
			)
		).calcula(orcamento)

		return desconto

if __name__ == '__main__':

	from orcamento import Orcamento, Item

	orcamento = Orcamento()
	orcamento.adiciona_item(Item('TENIS',150.0))
	orcamento.adiciona_item(Item('BLUSAO',180.0))
	orcamento.adiciona_item(Item('BIKE',1500.0))
	orcamento.adiciona_item(Item('LUVAS',70.0))
	#orcamento.adiciona_item(Item('BLUSA',30.0))
	#orcamento.adiciona_item(Item('CUECA',15.0))

	print 'Total do Orçamento %s' % orcamento.valor

	calculador = Calculador_de_descontos()

	desconto = calculador.calcula(orcamento)

	print 'Desconto calculado %s' % desconto
