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

    def length_km1(self):
        return self.length / 1000

    def dark(self):
        self.status = "Dark"

    def add_completed_footage(self, extra_footage):
        self.length += extra_footage

    def update_footage_status(self, length, status):
        self.length = length
        self.status = status
        print("\nUpdated Footage:", self.length, self.status)


fiber1 = Fiber("F001", 450, "Active")
fiber2 = Fiber("F002", 950)
fiber3 = Fiber("F003", status="Active")

fiber3.length = 250
fiber2.status = "Dark"

fiber1.dark()
fiber1.add_completed_footage(400)

fiber2.update_footage_status(900, "IPL")

fiber1.display()
fiber2.display()
fiber3.display()

print("\nFiber1 Length in KM:", fiber1.length_km1())
print("\nFiber1 Length:", fiber1.length)
print("\nFiber1 Instance Variables:", fiber1.__dict__)
print("\nFiber2 Instance Variables:", fiber2.__dict__)
