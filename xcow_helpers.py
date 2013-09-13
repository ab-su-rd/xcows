# can't get the hang of this, hs seems easier
# > let xs = ['x','x'..]
# > take xs_len xs

quit, playmore = range(2)
def get_xs(xs_len):
  xs = ""
  for _ in range(xs_len):
    xs += 'x'
  return xs

def play_more():
  print "\nDo you want to play more ? (c)ontinue (q)uit  :",
  choice = raw_input()
  if isinstance(choice, str):
    if choice == "q" or choice == "quit":
      return quit
    elif choice == "c" or choice == "continue":
      return playmore
  abuse.on_bad_play_more()
  return playmore

# helpers
# once again, hs feels better. could've easily got EQ, LT, GT to use for result
def is_valid_guess(guess, correct_word):
  if len(guess) == len(correct_word):
    return True
  else:
    return False

def control_for_edges(x):
  if x < 2:
    return 2
  elif x > 10:
    return 10
  return x
