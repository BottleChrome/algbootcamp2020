# N개의 자연수가 있는 수열이 주어졌을 때, 두 번째로 작은 수를 찾는 프로그램을 작성
# 합니다. 중복된 숫자가 제일 작은 수인 경우, 두 번째로 작은 숫자는 그 숫자보다 커야
# 합니다.
# 예를 들어서 10개의 자연수가 다음과 같이 주어집니다.
# 4 3 2 7 5 2 3 6 9 10
# 이 경우 2가 제일 작은 수인데, 중복되어 있습니다. 그 다음 작은 수는 3이 됩니다.
# 그래서 두 번째로 작은 수는 3이 됩니다.
# [입력]
# 첫 번째 줄에 수일의 길이 N이 주어집니다. ( ≦ ≦ )
# 두 번째 줄에 N개의 자연수 수열값이 주어집니다. ( ≦  ≦ )
# [출력]
# 두 번째로 작은 수를 출력합니다.
# [예제]
# 입력 출력
# 10
# 4 3 2 7 5 2 3 6 9 10 3

n = int(input())
array = list(map(int, input().split()))

array.sort()
i = 0
while array[i] == array[0]:
    i += 1
print(array[i])    

min = array[0]
lmin = array[0] + array[1]
for a in array :
    if a < min :
        lmin = min
        min = a
    elif (a < lmin) & (a > min):
        lmin = a 

print(lmin)


