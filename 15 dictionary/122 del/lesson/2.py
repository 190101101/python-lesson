eng_tr = {}
tr_eng = {}

p1 = {
	'brand':'ford',
	'model':'mustang',
	'year':1964,
	'color':'red',
	'price':30000,
	'km':177000,
	'engine':1.6,
}

p1.pop('price')

del p1['km']
del p1['engine']

print(p1)