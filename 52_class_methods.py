class Fiber:
    # Class variables
    total_fibers = 0
    network_type = "FTTH"

    def __init__(self, fiber_id, length=0, status="Unknown"):
        # Instance variables
        self.fiber_id = fiber_id
        self.length = length
        self.status = status

        # Count every Fiber object
        Fiber.total_fibers += 1

    # Class method to display network type
    @classmethod
    def show_network_type(cls):
        print("\nNetwork Type:", cls.network_type)

    # Class method to change network type
    @classmethod
    def change_network_type(cls, new_value):
        cls.network_type = new_value
        print("Updated Network Type:", cls.network_type)

    # Alternative constructor
    @classmethod
    def from_string(cls, data):
        fiber_id, length, status = data.split(",")
        return cls(fiber_id, int(length), status)

    # Instance method
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

# Class method
Fiber.show_network_type()

# Change class variable using class method
Fiber.change_network_type("FTTx")

# Modify instance variables
fiber3.length = 250
fiber2.status = "Dark"

# Instance methods
fiber1.dark()
fiber1.add_completed_footage(400)

fiber2.update_footage_status(900, "IPL")

# Display Fiber information
fiber1.display()
fiber2.display()
fiber3.display()

# Total objects
print("\nTotal Fibers:", Fiber.total_fibers)

# Alternative constructor
fiber4 = Fiber.from_string("F004,850,Active")

print("\nFiber created using class method:")
fiber4.display()

# Total after creating fiber4
print("\nTotal Fibers:", Fiber.total_fibers)
