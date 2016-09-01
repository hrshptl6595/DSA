def ramanujan(n):
	for i in range(int(pow(n,1/2))):
		for j in range(i):
			for k in range(j):
				for l in range(k):
					if ((i*i*i+j*j*j) == (k*k*k+l*l*l) and ((i*i*i)+(j*j*j))<=n):
						print(i*i*i+j*j*j)

n = int(input("Enter a number\n>"))
print(ramanujan(n))