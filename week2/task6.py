num1 = int(input("Enter the starting number: "))
num2 = int(input("Enter the ending number: "))

for i in range(num1 ,   num2):

    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)        
            