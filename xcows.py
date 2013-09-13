from random import choice

words_filename = "words.txt"

class xcows:
  difficulty = 4 # def - seems fairy easy

  words_filename = "words.txt" # add as option for user, diff topics etc
  all_words = [""]
  current_word = ""; current_word_len = 0

  loss, win, reset = range(3) # result enums

  def __init__(self):
    self.load_words()

  def load_words(self):
    words_file = open(self.words_filename, "r") 
    self.all_words = words_file.readlines()

  def init_round(self):
    self.reset_round()

  def reset_round(self):
    self.current_word, self.current_word_len = self.choose_word_by_difficulty()

  def choose_word_by_difficulty(self):
    while True:
      rand_word = self.get_rand_word()
      if self.difficulty-1 <= len(rand_word) <= self.difficulty+1:
        return rand_word, len(rand_word)

  def get_rand_word(self):
    return choice(self.all_words).rstrip()

  def get_cows_bulls_n_result(self, guess) :
    cows = 0; bulls = 0; result = self.loss
    for i in range(len(guess)):
      if guess[i] == self.current_word[i]:
        bulls += 1
      else:
        for word_char in self.current_word:
          if guess[i] == word_char:
            cows += 1
            break
    if bulls == self.current_word_len:
      result = self.win
    else:
      result = self.loss
    return cows, bulls, result
