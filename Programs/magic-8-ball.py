# Codecademy Magic-8 Ball Program

#Importing Random module
import random

name = "Alasdair"
question = "Will I sleep tonight?"
answer = ""
# Generating random integer
random_number = random.randint(1,9)

# Specifying possible outcomes of randint
if random_number == 1:
  print(answer = "Yes- definitely.")
elif random_number == 2:
  print(answer = "It is decidedly so.")
elif random_number == 3:
  print(answer = "Without a doubt.")
elif random_number == 4:
  print(answer = "Reply hazy, try again.")
elif random_number == 5:
  print(answer = "Ask again later.")
elif random_number == 6:
  print(answer = "Better not tell you now.")
elif random_number == 7:
  print(answer = "My sources say no.")
elif random_number == 8:
  print(answer = "Outlook not so good.")
elif random_number == 9:
  print(answer = "Very doubtful.")
else:
  print("Error")

# Outputting question and response to console
print(name + " asks: " + question)
print("Magic 8-Ball's answer: " + answer)
