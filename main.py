def in_area(x, y):
    if -1 <= x <= 1 and 0 <= y <= 2:
        if y <= 1 and x ** 2 + y ** 2 <= 1:
            return True
    else: return False


x, y = map(float, input("Введите два числа - значения x и y через пробел (разделитель дробной части - запятая): ").split())

