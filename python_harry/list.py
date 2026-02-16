numbers = [1, 2, 3, 4]
names = ["Alice", "Bob", "Charlie"]
mixed = [1, "Python", 3.5, True]
print(mixed, names)

items = ["apple", "banana", "orange"]
print(items[0])
print(items[2])

print(items[-1])
print(items[-2])

items = ["apple", "banana", "orange", "mango"]
print(items[1:3])
print(items[:2])
print(items[2:])


items[1] = "grapes"
print(items)

items = ["apple", "banana", "orange"]
count = len(items)
print(count)

items = ["apple", "banana"]
items.append("orange")
print(items)

items = ["apple", "banana"]
items.insert(1, "orange")

items = ["apple", "banana"]
more_items = ["orange", "mango"]
items.extend(more_items)

items = ["apple", "banana", "orange"]
items.remove("banana")
items.pop()
print(items.pop(0))
print(items)

items = ["apple", "banana"]
items.clear()
print(items)

items = ["apple", "banana", "orange"]
position = items.index("banana")



items = ["apple", "banana", "apple"]
count = items.count("apple")
print(count)

numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)

numbers.sort(reverse=True)

numbers = [3, 1, 7, 5]
new_list = sorted(numbers)
print(new_list)

items = ["apple", "banana", "orange"]
items.reverse()
print(items)

items = ["apple", "banana"]
new_items = items.copy()
print(new_items)

items = ["apple", "banana", "orange"]
print("apple" in items)
print("grape" not in items)

items = [1, 2, 3]
items[0] = 10
print(items)