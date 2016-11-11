import random
def pi_cal(m):
	n=0
	for i in range(m):
		x = random.random()
		y = random.random()
		if x**2 + y**2 < 1:
			n+=1
	return 4*(n/m)

if __name__ == '__main__':
	m = int(input("Number of iterations:\n>"))
	print(pi_cal(m))