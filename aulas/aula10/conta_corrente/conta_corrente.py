class ContaCorrente:

	def __init__(self, numero, nomeCorrentista, saldo=0.0):
		self.numero = numero
		self.alterarNome(nomeCorrentista)
		self.saldo = saldo

	def alterarNome(self, nomeCorrentista):
		self.nomeCorrentista = nomeCorrentista

	def deposito(self, valor):
		self.saldo += valor

	def saque(self, valor):
		self.saldo -= valor

	def calculaJurosDeSaldoNegativo(self, tx_juros):
		if self.saldo >= 0:
			return 0

		return self.saldo * tx_juros