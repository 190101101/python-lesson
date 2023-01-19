class saat:

	def __init__(self, saat1):
		self.__saat1 = saat1

	def saat1_kur(self, saat1):
		self.__saat1 = saat1

	def saat_kac(self):
		return self.__saat1

class takvim(object):

	def __init__(self, d):
		self.takvim_kur(d)

	def takvim_kur(self, d):
		self.d = d

	def bugun_ne(self):
		return self.d


class saatlitakvim(saat, takvim):

	def __init__(self, gun, saat1):
		saat.__init__(self, saat1)
		takvim.__init__(self, gun)

qq = saatlitakvim(8,12)
print(qq.saat_kac())