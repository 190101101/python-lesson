
class a:

	def __init__(self, text1):
		self.__text1 = text1

	def text1(self):
		return self.__text1


#
class b(object):

	def __init__(self, text2):
		self.text2(text2)

	def text2(self, text2):
		self.text2 = text2

	def text22(self):
		return self.text2


#
class c(a, b):
	def __init__(self, text1, text2):
		a.__init__(self, text1)
		b.__init__(self, text2)

tt = c('text1','text2')
print(tt.text1())
print(tt.text22())
