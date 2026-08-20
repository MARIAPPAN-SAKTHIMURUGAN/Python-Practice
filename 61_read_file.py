def fiber_text_open():

    file_path = r"C:\Users\LENOVO\Desktop\fiber_data.txt"

    with open(file_path, "r") as file:

        print("Read Whole File (read()):")
        data = file.read()
        print(data)

        file.seek(0)

        print("\nFirst Two Lines (readline()):")
        line1 = file.readline()
        line2 = file.readline()

        print(line1.strip())
        print(line2.strip())

        file.seek(0)

        print("\nRead All Lines (readlines()):")
        lines = file.readlines()
        print(lines)

        file.seek(0)

        print("\nProcess File Line by Line:")
        
        for line in file:

            fiber_id, length, status = line.strip().split(",")

            length = int(length)

            print("\nFiber ID:", fiber_id)
            print("Length:", length, "Meters")
            print("Length in KM:", length / 1000)
            print("Status:", status)


fiber_text_open()
