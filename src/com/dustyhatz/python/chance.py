#-------------------------------------------------------------------------
# This program includes many functions each representing a game of chance
#-------------------------------------------------------------------------


# Import random in order to generate random numbers
import random


# Starting balance
money = 100


# Coin Flip game
def flip_coin(bet, call):

  # Check that player has enough money to place bet
  if bet > money:
    print("ERROR: You do not have enough money to place bet!")
  
  # Check that player call is either heads or tails
  elif call.lower() != "heads" and call.lower() != "tails":
    print("ERROR: Must call 'heads' or 'tails'.")

  else:
    # Flip coin
    flip = random.randint(1,2)
    print(f"Flipping coin...you called {call}...")
    
    # Check for win or loss
    # WIN - Heads when calling heads
    if flip == 1 and call.lower() == "heads":
      print(f"LANDED ON HEADS\nYou win ${bet}")
      return bet
    
    # WIN - Tails when calling tails
    elif flip == 2 and call.lower() == "tails":
      print(f"LANDED ON TAILS\nYou win ${bet}")
      return bet
    
    # LOSS - Heads when calling Tails
    elif flip == 1 and call.lower() == "tails":
      print(f"LANDED ON HEADS\nSorry, you lost ${bet}")
      return -bet
    
    # LOSS - Tails when calling Heads
    elif flip == 2 and call.lower() == "heads":
      print(f"LANDED ON TAILS\nSorry, you lost ${bet}")
      return -bet

    
def cho_han(bet, call):
  
  # Check that player has enough money to place bet
  if bet > money:
    print("ERROR: You do not have enough money to place bet!")
  
  # Check that player call is either odd or even
  elif call.lower() != "odd" and call.lower() != "even":
    print("ERROR: Must call 'odd' or 'even'.")
  
  else:
    # Roll the dice
    roll = random.randint(1,6) + random.randint(1,6)
    print(f"Rolling dice...you called {call}...")

    # WIN - Rolled even when calling even
    if roll % 2 == 0 and call.lower() == "even":
      print(f"ROLL IS EVEN\nYou win ${bet}")
      return bet

    # WIN - Rolled odd when calling odd
    elif roll % 2 != 0 and call.lower() == "odd":
      print(f"ROLL IS ODD\nYou win ${bet}")
      return bet

    # LOSS - Rolled even when calling odd
    elif roll % 2 == 0 and call.lower() == "odd":
      print(f"ROLL IS EVEN\nSorry, you lost ${bet}")
      return -bet

    # LOSS - Rolled odd when calling even
    elif roll % 2 != 0 and call.lower() == "even":
      print(f"ROLL IS ODD\nSorry, you lost ${bet}")
      return -bet



money += flip_coin(30, "heads")
money += cho_han(10, "even")
print(f"Your total amount of money is ${money}")

