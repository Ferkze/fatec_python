from pprint import pprint

class Aluno:
	def __init__(self, nome, idade, peso, altura, salario):
		self.nome = nome
		self.idade = idade
		self.peso = peso
		self.altura = altura
		self.salario = salario

	def engordar(self, peso):
		self.peso += peso

	def emagrecer(self, peso):
		if (peso > self.peso):
			self.peso = 0
		else:
			self.peso -= peso

	def crescer(self, altura):
		self.altura += altura

	def envelhecer(self, anos):
		anosAntes = self.idade
		self.idade += anos

		if (anosAntes < 25):
			if (self.idade < 25):
				self.crescer(anos * 0.5)
			else:
				self.crescer((25 - anosAntes) * 0.5)

	def aumentarSalarioPercentual(self, percentual):
		if percentual <= 0:
			return self.salario
		return self.salario * (1+percentual)