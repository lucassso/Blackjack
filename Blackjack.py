card = ["ace","ace","ace","ace","2","2","2","2","3","3","3","3","4","4","4","4","5","5","5","5","6","6","6","6","7","7","7","7","8","8","8","8","9","9","9","9","10","10","10","10","jack","jack","jack","jack","queen","queen","queen","queen","king","king","king","king"]
score = 0
dscore = 0
import random
from random import shuffle
pick1 = (random.choice(card))
card.remove(pick1)
shuffle(card)
pick2 = (random.choice(card))
card.remove(pick2)
shuffle(card)
pick3 = (random.choice(card))
card.remove(pick3)
shuffle(card)
pick4 = (random.choice(card))
card.remove(pick4)
shuffle(card)
pick5 = (random.choice(card))
card.remove(pick5)
dealer = 0
while dealer == 0:
  dpick1 = (random.choice(card))
  card.remove(dpick1)
  if dpick1 == "ace":
    dscore += 1
  elif dpick1 == "2":
    dscore += 2
  elif dpick1 == "3":
    dscore += 3
  elif dpick1 == "4":
    dscore += 4
  elif dpick1 == "5":
    dscore += 5
  elif dpick1 == "6":
    dscore += 6
  elif dpick1 == "7":
    dscore += 7
  elif dpick1 == "8":
    dscore += 8
  elif dpick1 == "9":
    dscore += 9
  elif dpick1 == "10":
    dscore += 10
  elif dpick1 == "jack":
    dscore += 10
  elif dpick1 == "queen":
    dscore += 10
  elif dpick1 == "king":
    dscore += 10
  if dscore > 17:
    dealer += 1


print("")
input("Blackjack, a project by Lucas.")
print("""
""")
print("You get dealt a "+pick1+" and a "+pick2+".")
if pick1 == "ace":
  a1 = input("You got an ace. Would you like it to be a 1 or an 11?\n")
  if a1 == "1":
    score += 1
    print("Okay, it is a 1.")
  elif a1 == "11":
    score += 11
    print("Okay, it is an 11.")
  else:
    quit()
elif pick1 == "2":
  score += 2
elif pick1 == "3":
  score += 3
elif pick1 == "4":
  score += 4
elif pick1 == "5":
  score += 5
elif pick1 == "6":
  score += 6
elif pick1 == "7":
  score += 7
elif pick1 == "8":
  score += 8
elif pick1 == "9":
  score += 9
elif pick1 == "10":
  score += 10
elif pick1 == "jack":
  score += 10
elif pick1 == "queen":
  score += 10
elif pick1 == "king":
  score += 10
if pick2 == "ace":
  a2 = input("You got an ace. Would you like it to be a 1 or an 11?\n")
  if a2 == "1":
    score += 1
    print("Okay, it will be a 1.")
  elif a2 == "11":
    score += 11
    print("Okay, it will be an 11.")
  else:
    quit()
elif pick2 == "2":
  score += 2
elif pick2 == "3":
  score += 3
elif pick2 == "4":
  score += 4
elif pick2 == "5":
  score += 5
elif pick2 == "6":
  score += 6
elif pick2 == "7":
  score += 7
elif pick2 == "8":
  score += 8
elif pick2 == "9":
  score += 9
elif pick2 == "10":
  score += 10
elif pick2 == "jack":
  score += 10
elif pick2 == "queen":
  score += 10
elif pick2 == "king":
  score += 10
if score == 21:
  print("You got 21! You win!")
  quit()
