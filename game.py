import random
print("Hello iam Candy , A virtual computer.")
name = input("What is your name? ")
print(f"Welcome {name}")
options = ["rock","paper","scissor"]
candwin = False
uwin = False
candpoint = 0
upoint = 0
print("""Pick an option
  1. rock
  2. Paper
  3. Scissor""")
def point():
  global candwin,candpoint,uwin,upoint,candy_pick
  if candwin :
    candpoint += 1
    print(f"Candy picked {candy_pick}")
    print("Candy won")
    print(f"Candy Got {candpoint}")
  elif uwin :
    upoint += 1
    print(f"Candy picked {candy_pick}")
    print(f"{name} won")
    print(f"You Got {upoint}")
# def slwin():
#    global uwin,candwin
#    if user_pick == candy_pick:
#     print(f"Candy picked {candy_pick}")
#     print("Match draw")
#    elif user_pick == "rock" and candy_pick == "scissor":
#      uwin = True
#    elif user_pick == "paper" and candy_pick == "rock":
#      uwin = True
#    elif user_pick == "scissor" and candy_pick == "paper":
#      uwin = True
#    elif user_pick == "scissor" and candy_pick == "rock":
#      candwin = True
#    elif user_pick == "rock" and candy_pick == "paper":
#      candwin = True
#    elif user_pick == "paper" and candy_pick == "scissor":
#      candwin = True
#    # point()
while True:
 user_pick = input("Type rock paper or scissor or Q to quit: ").lower()
 if user_pick == "q":
   print(f"Your scored {upoint}")
   print(f"Candy scored {candpoint}")
   quit()
 elif user_pick != "":
   if user_pick in options:
     randpick = random.randint(0,2)
     candy_pick = options[randpick]
     if user_pick == candy_pick:
       print(f"Candy picked {candy_pick}")
       print("Match draw")
     elif user_pick == "rock" and candy_pick == "scissor":
       uwin = True
     elif user_pick == "paper" and candy_pick == "rock":
       uwin = True
     elif user_pick == "scissor" and candy_pick == "paper":
       uwin = True
     elif user_pick == "scissor" and candy_pick == "rock":
       candwin = True
     elif user_pick == "rock" and candy_pick == "paper":
       candwin = True
     elif user_pick == "paper" and candy_pick == "scissor":
      candwin = True
     point()
     candwin = False
     uwin = False
     continue
   else:
     print("Invalid choice : You must select rock paper or scissor")
     continue
 else:
  print("You must selet an option")
  continue