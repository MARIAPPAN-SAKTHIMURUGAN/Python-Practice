class Fiber:
    # Class variables
    total_fibers = 0
    network_type = "FTTH"

    def __init__(self, fiber_id, length=0, status="Unknown"):
        # Instance variables
        self.fiber_id = fiber_id
        self.length = length
        self.status = status

        # Count every Fiber object created
        Fiber.total_fibers += 1

    def display(self):
        print("\nFiber ID:", self.fiber_id)
        print("Length:", self.length, "Meters")
        print("Status:", self.status)
        print("Length in KM:", self.length / 1000)

    def dark(self):
        self.status = "Dark"

    def add_completed_footage(self, extra_footage):
        self.length += extra_footage

    def update_footage_status(self, length, status):
        self.length = length
        self.status = status


# Creating Fiber objects
fiber1 = Fiber("F001", 450, "Active")
fiber2 = Fiber("F002", 950)
fiber3 = Fiber("F003", status="Active")

# Display class variable
print("Network Type:", Fiber.network_type)

# Change class variable
Fiber.network_type = "FTTx"

print("Updated Network Type:", Fiber.network_type)

# Modify instance variables
fiber3.length = 250
fiber2.status = "Dark"

# Use instance methods
fiber1.dark()
fiber1.add_completed_footage(400)

fiber2.update_footage_status(900, "IPL")

# Display fiber information
fiber1.display()
fiber2.display()
fiber3.display()

# Display total objects created
print("\nTotal Fibers:", Fiber.total_fibers)

# Display instance variables
print("\nFiber1 Instance Variables:")
print(fiber1.__dict__)

print("\nFiber2 Instance Variables:")
print(fiber2.__dict__)

print("\nFiber3 Instance Variables:")
print(fiber3.__dict__)
