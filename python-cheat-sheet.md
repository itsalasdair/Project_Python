# Comments

```
# This is a Comment, used to document your code
This is uncommented
```

# Printing text to the console

```
print("This is text to print. Cool!")
```

Strings (text) can be quoted by double quotes or single quotes("" or '')\
Either can be used, however use double quotes if the string includes apostrophes, eg. they're


# Variables

Variables allow you to store data into a value for reuse, such as a date or user ID

Variables can be declared with a =

Example:

```
myVariable = "Hello!"


print(myVariable)
```

They can be updated throughout your code

Example:

```
myVariable = "Hello!"

print(myVariable)

my variable = "Goodbye!"

print(myVariable)
```

# Numbers

Python has multiple ways of storing numbers:

An ```integer``` is a whole number: 9\
A ```point``` is a decimal number: 1.8

```
thisIsAnInteger = 8
thisIsAFloat = 4.1
```


#Calculations

Python can perform addition, subtraction, multiplication and division:
```
+ - * /
```

Example:

```
print(500 - 50 + 1 * 2)
```

You can also perform calculations with stored data in variables:

```
price_of_bananas = 0.49
bananas_in_bunch = 5

print(price_of_bananas + bananas_in_bunch)
```


# Modulo

The Modulo component is a companion to the division operator and is indicated by ```%```\
It gives the remainder of a division calculation

Example:
```
print(29 % 5)
```
... prints 4. 29 / 5 is 5 with a remainder of 4


# Concatenation

You can concatenate strings with the ```+``` operator

```
greeting_text = "Hello there"
question_text = "How are you doing?"
full_text = greeting_text + question_text

print(full_text)
```
... this prints "Hello thereHow are you doing?"

We can add a space inbetween these 2 variables, or even add a comma:

```
full_text = greeting_text + ", " + question_text
print(full_text)
```
... this prints "Hello there, How are you doing?"

You can also define the formatting within the variable:

```
greeting_text = "Hello there, "
question_text = "How are you doing?"
full_text = greeting_text + question_text
print(full_text)
