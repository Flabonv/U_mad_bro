# Simple status inquiry on your mood if you need a break in your code
def umadbro():
  while True:
    rep = raw_input("U mad bro(ah)? [yes/no]  ")
    if (rep == 'yes'):
      print("\nDeal with it!!!\n")
      break
    if (rep == 'no'):
      print("\nCool story bro(ah)!\n")
      break
    if (rep == 'Bizz'):
      print('\nI welcome you my Master...')
      break
    else:
      print("\nDon't be a smart ass!\n")
