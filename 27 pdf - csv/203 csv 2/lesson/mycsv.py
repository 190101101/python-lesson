import csv

def csv_oku(file_yolu):

	with open(file_yolu, 'r') as dosya:
		filmler = csv.reader(dosya, delimiter=',')

		for film in filmler:
			print(film)

def csv_oku_noktali_virgul(file_yolu_noktali_virgul):

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


def csv_sniffer(file_yolu):
	with open(file_yolu, 'r') as dosya:
		icerik = dosya.read()
		has_reader = csv.Sniffer().has_header(icerik)
		print(has_reader)
		dialect = csv.Sniffer().sniff(icerik)
		print('ayirac: ', dialect.delimiter)