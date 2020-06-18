import math

cores = set(('preto', 'branco', 'vermelho', 'verde', 'azul'))
tamanhos = set((1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144))


class Retangulo():
    'Define um Retangulo'

    def __init__(self, lado1, lado2):
        self.setLados(lado1, lado2)
        self.cor = ''

    def setLados(self, lado1, lado2):
        if lado1 not in tamanhos:
            print(
                'Lado 1 {} não permitido, os tamanhos permitidos são: {}'.format(lado1, tamanhos))
            self.lado1 = 0
        else:
            self.lado1 = lado1
        if lado2 not in tamanhos:
            print(
                'Lado 2 {} não permitido, os tamanhos permitidos são: {}'.format(lado2, tamanhos))
            self.lado2 = 0
        else:
            self.lado2 = lado2

    def getLado1(self):
        return self.lado1

    def getLado2(self):
        return self.lado2

    def calculaArea(self):
        return self.lado1 * self.lado2

    def calculaPerimetro(self):
        return 2 * (self.lado1 + self.lado2)

    def trocaCor(self, cor):
        if cor not in cores:
            print('Cor {} não permitida, as cores permitidas são: {}'.format(cor, cores))
            self.cor = ''
        else:
            self.cor = cor

    def mostraCor(self):
        if self.cor == '':
            print('Retangulo sem cor')
        else:
            print('Retangulo {}'.format(self.cor))

    def cabeNaCaixa(self, area=100):
        quantidade = area / self.calculaArea()
        if quantidade < 1:
            print('O Retangulo não cabe na caixa')
            return

        resto = area % self.calculaArea()
        if resto == 0:
            print('{} x Retangulo cabe perfeitamente na caixa'.format(quantidade))
        else:
            print('{} x Retangulo cabe na caixa, porém sobra {} de espaço'.format(
                math.floor(quantidade), resto))


retangulo1 = Retangulo(5, 2)
retangulo1.trocaCor('Preto')
retangulo1.mostraCor()
retangulo1.cabeNaCaixa(100)

retangulo2 = Retangulo(8, 5)
retangulo2.trocaCor('azul')
retangulo2.mostraCor()
retangulo2.cabeNaCaixa(100)

retangulo3 = Retangulo(144, 4)
retangulo3.trocaCor('amarelo')
retangulo3.mostraCor()
retangulo3.cabeNaCaixa(100)
