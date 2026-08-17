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

    # Class method
    @classmethod
    def show_network_type(cls):
        print("\nNetwork Type:", cls.network_type)

    # Class method
    @classmethod
    def change_network_type(cls, new_value):
        cls.network_type = new_value
        print("Updated Network Type:", cls.network_type)

    # Class method
    @classmethod
    def from_string(cls, data):
        fiber_id, length, status = data.split(",")
        return cls(fiber_id, int(length), status)

    # Static method
    @staticmethod
    def km_to_meter(km):
        return km * 1000

    # Static method
    @staticmethod
    def meter_to_km(meter):
        return meter / 1000

    # Static method
    @staticmethod
    def valid_length(length):
        return length > 0

    # Static method
    @staticmethod
    def valid_status(status):
        valid_statuses = ["Active", "Inactive", "Dark"]
        return status in valid_statuses

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

# Class methods
Fiber.show_network_type()
Fiber.change_network_type("FTTx")

# Instance modifications
fiber3.length = 250
fiber2.status = "Dark"

fiber1.dark()
fiber1.add_completed_footage(400)

fiber2.update_footage_status(900, "Active")

# Display Fiber information
fiber1.display()
fiber2.display()
fiber3.display()

# Total Fiber objects
print("\nTotal Fibers:", Fiber.total_fibers)

# Instance variables
print("\nFiber1 Instance Variables:")
print(fiber1.__dict__)

print("\nFiber2 Instance Variables:")
print(fiber2.__dict__)

print("\nFiber3 Instance Variables:")
print(fiber3.__dict__)

# Static methods
print("\n5 KM in Meters:", Fiber.km_to_meter(5))
print("5000 Meters in KM:", Fiber.meter_to_km(5000))

print("\nValid Length (500):", Fiber.valid_length(500))
print("Valid Length (-50):", Fiber.valid_length(-50))

print("\nValid Status (Active):", Fiber.valid_status("Active"))
print("Valid Status (Fiber):", Fiber.valid_status("Fiber"))

# Class method as alternative constructor
fiber4 = Fiber.from_string("F004,850,Dark")

print("\nFiber Created Using Class Method:")
fiber4.display()

print("\nTotal Fibers:", Fiber.total_fibers)
