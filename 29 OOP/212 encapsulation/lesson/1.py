class telefon:
	def __init__(self):
		self.__fiyat = 1000

	def sat(self):
		print('satis fiyati {} tl'.format(self.__fiyat))

	def set_fiyat(self, yeni_fiyat):
		if yeni_fiyat <= 0:
			print('negativ fiyat olamaz')
		else:
			self.__fiyat = yeni_fiyat

	def get_fiyat(self):
		return self.__fiyat

tel = telefon()
tel.sat()
tel.__fiyat = 5000
print(tel.__fiyat)

tel.renk = 'Siyah'
print(tel.renk)

tel.set_fiyat(8000)
tel.sat()

print(tel.get_fiyat())

tel.set_fiyat(6000)
print(tel.get_fiyat())
