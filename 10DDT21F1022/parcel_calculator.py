def calculate_price(length, width, height, weight):
	volume = length * width * height

	if weight<=1:
		if volume<=5000:
			price = 3
		elif volume>=5001 and volume<=10000:
			price = 5
		elif volume>10000:
			price = 7
	elif weight>1 and weight <=5:
		if volume>=0 and volume <=5000:
			price = 5
		elif volume>=5001 and volume<=10000:
			price = 7
		elif volume>10000:
			price = 9 
	elif weight>5:
		if volume<=5000:
			price = 7
		elif volume>=5001 and volume<=10000:
			price = 9
		elif volume>10000:
			price = 11
	return price
