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


class FiberOutput(Fiber):
    def __init__(self, fiber_id, length, status, splitter_ratio):

        # Call parent class constructor
        super().__init__(fiber_id, length, status)

        self.splitter_ratio = splitter_ratio


class FTTHFiber(FiberOutput):

    # Method overriding
    def display(self):

        # Call parent display() method
        super().display()

        # Add child-specific information
        print("Splitter Ratio:", self.splitter_ratio)


# Parent class object
fiber1 = Fiber("E001", 450, "Active")

# Child class object
fiber2 = FTTHFiber("E002", 450, "Active", "1:8")


# Display parent class information
print("\nParent Class:")
fiber1.display()


# Display child class information
print("\nChild Class (Using super()):")
fiber2.display()
