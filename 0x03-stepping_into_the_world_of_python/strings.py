#!/usr/bin/python3

print("Today is a good day to learn Python")
print('Python is fun')
print("Python's string are easy to use")
print('We can even include "quotes" in strings')
print("hello" + " world")
greeting = "Hello"
name = "Tim"
print(greeting + name)

# if we want a space, we can add that too
print(greeting + ' ' + name)


age = 24
print(age)

print(type(greeting))
print(type(age))

# Here age is now bound to a string value.
# It's no longer an int, it's a string.
age = "2 years"
print(age)
print(type(age))


age_in_words = "2 years"
print(name + " is " + age + " years old")
print(type(age))
