# Basic tip calculator (Python 3)


# Define tip function
def tip():

	# Get total bill amount and desired tip percentage from user
	total = float(input("Total bill: "))
	percentage = int(input("Tip percentage: "))

	# Return the amount to tip rounded to the nearest hundredth
	return "%.2f" % ((percentage/100) * total)

# Print the recommended tip amount
print("Amount to tip: $" + tip())
