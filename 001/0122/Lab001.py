# 하노이 탑은 세 개의 기둥을 가지고, 크기가 큰 원반부터 작은순으로 쌓여 있는 탑입니
# 다. 하노이 탑의 윈반들을 현재 기둥에서 옆의 기둥으로 옮기고자 합니다. 원반은 한
# 번에 하나씩 옮길 수 있고, 반드시 기둥에 원반을 넣어야 합니다. 또한 작은 원반 위에
# 큰 원반이 놓일 수 없습니다.
# 원반의 개수가 주어졌을 때, 왼쪽 기둥에 있는 원반들을 가운데 기둥으로 옮길 때, 최소
# 횟수로 원반을 옮길 때, 그 횟수를 구하고자 합니다.
# [입력] 원반의 개수 n이 주어집니다. ( ≦  ≦ )
# [출력] n개의 원반을 최소한으로 옮기는 횟수를 출력합니다..
# [예제]
# 입력 출력
# 5 1




def hanoi(n,k) :
    k -= 1
    if k == 0 :
        return n
    if n == 0 :
        return
    if n == 1 :
        return 1
    else :
        hanoi(n+1)
    
    if n == 1: return 1 
    else :
        print(2 * hanoi(n-1) + 1)
        return 2 * hanoi(n-1) + 1
n = 32
k = int(input())
print(hanoi(n))



