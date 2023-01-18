import csv


def csv_kopyala(file_yolu):
	yeni_file_yolu = '../../../00 bin/docs/data/copymovie.csv'

	open(yeni_file_yolu, 'x')

	with open(file_yolu, 'r') as movies, open(yeni_file_yolu, 'a', newline='') as movies_c:
		filmler = csv.reader(movies)
		writer = csv.writer(movies_c, quoting=csv.QUOTE_ALL)

		for film in filmler:
			writer.writerow(film)