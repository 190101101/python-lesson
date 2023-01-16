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
def sona_gelindi_mi(satir):
	bitirme_metni = "*** END OF THE PROJECT"
	return satir.startswith(bitirme_metni)

#
def satirdaki_kelimeler(satir):
	satir_kelimeleri = []
	kelime_dizisi = satir.split()
	
	for kelime in kelime_dizisi:
		kelime = kelime.strip(noktalama_isaretleri)
		kelime = kelime.lower()

		#alpha numeric
		if kelime.isalpha() and len(kelime)  > 0:
			satir_kelimeleri.append(kelime)

	return satir_kelimeleri

# 
def kelimeleri_doldur(file, kelimeler):

	for satir in file:
		if not sona_gelindi_mi(satir):
			satir_kelimeler = satirdaki_kelimeler(satir)
			kelimeler.extend(satir_kelimeler)

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

	#
	kelimeleri_doldur(file, kelimeler)

	return kelimeler

#
def liste_sirala(liste, azalan_mi):
	return sorted(liste, reverse=azalan_mi, key = lambda x:len(x))

#
def tekrarlari_sil(liste):
	return list(set(liste))


pride_kelimeleri = kitap_oku('Alice_Adventures')
pride_kelimeleri = liste_sirala(pride_kelimeleri, True)

print(pride_kelimeleri[:20])
print(tekrarlari_sil(pride_kelimeleri[:20]))