def zip1():
    fiber_ids = ["F001", "F002", "F003"]
    lengths = [250, 450, 600]
    status = ["Active", "Active", "Pending"]

    for num, (fiber_id, length, current_status) in enumerate(
        zip(fiber_ids, lengths, status),
        start=1
    ):
        print(
            f"Num: {num}\n"
            f"Fiber: {fiber_id}\n"
            f"Length: {length}\n"
            f"Status: {current_status}\n"
        )


zip1()
