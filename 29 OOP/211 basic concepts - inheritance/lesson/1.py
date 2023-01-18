class Penguen:
	tur = 'kus'

	def __init__(self, ad, yas, renk):
		self.ad = ad
		self.yas = yas
		self.renk = renk

	def yuzme(self):
		return f"{self.ad} yuze bilir."

	def sarki_soyle(self, soylemek=False):
		if soylemek == True:
			return f"{self.ad} sarki soyleye bilir."
		else:
			return f"{self.ad} sarki soyleye bilmir."

	def dans(self, dans=False):
		if dans == True:
			return f"{self.ad} dans ede bilir."
		else:
			return f"{self.ad} dans ede bilmir."


class kus:

	def __init__(self):
		print('kus yaratildi')

	def kimimBen(self):
		print('ben bir kusum')

	def ucma(self):
		print('kuslar uca bilir')

	def yuzme(self):
		print('kuslar yuze bilir')
		

minik_kus = kus()
minik_kus.kimimBen()
minik_kus.ucma()
minik_kus.yuzme()

#minik_kus.gece_gorusu()

print('----')

class baykus(kus):

	def __init__(self):
		super().__init__()
		print('baykus yaratildi')

	def kimimBen(self):
		print('ben bir baykusum')

	def ucma(self):
		print('baykuslar uca bilir')

	def yuzme(self):
		print('baykuslar yuze bilmir')
	
	def gece_gorusu(self):
		print('baykuslar gece gore bilir')

kucuk_baykus = baykus()
kucuk_baykus.kimimBen()
kucuk_baykus.ucma()
kucuk_baykus.yuzme()
kucuk_baykus.gece_gorusu()
