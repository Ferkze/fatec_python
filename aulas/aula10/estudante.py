class Estudante:
	def __init__(self, nome):
		self.nome = nome

	def estudar(self, materia):
		print("{} está estudando {}".format(self.nome, materia))

fabio = Estudante("Fabio")
fabio.estudar("Multimidia e Hipermidia")
