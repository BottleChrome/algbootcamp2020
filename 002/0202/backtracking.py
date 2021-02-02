def backtracking(varr, current, n, k) :
  if current == k :
    s = " "
    for i in range(k):
      s += str(varr[i]) + ' '
    print(s)
    return

  for i in range(1, n+1):
    isOK = True
    for j in range(current) :
      if i == varr[j] :
        isOK = False
        break
    if not isOK : continue
    varr[current] = i
    backtracking(varr, current+1, n, k )

n , k = map(int, input().split())
varr = [0] * k
backtracking(varr, 0 , n , k)

