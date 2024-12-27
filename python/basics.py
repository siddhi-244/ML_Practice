# to print anything in the output window
# print("Hello World")

# indentation is very important in python

# Variables in python
# a = 23
# name = "Siddhi"

# print(name + " is "+ str(a) +" years old.")

# Casting
# x = str(3)    # x will be '3'
# y = int(3)    # y will be 3
# z = float(3)  # z will be 3.0

# print(x,y,z)


# get the type
# print(type(z))

# variable names are case sensitive as in a and A are 2 different variables

# multiple variables
# b , c = 'Hello' , 'Bye'
# print(b)
# print(c)

# same value can be assigned to multiple variables
# u = v = "Siddhi"
# print(u)
# print(v)

# Unpack a Collection
# fruits = ["Mango","Apple","Orange"]
# e , f, g = fruits
# print(e)
# print(f)
# print(g)

# Global Keyword
# Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
# To create a global variable inside a function, you can use the global keyword

# def myfunc():
#   global x
#   x = "fantastic"

# myfunc()

# print("Python is " + x)  

# Data Types 
"""
Text Type: 	str
Numeric Types: 	int, float, complex
Sequence Types: 	list, tuple, range
Mapping Type: 	dict
Set Types: 	set, frozenset
Boolean Type: 	bool
Binary Types: 	bytes, bytearray, memoryview
None Type: 	NoneType
"""

# x = 1    # int
# y = 2.8  # float
# z = 1j   # complex

# Slicing Strings
b = "Hello, World!"
# with start(inclusive) and end index(exclusive)
# print(b[2:5])
# # slicing from the start of the string
# print(b[:8])
# # slice till the end of string
# print(b[5:])
# # negative indexing - start with -1 from the end of the string
# print(b[-5:-2])

# print string in upper case
# print(b.upper())
# print string in lower case
# print(b.lower())
# remove white spaces - after and before a string
# print(b.strip())
# returns string
# print(b.replace("H", "J"))
# eturns a list where the text between the specified separator becomes the list items.
# print(b.split(","))

# format strings
# age = 36
# txt = f"My name is John, I am {age}"
# print(txt)

# lists - allows duplicate values
# thislist = ["apple", "banana", "cherry"]
# print(thislist)
# access item
# print(thislist[1])
# negative indexing - -1 represents last item
# print(thislist[-1])
# slicing
# print(thislist[1:3])
# changing list items
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)
# insert items
# thislist.insert(2, "watermelon")
# print(thislist)
# add an element at the end of the list
# thislist.append("chickoo")
# print(thislist)
# extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
# thislist.extend(('dh','dghdh'))
# print(thislist)
# remove item - remove() method removes the specified item
# thislist.remove('banana')
# print(thislist)
# If there are more than one item with the specified value, the remove() method removes the first occurrence:
# Remove Specified Index
# The pop() method removes the specified index. If you do not specify the index, the pop() method removes the last item.
# thislist.pop(1)
# print(thislist)
# The del keyword also removes the specified index:
# del thislist[0]
# print(thislist)
# delete the list completely
# del thislist
# print(thislist) - error as list is deleted
# clear list
# thislist.clear()
# print(thislist)

# Looping Lists
# for x in thislist:
#     print(x)
# looping using indexes
# for i in range(len(thislist)):
#     print(thislist[i],i)

# while loop
# i =0
# while i<len(thislist):
#     print(thislist[i])
#     i += 1

# looping using list comprehension - List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
# syntax - newlist = [expression for item in iterable if condition == True]
# [print(x) for x in thislist]

# sort list
# thislist.sort()
# print(thislist)
# sort in descending order
# thislist.sort(reverse=True)
# print(thislist)

# copy lists
# mylist = thislist.copy()
# print(mylist)
# another way to copy list
# mylist = list(thislist)
# print(thislist)
# using slice operator
# mylist = thislist[:]
# print(mylist)

# join two lists
# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]

# list3 = list1 + list2
# list2.extend(list1)
# print(list2) 

# Tuples
# thistuple = ("apple", "banana", "cherry")
# print(thistuple)
# access element
# print(thistuple[1])
# to update tuples we can either convert it to a list or make new tuples since tuples are immutable
# unpack a tuple
# (a,b,c) = thistuple
# print(a,b,c)


# Sets - A set is a collection which is unordered, unchangeable*, and unindexed.
# myset = {"apple", "banana", "cherry"}
# print(myset)
#  Sets are unordered, so you cannot be sure in which order the items will appear.
# duplicates are not allowed in a set
# The values True and 1 are considered the same value in sets, and are treated as duplicates:

# another way to make sets
# thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
# print(thisset) 

# access set items
# for x in thisset:
#   print(x) 

#   check if element is present in set
# print("banana" in thisset)
# print("banana" not in thisset)

# Once a set is created, you cannot change its items, but you can add new items.
# thisset.add('mango')
# print(thisset)

# To add items from another set into the current set, use the update() method.
# tropical = {"pineapple", "mango", "papaya"}

# thisset.update(tropical)

# print(thisset)

# you can add any iterable in a set
# mylist = ["kiwi", "orange"]
# thisset.update(mylist)
# print(thisset)

# remove item from a set
# If the item to remove does not exist, remove() will raise an error.
# thisset.remove("banana")
# If the item to remove does not exist, discard() will NOT raise an error.
# thisset.discard("cherry")
# print(thisset) 

# The union() method returns a new set with all items from both sets.

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}

# set3 = set1.union(set2)
# print(set3) 

# join a set and tuple
# x = {"a", "b", "c"}
# y = (1, 2, 3)

# z = x.union(y)
# print(z) 

# The intersection() method will return a new set, that only contains the items that are present in both sets.
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1.intersection(set2)
# print(set3) 

# You can use the & operator instead of the intersection() method, and you will get the same result.


# Dictionaries
# Dictionaries cannot have two items with the same key:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# print(thisdict)

# access item
# print(thisdict["brand"])

# print(thisdict.get("model"))

# get all keys
# print(thisdict.keys())
# get all values
# print(thisdict.values())
# add new values
# thisdict["name"] = "xyz"
# print(thisdict)
# change values
# thisdict["brand"] = "xyz"
# print(thisdict)

# remove items
# thisdict.pop("model")
# print(thisdict) 

# empty the dict
# thisdict.clear()
# print(thisdict) 

# copy dictionaries 
mydict = thisdict.copy()
print(mydict)

