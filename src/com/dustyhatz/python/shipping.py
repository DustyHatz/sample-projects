# Basic shipping cost program
# Calculates the separate costs of three different shipping options
# Calculates the cheapest of the three options


# Define function to calculate cost of Ground Shipping based on package weight
# Cost is a flat rate of $20 plus the price per pound of package weight
def gs(weight):
  cost = 20.00

  if weight <= 2:
    cost += (weight * 1.50)

  elif weight > 2 and weight <= 6:
    cost += (weight* 3.00)

  elif weight > 6 and weight <= 10:
    cost += (weight * 4.00)

  else:
    cost += (weight * 4.75)

  # Returns cost as a String to the nearest hundredth.
  return "%.2f" % cost


# Define function to calculate cost of Drone Shipping based on package weight
# No flat rate. Cost is price per pound of package weight.
def ds(weight):

  if weight <= 2:
    cost = (weight * 4.50)

  elif weight > 2 and weight <= 6:
    cost = (weight* 9.00)

  elif weight > 6 and weight <= 10:
    cost = (weight * 12.00)

  else:
    cost = (weight * 14.75)

  return "%.2f" % cost


# Define Premium Shipping at a flat rate of $125.00
ps = 125.00


# Define function to calculate the cheapeast shipping option based on package weight
def cheapest_shipping(weight):

  # Must convert function returns to floats in order to implement boolean operators
  if float(gs(weight)) >= ps and float(ds(weight)) >= ps:
    return "Premium shipping is your cheapest option and would cost $125.00 to ship a " + str(weight) + " pound package."
  
  elif float(gs(weight)) < ps and float(gs(weight)) < float(ds(weight)):
    return "Ground shipping is your cheapest option and would cost $" + str(gs(weight)) + " to ship a " + str(weight) + " pound package."
  
  else:
    return "Drone shipping is your cheapest option and would cost $" + str(ds(weight)) + " to ship a " + str(weight) + " pound package."


# Print the cost of Ground Shipping for a 4.8lb package
print(gs(4.8))

# Print the cost of Drone Shipping for a 4.8lb package
print(ds(4.8))

# Print the cheapest shipping option for a 4.8lb package
print(cheapest_shipping(4.8))


