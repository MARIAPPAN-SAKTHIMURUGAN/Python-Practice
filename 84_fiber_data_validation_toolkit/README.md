# Fiber Data Validation Toolkit

A Python-based telecom fiber data validation toolkit designed to validate FTTH/FTTx fiber planning data and calculate required splitter capacity.

## Features

* Fiber ID validation using Regular Expressions
* Fiber length validation
* Homepass validation
* Custom exception handling
* CSV data processing
* Dataclass-based fiber model
* Decorator-based validation logging
* Validation error logging
* Splitter requirement calculation
* Type hints
* pathlib for file handling

## Technologies

* Python
* CSV
* pathlib
* dataclasses
* Regular Expressions
* Logging
* Custom Exceptions
* Decorators
* Type Hints

## Telecom Use Case

This project simulates validation of fiber planning data used in FTTH/FTTx network design.

Example:

```text
Fiber ID: FIB-1001
Length: 4500 meters
Homepass: 1389
Status: Active
```

### Splitter Calculation

The project calculates the required number of 1:16 splitters using:

```python
(homepass + 15) // 16
```

For 1389 homepasses:

```text
(1389 + 15) // 16
= 1404 // 16
= 87 splitters
```

## Sample Validation

| Fiber ID | Length | Homepass | Result           |
| -------- | -----: | -------: | ---------------- |
| FIB-1001 |   4500 |     1389 | Valid            |
| FIB-1002 |   2500 |      500 | Valid            |
| FIB-1003 |   -100 |      300 | Invalid Length   |
| FIB-ABC  |   5000 |      800 | Invalid Fiber ID |
| FIB-1004 |   6000 |     1200 | Valid            |

## Project Structure

```text
84_fiber_data_validation_toolkit/
│
├── main.py
├── fiber_validator.py
├── fiber_data.csv
├── README.md
└── .gitignore
```

## How to Run

Open the project folder in the terminal and run:

```bash
python main.py
```

## Python Concepts Used

This project combines several Python concepts learned throughout the course:

* Functions
* Modules
* Exception Handling
* Custom Exceptions
* Regular Expressions
* Decorators
* Dataclasses
* Type Hints
* CSV File Handling
* pathlib
* Logging
* `try / except / else`
* `raise`
* `*args` and `**kwargs`

## Future Improvements

Possible future enhancements:

* Excel input/output using OpenPyXL
* Pandas-based validation
* GIS integration
* AutoCAD automation
* Fiber route validation
* BOQ generation
* ODN capacity analysis
* Automated validation reports
* Database integration using SQL

## Author

Mariappan Sakthimurugan

Telecom Fiber Planning | GIS & AutoCAD | Python Automation | FTTx/FTTH
