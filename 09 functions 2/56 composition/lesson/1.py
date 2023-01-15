import math

def area(radius):
	return math.pi * radius ** 2

def distance(x1, y1, x2, y2):
	dx = x2 - x1
	dy = y2 - y1

	total_cube = dx**2 + dy**2
	return math.sqrt(total_cube)

def area_of_circle_passing_through_two_points(x1, y1, x2, y2):
	p1 = distance(x1, y1, x2, y2)
	p2 = area(p1)
	return p2

def is_even(p1):
	return p1 % 2 == 0

def is_odd(p1):
	return p1 % 2 == 1

print(area_of_circle_passing_through_two_points(1, 6, 4, 10))
print(is_even(10))
print(is_odd(9))