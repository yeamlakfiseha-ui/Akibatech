num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 >= num2 and num2 >= num3:
    print("The numbers in order are:", num1, num2, num3)

elif num1 >= num3 and num3 >= num2:
    print("The numbers in order are:", num1, num3, num2)

elif num2 >= num1 and num1 >= num3:
    print("The numbers in order are:", num2, num1, num3)

elif num2 >= num3 and num3 >= num1:
    print("The numbers in order are:", num2, num3, num1)

elif num3 >= num1 and num1 >= num2:
    print("The numbers in order are:", num3, num1, num2)

else:
    print("The numbers in order are:", num3, num2, num1)