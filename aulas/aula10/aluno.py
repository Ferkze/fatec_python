from pprint import pprint

class Aluno:
	def __init__(self, nome, idade, peso, altura, salario = 0):
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

	def setSalario(self, salario):
		self.salario = salario

	def demissao(self):
		self.salario = 0

	def aumentarSalarioPercentual(self, percentual):
		if percentual <= 0:
			return
		self.salario *= (1+percentual)


douglas = Aluno('Douglas Duarte',43, 67.0, 167)
pprint(vars(douglas))

douglas.engordar(1)
pprint(vars(douglas))

douglas.emagrecer(2)
pprint(vars(douglas))

douglas.crescer(3)
pprint(vars(douglas))

douglas.envelhecer(4)
pprint(vars(douglas))

fabio = Aluno('Fabio Martins', 19, 72.0, 172, 11200)
fabio.aumentarSalarioPercentual(0.2)
pprint(vars(fabio))
fabio.demissao()
fabio.setSalario(15000)
pprint(vars(fabio))
