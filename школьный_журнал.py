
# Создается переменная с учителем и его паролем
teacher_loger = {  
                        'M':'567',
                        'R':'123',
                        'I':'890',
                        'B':'456'
                }

# Создается переменна с ученикоми и их оценками по предметам
class_journal = {
                        'Ivanov Ivan':
                        {
                            'Math':[4],
                            'Rus':[5,5,5,4],
                            'Info':[5,5,5],
                            'Bio':[]
                        },
                        'Petya Petrov':
                        {
                            'Math':[5,5,5],
                            'Rus':[4,4],
                            'Info':[5,3,4],
                            'Bio':[]
                        },
                        'Kirill Kirillov':
                        {
                            'Math':[4,4,5],
                            'Rus':[5,3,3],
                            'Info':[4,4,4,5],
                            'Bio':[]
                        },
                        'Elena Elenovna':    
                        {   
                            'Math':[],
                            'Rus':[],
                            'Info':[],
                            'Bio':[]
                        }                
                }
# Создается переменная со списком предметов
list_subjects = list(list(class_journal.values())[0].keys())

# Создается переменная со списком учеников
list_students = list(class_journal.keys())





#  Создается переменна которая предлагает добавить оценку или вывести топ лучших учеников по предмету
main_menu = "\nВы хотите: \n\t1) Добавить оценку, \n\t2) Ввевести топ лучших учеников по предмету\n\t3) Вывести список учеников"
# Эту переменную выводят
print(main_menu)
# Создается переменная которая дает выбрать первый или второй пункт
choise = input("Введите 1,2 или 3  ")
# Проверка на то что если вы выбрали 1 то запрашивается имя и пароль
if choise == '1':
    login = input("\nВвеидте свое имя: ")
    password = input("Введите пароль: ")
    # Создается переменная в которой хранится индекс предмета


    index_subject = 0
    # Создается флаг который отвечает за успешный вход в аккаунт
    autorized = False
    # Проходится по имени учителей и их паролей

    for loger_login,loger_password in teacher_loger.items():
        # Проверка на то что совпадает ли то имя и пароль что ввел пользователь с тем именем и паролем что хранится в переменной teacher_loger  если да  то флаг становится равным True значит вход в аккаунт прошел успешно и цикл ломается
            if loger_login == login and loger_password == password:
                

                autorized = True
                break
            # К инедксу переменной прибавляется 1
            index_subject += 1
    
    # Проверка на то что правда ли вход прошел успешно и если да то выводит вы вошли как (учитель) , ваш предмет: (список предметов по индексу index_subject), а потом выводит доступных учеников
    if autorized == True:
        print(f"Вы вошли как {login}, ваш предмет: {list_subjects[index_subject]}")
        print("\nДоступны ученики: ")
        for i in range(len(list_students)):
            print(f"\t{i+1}) {list_students[i]}:")
        # Создается переменная где запрашивают имя ученика которому хотят добавить оценку
        name_student = input("\nВведите имя ученика, которому хотите добавить оценку: ")
        #  Создается переменная где запрашивают оценку ученика
        mark_student = int(input("Введите оценку ученика: "))
        # Обращаемся к определенному студенту и к определленному предмет и с помощью append() добавляем оценку
        class_journal[name_student][list_subjects[index_subject]].append(mark_student)
        # Выводит что оценка успешно добавлена и пишет Текущий классный журнал:
        print("\nОценка успешно добавлена!\n\nТекущий классный журнал: ")
        # Проходит по словарю взяв от туда ключи и значения и выводит учеников
        for i,j in class_journal.items():
            print(f"\t{i}:")
            # Проходит по словарю вляв от туда ключи и значения
            for k,l in j.items():
                # Выводит предмет и оценку по нему 
                print(f"\t\t{k}: {l}")
            # Выводит пустую строчку для красоты
            print()
    # Когда была проверка на то что если пользователь прав то заходит в акккаунт а тут иначе вывести такого пользователя нет! 
    else:
        print("Такого пользователя нет!") 
# Иначе если пользователь ввел 2 то вывести вы выбрали второй пункт 
elif choise == '2':
    print("Вы выбрали второй пункт")

    mean_marks_list = []
    for i in range(len(list_subjects)): 
        mean_marks_list.append({}) 

    for i,j in class_journal.items():
        index = 0
        for k,l in j.items():
            # Здесьиспользование if - это тернальный оператор
            # mean_marks_list[index].update({i:(sum(l)/len(l)) if len(l) != 0 else 0})
            if len(l) != 0:
                mean_marks_list[index].update({i:sum(l)/len(l)})
            else:
                mean_marks_list[index].update({i:0})
            index += 1
    
    for i in range(len(list_subjects)):
        for l in range(len(list_students)):
            max_mean_value= -1
            max_mean_key = ""
            for j,k in mean_marks_list[i].items():
                if k > max_mean_value:
                    max_mean_value = k
                    max_mean_key = j
            print(f"\t{l+1}. {max_mean_key} : {max_mean_value}")
            if max_mean_key:
                del mean_marks_list[i][max_mean_key]
            
                                       
             
             


elif choise == '3':
    for i in range(len(list_students)):
        print(f"\t{i+1}. {list_students[i]}")


                
    

# Если пользователь ввел пункт которого нет то говорят Такого пункта нет,будте внимательнее!
else:
    print("Такого пункта нет, будте внимательнее!")



    









    





                




