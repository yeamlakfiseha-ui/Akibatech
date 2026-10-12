destination = input("Enter the destination: ")
distance = float(input("Enter the distance in kilometers: "))
average_speed = float(input("Enter the average speed in km/h: "))
time = distance / average_speed
minutes = (time - int(time)) * 60
print("The estimated travel time to " + destination + " is " + str(int(time)) + " hours and " + str(int(minutes)) + " minutes.")
