class BombaCombustivel():

    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.setTipoCombustivel(tipoCombustivel)
        self.setValorLitro(valorLitro)
        self.setQuantidadeCombustivel(quantidadeCombustivel)

    def setTipoCombustivel(self, tipoCombustivel):
        self.tipoCombustivel = tipoCombustivel

    def setValorLitro(self, valorLitro):
        self.valorLitro = float(valorLitro)

    def setQuantidadeCombustivel(self, quantidadeCombustivel):
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self, valor):
        totalLitros = valor / self.valorLitro
        if (totalLitros <= self.quantidadeCombustivel):
            self.setQuantidadeCombustivel(
                self.quantidadeCombustivel - totalLitros)

    def abastecerPorLitro(self, totalLitros):
        if (totalLitros <= self.quantidadeCombustivel):
            self.setQuantidadeCombustivel(
                self.quantidadeCombustivel - totalLitros)

    def abastecerBomba(self, litros):
        'Abastece o estoque de combustivel da bomba'
        self.quantidadeCombustivel += litros

    def vazar(self, vazamento):
        'Abastece o estoque de combustivel da bomba'
        if vazamento > self.quantidadeCombustivel:
            vazamento = self.quantidadeCombustivel
        self.quantidadeCombustivel -= vazamento

    def explodir(self):
        'Explode, causando danos em dimensões de acordo com os litros que tem'
        print('BOOOOM, {}cm2 of explosion'.format(
            self.quantidadeCombustivel*10))
        self.setQuantidadeCombustivel(0)


# Teste da classe
bomba1 = BombaCombustivel('Gasolina Aditivada', 3.03, 10000)
bomba1.abastecerPorLitro(100)
print(bomba1.quantidadeCombustivel)
bomba1.abastecerPorValor(100)
bomba1.vazar(4000)
bomba1.abastecerBomba(2200)
print(bomba1.quantidadeCombustivel)
bomba1.explodir()
print(bomba1.quantidadeCombustivel)
