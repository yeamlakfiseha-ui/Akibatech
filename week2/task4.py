
num = input("Enter a word:  ")
num = num.lower()  # Convert the input to lowercase for case-insensitive comparison
if num == num[::-1] :
    print(num, "is a palindrome.")
else:
    print(num, "is not a palindrome.")     
