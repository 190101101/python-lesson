class Penguen:
	tur = 'kus'

	def __init__(self, ad, yas, renk):
		self.ad = ad
		self.yas = yas
		self.renk = renk

kral = Penguen('kral', 4, 'turuncu')
sari_goz = Penguen('sari goz', 1, 'kahve')

print(kral.ad)
print(kral.yas)
print(kral.renk)
print(kral.__class__.tur)
