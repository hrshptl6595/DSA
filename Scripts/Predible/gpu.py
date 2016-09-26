import heapq
a = input()
s = a.split()
x = int(s[0])
y = int(s[1])
g = []
for i in range(x):
    g.append(input())
gpu = []
for i in g:
    temp = i.split()
    t2 = []
    for j in temp:
        t2.append(int(j))
    gpu.append(t2)

def smallest(lists):
    minRange=float("inf")
    minListIndex=0
    maxList=0
    minimum=float("inf")
    maximum=0
    index=0
    localMinRange=0
    inRange=[]
    for i in range(0,len(lists)):
        inRange.append(lists[i][0])
        if(lists[i][0]<minimum):
            minimum=lists[i][0]
            minListIndex=i
        if(lists[i][0]>maximum):
            maximum=lists[i][0]

    minRange=maximum-minimum
    minList=[]
    
    index=lists[minListIndex].index(minimum)
    while True:
        index=lists[minListIndex].index(minimum)
        if index+1>len(lists[minListIndex])-1:
            break
        else:
            inRange.insert(minListIndex,lists[minListIndex][index+1])
            inRange.remove(lists[minListIndex][index])
            
            minListIndex=inRange.index(min(inRange))
            
            minimum=min(inRange)
            localMinRange=(max(inRange)-min(inRange))
            if localMinRange<minRange:
                minRange=localMinRange
                minList=inRange
            
            #print inRange
            
    output=[min(minList),max(minList)]
    return output
range = smallest(gpu)
print(range[0],range[1])