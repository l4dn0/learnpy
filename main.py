from funcs import enter_coordinates
from funcs import get_count_cords
from funcs import print_list

def main():
    while True:
        command = int(input("""выберите команду:
    0 - завершить программу
    1 - ввести координаты точки
    2 - вывести количество точек, которые попали в заданную область
    3 - вывести координаты точек, которые не попали в заданную область
    4 - стереть из памяти до этого введёные координаты точек
-> """))
        match command:
            case 0:
                exit()
            case 1:
                enter_coordinates()
            case 2:
                print(f"\n{get_count_cords()} - количество входящих в область точек.\n")
            case 3:
                print_list()


if __name__ == "__main__":
    main()