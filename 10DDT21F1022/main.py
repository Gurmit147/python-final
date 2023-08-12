from parcel_calculator import calculate_price
from savetxt import *
# Get user input for parcel dimensions and weight
length = float(input("Enter parcel length in centimeters: "))
width = float(input("Enter parcel width in centimeters: "))
height = float(input("Enter parcel height in centimeters: "))
weight = float(input("Enter parcel weight in kilograms: "))

# Calculate parcel price using imported function
price = calculate_price(length, width, height, weight)

# Print parcel price to user
print("The price of your parcel is: $", price)

# Save data to a text file
save(length,width,height,weight)
    
