import random
low = input("Enter a random number")
if low.isdigit():
  low = int(low)
#alt method
#low = int(input("Enter a random number"))
fnumber = random.randint(0,low)
# print(gnumber)
def result():
 print("You got it ", fnumber , " is correct")
 print("Tottal Try" , usertry)
usertry = 0
while True:
 gnumber = int(input("Guess the number: "))
 if gnumber > low:
   print("Please guess a number under" , low)
 elif gnumber < low:
  usertry += 1
 if gnumber == fnumber:
    result()
    break
 elif gnumber != fnumber:
    print("Incorrect number" , gnumber , " Try again Next Time !")
    continue