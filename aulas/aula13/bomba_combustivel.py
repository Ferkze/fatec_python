class BombaCombustivel():

    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.opcoesAbastecimentoValor = set((10, 20, 50, 100))
        self.opcoesAbastecimentoLitro = set((5, 10, 25, 40))
        self.setTipoCombustivel(tipoCombustivel)
        self.setValorLitro(valorLitro)
        self.setQuantidadeCombustivel(quantidadeCombustivel)

    def setTipoCombustivel(self, tipoCombustivel):
        self.tipoCombustivel = tipoCombustivel

    def setValorLitro(self, valorLitro):
        self.valorLitro = float(valorLitro)

    def addOpcaoLitro(self, opcao):
        'Adiciona opção de abastecimento por Litro'
        self.opcoesAbastecimentoLitro.add(opcao)

    def addOpcaoValor(self, opcao):
        'Adiciona opção de abastecimento por Valor'
        self.opcoesAbastecimentoValor.add(opcao)

    def removeOpcaoLitro(self, opcao):
        'Remove opção de abastecimento por Litro'
        self.opcoesAbastecimentoLitro.remove(opcao)

    def removeOpcaoValor(self, opcao):
        'Remove opção de abastecimento por Valor'
        self.opcoesAbastecimentoValor.remove(opcao)

    def setQuantidadeCombustivel(self, quantidadeCombustivel):
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self, valor):
        if valor not in self.opcoesAbastecimentoValor:
            print('Valor {} não permitido, opções: {}'.format(
                valor, self.opcoesAbastecimentoValor))
            return
        try:
            totalLitros = valor / self.valorLitro
            if (totalLitros <= self.quantidadeCombustivel):
                self.setQuantidadeCombustivel(
                    self.quantidadeCombustivel - totalLitros)
        except ZeroDivisionError:
            print('O valor do litro não pode estar zerado')

    def abastecerPorLitro(self, totalLitros):
        if totalLitros not in self.opcoesAbastecimentoLitro:
            print('Litros {} não permitido, opções: {}'.format(
                totalLitros, self.opcoesAbastecimentoLitro))
            return
        try:
            if totalLitros < 0:
                raise ValueError
            if (totalLitros <= self.quantidadeCombustivel):
                self.setQuantidadeCombustivel(
                    self.quantidadeCombustivel - totalLitros)
        except ValueError:
            print('Não é permitido drenar o veículo')

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
        try:
            if self.quantidadeCombustivel <= 0:
                raise Exception
            print('BOOOOM, {}cm2 of explosion'.format(
                self.quantidadeCombustivel*10))
            self.setQuantidadeCombustivel(0)
        except Exception:
            print('Não é possível causar explosão no posto desabastecido')


# Teste da classe
bomba1 = BombaCombustivel('Gasolina Aditivada', 3.03, 10000)
bomba1.abastecerPorLitro(100)
print(bomba1.quantidadeCombustivel)
bomba1.abastecerPorValor(100)
bomba1.vazar(4000)
bomba1.abastecerBomba(2200)
bomba1.abastecerPorLitro(5)
print(bomba1.quantidadeCombustivel)
bomba1.explodir()
print(bomba1.quantidadeCombustivel)
bomba1.abastecerPorLitro(-10)
