
class abuses:

  def __init__(self):
    pass

  def on_difficulty(self, difficulty):
    print ""
    if difficulty < 2:
      print "them cows.. they be weepin for company :("
      difficulty = 2
    elif difficulty < 4:
      print "what are you, some sort of a wuss ?!"
    elif difficulty == 4:
      print "green as they come. boy, didn't your just make my day!"
    elif difficulty <= 8:
      print "alright!"
    elif difficulty <= 10:
      print "BIGMOUTH!"
    else:
      print "sorry, we don't do smart kids"
      print "good luck to you, FREAK!"
      exit()

  def on_invalid_difficulty(self, difficulty):
    print ""
    print "pssch.."
    print "well, it's not a numbers game anyway"
    print "let's chalk you up to a rook, and take it from there"

  def on_round_init(self, round_number, word_len):
    print "\n*** commencing round number :  %i" % round_number
    print "(you can wimp out and reset by typing 'xx' at the prompt anytime)"
    print "your herd size for this round is %i" % word_len # maybe give out a hint here, like the number of unique characters ?
    print "you may begin to guess now"


  def on_incorrect_guess(self, cows, bulls, guess_len):
    print "you have (%i) cows, and (%i) bulls from a total herd of (%i)" % (cows, bulls, guess_len)
    if bulls >= guess_len/2:
      print "looking bullish!"
    elif cows > guess_len/2:
      print "fat cows!"
    else:
      print "fat bovine chance... you're gonna keep me here all day"

  def on_invalid_guess(self, guess):
    print "your guess should have the right number of characters"

  def on_round_wimp(self, correct_word):
    print "wimp!"
    print "the word was :  %s" % correct_word
    print "ending round...."

  def congratulate_on_win(self, tries, guess):
    print "\nwell done, you win!"
    print "the word was indeed, \"%s\"" % guess
    print "and you took %i tries to find it out!" % tries

  def on_bad_play_more(self):
    print "bad choice, we are going to continue"
