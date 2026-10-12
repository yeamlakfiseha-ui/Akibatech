num = 2134


i = 0
while i <= 5:
    num1 = int(input("Guess the number: "))
    i += 1
    if num1 == num:
        print("Congratulation you guessed the number")
        print(f"you guessed the number in {i} attempts")
        
        break
    else:
        print("that's the wrong number")    