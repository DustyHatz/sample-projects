# A program to practice creating a marketplace with buyers and sellers (in this case for video games)
#
# Future implementations:
# Wallet: Give each client a wallet and update dollar amounts according to buying/selling
# Wish List: Items that the client is interested in but does not currently purchase
# Expiring Items: Automatically remove an item base on an expiration date
#
# By: Dustin Hatzenbuhler


class VideoGame:
  pass

  # Art Constructor method
  def __init__(self, title, condition, console, owner):
    self.title = title
    self.condition = condition
    self.console = console
    self.owner = owner

  # String representation method
  def __repr__(self):

    return f'{self.title}, "{self.condition}", {self.console} - {self.owner.name}, {self.owner.location}.'


class Marketplace:
  pass

  # Marketplace constructor method
  def __init__(self):

    # Create the list of games for sale (initially empty)
    self.listings = []


  # Method for adding new listings to the marketplace
  def add_listing(self, new_listing):

    self.listings.append(new_listing)


  # Method for removing an expired listing
  def remove_listing(self, expired_listing):

    self.listings.remove(expired_listing)


  # Method to print all current listings
  def show_listings(self):

    if self.listings:

      print('Current games for sale:')

      for listing in self.listings:

        print(listing)
    
    else:
      
      print('No games currently for sale...')


class Client:
  pass

  # Client constructor method
  def __init__(self, name, location, is_store):
    self.name = name
    self.location = 'Private Entity' if (not is_store and not location) else location
    self.is_store = is_store
    

  # Client string repesentation method
  def __repr__(self):

    # Check whether client is a museum or a collector
    store_or_private = 'Store' if self.is_store else 'Private Entity'

    # Print client information
    return f"{self.name}, {self.location}, {store_or_private}"


  # Method to sell a game
  def sell_game(self, game, price):

    # Ensure the client owns the game they are selling
    if game.owner == self:

      # Create a new_listing
      new_listing = Listing(game, price, self)

      # Add the new listing to the marketplace
      gameo_vids.add_listing(new_listing)


  # Method to buy a game
  def buy_game(self, game):

    # Ensure the game is not owned by the buyer 
    if game.owner != self:

      # Set the game listing to None in case the desired game is not listed
      game_listing = None

      # Iterate over listings in the marketplace
      for listing in gameo_vids.listings:

        # If the listed game matches the desired game
        if listing.game == game:

          # Update the new game listing variable to be that listing
          game_listing = listing

          # Stop iterating over the listings if a match is found
          break
      
      # Ensure the game listing was found
      if game_listing != None:

        # Update the listing's owner to be the current buyer 
        game_listing.game.owner = self

        # Remove the listing from the marketplace
        gameo_vids.remove_listing(game_listing)


class Listing:
  pass

  # Listing constructor method
  def __init__(self, game, price, seller):
    self.game = game
    self.price = price
    self.seller = seller

  # Listing string representation method
  def __repr__(self):

    return f'{self.game.title}, ${self.price}'


# MAIN PROGRAM

# Create new marketplace
gameo_vids = Marketplace()

# Create example client (Store)
dustin = Client('Dustin Hatzenbuhler', 'Games 4 U, Saint Paul', True)

# Create example client (Private Entity)
penny = Client('Penny Pie', None, False)

# Create example video game
gta_v = VideoGame('Grand Theft Auto V', 'New', 'Xbox', dustin)

# List the video game for sale
kalyn.sell_game(gta_v, '20 (USD)')

# Display the current list of games for sale
gameo_vids.show_listings()

# Client "penny" buys the video game
penny.buy_game(gta_v)

# Display the updated list of games for sale
gameo_vids.show_listings()
