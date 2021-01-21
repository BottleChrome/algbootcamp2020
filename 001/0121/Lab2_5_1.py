# 소수의 개수를 구하는 것은 오랜세월 많은 연구가 이루어져왔습니다. 소수와 관련되어
# 서는 n이 주어졌을 때, n이하의 소수의 개수는 으로 표현하고 있습니다.
# 소수의 개수는  정도까지 계산이 되어져 있습니다. 여기서는 주어진 n에 대하여 n
# 이하의 소수의 개수를 출력하는 프로그램을 작성토록 합니다.
# [입력] n( ≦ )이 주어집니다.
# [출력] n이하의 소수의 개수를 출력합니다.
# [예제]
# 입력 출력
# 1000000 78498

import math
n = int(input())
# 0 ~ 999999
sosu_list = [1 for x in range(n)]
sosu_list[0] = 0
for i in range(2, int(math.sqrt(n))+1):
    for j in range(2*i,n+1,i):
        sosu_list[j-1] = 0
print(sum(sosu_list))





