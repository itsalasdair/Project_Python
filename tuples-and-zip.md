# Tuples

A data structure in Python that allow you to group and store multiple pieces of data inside of it.\
Similar to lists, how unlike lists, a Tuple cannot be changed (order, new, remove elements)



```
my_info = ("Mike", 24, "Programmer")
```
... if you then input `my_info` into the Python interpreter, the above information will be outputted

To access data within a tuple, this works the same as a list. If I wanted to access the 1st index element,\
you can do:

```
my_info[1]
```

**Immutable**

Once it has been configured, you cannot change/modify it.

**Unpacking a Tuple**

We have set up the follow:

```
my_info = ("Mike", 24, "Programmer")
```
.. we can now unpack it and assign variables to elements of the tuple:

```
name, age, occupation = my_info
```
... if we then input `name` into the console, `Mike` will be outputted

The number of elements in the tuple and number of variables must match.

To define a tuple, you must have 2 or elements, or you can: `one_element_tuple = (4,)`


## .zip()


The `.zip()` function allows you to quickly combine associated datasets together easily to form lists

Example:

```
names = ["Tom", "Elliot", "Harry", "Alex", "Phil"]
ages = [12, 12, 13, 11, 12]

names_and_ages = zip(names, heights)
```
... this would output something like this: `<zip object at 0x7fdce5edc940>`. This hash is where the data is stored in computer memory. You would then need to use `.list()` to view the contents:
```
converted_list = list(names_and_ages)
print(converted_list)
```

Output:
```
[('Tom', 12), ('Elliot', 12), ('Harry', 13), ('Alex', 11), ('Phil', 12)]
```
.. as you can see, the internal brackets of the list are `(`'s and not `[`'s, square brackets. This is because they are tuples.
