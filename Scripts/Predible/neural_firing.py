def neural(seq):
    count = []
    for x in seq:
        c = 0
        for i in range(len(x)):
            if x[i] == '1':
                for j in range(i+1,len(x)):
                    if x[j] == '0':
                        c = c+1
                    else:
                        break
        count.append(c)
    return count

n = int(input(""))
s = []
for i in range(n):
    s.append(input())
out = neural(s)
for i in out:
    print(i)