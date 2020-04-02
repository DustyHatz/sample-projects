# Practice building a system of classes to create a working structure for a business.
# In this case, two restuarants "Presto Pesto" and "Mini Panini"

from datetime import time


# Create a class for the Business
class Business:
  
  # Constructor takes two parameters: the business name and a list of franchises
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises
    
  def __repr__(self):
    return f"{self.name}"


# Create a class for the Franchises
class Franchise:
  
  # Constructor takes two parameters: the address, and a list of offered menus
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
    
  def __repr__(self):
    return f"Restuarant Located at {self.address}"
  
  # Function to find out which menus are being offered at a given time
  def available_menus(self, time):
    available_menu = []

    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menu.append(menu)

    return available_menu
    
    
# Create a class for a menu
class Menu:
  
  # Constructor take in four paramteres: the menu name, a dict of items and prices, and the start and ending times the menu is offered
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
    
  def __repr__(self):
    return f"{self.name} menu available from {self.start_time} to {self.end_time}"

  # Function to calculate the total bill. Takes in a list of the names of the purchased items
  def calculate_bill(self, purchased_items):
    total_price = 0

    for item in purchased_items:
      if item in self.items:
        total_price += self.items[item]

    return f"Total bill: ${total_price:.2f}"
  
  
# Presto Pesto Store

# Brunch menu
brunch = Menu("brunch", {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}, 1100, 1600)

# Early Bird Menu
early_bird = Menu("early bird", {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}, 1500, 1800)

# Dinner Menu
dinner = Menu("dinner", {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}, 1700, 2300)

# Kids Menu
kids = Menu("kids", {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}, 1100, 2100)

# Create list of all menus
menus = [brunch, early_bird, dinner, kids]

# Create new Franchise for Flagship store
flagship_store = Franchise("1232 West End Road", menus)

# Create new Franchise for the new store
new_installment = Franchise("12 East Mulberry Street", menus)

# Create a new Business
basta = Business("Presto Pesto", [flagship_store, new_installment])


# Mini Panini Store

# Create Menu for Mini Panini store
panini_menu = Menu("Take a' Arepa", {
  'panini pabellon': 7.00, 'pernil panini': 8.50, 'guayanes panini': 8.00, 'jamon panini': 7.50
}, 1000, 2000)

# Create new Franchise for Take a' Arepa store
panini_place = Franchise("189 Fitzgerald Avenue", panini_menu)

# Create a Business for Take a' Arepa
panini = Business("Take a' Arepa", [panini_place])

