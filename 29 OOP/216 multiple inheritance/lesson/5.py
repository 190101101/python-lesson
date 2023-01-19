#
class a:

	def __init__(self, text1):
		self.__text1 = text1

	def a_set(self, text1):
		self.__text1 = text1

	def a_get(self):
		return self.__text1

#	
class b(object):
	
	def __init__(self, text2):
		self.b_set(text2)

	def b_set(self, text2):
		self.text2 = text2

	def b_get(self):
		return self.text2

#	
class c(a, b):

	def __init__(self, text1, text2):
		a.__init__(self, text1)
		b.__init__(self, text2)

qq = c('text a', 'text b')
print(qq.a_get())
