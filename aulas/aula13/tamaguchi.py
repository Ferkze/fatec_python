alimentos = set((
    'Pão',
    'Gosma',
    'Sujeira',
    'Barata'
))
alimentos_ruins = set((
    'Pão'
))
alimentos_bons = set((
    'Gosma',
    'Sujeira',
    'Barata'
))


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
        if alimento in alimentos:
            self.fome -= 1
            if alimento in alimentos_bons:
                print('Yum yum %s!' % alimento)
            elif alimento in alimentos_ruins:
                self.fome += 2
                print('Bleh %s!' % alimento)

        else:
            print('Tamagushi não conhece o alimento %s, agora conhce' % alimento)
            alimentos.add(alimento)

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
