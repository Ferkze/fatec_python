class TV:
	'Classe TV'
	def __init__(self, marca, tipo, volume = 0, brilho = 10, canal = 0):
		self.setMarca(marca)
		self.setTipo(tipo)
		self.volume = volume
		self.brilho = brilho
		self.setCanal(canal)

	def setMarca(self, marca):
		'Configura a marca da TV'
		if marca == '':
			self.marca = 'Não especificado'
		elif (marca not in ['Philips', 'Semp Toshiba', 'TCL', 'Samsung']):
			self.marca = 'Marca desconhecida'
		else:
			self.marca = marca

	def setTipo(self, tipo):
		'Configura o tipo da TV'
		if tipo == '':
			self.tipo = 'Não especificado'
		elif (tipo not in ['LED', 'Plasma', 'OLED', 'LCD']):
			self.tipo = 'Tipo desconhecido'
		else:
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
tv = TV('Samsung', 'LCD', volume=63, brilho=8, canal=13)
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
