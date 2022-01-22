# Additional Python List Methods

... extended:

`.count()` - A list method to count the number of occurences of an element in a list\
`.insert()` - A list method to insert a value into a specific index number of a list\
`.pop()` - A list method to remove a value from a specific index number of a list\
`.range()` - A method function to create a sequence of Integers\
`.len()` - A list function to get the length of a list\
`.sort() / .sorted()` - A method function to sort a list\

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
