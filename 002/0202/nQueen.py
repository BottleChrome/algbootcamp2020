

n = int(input())
row = [0] * n
result = 0
numSet = set(range(n))
flag = [[False]* (2*n) for _ in range(3)]

def check(x, flag) :
  for i in range(x):
    if abs(row[x]-row[i]) == x- i:
      return False
  return True
# def choose(numSet) :
  
        
def nQueen(x, numSet,flag) :
  global result
  if x == n :
    result += 1; # print(row)
  else:
    for i in numSet:
      row[x] = i
      candidate = numSet - {i}
      
      if check(x,flag):
        nQueen(x+1,candidate,flag)

nQueen(0,numSet,flag)
print(result)
# print(numSet)

