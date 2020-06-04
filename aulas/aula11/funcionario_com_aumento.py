class Funcionario:

    def __init__(self, nome, salario, divida=0.0):
        self.nome = nome
        self.salario = float(salario)
        self.divida = float(divida)

    def getNome(self):
        return self.nome

    def getSalario(self):
        return self.salario

    def aumentarSalario(self, percentualDeAumento):
        self.salario += self.salario * (percentualDeAumento / 100.0)

    def demitir(self):
        self.salario = 0

    def endividar(self, divida):
        'Adiciona dívida ao Funcionário e suja seu nome se for incompatível com seu salário'
        if self.salario < divida:
            self.nome = "*{} [Nome sujo]".format(self.nome)
        self.divida += divida

    def pagarDivida(self):
        'Paga a dívida do Funcionário se o salário der e limpa seu nome'
        if self.salario < self.divida:
            print('Incapaz de pagar dívida com salário de %.2f' % self.salario)
        else:
            self.nome = self.nome[1:-11]
            print('Dívida de %.2f foi paga' % self.divida)
            self.divida = 0

    def empregar(self, salario):
        'Emprega o funcionário, dando-lhe um salário'
        self.salario = salario


# TESTE DA CLASSE
harry = Funcionario("Harry", 25000)
harry.aumentarSalario(10)
harry.demitir()
harry.endividar(10000)
print('Nome: %s' % harry.getNome())
harry.empregar(30000)
harry.pagarDivida()
print('Nome: %s' % harry.getNome())
print('Salario: %.2f' % harry.getSalario())
