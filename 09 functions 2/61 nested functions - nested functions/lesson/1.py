def common_floor(p1):

	def p5x(p1):
		if p1 % 5 == 0:
			return True
		else:
			return False

	def p8x(p1):
		if p1 % 8 == 0:
			return True
		else:
			return False

	if p5x(p1) and p8x(p1):
		return True
	else:
		return False

print(common_floor(10))
print(common_floor(40))
print(common_floor(120))