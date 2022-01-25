# Python Lists

We can create a variable and assign lists of data to the variable. For example, if we wanted to store various heights:

```
heights = [60, 51, 72, 55]
```

We can use strings as well as integers:

```
names = ["Tom", "Alex", "William", "Elliot"]
```

Strings and Integers can be used in conjuntion with eachother:
```
people = ["Tom", 52]
```

Example with a string, integer, float and boolean value:
```
mixed = ["Tom", 81, 5.1, True]
```

Empty lists can be used to input data at a later time:
```
empty_list = []
```

# List Methods

Methods, and List Methods allow you to create, manipulate and delete data within a variable.

The List Methods will always follow the form of `list_name.method()`

The `.append()` method allow you to add an element to the end of a list

Example (either ' or " can be used):

```
append_example = ["This", "is", "an", "example"]
append_example.append("list")

print(append_example)
```
... this will output:
```
['This', 'is', 'an', 'example', 'list']
```

# Accessing List Elements

Values within the list are assigned a number in the list, called an index. The index always starts at **0**, however will be referenced as the 1st value

Lets pull the 3rd value from the list below

```
my_list = ["Tom", "Elliot", "Harry", "Scott", "Fred"]

print(my_list[2])
```
... Harry will be outputted

Lets full the **1st value**, (index number 0) from the list:

```
my_list = ["Tom", "Elliot", "Harry", "Scott", "Fred"]

print(my_list[0])
```
... Tom will be outputted


# Negative Index

This can be used if you want to select the last item on the index, if you don't know what the last element index number is.

To use this, we need to set the index number as `[-1]`

```
my_list = ["Tom", "Elliot", "Harry", "Scott", "Fred"]

print(my_list[-1])
```
... Fred will be outputted

You can also use it to work back from the end of the list. Eg, `[-2]` would be the second from last, and so on


# Modifying List Elements

Elliot has left, and our new friend is Sam. We can replace Elliot with Sam by using the following code:

```
my_list = ["Tom", "Elliot", "Harry", "Scott", "Fred"]

my_list[1] = "Sam"

print(my_list)
```

# Removing List Elements

You can remove elements in a list by using the `.remove()` method.

Example:

```
my_list = ["Tom", "Elliot", "Harry", "Scott", "Fred"]
```
... we want to remove Harry

```
my_list.remove("Harry")
```
... Harry will be removed from the list


# Two-Dimensional Arrays (Lists)

We can add multiple lists into a single lists

Example:
```
people_plus_scores = [["Tom", 18], ["Elliot", 21], ["Harry", 14], ["Scott", 16], ["Fred", 9]]
```

If we wanted to append a sub-list to this list:

```
people_plus_scores.append(["Joseph", 15])
```

It may be easier to format 2D lists in a different way to help with understanding:
```
people_plus_scores = [
  ["Tom", 18],
  ["Elliot", 21],
  ["Harry", 14],
  ["Scott", 16],
  ["Fred", 9]
]
```

Accessing 2D lists is the same as a normal list, however we request 2 index values as opposed to 1.\
To get the value we use **row** and **column**. Example, we are looking for Scott's score:

```
scotts_score = people_plus_scores[3][1]
print(scotts_score)
```

Modifying two-dimensional lists works the same way. We are going to change Harry's score to 15:

```
people_plus_scores = [
  ["Tom", 18],
  ["Elliot", 21],
  ["Harry", 14],
  ["Scott", 16],
  ["Fred", 9]
]

people_plus_scores[2][1] = 15
```

Modifying with negative indices (counting back from the end value):

```
people_plus_scores = [
  ["Tom", 18],
  ["Elliot", 21],
  ["Harry", 14],
  ["Scott", 16],
  ["Fred", 9]
]

people_plus_scores[-3][-2] = 15
```
... this will change Harry's score to 15 using negative indices

___

Using `.remove`, we can remove data from a value within the list, it will remove the **first matching instance** of the value in a list/sub-list. Let's add another column to our list - age:

```
names_scores_age = [
  ["Tom", 18, 12],
  ["Elliot", 21, 13],
  ["Harry", 14, 12],
  ["Scott", 16, 12],
  ["Fred", 9, 13]
]
```
... Elliot does not want his age shown - lets remove it with `.remove`. We will need to input the **sub-list** of which the value exists:

```
names_scores_age = [
  ["Tom", 18, 12],
  ["Elliot", 21, 13],
  ["Harry", 14, 12],
  ["Scott", 16, 12],
  ["Fred", 9, 13]
]

names_scores_age[1].remove(13)
```

# Example of Usages

```
# Users, clothes size and whether they have expedited shipping
customer_data = [
  ["Ainsley", "Small", True],
  ["Ben", "Large", False],
  ["Chani", "Medium", True],
  ["Depak", "Medium", False]
]

# Modifying expedited shipping for Chandi to False
customer_data[2][2] = False
# Removing shipping preferences for Ben
customer_data[1].remove(False)

# Adding new clients
new_data = [
  ["Amit", "Large", True], ["Karim", "X-Large", False]
]
# Concatonating previous and new users in to new value
customer_data_final = customer_data + new_data

# Final values
print(customer_data_final)
```
