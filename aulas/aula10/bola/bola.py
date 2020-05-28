class Bola:
	'Classe para definir uma bola'
	def __init__(self, raio):
		self.raio = raio
		self.cor = "sem cor"

	def trocaCor(self, cor):
		self.cor = cor

	def mostraCor(self):
		print(self.cor)

	def calcularDiametro(self):
		return self.raio * 2

	def mostrarRaio(self):
		print(self.raio)

	def mostrarDiametro(self):
		print(self.calcularDiametro())

	def estourar(self):
		self.raio = 0
		print('Bola {}: Puff!'.format(self.cor))

# Teste da Classe

bola = Bola(5)
bola.trocaCor("Azul")
bola.mostraCor()
bola.mostrarDiametro()
bola.estourar()
bola.mostrarRaio()