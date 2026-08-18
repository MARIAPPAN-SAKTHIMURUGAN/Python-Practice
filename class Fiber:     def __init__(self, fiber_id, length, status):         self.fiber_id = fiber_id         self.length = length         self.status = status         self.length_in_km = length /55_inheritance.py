class Fiber:
    def __init__(self, fiber_id, length, status):
        self.fiber_id = fiber_id
        self.length = length
        self.status = status
        self.length_in_km = length / 1000


class FiberOutput(Fiber):
    def __init__(self, fiber_id, length, status, splitter_ratio):
        super().__init__(fiber_id, length, status)
        self.splitter_ratio = splitter_ratio


class FTTHFiber(FiberOutput):

    def display(self):
        print("\n--- FTTH Fiber Details ---")
        print("Fiber ID:", self.fiber_id)
        print("Length:", self.length, "Meters")
        print("Status:", self.status)
        print("Length in KM:", self.length_in_km)
        print("Splitter Ratio:", self.splitter_ratio)


# Create FTTH Fiber object
fiber1 = FTTHFiber("E001", 450, "Active", "1:8")

# Display Fiber details
fiber1.display()
