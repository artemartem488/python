
















arr = list(map(int,input('Введите список через пробел').split()))


n = len( arr)



for i in range(n):
    swapped = False
    for j in range(0,n-i-1):
        if  arr[j] >  arr[j+1]:
            arr[j], arr[j+1] =  arr[j+1], arr[j]
            swapped = True
    if not swapped:
        break

print('Отсортированный список:', arr)




# print( arr) - в теле первого for чтоб выводить каждый раз как список изменяется














