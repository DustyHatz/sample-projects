# Simple data analysis example using hair salon styles and prices


# List of offered hairstyles
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

# Initial prices for each hairstyle
prices = [30, 25, 40, 20, 20, 35, 50, 35]

# Total number of each haircut from last week
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Initialize the total price of all haircuts
total_price = 0

# Add all prices to the total price
# Can also be done with the sum() function
for price in prices:
  total_price += price
print(f"Total Price: ${total_price}")

# Calculate the average haircut price
average_price = total_price / len(prices)
print(f"Average Haircut Price: ${average_price}")

# Salon wants to charge $5 less for each haircut
new_prices = [price - 5 for price in prices]
print(new_prices)

# Initialize variable for total revenue
total_revenue = 0

# Calculate the total revenue from last week
for i in range(0, len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print(f"Total Revenue: ${total_revenue:,}")

# Calculate the average daily revenue
average_daily_revenue = total_revenue / 7
print(f"Average Daily Revenue: ${average_daily_revenue}")

# Salon wants to advertise all hairstyles under $30
cuts_under_30 = [hairstyles[i] for i in range(0, len(hairstyles)) if new_prices[i] < 30]
print(cuts_under_30)