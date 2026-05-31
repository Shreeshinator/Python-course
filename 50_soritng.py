# sorting in python

#---------LISTS---------
numbers = [5, 2, 9, 1, 5, 6
]   
numbers.sort()  # sorts in place

#---------TUPLES---------
points = [(2, 3), (1, 2), (4, 1)]
#tuples are immutable, so we use sorted() which returns a new sorted list
sorted_points = sorted(points)  # sorts by first element, then second if tie

#---------DICTIONARIES---------
students = {"Alice": 85, "Bob": 92, "Charlie": 78}

# sort by name (key)
sorted_by_name = dict(sorted(students.items()))# typecast to dict to get back a dictionary otherwise it returns a list of tuples
