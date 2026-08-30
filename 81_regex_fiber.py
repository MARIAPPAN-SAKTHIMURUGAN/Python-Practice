import re

text = "Fiber: FIB-1001"

data = """

Fiber: FIB-1001,

Splitter: SPL-201,

Fiber: FIB-1002,

Splitter: SPL-202,

Fiber: FIB-1003,

"""

result = re.search(r"FIB-\d+", text)

result2 = re.search("FIB", text)

result3 = re.findall(r"FIB-\d+", data)

result4 = re.findall(r"SPL-\d+", data)


print("Search FIB:", result2.group())

print("Search FIB with \\d+:", result.group())

print("Find all FIB:", result3)

print("Find all SPL:", result4)


fiber_id = "FIB-1001"

if re.fullmatch(r"FIB-\d+", fiber_id):
    print("Fiber ID valid")
else:
    print("Fiber ID is not valid")
new_data=re.sub(r"FIB-\d+","FIB-XXXX",data)
print(new_data)
new_data1=re.split(",",data)
print(new_data1)
