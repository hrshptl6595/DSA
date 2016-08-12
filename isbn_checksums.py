def checksums(n):
	temp = n
	i=2
	s=0
	while (temp>0):
		s+=((temp%10)*i)
		temp = temp//10
		i = i + 1

	isbn = str(n)+str(11 - s%11)
	return isbn

n = int(input("Enter a number to check\n>"))
print("ISBN: ",checksums(n))