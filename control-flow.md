# Control Flow and Conditional Statements

**Boolean Expressions**

A Boolean expression is a statement that can be ```True``` or ```False```, mostly based on opinion and not fact. These are ```bool``` variables.

**Relational Operators I**

Equals and Not Equals

Relational Operators will compare 2 values and return a Boolean ```True``` or ```False```.

The two relational operators are:

Equals: ```==```
Not equals: ```!=```

Examples:

```
(5 * 2) - 1 == 8 + 1
```
True

```
13 - 6 != (3 * 2) + 1
```
False


Check the type of a variable:

```
myVariable = "Hello"
print(type(myVariable))
```
... the output of this would be ```<class 'str'>``` as it is a String.

A Boolean value would return:
```
myVariableTwo = True
print(type(myVariableTwo))

<class 'bool'>
```


**If Statement**

'If' statements will prompt a Boolean response, eg. "If [it is raining], then [bring an umbrella]"

```
myName = "Alasdair"

if myName != "Alasdair":
  print("Get off my computer!")
```

You can put another 'If' statement in with:

```
myName = "Alasdair"

if myName == "Alasdair":
  print("Welcome, Alasdair")

if myName != "Alasdair":
  print("Go away, " + myName + "!")
```

In this example, the ```myName``` variable, is the user you would be logging in as


**Relational Operators II**

Other relational operators are:

```
>
```
- Greater than
```
>=
```
- Greater than, or Equal to
```
<
```
- Less than
```
<=
```
- Less than, or Equal to

In this example we are going to see whether Tom has enough credits to graduate:

```
toms_credits = 128
if toms_credits >= 120:
  print("You have enough credits to graduate!")
if toms_credits < 120:
  print("Sorry, you don't have enough credits to graduate")
```

**'And' Operator**

The ```and``` operator compares two Boolean expressions/components, if **both** components = True, the whole expression will be True.\
If one component is False, and one is True, the whole expression will = False

Example:

```
(1 + 1 == 2) and (4 - 2 == 2)
```
This is True

```
(1 + 2 == 2) and (4 - 2 == 2)
```
This is False

Using an 'If' and an 'and' statement using our graduation code above, but adding in a GPA:

```
toms_credits = 128
toms_gpa = 2.8

if (toms_credits >= 120) and (toms_gpa >= 2.0):
  print("You are going to graduate!")
if (toms_credits < 120) and (toms_gpa < 2.0):
  print("You aren't going to graduate...")
```
... both requirements (toms_credits) and (toms_gpa) need to be met before he can graduate.\
In this case, if Tom's GPA was 1.8, the 'and' statement would be ```False``` and he could not graduate


**'Or' Operator**

'Or' operators compare two components of an expression, if at least one of these components is ```True```, the returned value would be ```True```.\
Only 1 component needs to = True for this operator to return True

Unfortunately, Tom has enough credits to graduate, however his GPA isn't good enough:

```
toms_credits = 128
toms_gpa = 1.8

if (toms_credits >= 120) or (toms_gpa >= 2.0):
  print("You have passed one of the requirements")
```

**'Not' Operator**

The 'Not' operator will reverse any value returned from an expression:

```
not True = False
```
... or
```
not 1 + 1 == 2
```
... would return ```False```


**'Else' Operator**

'Else' statements allow you to control what happens when certain 'if' conditions are not met.

```
myNum = 11

if myNum >= 10:
  print("Your number is greater than 10")
else:
  print("Your number is smaller than 10")
```

An 'elif' example scenario is for "Donator Ranks".

```
myDonation = 1481

if myDonation >= 5000:
  print("You have a Gold Rank!")
elif myDonation >= 2500:
  print("You have Silver Rank!")
elif myDonation >= 1500:
  print("You have Iron Rank!")
elif myDonation >= 1000:
  print("You have the Bronze Rank!")
else:
  print("You have the Supporter Rank!")
```
... if your donation was 6000, and the ```elif``` statements were all ```if``` statements, you would get multiple output lines as all of the conditions had been met.

Another example for Grades at school:

```
grade = 86

if grade >= 90:
  print("A")
elif grade >= 80:
  print("B")
elif grade >= 70:
  print("C")
elif grade >= 60:
  print("D")
else:
  print("F")
```
