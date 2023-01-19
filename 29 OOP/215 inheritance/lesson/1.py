import math

class anasinif:
	pass


class altsinif1(anasinif):
	pass


class altsinif2(anasinif):
	pass


class sekil:

	def __init__(self, renk='kirmizi'):
		self.renk = renk


class daire(sekil):
	
	def __init__(self, yaricap, renk='mavi'):
		super().__init__(renk='renk')
		self.yaricap = yaricap

	def alan(self):
		return math.pi ** self.yaricap ** 2
	

class dikdortgen(sekil):
	
	def __init__(self, kisa=1.0, uzun=1.0, renk='turuncu'):
		super().__init__(renk=renk)
		self.kisa = kisa
		self.uzun = uzun

	def alan(self):
		return self.kisa * self.uzun


class kare(sekil):

	def __init__(self, kenar=1.0, renk='beyaz'):
		super().__init__(renk=renk)
		self.kenar = kenar		

	def alan(self):
		return self.kenar**2

ss = sekil('mor')
print(ss.renk)

dd = daire(5, 'yesil')
print(dd.yaricap)
print(dd.renk)


qq = dikdortgen(kisa=2, uzun=8, renk='sari')
print(qq.renk)
print(qq.alan())


print(isinstance(ss, object))
print(issubclass(kare, sekil))
print(issubclass(sekil, kare))