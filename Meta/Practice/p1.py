def cheeseburger():
	check = []
	result = []
	answer = []

	with open('input.txt', 'r') as file:
		lines = file.readlines()

	for line in lines[1:]:
		values = line.split()
		buns = (2 * int(values[0])) + (int(values[1]) + 1)
		check.append([buns, int(values[0]) + 2*(int(values[1]))])
		result.append([int(values[2]) + 1, int(values[2])] )

	for i in range(len(result)):
		if result[i][0] <= check[i][0] and result[i][1] <= check[i][1]:
			answer.append('YES')
		else:
			answer.append('NO')

	for i in range(len(answer)):
		print('Case #' + str(i+1) + ': ' + answer[i])

cheeseburger()
