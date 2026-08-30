```python
"""
Higher-Order Function - Telecom Fiber Calculations

This program demonstrates how a function can receive
another function as an argument.

Telecom calculations:
1. Fiber length in kilometers
2. Fiber length in feet
3. Required splitter count
"""


def length_in_km(length):
    """Convert fiber length from meters to kilometers."""
    return length / 1000


def length_in_feet(length):
    """Convert fiber length from meters to feet."""
    return length * 3.28084


def splitter_count(homepass):
    """Calculate the number of 1:16 splitter units required."""
    return homepass / 16


def final_fun(function, value):
    """
    Higher-order function.

    Receives another function and a value,
    then executes that function with the value.
    """
    return function(value)


# Execute different telecom calculations
km = final_fun(length_in_km, 4500)
feet = final_fun(length_in_feet, 3000)
hp = final_fun(splitter_count, 1245)

# Display results
print("Length in KM:", km)
print("Length in Feet:", feet)
print("Splitter Count:", hp)
```

### Output

```text
Length in KM: 4.5
Length in Feet: 9842.52
Splitter Count: 77.8125
```
