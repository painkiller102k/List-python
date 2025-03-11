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
    print("12 - Exit")  # Завершить программу

    choice = input("Выберите действие: ")
    if choice == "1":
        print(word_list)
    elif choice == "2":
        word_list.reverse()
        print(word_list)
    elif choice == "3":
        while True:
            täht = input("Введите букву: ")
            try:
                print(word_list.index(täht))
                break
            except ValueError:
                print("Буква не найдена, попробуйте снова.")
    elif choice == "4":
        while True:
            täht = input("Введите букву: ")
            try:
                word_list.remove(täht)
                print(word_list)
                break
            except ValueError:
                print("Буква не найдена, попробуйте снова.")
    elif choice == "5":
        print(len(word_list))
    elif choice == "6":
        while True:
            täht = input("Введите букву которую хочешь добавить: ")
            a = input("Введите номер позиции: ")
            try:
                word_list.insert(int(a), täht)
                print(word_list)
                break
            except ValueError:
                print("Буква не найдена, попробуйте снова.")
    elif choice == "7":
        word_list.clear()
        print(word_list)
    elif choice == "8":
        while True:
            täht = input("Введите букву: ")
            try:
                print(word_list.count(täht))
                break
            except ValueError:
                print("Буква не найдена, попробуйте снова.")
    elif choice == "9":
        while True:
            old = input("Введите букву, которую хотите заменить: ")
            new = input("Введите новую букву: ")
            try:
                index = word_list.index(old)
                word_list[index] = new
                print(word_list)
                break
            except ValueError:
                print("Буква не найдена, попробуйте снова.")
    elif choice == "10":
        random.shuffle(word_list)
        print(word_list)
    elif choice == "11":
        word_list = original_list.copy()
        print("Список восстановлен:", word_list)
    elif choice == "12":
        print("Вы вышли из программы")
        exit()
    else:
        print("Неверный выбор")
        break

print("Программа завершена")
