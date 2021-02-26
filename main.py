# coding: utf-8
from parking import Parking


__author__ = 'Eric-Nicolas'


def main() -> None:
    print("Welcome to the level -1, what do you want to do?")

    parking = Parking(27)

    if parking.is_available(3):
        print("The emplacement n°3 is available.\n")
    else:
        print("The emplacement n°3 is not available.\n")

    parking.place_vehicle(0)
    parking.show_emplacements()


if __name__ == '__main__':
    main()
