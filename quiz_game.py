print("Welcome to super quiz")
confirm = input("do you want to play? yes/no")
if confirm.lower() != "yes":
  exit()
else:
  print('You said',confirm,"!","Ok lets begin!")
name = input("Whats your name? ")
age = input("Whats your age? ")
point = 0
print('Name :',name)
print('Age :',age)
qs = input("Q.1: What is the capital of bangladesh? ")
if qs.lower() == "dhaka":
  print("Your answer is correct")
  point += 1
else:
  print("Incorrect answer")
qs = input("Who is throffin? ")
if qs.lower() == "the goat":
 print("Correct answer")
 point += 1
else:
  print("Incorrect answer")
qs = input("what is your passion? ")
if qs.lower() == "coding":
   print("correct")
   point += 1
else:
  print("Incorrect answer")
print("Examinar name:",name)
print("Examinar age:",age)
print(f"Score point is {point}")