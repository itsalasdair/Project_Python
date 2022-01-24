# Example usage of 'if', 'and' & 'not'

credits = 120
gpa = 1.8

if not credits >= 120:
  print("You do not have enough credits to graduate.")
if not gpa >= 2.0:
  print("Your GPA is not high enough to graduate.")
if not (credits >= 120) and not (gpa >= 2.0):
  print("You do not meet either requirement to graduate!")
