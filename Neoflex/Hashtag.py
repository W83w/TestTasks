def func2(a='Hello there thanks for trying my Kata'):
    a = str(input("Введите тег"))
    if a != None:
        uppend_ = []
        if type(a) == str:
            a = a.split()
            for i in a:
                i1 = i[0].upper()
                uppend_.append(i1 + i[1:])
        else:
            print("Что то не то")

        uppend_string = ''
        for el in uppend_:
            uppend_string += el
        print(f"#{uppend_string}")
    else:
        print("Что-то не так")


