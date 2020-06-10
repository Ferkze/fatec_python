import math

class Retangulo():
	'Define um Retangulo'

	def __init__(self, lado1, lado2):
		self.setLados(lado1, lado2)
		self.cor = ''

	def setLados(self, lado1, lado2):
		self.lado1 = lado1
		self.lado2 = lado2

	def getLado1(self):
		return self.lado1

	def getLado2(self):
		return self.lado2

	def calculaArea(self):
		return self.lado1 * self.lado2

	def calculaPerimetro(self):
		return 2 * (self.lado1 + self.lado2)

	def trocaCor(self, cor):
		self.cor = cor

	def mostraCor(self):
		if self.cor == '':
			print('Retangulo sem cor')
		else:
			print('Retangulo {}'.format(self.cor))

	def cabeNaCaixa(self, area = 100):
		quantidade = area / self.calculaArea()
		if quantidade < 1:
			print('O Retangulo não cabe na caixa')
			return

		resto = area % self.calculaArea()
		if resto == 0:
			print('{} x Retangulo cabe perfeitamente na caixa'.format(quantidade))
		else:
			print('{} x Retangulo cabe na caixa, porém sobra {} de espaço'.format(math.floor(quantidade), resto))

retangulo1 = Retangulo(5, 2)
retangulo1.trocaCor('Preto')
retangulo1.mostraCor()
retangulo1.cabeNaCaixa(100)

retangulo2 = Retangulo(7, 5)
retangulo2.mostraCor()
retangulo2.cabeNaCaixa(100)

retangulo3 = Retangulo(120, 2)	
retangulo3.mostraCor()
retangulo3.cabeNaCaixa(100)