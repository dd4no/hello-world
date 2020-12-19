index = 0
total = 0
count = 0
print("PLACE  VALUE          RUNNING SUM")
while index < 64:
    count = count + 1
    value = 2**index
    total = total + value
    print(index, "     ", value, "           ", total)
    index = index + 1
    if count == 8:
        print("----------------------------------------------------------------")
        count = 0
print()


    
    
    
    
