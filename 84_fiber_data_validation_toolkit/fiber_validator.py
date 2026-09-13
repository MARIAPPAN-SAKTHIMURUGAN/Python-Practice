from pathlib import Path
from dataclasses import dataclass
import csv
import re
import logging
class FiberValidationError(Exception):
    pass

logging.basicConfig(
    filename="fiber_validation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
def validation_log(function):
    def wrapper(*args,**kwargs):
        logging.info(f"Validation Started: {function.__name__}")
        try:
            result=function(*args,**kwargs)
        except Exception as e:
            logging.error(
                f"Validation Failed: {function.__name__} - {e}"
            )
            raise
        else:
        
            logging.info(f"Validation Completed: {function.__name__}")
        return result
    return wrapper
                     
    

@dataclass
class Fiber:

    fiber_id: str
    length: float
    homepass: int
    status: str


def read_fiber_data(filename: str) -> list[Fiber]:

    fibers = []
    # Find CSV in the same folder as this Python file
    file_path = Path(__file__).parent / filename

    with open(file_path, "r", newline="") as file:

        reader = csv.DictReader(file)
        for row in reader:
            fiber = Fiber(
                fiber_id=row["fiber_id"],
                length=float(row["length"]),
                homepass=int(row["homepass"]),
                status=row["status"]
            )

            fibers.append(fiber)

    return fibers
@validation_log
def validate_fiber_id(fiber_id: str):
    if not re.fullmatch(r"FIB-\d+", fiber_id):
        raise FiberValidationError(
            f"Invalid Fiber ID: {fiber_id}"
        )

    return True
@validation_log
def validate_fiber_length(length:float):
    if length<=0:
        raise FiberValidationError("Fiber Length must be greater than Zero")
    return True
@validation_log
def validate_homepass(homepass:int):
    if homepass<=0:
        raise FiberValidationError("Homepass must be greater than Zero")
    return True
def calculate_splitter(homepass:int):
    splitter=(homepass+15)//16
    return splitter
def validate_fiber(fiber:Fiber):
    validate_fiber_id(fiber.fiber_id)
    validate_fiber_length(fiber.length)
    validate_homepass(fiber.homepass)
    return True