print("Your score is %s."% score)
print("")
hit1 = input("Hit or stay?\n")
if hit1 == "hit":
  print("")
  print("You get a %s." % pick3)
  if pick3 == "ace":
    a3 = input("You got an ace. Would you like it to be a 1 or an 11?\n")
    if a3 == "1":
      score += 1
      print("Okay, it will be a 1.")
    elif a3 == "11":
      score += 11
      print("Okay, it will be an 11.")
  elif pick3 == "2":
    score += 2
  elif pick3 == "3":
    score += 3
  elif pick3 == "4":
    score += 4
  elif pick3 == "5":
    score += 5
  elif pick3 == "6":
    score += 6
  elif pick3 == "7":
    score += 7
  elif pick3 == "8":
    score += 8
  elif pick3 == "9":
    score += 9
  elif pick3 == "10":
    score += 10
  elif pick3 == "jack":
    score += 10
  elif pick3 == "queen":
    score += 10
  elif pick3 == "king":
    score += 10
  if score > 21:
    print("You bust!")
    quit()
  if score == 21:
    print("You got 21! You win!")
    quit()
  print("Your current score is now %s."% score)
  hit2 = input("Hit or stay?\n")
  if hit2 == "hit":
    print("")
    print("You get a %s."% pick4)
    if pick4 == "ace":
      a4 = input("You got an ace. Would you like it to be a 1 or an 11?\n")
      if a4 == "1":
        score += 1
        print("Okay, it will be a 1.")
      elif a4 == "11":
        score += 11
        print("Okay, it will be an 11.")
      else:
        quit()
    elif pick4 == "2":
      score += 2
    elif pick4 == "3":
      score += 3
    elif pick4 == "4":
      score += 4
    elif pick4 == "5":
      score += 5
    elif pick4 == "6":
      score += 6
    elif pick4 == "7":
      score += 7
    elif pick4 == "8":
      score += 8
    elif pick4 == "9":
      score += 9
    elif pick4 == "10":
      score += 10
    elif pick4 == "jack":
      score += 10
    elif pick4 == "queen":
      score += 10
    elif pick4 == "king":
      score += 10
    if score > 21:
      print("You bust!")
      quit()
    if score == 21:
      print("You got 21! You win!")
      quit()
    print("Your score is %s."% score)
    hit3 = input("Hit or stay?\n")
    if hit3 == "hit":
      print("")
      print("You get a %s"% pick5)
      if pick5 == "ace":
        a5 = input("You got an ace. Would you like it to be a 1 or an 11?\n")
        if a5 == "1":
          score += 1
          print("Okay, it will be a 1.")
        elif a5 == "11":
          score += 11
          print("Okay, it will be an 11.")
        else:
          quit()
      elif pick5 == "2":
        score += 2
      elif pick5 == "3":
        score += 3
      elif pick5 == "4":
        score += 4
      elif pick5 == "5":
        score += 5
      elif pick5 == "6":
        score += 6
      elif pick5 == "7":
        score += 7
      elif pick5 == "8":
        score += 8
      elif pick5 == "9":
        score += 9
      elif pick5 == "10":
        score += 10
      elif pick5 == "jack":
        score += 10
      elif pick5 == "queen":
        score += 10
      elif pick5 == "king":
        score += 10
      if score == 21:
        print("You bust!")
        quit()
      if score == 21:
        print("You got 21! You win!")
        quit()
      if score < 21:
        print("You got five cards without busting! You win!")
        quit()
    elif hit3 == "stay":
      print("")
      print("You stay.")
    else:
      quit()
  elif hit2 == "stay":
    print("")
    print("You stay.")
  else:
    quit()    
elif hit1 == "stay":
  print("")
  print("You stay.")
else:
  quit()
print("")
print("Your score is %s."% score)
print("Dealer score is %s."% dscore)
if dscore == 21 and score == 21:
  print("You both have 21. You tie!")
  quit()
if dscore == score:
  print("You and the dealer both have %s. You tie!"% score)
  quit()
if dscore > 21 and score < 22:
  print("Dealer busts. You have %s. You win!"% score)
  quit()
if dscore < 22 and score > 21:
  print("You bust. The dealer wins.")
  quit()
if dscore > 21 and score > 21:
  print("You both bust. Nobody wins.")
  quit()
if dscore < 22 and score < 22:
  if dscore > score:
    print("Dealer has "+str(dscore)+". You have "+str(score)+". The dealer wins.")
    quit()
  if dscore < score:
    print("You have "+str(score)+". The dealer has "+str(dscore)+". You win!")
    quit()
