from abc import ABC, abstractmethod


class Fiber(ABC):

    def __init__(self, fiber_id, length, status):
        self.__fiber_id = fiber_id
        self._length = length
        self.status = status
        self.length_in_km = length / 1000

    def display(self):
        print("\n--- Fiber Details ---")
        print("Fiber ID:", self.__fiber_id)
        print("Length:", self._length, "Meters")
        print("Status:", self.status)
        print("Length in KM:", self.length_in_km)

    @abstractmethod
    def splitter(self):
        pass

    @abstractmethod
    def splitter_print(self):
        pass


class FTTxCity(Fiber):

    def __init__(self, fiber_id, length, status, homepass):
        super().__init__(fiber_id, length, status)
        self.homepass = homepass

    def display(self):
        super().display()
        print("HomePass:", self.homepass)

    def splitter(self):
        self.splitter_required = self.homepass / 4

    def splitter_print(self):
        print(
            "Splitter Requirement based on HomePass:",
            self.splitter_required
        )


class FTTxRural(Fiber):

    def __init__(self, fiber_id, length, status, homepass):
        super().__init__(fiber_id, length, status)
        self.homepass = homepass

    def display(self):
        super().display()
        print("HomePass:", self.homepass)

    def splitter(self):
        self.splitter_required = self.homepass / 2

    def splitter_print(self):
        print(
            "Splitter Requirement based on HomePass and distance in Rural:",
            self.splitter_required
        )


# Create different fiber objects
fibers = [
    FTTxCity("E001", 780, "IPL", 1600),
    FTTxRural("E002", 780, "IPL", 9800)
]


# Polymorphism + Abstraction
for fiber in fibers:
    fiber.display()
    fiber.splitter()
    fiber.splitter_print()
