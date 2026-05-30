#collectins are data structures that can hold multiple items. They include lists, tuples, sets, and dictionaries.
#list is a collection of items that are ordered and changeable. It allows duplicate members.
#set is a collection of items that are unordered and unindexed. It does not allow duplicate members.
#tuple is a collection of items that are ordered and unchangeable. It allows duplicate members.
#dictionary is a collection of items that are unordered, changeable, and indexed. It does not allow duplicate members.

fruits = ("apple", "banana", "cherry") #tuple
# fruits [ apple, banana, cherry] list
# fruits = {"apple", "banana", "cherry"} #set
# fruits = {"apple": "red", "banana": "yellow", "cherry": "red"} #dictionary

# fruits.append("orange")  # This would cause an error since tuples are immutable

print(fruits)  # ('apple', 'banana', 'cherry')
for x in fruits:
    print(x) # apple banana cherry
