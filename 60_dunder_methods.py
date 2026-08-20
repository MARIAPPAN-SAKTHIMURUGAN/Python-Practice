class Fiber:
    def __init__(self, fiberid, length, status):
        self.fiberid = fiberid
        self.length = length
        self.status = status

    def display(self):
        print("\nFiber Id:", self.fiberid)
        print("Length in Meters:", self.length)
        print("Status:", self.status)

    def __str__(self):
        return (
            f"\nFiber Id: {self.fiberid}"
            f"\nLength in Meters: {self.length}"
            f"\nStatus: {self.status}"
        )

    def __add__(self, other):
        return self.length + other.length

    def __sub__(self, other):
        return self.length - other.length

    def __eq__(self, other):
        return self.fiberid == other.fiberid


fiber1 = Fiber("F001", 500, "Active")
fiber2 = Fiber("F001", 500, "PDA")
fiber3 = Fiber("F002", 500, "Active")


print("__STR__ Output:")
print(fiber1)


print("\nDisplay output:")
fiber1.display()


print("\n__add__ function:")
print("Total Length:", fiber1 + fiber2)


print("\n__sub__ function:")
print("Length Difference:", fiber1 - fiber2)


print("\n__eq__ function:")
print("Fiber1 == Fiber2:", fiber1 == fiber2)
print("Fiber1 == Fiber3:", fiber1 == fiber3)
