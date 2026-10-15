count_even = 0
count_odd = 0
total = 0
average = 0
for i in range(10):
    num = int(input("Enter 10 numbers: "))
    
    if num % 2 == 0:
        count_even =+ 1
    else:
        count_odd =+ 1
    total += num

    if i == 0:
        largest = num
        smallest = num
    else:
        if num > largest:
            largest = num

        if num < smallest:
            smallest = num

    average = total / 10       

print("Odd numbers are: ", count_odd)
print("Even numbers are: ", count_even)
print("largest number is: ", largest)
print("smallest number is: ",smallest)
print("the sum is: ", total)
print("the average is: ", average)




