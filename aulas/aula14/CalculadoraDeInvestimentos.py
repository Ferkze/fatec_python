import math


class CalculadoraDeInvestimentos:

    def __init__(self, taxa, valor, periodos, nome_periodo):
        self.taxa = taxa
        self.valor = valor
        self.periodos = periodos
        self.nome_periodo = nome_periodo

    def getTaxa(self):
        return self.taxa

    def setTaxa(self, taxa):
        self.taxa = taxa

    def getValor(self):
        return self.valor

    def setValor(self, valor):
        self.valor = valor

    def getPeriodos(self):
        return self.periodos

    def setPeriodos(self, periodos):
        self.periodos = periodos

    def getNomePeriodo(self):
        return self.nome_periodo

    def setNomePeriodo(self, NomePeriodo):
        self.nome_periodo = nome_periodo

    def calculaJurosFinal(self, valor=None, taxa=None, periodos=None):
        try:
            if valor is None:
                valor = self.getValor()
            if taxa is None:
                taxa = self.getTaxa()
            if periodos is None:
                periodos = self.getPeriodos()
            return valor * ((math.pow(1+taxa, periodos)) - 1)
        except TypeError:
            print('Erro nas variáveis de cálculo de juros')

    def calculaValorFinal(self, valor=None, taxa=None, periodos=None):
        try:
            if valor is None:
                valor = self.getValor()
            if taxa is None:
                taxa = self.getTaxa()
            if periodos is None:
                periodos = self.getPeriodos()
            return valor + self.calculaJurosFinal(valor, taxa, periodos)
        except TypeError as err:
            print('Erro nas variáveis do cálculo de valor total:', err)

    def mostraJuroPorPeriodo(self):
        juros_periodos = self.calculaJuros()
        for periodo in range(len(juros_periodos)):
            print('Juros de {:.2f} no período {} ({})'.format(
                juros_periodos[periodo], periodo+1, self.nome_periodo))

    def calculaJuros(self, periodo_juros=[], periodos=12):
        atual = len(periodo_juros)
        if atual == periodos:
            return periodo_juros
        periodo_juros.append(self.calculaJurosFinal(periodos=atual+1))
        return self.calculaJuros(periodo_juros, periodos)

    def mostraMontantePorPeriodo(self):
        juros_periodos = self.calculaMontantes()
        for periodo in range(len(juros_periodos)):
            print('Montante de {:.2f} no período {} ({})'.format(
                juros_periodos[periodo], periodo+1, self.nome_periodo))

    def calculaMontantes(self, periodo_montantes=[], periodos=12):
        atual = len(periodo_montantes)
        if atual == periodos:
            return periodo_montantes
        periodo_montantes.append(self.calculaValorFinal(
            periodos=atual+1, valor=self.getValor()))
        return self.calculaMontantes(periodo_montantes, periodos)

    def analiseRentabilidade(self):
        try:
            montantes_periodos = self.calculaMontantes(
                periodos=self.periodos)
            montantes_rentabilizados = set()
            for montante in montantes_periodos:
                montantes_rentabilizados.add('{:.2f}'.format(montante))
            if len(montantes_rentabilizados) != self.periodos:
                periodos = self.periodos - len(montantes_rentabilizados)
                print(
                    '%d de %d períodos não estão sendo rentabilizados durante a aplicação' % (periodos, self.periodos))
            else:
                print('Períodos estão sendo bem rentabilizados!')
        except TypeError as err:
            print('Erro ao analisar a rentabilidade:', err)

    def analisaInvestimento(self):
        print('Investimento de {} a {:.2f}%, por {} x {}'.format(
            self.getValor(), self.getTaxa(), self.getPeriodos(), self.getNomePeriodo()))
        print('Rende {:.2f} em juros, montante total de {:.2f}'.format(
            self.calculaJurosFinal(), self.calculaValorFinal()))


# Teste da classe
calculadora = CalculadoraDeInvestimentos(
    0.05, 1000, 12, 'anos')
juros = calculadora.calculaJurosFinal()
total = calculadora.calculaValorFinal()

calculadora.mostraJuroPorPeriodo()
calculadora.mostraMontantePorPeriodo()

c2 = CalculadoraDeInvestimentos(0.00005, 100, 24, 'mês')
c2.mostraMontantePorPeriodo()
c2.analiseRentabilidade()
