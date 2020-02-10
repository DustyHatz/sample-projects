from datetime import time

class Menu:
  
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
    
  def __repr__(self):
    return f"{self.name} menu available from {self.start_time} to {self.end_time}"

  def calculate_bill(self, purchased_items):
    total_price = 0
    for item in purchased_items:
      if item in self.items:
        total_price += self.items[item]
    return f"Total bill: ${total_price:.2f}"
    
    
class Franchise:
  
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
    
  def __repr__(self):
    return f"Restuarant Located at {self.address}"
  
  def available_menus(self, time):
    available_menu = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menu.append(menu)
    return available_menu

      
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

print(flagship_store.available_menus(1200))