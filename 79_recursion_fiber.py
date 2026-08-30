def fiber_sections(length):

    if length <= 1000:
        print("Final section:", length, "meters")
        return

    print("Section:", 1000, "meters")

    fiber_sections(length - 1000)


fiber_sections(4500)
