def fiber_log(decorator):
    def tesing_decorator(value):
        print("Fiber Log started")
        decorator(value)
        
        print("Fiber Log Completed")
    return tesing_decorator
@fiber_log
def fiber_Km_calculation(length):
    print("Length in Feet:",length)
    km=length/1000
    print("Length in Km:",km)
@fiber_log
def spitter_calculation(homepass):
    print("Home pass details:",homepass)
    splitter=homepass/16
    print("Required Splitter:",splitter)
fiber_Km_calculation(4000)
spitter_calculation(1200)
