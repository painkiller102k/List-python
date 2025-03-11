import random

word = "Programmeerimine"
word_list = list(word)
print(word_list)
original_list = word_list.copy()

while True:
    print("1 - Loetelu väljastamine")  # Выводим список
    print("2 - Laienda nimekirja")  # Перевернуть список
    print("3 - Leia kirja indeks")  # Найти индекс буквы
    print("4 - Kustutada täht")  # Удалить букву
    print("5 - Prindi nimekirja pikkus")  # Вывести длину списка
    print("6 - Lisa täht")  # Добавить букву
    print("7 - Tühjendage nimekiri")  # Очистить список
    print("8 - loendage konkreetse tähe arvu")  # Посчитать количество определенной буквы
    print("9 - Asendada täht")  # Заменить букву в списке
    print("10 - Nimekirja segamine")  # Перемешать список
    print("11 - Loendi algse järjekorra taastamine") #Восстановить исходный порядок списка
    print("12 - Muuda kõik tähed suureks või väikseks") # Сделать все буквы заглавными или маленькими.
    print("13 - Exit")  # Завершить программу

    choice = input("Valige tegevus: ") #выберите действие
    if choice == "1":
        print(word_list)
    elif choice == "2":
        word_list.reverse()
        print(word_list)
    elif choice == "3":
        while True:
            täht = input("Sisestage täht: ") #введите букву
            try:
                print(word_list.index(täht))
                break
            except ValueError:
                print("Täht ei leitud, proovige uuesti.") #буква не найдена, попробуйте снова
    elif choice == "4":
        while True:
            täht = input("Sisestage täht: ") #введите букву
            try:
                word_list.remove(täht)
                print(word_list)
                break
            except ValueError:
                print("Täht ei leitud, proovige uuesti.") #Буква не найдена, попробуйте снова.
    elif choice == "5":
        print(len(word_list))
    elif choice == "6":
        while True:
            täht = input("Sisestage täht, mida soovite lisada: ") #Введите букву которую хочешь добавить
            a = input("Sisestage positsiooni number: ") #Введите номер позиции
            try:
                word_list.insert(int(a), täht)
                print(word_list)
                break
            except ValueError:
                print("Täht ei leitud, proovige uuesti.") #Буква не найдена, попробуйте снова
    elif choice == "7":
        word_list.clear()
        print(word_list)
    elif choice == "8":
        while True:
            täht = input("Sisestage täht ") #Введите букву
            try:
                print(word_list.count(täht))
                break
            except ValueError:
                print("äht ei leitud, proovige uuesti.") #Буква не найдена, попробуйте снова.
    elif choice == "9":
        while True:
            old = input("Sisestage täht, mida soovite asendada: ") #Введите букву, которую хотите заменить:
            new = input("Sisestage uus täht: ") #Введите новую букву:
            try:
                index = word_list.index(old)
                word_list[index] = new
                print(word_list)
                break
            except ValueError:
                print("Täht ei leitud, proovige uuesti.") #Буква не найдена, попробуйте снова.
    elif choice == "10":
        random.shuffle(word_list)
        print(word_list)
    elif choice == "11":
        word_list = original_list.copy()
        print("Nimekiri on taastatud:", word_list) #Список восстановлен:
    elif choice =="12":
        print("1 - Muuda kõik tähed suureks ")  #все буквы в списке заглавные
        print("2 - Muuda kõik tähed väikseks ")  #все буквы в списке маленькие
        choice2 = input("Valige tegevus: ")  # Выберите действие
        if choice2 == "1":
            word_list = [char.upper() for char in word_list]
        elif choice2 == "2":
            word_list = [char.lower() for char in word_list]
        else:
            print("Vale valik")  # Неверный выбор  
        print(word_list)
    elif choice == "13":
        print("Sa oled programmist väljas!") #Вы вышли из программы
        exit()
    else:
        print("Vale valik") #неверный выбор
        break

print("Программа завершена") 
