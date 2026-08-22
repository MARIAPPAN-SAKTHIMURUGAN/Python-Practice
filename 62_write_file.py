def write_fiber_file():

    fibers = [
        "F001,450,Active\n",
        "F002,950,Dark\n",
        "F003,780,IPL\n",
        "F004,1200,Active\n"
    ]

    with open("fiber_output.txt", "w") as file:

        print("Writing Fiber Data...")

        for fiber in fibers:
            file.write(fiber)

    print("Fiber data written successfully.")


write_fiber_file()
