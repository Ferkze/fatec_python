class Tamagushi:

    def __init__(self, nome, fome, saude, idade):
        self.setNome(nome)
        self.setFome(fome)
        self.setSaude(saude)
        self.setIdade(idade)

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setFome(self, fome):
        self.fome = fome

    def getFome(self):
        return self.fome

    def setSaude(self, saude):
        self.saude = saude

    def getSaude(self):
        return self.saude

    def setIdade(self, idade):
        self.idade = idade

    def getIdade(self):
        return self.idade

    def getHumor(self):
        return self.getFome() * self.getSaude()

    def alimentar(self, alimento):
        'Alimenta o Tamagushi com o parâmetro alimento e diminui sua fome'
        self.fome -= 1
        print('Yum yum %s!' % alimento)

    def crescer(self):
        'Faz o Tamagushi crescer aumentando a idade dele'
        self.setIdade(self.getIdade()+1)

    def morrer(self):
        'Mata o Tamagushi zerando a saúde dele'
        self.setSaude(0)


# TESTE DA CLASSE
bicho = Tamagushi('Tamagoshi', 10, 10, 10)

bicho.alimentar('Pão')
bicho.crescer()

print('Humor: %d – Idade: %d – Fome: %d' %
      (bicho.getHumor(), bicho.getIdade(), bicho.getSaude()))
bicho.morrer()
print('Saúde do bicho: %d' % bicho.getSaude())
