# 소수의 개수를 구하는 것은 오랜세월 많은 연구가 이루어져왔습니다. 소수와 관련되어
# 서는 n이 주어졌을 때, n이하의 소수의 개수는 으로 표현하고 있습니다.
# 소수의 개수는  정도까지 계산이 되어져 있습니다. 여기서는 주어진 n에 대하여 n
# 이하의 소수의 개수를 출력하는 프로그램을 작성토록 합니다.
# [입력] n( ≦ )이 주어집니다.
# [출력] n이하의 소수의 개수를 출력합니다.
# [예제]
# 입력 출력
# 1000000 78498

n = int(input())

sosu_list = []
for i in range(1, n+1 ):
    isin = True
    for j in range(2,i):
        if i % j == 0 :
            isin = False
    if isin :
        sosu_list.append(i)
print(len(sosu_list))





