p1 = {
	'brand':'ford',
	'model':'mustang',
	'year':1964,
	'color':'green',
	'price':30000,
	'km':177000,
	'engine':1.6,
}

print(p1.get('color'))
print(p1['color'])

print('color' in p1)
print('color' in p1.keys())
print(1964 in p1.values())