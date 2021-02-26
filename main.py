# coding: utf-8
from parking import Parking


__author__ = 'Eric-Nicolas'


def get_number_safely(prompt: str, a: int, b: int) -> int:
    number = -1
    while number == -1:
        number = input(prompt)
        try:
            number = int(number)
            if number < a or number > b:
                raise ValueError
        except ValueError:
            print("Please enter a number between " + str(a) + " and " + str(b) + "!\n")
            number = -1
    return number


def main() -> None:
    parking = Parking()
    while True:
        print("Welcome to the level -1, what do you want to do?")
        print("1: Place a vehicle")
        print("2: Retrieve a vehicle\n")

        user_choice = get_number_safely("Enter the digit 1 or 2: ", 1, 2)

        if user_choice == 1:
            emplacement = get_number_safely("Select the emplacement where you want to place the vehicle : ", 0, parking.length - 1)
            parking.place_vehicle(emplacement)
        else:
            emplacement = get_number_safely("Select the emplacement where you want to retrieve the vehicle : ", 0, parking.length - 1)
            parking.retrieve_vehicle(emplacement)

        print()
        parking.show()
        print()


if __name__ == '__main__':
    main()
