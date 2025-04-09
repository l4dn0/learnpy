list_cords = []
unlist_cords = []

def enter_coordinates():
    def in_area(x, y):
        if -1 <= x <= 1 and 0 <= y <= 2:
            if not(y <= 1 and x ** 2 + y ** 2 <= 1):
                return True
        return False

    x, y = map(float, input("\nВведите два числа - значения x и y через пробел (разделитель дробной части - запятая): ").split())
    if in_area(x, y):
        print("Точка попадает в область!\n")
        if len(list_cords) == 0:
            list_cords.append([x, y])
        else:
            for i in range(len(list_cords)):
                if list_cords[i][0] != x and list_cords[i][1] != y:
                    list_cords.append([x, y])
        return True
    else:
        print("Точка не попадает в область!\n")
        unlist_cords.append([x, y])
        return False


def get_count_cords():
    return len(list_cords)

def print_list():
    print("\n")
    print(list_cords)
    print("\n")