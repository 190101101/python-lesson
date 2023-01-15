eng_tr = {}
tr_eng = {}

p1 = {
	'brand':'ford',
	'model':'mustang',
	'year':1964,
}

p2 = {'color':'red'}
p2 = {'price':30000}
p2 = {'km':177000}
p2 = {'engine':1.6}

p1.update(p2)
print(p1)