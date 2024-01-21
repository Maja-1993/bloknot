

def input_data():
    name = name_data ()
    surname = surname_data ()
    phone = phone_data ()
    adres = adres_data ()
    var=int(input(f"В каком формате записать данные\n\n"
    f"1 Вариант: \n"
    f"{name}\n{surname}\n{phone}\n{adres}\n\n"
    f"2 Вариант: \n"
    f"{name};{surname};{phone};{adres}\n"
    f"Выберите вариант:"))

    while var !=1 and var !=2:
        print("Неправильный ввод")
        var = int(input("Введите число"))

    if var ==1:
        with open("telef1.csv", "a", encoding="utf-8") as f:
            f.write(f"{name}\n{surname}\n{phone}\n{adres}\n\n")
    elif var ==2:
        with open("telef2.csv", "a", encoding="utf-8") as f:
            f.write(f"{name};{surname};{phone};{adres}\n")


def print_data():
    print("Вывожу данные из 1 файла: \n")
    with open("telef1.csv", "r", encoding="utf-8") as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range (len (data_first)):
            if data_first [i]== "\n" or i == len (data_first)-1:
             data_first_list.append ("".join(data_first[j:i+1]))  
             j=i
        print(data_first_list)

    print("Вывожу данные из 2 файла: \n")
    with open("telef2.csv", "r", encoding="utf-8") as f:
        data_second = f.readlines()
        print(*data_second)

print_data
input_data