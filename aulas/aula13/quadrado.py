import math

cores = set(('preto', 'branco', 'vermelho', 'verde', 'azul'))
tamanhos = set((1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144))


class Quadrado():
    'Define um quadrado'

    def __init__(self, lado, cor):
        self.trocarCor(cor)
        self.setLado(lado)

    def trocarCor(self, cor):
        if cor not in cores:
            print('Cor {} não permitida, as cores permitidas são: {}'.format(cor, cores))
            self.cor = ''
        else:
            self.cor = cor

    def setLado(self, lado):
        if lado not in tamanhos:
            print(
                'Lado {} não permitido, os tamanhos permitidos são: {}'.format(lado, tamanhos))
            self.lado = 0
        else:
            self.lado = lado

    def getLado(self):
        return self.lado

    def calculaArea(self):
        return self.lado * self.lado

    def calculaPerimetro(self):
        return self.lado * 2

    def cabeNaCaixa(self, m=100):
        try:
            quantidade = m / self.lado
            if quantidade < 1:
                print('O quadrado não cabe na caixa')
                return

            resto = m % self.lado
            if resto == 0:
                print('{} x quadrado {} cabe perfeitamente na caixa'.format(
                    quantidade, self.cor))
            else:
                print('{} x quadrado {} cabe na caixa, porém sobra {} de espaço'.format(
                    math.floor(quantidade), self.cor, resto))
        except ZeroDivisionError:
            print('Lado vazio...')


quadrado1 = Quadrado(5, 'azul')
quadrado1.cabeNaCaixa(100)

quadrado2 = Quadrado(7, 'laranja')
quadrado2.cabeNaCaixa(100)

quadrado3 = Quadrado(55, 'preto')
quadrado3.cabeNaCaixa(100)

quadrado4 = Quadrado(144, 'branco')
quadrado4.cabeNaCaixa(100)
