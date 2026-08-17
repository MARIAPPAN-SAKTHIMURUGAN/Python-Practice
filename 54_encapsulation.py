class Fiber:
    def __init__(self, fiber_id, length, status):
        # Public variable
        self.fiber_id = fiber_id

        # Private variables
        self.__length = length
        self.__status = status

    # Display Fiber details
    def display(self):
        print("\n--- Fiber Details ---")
        print("Fiber ID:", self.fiber_id)
        print("Length:", self.__length, "Meters")
        print("Status:", self.__status)

    # Setter for length
    def set_length(self, length):
        if length >= 0:
            self.__length = length
        else:
            print("Invalid Length")

    # Getter for length
    def get_length(self):
        return self.__length

    # Setter for status
    def set_status(self, status):
        valid_statuses = [
            "Active",
            "Dark",
            "IPL",
            "Unknown"
        ]

        if status in valid_statuses:
            self.__status = status
        else:
            print("Invalid Status")

    # Getter for status
    def get_status(self):
        return self.__status


# Create Fiber objects
fiber1 = Fiber("F001", 500, "Active")
fiber2 = Fiber("F002", 900, "Dark")

# Display original values
fiber1.display()
fiber2.display()

# Get Fiber1 length
print("\nFiber1 Length:", fiber1.get_length())

# Update Fiber2 length
fiber2.set_length(fiber1.get_length())

print("Fiber2 Updated Length:", fiber2.get_length())

# Get statuses
print("Fiber1 Status:", fiber1.get_status())
print("Fiber2 Status:", fiber2.get_status())

# Update Fiber1 status
fiber1.set_status("Dark")

print("\nFiber1 Updated Status:", fiber1.get_status())

# Try invalid length
fiber1.set_length(-100)

# Try invalid status
fiber2.set_status("Invalid")

# Display final values
print("\n--- Final Fiber Details ---")

fiber1.display()
fiber2.display()
