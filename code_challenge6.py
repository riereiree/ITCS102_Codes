size = int(input("Enter the size: "))
variable = 1
for x in range (size):
    for y in range (x):
        print(variable, end=" ")
        variable += 1
    print()

size = int(input("Enter the size: "))
for x in range (6):
    for y in range (x):
        print(size, end=" ")
        size += 1
    print()
