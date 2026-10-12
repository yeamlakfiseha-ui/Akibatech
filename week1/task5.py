
name = input("Enter your name: ")
product = input("Enter the product name: ")
price = float(input("Enter the price of the product: "))
Quantity = int(input("Enter the number of product you bought: "))
total = price * Quantity
print ("\n============================================")
print ("        RECEIPT                             ")
print ("============================================")

print ("\nCustomer: " +name )

print ("\nProduct    Price   Qty")
print ("------------------------")
print (str(product)+"     " + str(price)+"   " + str(Quantity))

print ("\nTotal:    "+ str(total) + "ETB")
print ("\nThank you for shopping! " )
print ("============================================")  
