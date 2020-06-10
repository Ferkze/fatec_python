class ContaCorrente:

	def __init__(self, numero, nomeCorrentista, saldo=0.0):
		self.numero = numero
		self.alterarNome(nomeCorrentista)
		self.saldo = saldo

	def getNumero(self):
		return self.numero

	def getSaldo(self):
		return self.saldo

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

	def enviaTransferencia(self, conta, valor):
		if self.saldo < valor:
			return 'Saldo insuficiente'
		
		if conta.recebeTransferencia(valor):
			self.saldo -= valor
			return 'Transferencia bem sucedida para a conta {}'.format(conta.getNumero())

		return 'Transferencia mal sucedida para a conta {}'.format(conta.getNumero())

	def recebeTransferencia(self, valor):
		if valor <= 0:
			return False

		self.saldo += valor
		return True

conta = ContaCorrente(100, 'Tales')
conta.deposito(100)
print(conta.getSaldo())
conta.saque(200)
print(conta.getSaldo())
juros = conta.calculaJurosDeSaldoNegativo(0.01)
print('Juros diários de {} para o saldo negativo'.format(juros))

conta2 = ContaCorrente(200, 'Fabio', 200)
resultado = conta2.enviaTransferencia(conta, 150)
print(resultado)

print('Saldo da conta {}: {}'.format(conta.getNumero(), conta.getSaldo()))
