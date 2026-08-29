import logging


logging.basicConfig(
    filename="fiber.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class InvalidFiberLengthError(Exception):
    pass


def validate_fiber(fiber_id, length):

    logging.info(
        f"Validating fiber {fiber_id}"
    )

    if length <= 0:

        raise InvalidFiberLengthError(
            f"Invalid length: {length}"
        )

    logging.info(
        f"Fiber {fiber_id} is valid"
    )


fibers = [
    ("F001", 5000),
    ("F002", 3000),
    ("F003", -500),
    ("F004", 7000)
]


for fiber_id, length in fibers:

    try:

        validate_fiber(
            fiber_id,
            length
        )

    except InvalidFiberLengthError as e:

        logging.error(
            f"{fiber_id}: {e}"
        )

        print(
            f"{fiber_id} failed validation"
        )

    else:

        print(
            f"{fiber_id} passed validation"
        )

    finally:

        logging.info(
            f"Finished processing {fiber_id}"
        )
