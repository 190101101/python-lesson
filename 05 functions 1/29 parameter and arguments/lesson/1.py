import math

def p1():
	print('first function')

p1()

def user_name(name):
	print(f"name: {name}")

def user_age(age):
	print(f"age: {age}")

def user_info(name, age):
	user_name(name)
	user_age(age)

user_info('cookie', 6)

print(type(user_info))