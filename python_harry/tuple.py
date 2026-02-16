single = (5,) # Single element tuple
print(type(single))

items = ("apple", "banana", "orange")
print(items[0])
print(items[2])

items = ("apple", "banana", "orange")
print(items[-1])
print(items[-2])

items = ("apple", "banana", "orange", "mango")
print(items[1:3])
print(items[:2])
print(items[2:])

items = ("apple", "banana", "orange")
#items[1] = "grapes"  # This will raise a TypeError because tuples are immutable

items = ("apple", "banana", "apple")
count = items.count("apple")
print(count)

items = ("apple", "banana", "orange")
position = items.index("banana")
print(position)

items = ("apple", "banana", "orange")
for item in items:
    print(item)


#Packing
#Multiple values can be packed into a tuple.
data = 10, 20, 30
print(data)

#Unpacking
#Tuple values can be unpacked into separate variables.
a, b, c = data
print(a, b, c)

#Converting Between List and Tuple
#You can convert a tuple to a list and vice versa.

items = ("apple", "banana")
items_list = list(items)
items_tuple = tuple(items_list)
print(items_list)
print(items_tuple)