from pprint import pprint

alunos = set()


class Aluno:
    def __init__(self, nome, idade, peso, altura, salario=0):
        if self in alunos:
            print('Já é aluno cadastrado')
            return

        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.salario = salario
        alunos.add(self)

    def engordar(self, peso):
        try:
            self.peso += peso
        except TypeError as err:
            print('Erro no tipo de valor do peso engordado: {}'.format(err))

    def emagrecer(self, peso):
        try:
            if (peso > self.peso):
                self.peso = 0
            else:
                self.peso -= peso
        except TypeError as err:
            print('Erro no tipo de valor do peso emagrecido: {}'.format(err))

    def crescer(self, altura):
        try:
            self.altura += altura
        except TypeError as err:
            print('Erro no tipo de valor de crescimento de altura: {}'.format(err))

    def envelhecer(self, anos):
        try:
            anosAntes = self.idade
            self.idade += anos
        except TypeError as err:
            print('Erro no tipo de valor anos de envelhecimento: {}'.format(err))
        else:
            if (anosAntes < 25):
                if (self.idade < 25):
                    self.crescer(anos * 0.5)
                else:
                    self.crescer((25 - anosAntes) * 0.5)

    def setSalario(self, salario):
        self.salario = salario

    def demissao(self):
        self.salario = 0

    def aumentarSalarioPercentual(self, taxa):
        allowedRaises = set((0.05, 0.1, 0.15, 0.2, 0.25, 0.3))
        if taxa <= 0:
            return
        if taxa in allowedRaises:
            self.salario *= (1+taxa)
        else:
            print('Aumento de {} não permitido, somente esses percentuais: {}'.format(
                taxa, allowedRaises))

    def graduar(self):
        alunos.remove(self)


douglas = Aluno('Douglas Duarte', 43, 67.0, 167)
pprint(vars(douglas))

douglas.engordar(1)
pprint(vars(douglas))

douglas.emagrecer(2)
pprint(vars(douglas))

douglas.crescer('10')
pprint(vars(douglas))

douglas.envelhecer(4)
pprint(vars(douglas))

fabio = Aluno('Fabio Martins', 19, 72.0, 172, 11200)
fabio.aumentarSalarioPercentual(0.2)
fabio.aumentarSalarioPercentual(0.4)
pprint(vars(fabio))
fabio.demissao()
fabio.setSalario(15000)
fabio.emagrecer('-10')
pprint(vars(fabio))

print(alunos)

fabio.graduar()

print(alunos)
