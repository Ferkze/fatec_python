class ContaInvestimento:

    def __init__(self, numero, nomeCorrentista, taxaJuros, saldo=0.0):
        self.numero = numero
        self.alterarNome(nomeCorrentista)
        self.taxaJuros = taxaJuros
        self.saldo = saldo

    def alterarNome(self, nomeCorrentista):
        self.nomeCorrentista = nomeCorrentista

    def deposito(self, valor):
        try:
            if valor <= 0:
                raise ValueError
            self.saldo += valor
        except ValueError as err:
            print('Erro no valor provisionado de deposito: {}'.format(err))

    def saque(self, valor):
        try:
            if valor <= 0:
                raise ValueError
            self.saldo -= valor
        except ValueError as err:
            print('Erro no valor provisionado de saque: {}'.format(err))

    def adicionaJuros(self):
        self.saldo += (self.saldo * (self.taxaJuros / 100.0))

    def ajustarTaxaJuros(self, taxa):
        'Ajusta a taxa de juros'
        try:
            if taxa <= 0:
                raise ValueError
            self.taxaJuros = taxa
        except ValueError:
            print('Taxa de juros não pode ser ajustada abaixo de zero')

    def inativarConta(self):
        'Inativa a conta zerando seus atributos'
        try:
            if self.numero == 0:
                raise Exception
            self.numero = 0
            self.alterarNome('')
            self.saque(self.saldo)
            self.ajustarTaxaJuros(0)
        except Exception:
            print('Não é possível inativar uma conta não ativa')

    def adicionaPremiacao(self):
        'Premia a conta dobrando seu saldo'
        self.saldo *= 2


# TESTE DA CLASSE

conta = ContaInvestimento(100, 'Tales', 10)
conta.deposito(1000)
print(conta.saldo)
conta.adicionaJuros()
print(conta.saldo)
conta.ajustarTaxaJuros(-1)
conta.adicionaJuros()
print(conta.saldo)
conta.adicionaJuros()
print(conta.saldo)
conta.adicionaJuros()
print(conta.saldo)
conta.adicionaPremiacao()
print(conta.saldo)

conta.inativarConta()
conta.inativarConta()
