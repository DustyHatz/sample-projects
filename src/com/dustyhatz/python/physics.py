# This program defines multiple functions to help calculate some fundamental physics properties.

# Example data
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

# Function to convert temperature Fahrenheit to Celcius
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

# Function to convert temperature Celcius to Fahrenheit
def c_to_f(c_temp):
  f_temp = (c_temp * (9/5) + 32)
  return f_temp

# Function to calculate amount of force
def get_force(mass, acceleration):
  return mass * acceleration

# Function to calculate amount of energy (c is set to speed of light)
def get_energy(mass, c = 3*10**8):
  return mass * c**2

# Function to calculate amount of work
def get_work(mass, acceleration, distance):
  return get_force(mass, acceleration) * distance

# Testing Fahrenheit to Celcius function using 100 degrees Celcius
f100_in_celcius = f_to_c(100)
print(round(f100_in_celcius))

# Testing Celcius to Fahrenheit function using 0 degrees Celcius
c0_in_fahrenheit = c_to_f(0)
print(round(c0_in_fahrenheit))

# Testing the get force function using example data
train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies " + str(train_force) + " Newtons of force.")

# Testing the get energy function using example data
bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

# Testing the get work function using example data
train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")