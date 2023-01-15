#7
def which_day():
	p1 = input("c, ç, p, s harflerden birini secin ")
	
	if not (p1 == 'c' or p1 == 'ç' or p1 == 'p' or p1 == 's'):
		print('yanlis harf', p1, 'harf c, ç, p, s icinde degil ')
	else: 
		if p1 == 's':
			day = 'sali'

		if p1 == 'ç':
			day = 'carshamba'

		if p1 == 'c':
			weekday = input("gun hafta icimi? y/n ")

			if weekday == 'y':
				day = 'cuma'
			else:
				day = 'cumartesi'

		if p1 == 'p':
			weekend = input("gun hafta sonumu? y/n ")
			
			if weekend == 'y':
				day = 'pazar'

			else:
				weekend2 = input("gun hafta basimi? y/n ")

				if weekend2 == 'y':
					day = 'pazartesi'
				else:
					day = 'pershembe'

		print(f"sectiginiz gun {day}")

which_day()

#8
def nums(p1):

	if not p1.isdigit():
		print('tuhaf: cunku sayi girmediniz')
		return

	p1 = int(p1)

	if p1 <= 0:
		print('tuhaf: cunki sayi pozitif deyil')
		return
	else:
		if p1 % 2 == 1:
			print("tuhaf")
		else:
			if 1 <= p1 <= 10:
				print("tuhaf degil - 1-10 arasinda")
			elif 11 <= p1 <= 20:
				print('tuhaf - 11-20 arasinda')
			else:
				print("tuhaf degil - 20 den buyuk")		

nums('10')

