import math

class cember:

	def __init__(self, yaricap):
		self.__yaricap = yaricap

	def get_yaricap(self):
		return self.__yaricap

	def set_yaricap(self, yeni_yaricap):
		if yeni_yaricap > 0:
			self.__yaricap = yeni_yaricap
		else:
			print('yaricap pozitif olmali')

	def cevre(self):
		return math.pi * self.__yaricap**2


cember1 = cember(10)
print(cember1.get_yaricap())
print(cember1.cevre())


cember2 = cember(642)
print(cember2.get_yaricap())
print(cember2.cevre())