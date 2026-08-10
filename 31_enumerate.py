# 34 — enumerate()

fibers = ["F001", "F002", "F003", "F004", "F005"]

for number, fiber in enumerate(fibers, start=1):
    print(f"Fiber {number}: {fiber}")
