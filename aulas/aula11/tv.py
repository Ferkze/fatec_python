class TV:

	def __init__(self, marca, tipo):
		self.marca = self.setMarca(marca)
		self.tipo = self.setTipo(tipo)
		self.volume = 0
		self.brilho = 10
		self.setCanal(0)

	def setMarca(self, marca):
		'Configura a marca da TV'
		if (marca not in ['Philips', 'Semp Toshiba', 'TCL', 'Samsung']):
			return
		self.marca = marca

	def setTipo(self, tipo):
		'Configura o tipo da TV'
		if (tipo not in ['LED', 'Plasma', 'OLED', 'LCD']):
			return
		self.tipo = tipo

	def setCanal(self, canal):
		'Seleciona o canal passado de 0 a 100'
		if (canal < 0) or (canal > 100):
			return
		self.canal = canal

	def aumentaVolume(self):
		'Aumenta o volume de 1 em 1 até o máximo de 100'
		if (self.volume < 100):
			self.volume += 1

	def diminuiVolume(self):
		'Aumenta o volume de 1 em 1 até o mínimo de 1'
		if (self.volume > 0):
			self.volume -= 1

	def aumentaBrilho(self):
		'Aumenta o brilho de 1 em 1 até o máximo de 10'
		if (self.brilho < 10):
			self.brilho += 1

	def diminuiBrilho(self):
		'Diminui o brilho de 1 em 1 até o mínimo de 1'
		if (self.brilho > 1):
			self.brilho -= 1

# TESTE DA CLASSE
tv = TV('Samsung', 'LCD')
tv.setCanal(10)
tv.aumentaVolume()
tv.aumentaVolume()
tv.aumentaVolume()
tv.aumentaVolume()
tv.diminuiVolume()

tv.diminuiBrilho()
tv.diminuiBrilho()
tv.diminuiBrilho()
tv.aumentaBrilho()

print("[TV %s %s] Canal: %d - Volume: %d - Brilho: %d" % (tv.tipo, tv.marca, tv.canal, tv.volume, tv.brilho))
