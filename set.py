my_set = set()
n = int(input("Введите кол-во шагов:"))
for i in range(n):
    user_input = input(f"Шаг {i+1}: ")
    if user_input[0] == '+':
        my_set.add(user_input[2::])
    elif user_input[0] == '-':
        my_set.discard(user_input[2::])
my_set = list(my_set)
my_list = list(map(int,my_set))
my_list.sort()
print(my_list) 
       



    
    

    
    
