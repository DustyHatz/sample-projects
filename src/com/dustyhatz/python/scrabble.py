
# Dict of elidgible letters to play
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# Dict of letter point values 
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10, 1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Merge letter and points into a new dict
letter_to_points = {letter:point for letter, point in zip(letters, points)}

# Set spaces to equal 0 points
letter_to_points[" "] = 0

# Create dict of players and words they have played
player_to_words = {}

# Create empty dictionary to store players and their points
player_to_points = {}


# Function to score a word
def score_word(word):
  point_total = 0
  
  for letter in word:
    point_total += letter_to_points.get(letter)
    
  return point_total


# Function to update player's point totals
def update_point_totals():
  for player, words in player_to_words.items():
    player_points = 0

    for word in words:
      player_points += score_word(word)

    player_to_points[player] = player_points
  
  return player_to_points


# Function takes in a player and a word, scores the word, and updates the player's word list and point total
def play_word(player, word):
  
  if player in player_to_words:
    player_to_words[player].append(word)

  else:
    new_players = {}
    new_players[player] = [word]
    player_to_words.update(new_players)
    
  score_word(word)
  update_point_totals()
  return player_to_words


# Test with different players and words
print(player_to_words)
print(player_to_points)
play_word("player1", "Scrabble")
play_word("codey", "Absolutely")
play_word("player1", "Loopy")
play_word("DustyHatz", "Cash")
play_word("DustyHatz", "Sweet")
play_word("DustyHatz", "Totally")
print(player_to_words)
print(player_to_points)

