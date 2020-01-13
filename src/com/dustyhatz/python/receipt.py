# Basic program for creating purchasing information and receipts

# Loveseat item
lovely_loveseat_description = "LOVELY LOVESEAT. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."
lovely_loveseat_price = 254.00
print (lovely_loveseat_price)

# Settee item
stylish_settee_description = "STYLISH SETTEE. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."
stylish_settee_price = 180.50

# Lamp item
luxurious_lamp_description = "LUXURIOUS LAMP. Glass and iron. 36 inches tall. Brown with cream shade."
luxurious_lamp_price = 52.15

# Set sales tax
sales_tax = .088

# Create customer total
customer_one_total = 0

#Create customer itemization
customer_one_itemization = ""

# Customer 1 purchases a Loveseat
customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description

#Customer 1 purchases a lamp
customer_one_total += luxurious_lamp_price
customer_one_itemization += "\n" * 2 + luxurious_lamp_description

# Checkout
customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax

# Print receipt
print("Customer One Items:\n")
print(customer_one_itemization + "\n")
print("Customer One Total:")
print("$" + str(round(customer_one_total, 2)))
