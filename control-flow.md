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
