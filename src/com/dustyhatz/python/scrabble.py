
# Dict of elidgible letters to play
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# Dict of letter point values 
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Create new dict of letters and points
letter_to_points = {letter:point for letter, point in zip(letters, points)}

# Set spaces to equal 0 points
letter_to_points[" "] = 0

# Function to score a word
def score_word(word):
  point_total = 0
  
  for letter in word:
    point_total += letter_to_points.get(letter)
    
  return point_total

# Test score_word function
brownie_points = score_word("BROWNIE")

# Create dict of players and words they have played
player_to_words = {"player1" : ["BLUE", "TENNIS", "EXIT"], "wordNerd" : ["EARTH", "EYES", "MACHINE"], "Lexi Con" : ["ERASER", "BELLY", "HUSKY"], "Prof Reader" : ["ZAP", "COMA", "PERIOD"]}

# Create empty dictionary to store players and their points
player_to_points = {}


# Iterate over the players and their words played and create a new dict of players and current points
for player, words in player_to_words.items():
  player_points = 0
  
  for word in words:
    player_points += score_word(word)
  
  player_to_points[player] = player_points
  
print(player_to_points)

# TODO
# Create function that adds the word to the list of the player's played words
def play_word(player, word):
  for player, words in player_to_words.values():