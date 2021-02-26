# coding: utf-8

__author__ = 'Eric-Nicolas'


class Parking:
    def __init__(self, length: int) -> None:
        self._LENGTH = length
        self._AVAILABLE = 'A'
        self._VEHICLE = 'V'  # contains a vehicle
        self._DISABLED = 'D'  # for disabled people

        self.emplacements = []

        for i in range(self._LENGTH):
            if i < 15:
                self.emplacements.append(self._AVAILABLE)
            elif i < 25:
                self.emplacements.append(self._VEHICLE)
            else:
                self.emplacements.append(self._DISABLED)

    def is_available(self, index: int) -> bool:
        if index < 0 or index >= self._LENGTH:
            raise IndexError
        return self.emplacements[index] != self._VEHICLE

    def place_vehicle(self, index: int) -> None:
        if index < 0 or index >= self._LENGTH:
            raise IndexError
        self.emplacements[index] = self._VEHICLE

    def show_emplacements(self) -> None:
        for i in range(self._LENGTH):
            if self.is_available(i):
                print("The emplacement n°" + str(i) + " is available.")
            else:
                print("The emplacement n°" + str(i) + " is not available.")
