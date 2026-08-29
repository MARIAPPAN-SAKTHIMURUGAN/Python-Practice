import logging

logging.basicConfig(
    filename="fiber.log",
    level=logging.INFO
)


def fiber_validation():

    try:

        length = int(input("Enter Fiber Length: "))

        logging.info("Entered fiber length: %s", length)

        if length <= 0:
            raise ValueError("Invalid fiber length")

    except ValueError as e:

        logging.error("Validation failed: %s", e)

        print("Error:", e)

    else:

        km = length / 1000

        logging.info("Fiber length: %.2f KM", km)

        print("Fiber length in KM:", km)

    finally:

        logging.info("Fiber validation completed")

        print("Processing completed")


fiber_validation()
