import random

def TellAJoke():
	num = random.randint(0, 2)
	if(num == 0):
		input("How many computer programmers does it "\
		+ "take to change a light bulb?")
		print("None, that's a hardware problem.")
	elif(num == 1):
		input("What do you call 8 Hobbits?")
		print("A Hobbyte.")
	else:
		input("What are the two hardest problems in Computer Science?")
		print("Cache Invalidation, Naming Things, and Off-By-One Errors.")

def TellAFact():
	num = random.randint(0, 2)
	if(num == 0):
		print("Conditionals are how I make decisions. " \
	  + "I think about what to say based on your input before I say it!")
	elif(num == 1):
		print("There are powerful women in tech at " \
		+ "lots of major companies like: " \
		+ "Facebook, Google, IBM, HP, and more!")
	else:
		print("Grace Hopper created the first compiler for a programming language.")

username = input("Enter your name: ")
print("Hi, " + username + "! I am Francie." \
+ "I love studying about women in tech" \
+ " because they inspire me!")

birthYear = input("Year you were born:")
while(not birthYear.isdigit()):
	birthYear = input("That's not a number! Year you were born:")

print("Did you know know that Intel built the first" \
+ " microprocessor in 1971?")

if(birthYear > 1971):
  print("It happened " + str(int(birthYear) - 1971) \
  + " year(s) before you were born!")
elif(birthYear == 1971):
  print("It happened the year you were born!")
else:
  print("It happened " + str(1971 - int(birthYear)) \
  + " year(s) after you were born!")

info = ""
while info != "done":
  info = input("Tell me something about yourself, " \
  + username +" (type done to exit):")
  print("Really? Wow!")
  
  question = input("What do you want to know about me (AGE, JOKE, FACT): ")
	
  if(question == "AGE"):
		print("I am 1000 years old! Just kidding, I don't have an age.")
  elif(question == "JOKE"):
		TellAJoke()
  elif(question == "FACT"):
		TellAFact()
  else:
	  print("Nevermind...")
