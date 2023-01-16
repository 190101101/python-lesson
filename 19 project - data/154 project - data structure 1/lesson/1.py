import string
from collections import Counter

#
noktalama_isaretleri = string.punctuation
bosluk_karakterleri = string.whitespace

#
def dosyadan_oku(kitap_adi):
	return open(f"../../../00 library/docs/book/{kitap_adi}.txt", encoding='UTF-8')

#
def baslangici_atla(file):
	atlama_metni = "*** START OF THE PROJECT"	

	for satir in file:
		if satir.startswith(atlama_metni):
			break

#
def kitap_oku(kitap_adi):
	"""
	verilen kitaba gore ilgili kitapi okur
	return list kelimeler
	"""
	#kelimeleri tutalim
	kelimeler = list()

	#once file olarak okuyalim
	file = dosyadan_oku(kitap_adi)

	#shimdi [*** START OF THE PROJECT] gorunce atla
	baslangici_atla(file)


kitap_oku('Pride_and_Prejudice')
