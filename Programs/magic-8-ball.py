# Codecademy Magic-8 Ball Program

#Importing Random module
import random

name = "Alasdair"
question = "Am I tall?"
answer = ""

# Generating random integer
random_number = random.randint(1, 9)

# Specifying possible outcomes of randint
if random_number == 1:
  answer = ("Yes - definitely.")
elif random_number == 2:
  answer = ("It is decidedly so.")
elif random_number == 3:
  answer = ("Without a doubt.")
elif random_number == 4:
  answer = ("Reply hazy, try again.")
elif random_number == 5:
  answer = ("Ask again later.")
elif random_number == 6:
  answer = ("Better not tell you now.")
elif random_number == 7:
  answer = ("My sources say no.")
elif random_number == 8:
  answer = ("Outlook not so good.")
elif random_number == 9:
  answer = ("Very doubtful.")
else:
  answer = ("Try again")

# Outputting question and response to console
print(name + " asks: " + question)
print(answer)
