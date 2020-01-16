#-------------------------------------------------------------------------
# This program includes many functions each representing a game of chance
#-------------------------------------------------------------------------


# Import random in order to generate random numbers
import random


# Starting balance
money = 100


# Coin Flip game: Player bets on heads or tails
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


# Cho Han game: Player bets on whether the result of dice roll is even or odd   
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


# High Card game: Both players pick a card out of a single deck. Highest card wins.
def high_card(bet):

  # Check that player has enough money to place bet
  if bet > money:
    print("ERROR: You do not have enough money to place bet!")

  else:

    # Create deck of cards
    deck = list(range(1, 53))

    # Simulate two players picking one card out of the deck
    print("Picking cards...")

    # First player picks a card
    player = random.choice(deck)

    # Update deck minus the first player's card
    deck.remove(player)
    new_deck = deck

    # Second player picks a card
    cpu = random.choice(new_deck)

    # WIN - Player has a higher card
    if player > cpu:
      print(f"YOUR CARD: {player}\nOPPONENT CARD: {cpu}\nYou win ${bet}")
      return bet

    # LOSE - Player has the lower card
    else:
      print(f"YOUR CARD: {player}\nOPPONENT CARD: {cpu}\nYou lose ${bet}")
      return -bet


# Play games!
money += flip_coin(30, "heads")
money += cho_han(10, "even")
money += high_card(30)

print(f"Your total amount of money is ${money}")

