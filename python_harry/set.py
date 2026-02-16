numbers = {1, 2, 3, 4}
names = {"Alice", "Bob", "Charlie"}

empty_set = set()
print(type(empty_set))  # it prints <class 'set'>

numbers = {1, 2, 2, 3, 3, 4}
print(numbers)  # it prints {1, 2, 3, 4}

items = {"apple", "banana", "orange"}
for item in items:
    print(item)

items = {"apple", "banana"}
items.add("orange")
print(items)

items = {"apple", "banana"}
items.update(["orange", "mango"])
print(items)

items = {"apple", "banana"}
items.remove("banana")
print(items)  # it prints {'apple'}

items = {"apple", "banana"}
items.discard("grapes")
print(items)  # it prints {'apple', 'banana'}

items = {"apple", "banana", "orange"}
items.pop()
print(items)  # it prints the set with one item removed

items = {"apple", "banana"}
items.clear()
print(items)

a = {1, 2, 3}
b = {3, 4, 5}

result = a.union(b)
print(result)  # it prints {1, 2, 3, 4, 5}

result = a.intersection(b)
print(result)  # it prints {3}

result = a.difference(b)
print(result)  # it prints {1, 2}

result = a.symmetric_difference(b)
print(result)  # it prints {1, 2, 4, 5}

items = {"apple", "banana", "orange"}
print("apple" in items)

#Sets are Mutable
#Sets can be modified after creation.
items = {"apple", "banana"}
items.add("orange")
print(items)  # it prints {'apple', 'banana', 'orange'}
