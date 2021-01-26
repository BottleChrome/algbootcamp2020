



n = int(input())
array = tuple(map(int, input().split()))
sumList = []
sum = 0 
for a in array :
    sum += a
    sumList.append(sum)


k = int(input())
result = [ ]
for i in range(k) :
    start , end = list(map(int, input().split()))
    print(sumList[end-1] - sumList[start-1])
