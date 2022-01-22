# Codecademy Lists Challenge

last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below:
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

# Manual Grade List
gradebook = [
  ["physics", 98],
  ["calculus", 97],
  ["poetry", 85],
  ["history", 88]
]

# Adding CS and Visual Arts grades
gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])

# Modifying Visual Arts grades to +5 score
gradebook[5][1] = 98

# Removing Poetry grade score
gradebook[2].remove(85)
# Appending Poetry to Pass grade
# gradebook[2] = "Pass" caused orphaned 2nd list index
# Didn't use append, accidentally orphaned the "Pass" value*. Regenerated with below command:
gradebook[2] = [["Poetry", "Pass"]]

# Merging of last_semester_gradebook and gradebook
full_gradebook = gradebook + last_semester_gradebook

# Printing full_gradebook
print(full_gradebook)
