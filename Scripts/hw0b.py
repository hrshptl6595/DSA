#BT3051 Assignment 0b
#Roll number: ED13B045
#Time: 0:13

n = int(input("Enter a number\n>"))

def check_print(x):
	if (x%2 == 0):
		print(x//2)
		check_print(x//2)
	else:
		if(x==1):
			return x
		else:
			print(3*x+1)
			check_print(3*x+1)

check_print(n)