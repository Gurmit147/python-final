
def save(length, width, height, weight):
	with open("parcel.txt", "w") as file:
	    file.write("Length: " + str(length) + " cm\n")
	    file.write("Width: " + str(width) + " cm\n")
	    file.write("Height: " + str(height) + " cm\n")
	    file.write("Weight: " + str(weight) + " kg\n")


    