#-------------------------------------------------------------------------
# This program includes different functions each representing a game of chance
#-------------------------------------------------------------------------


# Import random in order to generate random numbers
import random


# Starting balance
money = 100


# Coin Flip game: Player bets on heads or tails
def flip_coin(bet, call):
  print("Playing Coin Flip...")
  # Check that player has enough money to place bet
  bet_valid = isinstance(bet, int) and bet <= money and bet > 0
  
  # Check that player places a bet greater than 0 and calls heads or tails
  call_valid = isinstance(call, str) and call.lower() == "heads" or call.lower() == "tails"
  
  if bet_valid and call_valid:
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

  else:
    print("ERROR: Invalid bet/call or not enough money!")
    return 0



# Cho Han game: Player bets on whether the result of dice roll is even or odd   
def cho_han(bet, call):

  print("Playing Cho Han...")

  # Check that player has enough money to place bet
  bet_valid = isinstance(bet, int) and bet <= money and bet > 0
  
  # Check that player places a bet greater than 0 and calls heads or tails
  call_valid = isinstance(call, str) and call.lower() == "even" or call.lower() == "odd"
  
  if bet_valid and call_valid:
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

  else:
    print("ERROR: Invalid bet/call or not enough money!")
    return 0

# High Card game: Both players pick a card out of a single deck. Highest card wins.
def high_card(bet):

  print("Playing High Card...")

  # Check that player has enough money to place bet
  bet_valid = isinstance(bet, int) and bet <= money and bet > 0

  if bet_valid:

    # Create deck of cards
    deck = list(range(1, 53))

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

  else:
    print("ERROR: Invalid bet/call or not enough money!")
    return 0


# Basic Roulette game: Player bets whether wheel will land on a speific number, 00, 0, even, or odd
def roulette(bet, call):

  print("Playing Roulette...")

  # Check that player has enough money to place bet and that bet is 1 or more
  bet_valid = isinstance(bet, int) and bet <= money and bet > 0

  if bet_valid:
    #If call is an integer
    if type(call) == int and bet_valid:

      print(f"You called {call}...")

      # Check that player places a bet greater than 0 and calls heads or tails
      if call == 00 or call == 0 or call in range(1, 36):
        
        # Spin Roulette Wheel
        result = random.randint(1,38)

        # WIN - Wheel lands on 00 (pays 35 to 1)
        if call == 00 and result == 38:
          print(f"WHEEL LANDED ON '00'\nYou win ${bet * 35}")
          return bet * 35

        # WIN - Wheel lands on 0 (pays 35 to 1)
        elif call == 0 and result == 37:
          print(f"WHEEL LANDED ON '0'\nYou win ${bet * 35}")
          return bet * 35

        # WIN - Wheel lands on called number (pays 35 to 1)
        elif call == result:
          print(f"WHEEL LANDED ON #{result}\nYou win ${bet * 35}")
          return bet * 35

        # LOSS - Wheel does not land on the called position
        else:
          print(f"WHEEL LANDED ON #{result}\nSorry, you lose ${bet}")
          return -bet
      
      else:
        print("ERROR: Call must be 0, 00, or 1-36")
        return 0

    # If call is a string
    elif type(call) == str and bet_valid:

      # Spin Roulette Wheel
      result = random.randint(1,38)

      # Convert call to lowercase for future checking
      call = call.lower()

      # WIN - Wheel lands on even number
      if call == "even" and result % 2 == 0:
        print(f"You called {call}...")
        print(f"WHEEL LANDED ON EVEN #{result}\nYou win ${bet}")
        return bet

      # WIN - Wheel lands on odd number
      elif call == "odd" and result % 2 == 1:
        print(f"You called {call}...")
        print(f"WHEEL LANDED ON ODD #{result}\nYou win ${bet}")
        return bet

      elif call != "odd" or call != "even":
        print("ERROR: Call must be 'even' or 'odd'")
        return 0

      else:
          print(f"WHEEL LANDED ON #{result}\nSorry, you lose ${bet}")
          return -bet

  else:
    print("ERROR: Invalid bet or not enough money!")
    return 0

# Play games!
money += flip_coin(1, "tails")
print()
money += cho_han(10, "even")
print()
money += high_card(30)
print()
money += roulette(10, "odd")

print(f"Your total amount of money is ${money}")

