def getMaxDays(a, N , maxWeight):
	
	matrix = [[0] * (maxWeight + 1) for i in range(N + 1)]
	
	for i in range(1, maxWeight + 1):
		matrix[0][i] = 0
	for i in range(N+1):
		matrix[i][0] = 1
	
	for i in range(1, N+1):
		for j in range(1, maxWeight + 1):
			if a[i-1] <= j:
				matrix[i][j] = matrix[i-1][j] + matrix[i-1][j-a[i-1]]
			else:
				matrix[i][j] = matrix[i-1][j]
	
	return matrix[N][maxWeight]



N,maxWeight = map(int, input().split())
a = list(map(int, input().split()))
print(getMaxDays(a, N, maxWeight))