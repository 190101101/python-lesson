class nokta:

	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def __str__(self):
		return f'bu bi noqtedir. kordinatlar: x:{self.x} - y:{self.y}' 

p1 = nokta(2,5)
# p2 = nokta(-1,4)


print(p1.__str__())
print(nokta.__name__)