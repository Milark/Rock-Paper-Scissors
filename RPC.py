player1 = raw_input("Player 1 Picks: ")
player2 = raw_input("Player 2 Picks: ")

if player1 not in ["rock", "paper", "scissors"]:
  print "INVALID ENTRY!"
  exit()
if player2 not in ["rock", "paper", "scissors"]:
  print "INVALID ENTRY!"
  exit()

print player1
print player2

if player1 == player2:
  print "It's a tie!"

if player1 == "rock":
  if player2 == "paper":
     print "Player 2 wins"
  if player2  == "scissors":
      print "Player 1 wins"

if  player1 == "paper":
  if player2 == "scissors":
    print "Player 2 wins"
  if player2 == "rock":
    print "Player 1 wins"
    
if player1 == "scissors":
  if player2 == "papper":
    print "Player 1 wins"
  if player2 == "rock":
    print "Player 2 wins"
