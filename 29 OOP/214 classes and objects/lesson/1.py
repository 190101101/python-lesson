class araba:
	"""
	bu araba classidir
	"""
	marka = 'bmw'

	def calisma(self):
		print('bu araba calisiyor')


print(araba.marka)
print(araba.__doc__)

p1 = araba()
p1.calisma()
