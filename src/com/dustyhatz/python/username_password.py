# A very simple Username and Password generator using a person's first and last name.
# No input error checking implemented


# Takes in person's first and last name
# Returns a username comprised of the first 3 letters of first name and first 4 letters of last name
def username_generator(first_name, last_name):
  username = first_name[:3] + last_name[:4]
  return username
  
  
# Takes in a username
# Creates a password by shifting every character in username one spot to the right
def password_generator(username):
  password = ""
  for c in range(0, len(username)):
    password += username[c-1]
  return password


# Examples
print(username_generator("Dustin", "Hatzenbuhler"))
print(password_generator(username_generator("Dustin", "Hatzenbuhler")))

