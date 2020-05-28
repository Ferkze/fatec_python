import math

class Quadrado():
	'Define um quadrado'

	def __init__(self, lado, cor):
		self.trocarCor(cor)
		self.setLado(lado)

	def trocarCor(self, cor):
		self.cor = cor

	def setLado(self, lado):
		self.lado = lado

	def getLado(self):
		return self.lado

	def calculaArea(self):
		return self.lado * self.lado

	def calculaPerimetro(self):
		return self.lado *2

	def cabeNaCaixa(self, m = 100):
		quantidade = m / self.lado
		if quantidade < 1:
			print('O quadrado não cabe na caixa')
			return

		resto = m % self.lado
		if resto == 0:
			print('{} x quadrado {} cabe perfeitamente na caixa'.format(quantidade, self.cor))
		else:
			print('{} x quadrado {} cabe na caixa, porém sobra {} de espaço'.format(math.floor(quantidade), self.cor, resto))

quadrado1 = Quadrado(5, 'Azul')
quadrado1.cabeNaCaixa(100)

quadrado2 = Quadrado(7, 'Vermelho')
quadrado2.cabeNaCaixa(100)

quadrado2 = Quadrado(120, 'Preto')	
quadrado2.cabeNaCaixa(100)