class Carro:

    def __init__(self, quilometrosLitro):
        self.quilometrosLitro = quilometrosLitro
        self.qtdeCombustivel = 0
        self.distancia_proximo_reparo = 400
        self.percorrido = 0
        self.quebrado = False

    def adicionarGasolina(self, quantidade):
        try:
            if quantidade < 0:
                raise ValueError
            self.qtdeCombustivel += float(quantidade)
        except ValueError as err:
            print('Erro de valor de adição de combustível: {}'.format(err))
        except TypeError as err:
            print('Erro de tipo de valor de adição de combustível: {}'.format(err))

    def andar(self, distancia):
        try:
            if self.quebrado:
                print('Carro quebrado não anda')
                return
            elif self.qtdeCombustivel <= 0:
                print('Carro sem gasolina não anda')
                return
            print('Andando {} km'.format(distancia))
            gasto = distancia / self.quilometrosLitro
            self.qtdeCombustivel -= gasto
            self.percorrido += distancia

            if self.percorrido > self.distancia_proximo_reparo:
                self.quebrar()
        except ZeroDivisionError as err:
            print('Quilometragem por litro não pode estar zero')
        except TypeError as err:
            print('Erro de tipo de variável de distância: {}'.format(err))

    def obterGasolina(self):
        print('gasosa:', self.qtdeCombustivel)

    def obterAutonomia(self):
        print('autonomia:', self.quilometrosLitro * self.qtdeCombustivel)
        return self.quilometrosLitro * self.qtdeCombustivel

    def ajustarProximoReparo(self):
        'Ajusta o próximo reparo para +400km'
        self.distancia_proximo_reparo = self.percorrido + 400

    def quebrar(self):
        'Quebra o carro, impossibilitando ele de andar'
        print('Quebrou!!!')
        self.distancia_proximo_reparo = 0
        self.quebrado = True

    def reparar(self):
        'Repara o carro'
        self.ajustarProximoReparo()
        self.quebrado = False


# TESTE DA CLASSE
meuFusca = Carro(15)
# 15 quilometros por litro de combustivel.
meuFusca.adicionarGasolina(20)
# abastece com 20 litros de combustivel.
meuFusca.andar(100)
meuFusca.obterGasolina()        # Imprime o combustivel que resta no tanque.
meuFusca.obterAutonomia()
meuFusca.andar(100)
meuFusca.obterGasolina()        # Imprime o combustivel que resta no tanque.
meuFusca.obterAutonomia()
meuFusca.andar(100)
meuFusca.andar(200)
meuFusca.adicionarGasolina(20)
meuFusca.andar(100)
meuFusca.andar(100)
meuFusca.andar(100)
meuFusca.reparar()
meuFusca.andar(50)
print('Cheguei')

car = Carro(-1)
car.andar(100)
car.adicionarGasolina(50)
car.andar('50')
