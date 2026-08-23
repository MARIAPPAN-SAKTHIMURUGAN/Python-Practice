import fiber_utility
import math as m


def fiber_calculation():

    length = 4000
    homepass = 700

    print(
        "Fiber Length in KM:",
        fiber_utility.calculate_length_inkm(length)
    )

    print(
        "Total No vault requirement per 1000':",
        fiber_utility.Vault_placement(length)
    )

    print(
        "Splitter Requirement for this FSA:",
        fiber_utility.splitter_calculation(homepass)
    )


def mathametic_function():

    print(m.sqrt(100))


fiber_calculation()
mathametic_function()