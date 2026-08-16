class Fiber:
    def __init__(self, fiber_id, length=0, status="Unknown"):
        self.fiber_id = fiber_id
        self.length = length
        self.status = status
        self.length_km = length / 1000

    def display(self):
        print("\nFiber ID:", self.fiber_id)
        print("Length:", self.length, "Meters")
        print("Status:", self.status)
        print("Length in KM:", self.length_km)


fiber1 = Fiber("F001", 450, "Active")
fiber2 = Fiber("F002", 950)
fiber3 = Fiber("F003", status="Active")

fiber1.display()
fiber2.display()
fiber3.display()
