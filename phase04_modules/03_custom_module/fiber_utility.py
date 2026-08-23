def calculate_length_inkm(length):
    return length / 1000


def vault_placement(length):
    return length / 1000


def splitter_calculation(homepass):
    return homepass / 32


if __name__ == "__main__":
    print("Testing Fiber Utility")

    length = 4000
    homepass = 700

    print("Fiber Length:", calculate_length_inkm(length), "KM")
    print("Vault Requirement:", vault_placement(length))
    print("Splitter Requirement:", splitter_calculation(homepass))



