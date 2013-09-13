from xcows  import xcows
from abuses import abuses
from xcow_helpers import get_xs, play_more, is_valid_guess, control_for_edges

# story

print "\n\nwelcome to xcows!"
print "initializing...\n"
localcows = xcows() # take out loadwords() from __init__() if we want to have topics etc
abuse = abuses()
print "OK, survived that. your turn now\n"

# difficulty
print "you'll need to tell us just a little bit more before we begin"
print "how big a herd can you handle ? (2,10) :  ",
try:
  x = int(raw_input())
  abuse.on_difficulty(x)
  x = control_for_edges(x)
  localcows.difficulty = x
except ValueError:
  abuse.on_invalid_difficulty(x)
print "difficulty set to %s" % localcows.difficulty

# add prev_words[] etc, for history/bookkeeping etc
round_number, num_wins, num_losses = 0, 0, 0
total_tries = 0

quit, playmore = range(2)
while True:
  round_number += 1
  tries = 0
  localcows.init_round()
  prompt_string = "\n" + get_xs(localcows.current_word_len)
  abuse.on_round_init(round_number, len(localcows.current_word))
  while True:
    tries += 1
    print prompt_string
    guess = ""
    try:
      guess = str(raw_input())
      if guess == "xx":
        num_losses += 1
        abuse.on_round_wimp(localcows.current_word)
        break
      elif is_valid_guess(guess, localcows.current_word):
        cows, bulls, result = localcows.get_cows_bulls_n_result(guess)
        if result == localcows.win:
          num_wins += 1
          abuse.congratulate_on_win(tries, guess)
          break
        else:
          abuse.on_incorrect_guess(cows, bulls, len(guess))
      else:
        abuse.on_invalid_guess(guess)
    except ValueError:
      print "stick to the alphabet!"
  total_tries += tries
  print "\nyour performance so far, %i wins, %i losses, out of a total of %i games" % (num_wins, num_losses, round_number)
  print "you have guessed %i times in this session" % total_tries
  if play_more():
    continue
  else:
    break

print "\n-- session stats"
print "%i wins, %i losses, out of a total of %i games" % (num_wins, num_losses, round_number)
print "you have guessed %i times in this session\n" % total_tries

print "good having you play the game. come back soon\n"
