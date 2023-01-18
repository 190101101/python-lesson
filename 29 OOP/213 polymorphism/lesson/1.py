class kus:

	def __init__(self):
		print('kus yaratildi')

	def kimimBen(self):
		print('ben bir kusum')

	def ucma(self):
		print('kuslar uca bilir')

	def yuzme(self):
		print('kuslar yuze bilir')

class penguen(kus):

	def __init__(self):
		super().__init__()
		print('penguen yaratildi')

	def kimimBen(self):
		print('ben bir penguenim')

	def ucma(self):
		print('penguenler uca bilmir')

	def yuzme(self):
		print('penguenler yuze bilir')
	
	def gece_gorusu(self):
		print('penguenlar gece gore bilir')

		
class baykus(kus):

	def __init__(self):
		super().__init__()
		print('baykus yaratildi')

	def kimimBen(self):
		print('ben bir baykusum')

	def ucma(self):
		print('baykuslar uca bilir')

	def yuzme(self):
		print('baykuslar yuze bilmir')
	
	def gece_gorusu(self):
		print('baykuslar gece gore bilir')


def ucabilirmi(kus):
	kus.ucma()

baykus = baykus()
ucabilirmi(baykus)

print('--')
penguen = penguen()
ucabilirmi(penguen)
