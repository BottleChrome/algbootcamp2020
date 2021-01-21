

answer = 0 
yaksu_list = []

count = 0
for i in range(1,int(math.sqrt(n))+1):
    if i * i == n : 
        count += 1
        yaksu_list.append(i)
    elif n % i == 0 :
        count += 2
        yaksu_list.append(i)
        yaksu_list.append(int(n/i))

print(sum(yaksu_list))