# Loops


## 'For' Loops

Useful for repeating patterns
Temporary variables can be used

Example:
```
board_games = ["Settlers of Catan", "Carcassone", "Power Grid", "Agricola", "Scrabble"]

for game in board_games:
  print(game)
```
.. `game` is a temporary variable

Another example:
```
for talking in range(10):
  print("I'm repeating myself!")
```
... this would repeat the line `I'm repeating myself!`, 10 time

If you wanted to count the number of 'repeats' you were on:

```
for talking in range(10):
  print("I'm repeating myself! " + str(talking + 1))
```
... outputted would be:

```
I'm repeating myself! 1
I'm repeating myself! 2
I'm repeating myself! 3
I'm repeating myself! 4
I'm repeating myself! 5
I'm repeating myself! 6
I'm repeating myself! 7
I'm repeating myself! 8
I'm repeating myself! 9
I'm repeating myself! 10
```

Example:

```
my_lines = "These are my lines, repeat them 5 times!"

for the_lines in range(5):
  print(my_lines)
```

## 'While' Loops

A `while` loop performs a set of operations as long as a condition is met/True.



This `while` loops will remain True until the count reaches 3:

```
count = 0

while count <= 3:
  print(count)
  count += 1
```

This `while` loop will count down from 10 and finish at 0

```
countdown = 10
print("Starting While Loop")
while countdown >= 0:
  print("Count is currently " + str(countdown))
  countdown -= 1
  print("- - - - - -")
print("Count finished")
```
... the same outcome, but coded differently:
```
countdown = 10
while countdown >= 0:
  print(countdown)
  countdown -= 1
print("We have liftoff!")
```
