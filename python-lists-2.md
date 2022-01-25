# Additional Python List Methods

... extended:

`.count()` - A list method to count the number of occurences of an element in a list\
`.insert()` - A list method to insert a value into a specific index number of a list\
`.pop()` - A list method to remove a value from a specific index number of a list\
`.range()` - A method function to create a sequence of Integers\
`.len()` - A list function to get the length of a list\
`.sort() / .sorted()` - A method function to sort a list\


**.count()**

'.count can be used to show the number of occurences of a single value within a list.

Lets find out how many `e`'s are in trees.

```
my_word = ["t", "r", "e", "e", "s"]
how_many_letters = my_word.count("e")
print(how_many_letters)
```
... 2!

Another example:

```
my_numbers = [100, 20, 50, 100, 200, 10, 400, 50, 100, 200, 100]

how_many_times = my_numbers.count(100)
print(how_many_times)
```
... 4!

Now lets find matching variables in a 2D list - lets looks for `[100, 50]`:

```
my_numbers = [
  [100, 50],
  [50, 20],
  [200, 100],
  [100, 50],
  [50, 50],
  [100, 50]
]

how_many_list = my_numbers.count([100, 50])
print(how_many_list)
```
... 3!


**.insert()**

The .insert() method takes two inputs, the index location you want to insert to, and the value. Negative indices can be used.

Example, our students are in a line to go to the canteen:

```
in_line = [
  ["Tom"],
  ["Elliot"],
  ["Harry"],
  ["Scott"],
  ["Fred"]
]
```
... however, Alex needs to get in before Harry - we can do this like so:

```
in_line.insert(2, ["Alex"])
```

**.pop()**

This method allows you to remove values from the list.\
You can remove the last value by just using `myList.pop()` or by specifying an index number `myList.pop(2)`.

```
myList = ["Elephants", "Tigers", "Koalas", "Trees"]
```
... Trees aren't animals, so lets remove it by removing the last value
```
myList.pop()
```
... this will remove the last value.

Lets remove Tigers too:
```
myList = ["Elephants", "Tigers", "Koalas"]
myList.pop(1)
```
... this will remove Tigers


**.range()**

If we want to create a range/array of indexed numbers, we can do so with `.range()`.\
The first number will be 0, so to make 0-10 we would use:

```
myRange = range(11)
```
... this would output `range(0, 10)`, not a full list. To view this as a list, we have to make use of the `.list()` module.

```
myRange = range(11)
print(list(myRange))
```
... this would output `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`

If you wanted to start your range at another number, you can do so - if we wanted to go from 2-20:
```
myRange = range(2,21)
# Remember (2,20) would not show the number 20
```

The third input will "skip" numbers. `range(2, 9, 2)` would start from to, end at 8 but go up in 2's.

```
newRange = range(1, 100, 10)
print(list(newRange))
```
... this would start at one, go up in 10's until it can get as near as 100 as possible.\
In this case, it would be: `[1, 11, 21, 31, 41, 51, 61, 71, 81, 91]`

Another example:

```
newRangeTwo = range(0, 40, 5)
print(list(newRangeTwo))
```
... output: `[0, 5, 10, 15, 20, 25, 30, 35]`. To include 40, we would change range to `range(0, 41, 5)`.


**.len()**

This module displays the number of items in a list.

```
superLongList = [1, 5, 5, 2, 6, 2, 7, 3, 6, 7]
print(len(superLongList))
```
... output: `10`


To return the length of a list you can also do `mylist.len()`


**.sort()**

Sorting index elements into alphabetical or numerical order can be done with `.sort()`. It modifies the existing list.

Lets sort this list of names into alphabetical order:
```
sort_me = ["Alex", "Tom", "Fred", "Boris", "Matt"]
sort_me.sort()

print(sort_me)
```
or
```
sort_me = ["Alex", "Tom", "Fred", "Boris", "Matt"]
sorted = sort_me.sort()
```

If you wanted to sort in **descending** order or **Z-A** just `sort_me(reverse=True)`.

___

The `.sorted()` function is different from the `.sort()` function\
Instead of modifying the existing list, it creates a new list and modifies that

We have a list of names `pre_sorted_names`, we would like a new list called `sorted_names`:

```
pre_sorted_names = ["Mike", "Tom", "Elliot", "Brad", "Timothy", "Scott"]

sorted_names = sorted(pre_sorted_names)

print(sorted_names)
```
... output: `['Brad', 'Elliot', 'Mike', 'Scott', 'Timothy', 'Tom']`


**Slicing Lists I**

You can capture a portion of a list by slicing the list and getting the information you want.

```
my_list = ["a", "b", "c", "d", "e", "f", "g"]
```
... we can grab from `b` to `f` through indexing, by running:
```
my_list = ["a", "b", "c", "d", "e", "f", "g"]

sliced_list = my_list[1:6]
print(sliced_list)
```
... we can then print the output with `print(sliced_list)`

The end of your slice must finish on the number **after** your intended stop.

Example, if I wanted the numbers 0-5 (0, 1, 2, 3, 4, 5), we would slice `[0:6]`. The slice would be terminated **on** 6, so would not include 6.


**Slicing Lists II**

With slicing you can also just specify the end index value, instead of including a starting index value:
```
my_list = ["a", "b", "c", "d", "e", "f", "g"]
new_sliced_list = my_list[:4]
```
... output: `['a', 'b', 'c', 'd']`


To slice the *last* index element in a list, we can use `my_list[-n:]`. For the last 2 values, `my_list[-2:]`

If you **just** want the last `n` of values at the end, we can do `my_list[:-2]`. This would output the **last 2** values


# Lists Review

```
# Inventory list
inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

# Owner would like to know how many items are in the list
inventory_len = len(inventory)

# Select the first element in `inventory` and save it to a variable called 'first'
first = inventory[0]
# Select the last element in 'inventory' and save it to  a variable called 'last'
last = inventory[-1]
# Select items from 'inventory' starting from 2 and up to, but not including 6
inventory_2_6 = inventory[2:6]
# Select first 3 items of inventory
first_3 = inventory[0:3]
# How many 'twin bed's in 'inventory'?
twin_beds = inventory.count("twin bed")
# Remove the 5th element of inventory
removed_item = inventory.pop(4)
# Add new item with .insert() as 11th element
inventory.insert(10, "19th Century Bed Frame")
# Sort 'inventory' with either .sort or .sorted ***
inventory.sort()

print(inventory)


# *** Remember, the sorted() function doesn’t change the original list — it creates a new list with the elements properly sorted. If you use sorted() you’ll have to set inventory equal to the value returned by sorted().
```
