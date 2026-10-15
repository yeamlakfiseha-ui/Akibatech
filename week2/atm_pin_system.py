num = 1234
i = 0 
count = 3
while i <= 3:
    num1 = int(input("Enter your ATM pin number: "))
    i += 1
    
    if num == num1:
        print("The pin is correct!")
        break
    else:
        count -= 1
        print("Incorrect PIN")
        print("Attempts remaining: ", count)
