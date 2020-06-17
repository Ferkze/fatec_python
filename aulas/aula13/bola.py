class Bola:
    'Classe para definir uma bola'

    def __init__(self, raio):
        self.raio = raio
        self.cor = "sem cor"

    def trocaCor(self, cor):
        try:
            if type(cor) == 'string':
                raise TypeError
            self.cor = cor
        except TypeError as err:
            print('Erro no tipo de valor atribuído à cor')

    def mostraCor(self):
        try:
            if self.raio == 0:
                raise ValueError
            print(self.cor)
        except ValueError:
            print('Não há bola, portanto não há cor')

    def calcularDiametro(self):
        return self.raio * 2

    def mostrarRaio(self):
        print(self.raio)

    def mostrarDiametro(self):
        print(self.calcularDiametro())

    def estourar(self):
        try:
            if self.raio == 0:
                raise Exception
            self.raio = 0
            print('Bola {}: Puff!'.format(self.cor))
        except Exception:
            print('Bola mucha não estoura')

# Teste da Classe


bola = Bola(5)
bola.trocaCor("Azul")
bola.mostraCor()
bola.mostrarDiametro()
bola.estourar()
bola.mostrarRaio()
bola.mostraCor()  # Exception
bola.trocaCor(1)  # Exception
bola.estourar()  # Exception
