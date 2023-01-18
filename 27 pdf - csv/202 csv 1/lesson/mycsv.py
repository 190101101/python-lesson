import csv

file_yolu = '../../../00 bin/docs/data/movie.csv'
file_yolu_noktali_virgul = '../../../00 bin/docs/data/movie_dotted.csv'

def csv_oku():

	with open(file_yolu, 'r') as dosya:
		filmler = csv.reader(dosya, delimiter=',')

		for film in filmler:
			print(film)

def csv_oku_noktali_virgul():

	with open(file_yolu_noktali_virgul, 'r') as dosya:
		filmler = csv.reader(dosya, delimiter=';')

		for film in filmler:
			print(film)


def csv_oku_dilect():
	csv.register_dialect('normal_okuma', delimiter=',', quoting=csv.QUOTE_NONE)
	# csv.register_dialect('normal_okuma', delimiter=',', quoting=csv.QUOTE_MINIMAL)

	with open(file_yolu, 'r') as dosya:
		filmler = csv.reader(dosya, dialect='normal_okuma')

		for film in filmler:
			print(film)
