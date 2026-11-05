isExpensive = True

while isExpensive == True:
    x = bool(input("Is it expensive? (True/False): "))

    if x == True:
        print("Continuing loop...")
        continue
    
    else:
        break