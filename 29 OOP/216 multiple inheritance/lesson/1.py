class Saat:

	def __init__(self, saat, dakika, saniye):
		self.__saat = saat
		self.__dakika = dakika
		self.__saniye = saniye

	def saat_kur(self, saat, dakika, saniye):
		self.__saat = saat
		self.__dakika = dakika
		self.__saniye = saniye

	def saat_kac(self):
		return "{0} : {1} : {2}".format(self.__saat, self.__dakika, self.__saniye)

#
class Takvim(object):

	def __init__(self, d,m,y):
		self.takvim_kur(d, m, y)

	def takvim_kur(self, d, m, y):
		self.d = d
		self.m = m
		self.y = y

	def bugun_ne(self):
		return "{d}:{m}:{y}".format(d=self.d,m=self.m,y=self.y)


class saatlitakvim(Saat, Takvim):

	def __init__(self, gun, ay, yil, saat, dakika, saniye):
		Saat.__init__(self, saat, dakika, saniye)
		Takvim.__init__(self, gun, ay, yil)

print('-----saatli takvim-----')

saatli_takvim = saatlitakvim(8,12,2020,16,45,7)
print(saatli_takvim.saat_kac())