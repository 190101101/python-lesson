class a:

	def __init__(self, text1):
		self.__text1 = text1

	def set_text1(self, text1):
		self.__text1 = text1

	def get_text1(self):
		return self.__text1


class b(object):

	def __init__(self, text2):
		self.set_text2(text2)

	def set_text2(self, text2):
		self.text2 = text2

	def get_text2(self):
		return self.text2

class c(a, b):

	def __init__(self, text1, text2):
		a.__init__(self, text1)
		b.__init__(self, text2)


cc = c('c class text 1 from a class', 'c class text 2 from b class')
print(cc.get_text1())
print(cc.get_text2())
