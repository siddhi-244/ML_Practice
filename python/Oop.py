# class myClass:
#     x = 7

# create object
# p1 = myClass()
# access a property
# print(p1.x)

# All classes have a function called __init__(), which is always executed when the class is being initiated. - bsically a constructor
# The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
# It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any function in the class

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def __str__(self):
#     return f"{self.name}({self.age})"
# functions in a class
#   def myfunc(self):
#     print("Hello my name is " + self.name + " and my age is " + str(self.age))

# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age) 

# The __str__() function controls what should be returned when the class object is represented as a string.
# print(p1)
# modify object properties
# p1.age = 40
# del obj property
# del p1.age 
# p1.myfunc()
# del obj
# del p1 

# inheritance
# Person is the parent class here
# The child's __init__() function overrides the inheritance of the parent's __init__() function.
# class Student(Person):
#   pass

# Now the Student class has the same properties and methods as the Person class.
# obj1 = Student("Siddhi",23)
# obj1.myfunc()

# class Student(Person):
#   # When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
#   # To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
#   def __init__(self, fname, age, year):
#     # Person.__init__(self, fname, lname) 
#     # Python also has a super() function that will make the child class inherit all the methods and properties from its parent:
#     super().__init__(fname,age)
#     # add properties
#     self.graduationyear = year
#   def welcome(self):
#     print("Welcome", self.name, "to the class of", self.graduationyear) 
# x = Student("Mike", 25, 2027) 
# x.welcome()

# Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.

# All these objects have a iter() method which is used to get an iterator:
# mytuple = ("apple", "banana", "cherry")
# myit = iter(mytuple)

# print(next(myit))
# print(next(myit))
# print(next(myit))


# Polymorphism
# methods/functions/operators with the same name that can be executed on many objects or classes. - function overloading

