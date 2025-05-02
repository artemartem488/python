














count = 0
summa = 0

n = int(input())
for i in range(n):

    temp = int(input())
    if temp >= 0:
        summa += temp
        count += 1
print(summa / count)
print(count)
        
