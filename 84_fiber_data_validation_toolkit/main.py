
from fiber_validator import (
    read_fiber_data,
    validate_fiber,
    calculate_splitter,
    FiberValidationError
)
import logging
def main():
    
    fibers1 = read_fiber_data("fiber_data.csv")

    for fiber in fibers1:
        print("\n============================")
        print("Fiber Id:",fiber.fiber_id)
        print("\n============================")
        try:
            validate_fiber(fiber)
            print("Fiber ID:", fiber.fiber_id) 
            print("Length:", fiber.length) 
            print("Homepass:", fiber.homepass)
            splitter = calculate_splitter(fiber.homepass) 
            print("Required Splitter:", splitter) 
            logging.info( f"{fiber.fiber_id}: Fiber is VALID" ) 
            logging.info( f"{fiber.fiber_id}: Required Splitter = {splitter}" )
        except FiberValidationError as e: 
            print("Fiber Status: INVALID") 
            print("Error:", e) 
            logging.error( f"{fiber.fiber_id}: Fiber is INVALID - {e}" )
if __name__ == "__main__":
    main()
    

    