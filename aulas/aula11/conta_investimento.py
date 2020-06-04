class ContaInvestimento:

    def __init__(self, numero, nomeCorrentista, taxaJuros, saldo=0.0):
        self.numero = numero
        self.alterarNome(nomeCorrentista)
        self.taxaJuros = taxaJuros
        self.saldo = saldo

    def alterarNome(self, nomeCorrentista):
        self.nomeCorrentista = nomeCorrentista

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        self.saldo -= valor

    def adicionaJuros(self):
        self.saldo += (self.saldo * (self.taxaJuros / 100.0))

    def ajustarTaxaJuros(self, taxa):
        'Ajusta a taxa de juros'
        self.taxaJuros = taxa

    def inativarConta(self):
        'Inativa a conta zerando seus atributos'
        self.numero = 0
        self.alterarNome('')
        self.saque(self.saldo)
        self.ajustarTaxaJuros(0)

    def adicionaPremiacao(self):
        'Premia a conta dobrando seu saldo'
        self.saldo *= 2


# TESTE DA CLASSE

conta = ContaInvestimento(100, 'Tales', 10)
conta.deposito(1000)
print(conta.saldo)
conta.adicionaJuros()
print(conta.saldo)
conta.ajustarTaxaJuros(12)
conta.adicionaJuros()
print(conta.saldo)
conta.adicionaJuros()
print(conta.saldo)
conta.adicionaJuros()
print(conta.saldo)
conta.adicionaPremiacao()
print(conta.saldo)

conta.inativarConta()
