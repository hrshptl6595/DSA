def delta(s,t):
	if s==t:
		return 0
	else:
		return 1
def EditDistanceRec(s,t):
	if len(s)==0:
		return len(t)
	elif len(t)==0:
		return len(s)
	else:
		return min(EditDistanceRec(s[:-1],t[:-1])+delta(s[-1],t[-1]),EditDistanceRec(s,t[:-1])+1, EditDistanceRec(s[:-1],t)+1)

print(EditDistanceRec("ACGAAC", "CGACAT"))