from dataclasses import dataclass


@dataclass
class Fiber:

    fiber_id: str
    length: float
    homepass: int

    def length_in_km(self):
        return self.length / 1000

    def splitter_count(self):
        return (self.homepass + 15) // 16


fiber1 = Fiber("FIB-1001", 4500, 1389)

print(fiber1)

print("Length in KM:", fiber1.length_in_km())
print("Splitter Count:", fiber1.splitter_count())
