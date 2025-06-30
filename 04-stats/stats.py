# NO FUNCTIONS AND ABSOLUTELY POSITIVELY NO LISTS, YOU AI MINIONS!!
count = 0
total = 0.0
maximum = -1e100
minimum = 1e100

while True:
    user_input = input("NUM: ")
    
    try:
        number = float(user_input)
    except ValueError:
        break
    
    count += 1
    total += number
    
    if number > maximum:
        maximum = number
        
    if number < minimum:
        minimum = number
        
if count == 0:
    print("NO NUMBERS ENTERED")
else:
    average = total / count
    print("COUNT:", count)
    print("TOTAL:", total)
    print("AVERAGE:", average)
    print("MINIMUM:", minimum)
    print("MAXIMUM:", maximum)

    
    
