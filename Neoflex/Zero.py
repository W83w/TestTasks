def func1():
    _dict = input("Введите массив чисел")
    _dict = _dict.split(',')
    c1, c2 = [], []
    for i in _dict:
        if i != '0':
            c1.append(i)  # сюда складываем не нули
        else:
            c2.append(i)  # сюда - нули
    print(*(c1 + c2))




