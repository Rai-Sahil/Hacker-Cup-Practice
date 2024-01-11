def spiral(row, col):
	if row == col:
		return row * col - (row - 1)
	elif row < col:
		# right half side
		if col % 2 == 0:
			return col * col - (row - 1)
		else:
			return (col - 1) * (col - 1) + row
	else:
		if row % 2 != 0:
			return row * row - (col - 1)
		else:
			return (row - 1) * (row - 1) + col

points = []

for _ in range(int(input().strip())):
    line = input().strip().split()
    points.append([int(line[0]), int(line[1])])


for col, row in points:
	print(spiral(row, col))
