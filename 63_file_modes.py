class Fiber:

    def __init__(self, fiberid, length, status):
        self.fiberid = fiberid
        self.length = length
        self.status = status

    def read_write(self, fiber_data):

        file_path = r"C:\Users\LENOVO\Desktop\fiber_data.txt"

        with open(file_path, "r+") as file:

            print("\n===== r+ : READ + WRITE =====")

            print("\nExisting Data:")
            print(file.read())

            for fib in fiber_data:
                file.write(fib)

            file.seek(0)

            print("\nNew Data:")
            print(file.read())

    def write_read(self, fiber_data):

        file_path = r"C:\Users\LENOVO\Desktop\fiber_data.txt"

        with open(file_path, "w+") as file:

            print("\n===== w+ : WRITE + READ =====")

            for fib in fiber_data:
                file.write(fib)

            file.seek(0)

            print("\nNew Data:")
            print(file.read())

    def append_read(self, fiber_data):

        file_path = r"C:\Users\LENOVO\Desktop\fiber_data.txt"

        with open(file_path, "a+") as file:

            file.seek(0)

            print("\n===== a+ : APPEND + READ =====")

            print("\nExisting Data:")
            print(file.read())

            for fib in fiber_data:
                file.write(fib)

            file.seek(0)

            print("\nNew Data:")
            print(file.read())


fiber1 = Fiber("", 0, "")

fiber2 = [
    "F034,450,Active\n",
    "F035,450,Active\n",
    "F036,450,Active\n"
]

fiber1.read_write(fiber2)

fiber1.write_read(fiber2)

fiber1.append_read(fiber2)
