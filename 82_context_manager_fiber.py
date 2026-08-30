class FiberProcessing:

    def __enter__(self):

        print("Fiber processing started")

        return self

    def __exit__(self, exc_type, exc_value, traceback):

        print("Fiber processing completed")


with FiberProcessing():

    print("Reading fiber data")
    print("Calculating fiber length")
    print("Generating report")
