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


#
makaroni = Penguen('makaroni', 8, 'sari siyah')
print(makaroni.yuzme())
print(makaroni.sarki_soyle(True))

print('-------')
#
neseli_ayaklar = Penguen('neseli_ayaklar', 1, 'gri papyon')
print(neseli_ayaklar.yuzme())
print(neseli_ayaklar.sarki_soyle(False))
print(neseli_ayaklar.dans(True))
