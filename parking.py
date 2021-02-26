# coding: utf-8

__author__ = 'Eric-Nicolas'


class Parking:
    def __init__(self) -> None:
        self._LENGTH = 27
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
        self._DEFAULT = self.emplacements

    @property
    def length(self) -> int:
        return self._LENGTH

    def is_available(self, index: int) -> bool:
        if index < 0 or index >= self._LENGTH:
            raise IndexError
        return self.emplacements[index] != self._VEHICLE

    def place_vehicle(self, index: int) -> None:
        if index < 0 or index >= self._LENGTH:
            raise IndexError
        elif self.emplacements[index] == self._VEHICLE:
            print("This emplacement is already occupied!")
            return
        self.emplacements[index] = self._VEHICLE

    def retrieve_vehicle(self, index) -> None:
        if index < 0 or index >= self._LENGTH:
            raise IndexError
        elif self.emplacements[index] != self._VEHICLE:
            print("This emplacement is already available!")
            return
        self.emplacements[index] = self._DEFAULT[index]

    def show(self) -> None:
        info = ''
        for i in range(self._LENGTH):
            info += "E. n°" + str(i) + " status : " + self.emplacements[i]
            if (i + 1) % 3 == 0:
                info += '\n'
            else:
                info += '\t'
        print(info)
