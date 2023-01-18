import csv

eklenecek_filmler = ['253', 'The Shawshank Redemption', '1994', 'R', '14 Oct 1994', '142 min', 'Crime, Drama', 'Frank Darabont', 'Stephen King (short story "Rita Hayworth and Shawshank Redemption"), Frank Darabont (screenplay)', 'Tim Robbins, Morgan Freeman, Bob Gunton, William Sadler', 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.', 'English', 'USA', 'Nominated for 7 Oscars. Another 19 wins & 30 nominations.', 'https://images-na.ssl-images-amazon.com/images/M/MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE@._V1_SX300.jpg', 'Internet Movie Database', '9.3/10', '80', '9.3', '1,825,626', 'tt0111161', 'movie', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'http://www.rottentomatoes.com/m/shawshank_redemption/', '27 Jan 1998', 'N/A', 'Columbia Pictures', 'N/A', 'True']

def csv_yazma(file_yolu):
	with open(file_yolu, 'a') as dosya:
		writer = csv.writer(dosya, delimiter=',', quoting=csv.QUOTE_ALL)
		writer.writerow(eklenecek_filmler)
