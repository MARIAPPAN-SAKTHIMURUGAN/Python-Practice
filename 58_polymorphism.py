class Fiber:

    def __init__(self, fiber_id, length, status):
        self.fiber_id = fiber_id
        self.length = length
        self.status = status
        self.length_in_km = length / 1000

    def display(self):
        print("\n--- Fiber Details ---")
        print("Fiber ID:", self.fiber_id)
        print("Length:", self.length, "Meters")
        print("Status:", self.status)
        print("Length in KM:", self.length_in_km)


class FTTx(Fiber):

    def display(self):
        print("\n--- FTTx Fiber ---")
        print("Fiber ID:", self.fiber_id)
        print("Length:", self.length, "Meters")
        print("Status:", self.status)
        print("Length in KM:", self.length_in_km)
        print("Network Type: FTTx")


class Backhaul(Fiber):

    def display(self):
        print("\n--- Backhaul Fiber ---")
        print("Fiber ID:", self.fiber_id)
        print("Length:", self.length, "Meters")
        print("Status:", self.status)
        print("Length in KM:", self.length_in_km)
        print("Network Type: Backhaul")


class Intracity(Fiber):

    def display(self):
        print("\n--- Intracity Fiber ---")
        print("Fiber ID:", self.fiber_id)
        print("Length:", self.length, "Meters")
        print("Status:", self.status)
        print("Length in KM:", self.length_in_km)
        print("Network Type: Intracity")


# Different child objects in one list
fibers = [
    FTTx("E001", 450, "Active"),
    Backhaul("E002", 450, "Active"),
    Intracity("E006", 50, "Active")
]


# Polymorphism
for fiber in fibers:
    fiber.display()
