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

**List Methods**

Methods, and List Methods allow you to create, manipulate and delete data within a variable.

The ```.append()``` method allow you to add an element to the end of a list

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

**Accessing List Elements**

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


**Negative Index**

This can be used if you want to select the last item on the index, if you don't know what the last element index number is.

To use this, we need to set the index number as ```[-1]```

```
my_list = ["Tom", "Elliot", "Harry", "Scott", "Fred"]

print(my_list[-1])
```
... Fred will be outputted


**Modifying List Elements**

Elliot has left, and our new friend is Sam. We can replace Elliot with Sam by using the following code:

```
my_list = ["Tom", "Elliot", "Harry", "Scott", "Fred"]

my_list[1] = "Sam"

print(my_list)
```

**Removing List Elements**

You can remove elements in a list by using the ```.remove()``` method.

Example:

```
my_list = ["Tom", "Elliot", "Harry", "Scott", "Fred"]
```
... we want to remove Harry

```
my_list.remove("Harry")
```
... Harry will be removed from the list


**Two-Dimentional (2D) Lists**

We can add multiple lists into a single lists

Example:
```
people_plus_heights = [["Tom", 18], ["Elliot", 21], ["Harry", 14], ["Scott", 16], ["Fred", 9]]
```

If we wanted to append a sub-list to this list:

```
people_plus_heights.append(["Joseph", 15])
```
