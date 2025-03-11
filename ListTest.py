from random import randint

a="Programmeerimine"
print(a)
a_list =list(a)
print(a_list)
a_list.reverse() # переворачивает список
print(a_list)
print(a_list.index("P")) # ищет букву в списке и возвращает ее индекс
print(len(a_list)) # длина списка
print(len(a)) # длина строки

a_list.remove("m") # удаляет букву из списка   
print(a_list)

kogus=a_list.count("m") # считает количество букв в списке
for m in range(kogus):
    a_list.remove("m") # удаляет букву из списка

tähed=randint(1,22)
for i in range(tähed):
    while 1:
        try:
            t=input("Sisesta täht: ")
            if t.isalpha():
                break
        except:
                print("On vaja täht")
    print(a_list)
    tähed=randint(1,10)
    for i in range(tähed):
        while 1:
            try:
                ind=input("Sisesta indeks: ")
                if ind.isnumeric() & int(ind)<len(a_list):
                    break
            except:
                print("On vaja indeks")
                a_list.insert(int(ind),t) # вставляет букву в список
                print(a_list)
def funktsioon(e):
    return len(e)
    a_list.sort(reverse=True, key=funktsioon) # сортирует список по длине элементов
    print(a_list)