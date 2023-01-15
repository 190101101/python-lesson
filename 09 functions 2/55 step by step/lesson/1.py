import math

def distance(x1, y1, x2, y2):
	dx = x2 - x1
	dy = y2 - y1
	print(f"dx: {dx}")
	print(f"dy: {dy}")

	total_cube = dx**2 + dy**2
	print(f"total cube: {total_cube}")
	return math.sqrt(total_cube)

print(distance(2, 6, 10, 21))