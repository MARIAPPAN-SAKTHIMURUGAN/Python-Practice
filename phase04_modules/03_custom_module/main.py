import fiber_utility

length = 4000
homepass = 700

print(
    "Fiber Length:",
    fiber_utility.calculate_length_inkm(length),
    "KM"
)

print(
    "Vault Requirement:",
    fiber_utility.vault_placement(length)
)

print(
    "Splitter Requirement:",
    fiber_utility.splitter_calculation(homepass)
)
