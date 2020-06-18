especies_conhecidas = set((
    'orangotango',
    'prego',
    'gibão'
))

especies_vivas = set((
    'orangotango',
    'prego'
))

especies_extintas = set((
    'gibão'
))


class Macaco:

    def __init__(self, nome, especie):
        self.nome = nome
        if especie not in especies_conhecidas:
            print('Nova espécie encontrada:', especie)
            especies_conhecidas.add(especie)
        if especie in especies_extintas:
            print('Espécie %s considerada extinta voltou a aparecer' % especie)
            especies_extintas.remove(especie)
        self.especie = especie
        self.bucho = []
        self.intestino = []

    def comer(self, comida):
        self.bucho.append(comida)

    def vomitar(self):
        'Vomitar limpa o bucho'
        self.bucho.clear()

    def verBucho(self):
        print('Bucho: %s' % self.bucho)

    def digerir(self):
        if (len(self.bucho) > 0):
            self.intestino.append(self.bucho.pop(0))

    def cagar(self):
        'Cagar tira um dejeto do intestino'
        if (len(self.intestino) > 0):
            poop = self.intestino.pop(0)
            print('Pooping %s' % poop)

    def passarMal(self):
        'Cagar elimina todos os dejetos do intestino'
        if (len(self.bucho) > 0):
            self.intestino.append(self.bucho)
            self.bucho.clear()
        if (len(self.intestino) > 0):
            print('Mega pooping of %d items' % len(self.intestino))

        self.intestino.clear()

    def morrer(self):
        'Cagar elimina todos os dejetos do intestino'
        especies_vivas.remove(self.especie)

    def extinguir(self):
        'Cagar elimina todos os dejetos do intestino'
        especies_extintas.add(self.especie)


# Teste
macaco1 = Macaco('Simao')
macaco2 = Macaco('Prego')

macaco1.comer('Maca')
macaco1.verBucho()
macaco1.comer('Banana')
macaco1.verBucho()
macaco1.vomitar()
macaco1.comer('Abacaxi')
macaco1.digerir()
macaco1.verBucho()
macaco2.comer('Maca')
macaco2.digerir()
macaco2.cagar()
macaco2.comer('Banaca')
macaco2.comer('Xuxu')
macaco2.comer(macaco1)
macaco2.passarMal()
