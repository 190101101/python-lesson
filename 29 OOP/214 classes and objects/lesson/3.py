class ogrenci:

	def __init__(self, isim, yas, sinif):
		self.isim = isim
		self.yas = yas
		self.sinif = sinif


ogr = ogrenci('kuki', 6, '3-a')
print(ogr.isim)
print(ogr.yas)
print(ogr.sinif)

del ogr.sinif

#print(ogr.sinif)
