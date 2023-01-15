#1
def hello():
	print('hello world')

hello()

#2
def say_hello(name1, name2):
	print(f"hello {name1} and {name2}")

say_hello('cookie', 'apsi')

#3
def hello_user(user):
	print(f"hello {user}")

hello_user('cookie')

#4
def max_num(p1, p2, p3):
	print(max(p1, p2, p3))

max_num(10, 11, 6)


#5
def text_to_strip_and_lower(text):
	return text.strip(' ').lower()

print(text_to_strip_and_lower('Hello my name is Cookie'))

#6
def mult(p1, p2):
	return p1 + p2

print(mult(10, 11))

#7
def difference(p1, p2, p3):
	return min(abs(p1), abs(p2), abs(p3))

print(difference(13, 9, 12))

#8
import math
def square_fragrance(p1):
	return math.sqrt(p1)

print(square_fragrance(10))

#9
def func_log(p1):
	return math.log(p1)

print(func_log(10))

#10
def hypotenuse(p1, p2):
	return math.sqrt(p1 ** 2 + p2 ** 2)

print(hypotenuse(7, 24))