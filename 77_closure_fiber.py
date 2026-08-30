```python
def fiber_length_calculation(length, homepass):
    """
    Closure example for telecom fiber calculations.

    The inner functions remember the values of
    length and homepass from the outer function.
    """

    def calculate_km():
        return length / 1000

    def calculate_feet():
        return length * 3.28084

    def splitter_calculation():
        return homepass / 16

    def splitter_checking_print():
        count = homepass / 16
        print("Splitter Required:", count)

    return (
        calculate_km,
        calculate_feet,
        splitter_calculation,
        splitter_checking_print
    )


# Create closure functions
km, feet, splitter, splitter1 = fiber_length_calculation(4000, 1389)

# Use the returned functions
print("Length in KM:", km())
print("Length in Feet:", feet())
print("Splitter Required:", splitter())

splitter1()
```
