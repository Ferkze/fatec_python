endividados = set()


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
        try:
            if percentualDeAumento < 0:
                raise ValueError
            self.salario += self.salario * (percentualDeAumento / 100.0)
        except ValueError:
            print('Não é possível diminuir o salário')

    def demitir(self):
        self.salario = 0

    def endividar(self, divida):
        'Adiciona dívida ao Funcionário e suja seu nome se for incompatível com seu salário'
        try:
            if "[Nome sujo]" in self.nome:
                raise Exception
            if self.salario < divida:
                self.nome = "*{} [Nome sujo]".format(self.nome)
                endividados.add(self.nome)
            self.divida += divida
        except Exception:
            print('Endividamento de pessoa com nome sujo não é possível')
        except TypeError as err:
            print('Erro no tipo do valor da dívida: {}'.format(err))

    def pagarDivida(self):
        'Paga a dívida do Funcionário se o salário der e limpa seu nome'
        if self.salario < self.divida:
            print('Incapaz de pagar dívida com salário de %.2f' % self.salario)
        else:
            endividados.remove(self.nome)
            self.nome = self.nome[1:-11]
            print('Dívida de %.2f foi paga' % self.divida)
            self.divida = 0

    def empregar(self, salario):
        'Emprega o funcionário, dando-lhe um salário'
        if self.nome in endividados:
            print('Funcionário na merda, cuidado!')
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
harry.demitir()
harry.endividar('1000')
harry.endividar(1000)
harry.endividar(1)
