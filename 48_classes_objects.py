class Fiber:
    def __init__(self, fiber_id, length, status):
        self.fiber_id = fiber_id
        self.length = length
        self.status = status

    def display(self):
        print("\nFiber ID:", self.fiber_id)
        print("Length:", self.length, "Meters")
        print("Status:", self.status)


fiber1 = Fiber("F001", 450, "Active")
fiber2 = Fiber("F003", 950, "Active")

fiber1.display()
fiber2.display()
