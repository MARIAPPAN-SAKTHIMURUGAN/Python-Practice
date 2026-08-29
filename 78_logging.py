import logging


logging.basicConfig(
    filename="fiber.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def fiber_processing(fiber_id, length):

    logging.info(
        f"Starting processing for {fiber_id}"
    )

    if length <= 0:

        logging.error(
            f"Invalid fiber length for {fiber_id}: {length}"
        )

        return

    if length > 5000:

        logging.warning(
            f"Fiber {fiber_id} has high length: {length} meters"
        )

    logging.info(
        f"Fiber {fiber_id} processed successfully"
    )


fiber_processing("F001", 3000)

fiber_processing("F002", 7000)

fiber_processing("F003", -500)
