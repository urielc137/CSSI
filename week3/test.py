#!/usr/bin/env python
#print ("hello cssi")
#print ("hello cssi")
#print ("hello cssi")

#name = "Bob"
#name = 55
#print(name)

#name = raw_input("Enter name: ")
#print("Hi there...")
#print(name)

#print("na " * 16)
#print("BATMAN")

#user_input = raw_input("Enter anything: ")
#print("You entered a ", str(type(user_input)))
print("raw_input gives us strings")
num1 = raw_input("Enter number #1: ")
num2 = raw_input("Enter number #2: ")
print(num1+num2)
print(type(num1+num2))

print("int(raw_input) gives us int")
num1 = int(raw_input("Enter number #1: "))
num2 = int(raw_input("Enter number #2: "))
print(num1+num2)
print(type(num1+num2))

num = int(raw_input("Enter a number: "))
if num > 0:
    print("That's a positive number!")
elif num < 0:
    print("That's a negative number!")
else:
    print("Zero is neither posiitve or negative")

#age = 20
#if x > 18:
#    print("You can buy lottery tickets")

#    if x > 25:
#        print("You can also rent a car!")
#    print("And you can get your own credit card!")
#print("End Program.")

string = "hello there"
for letter in string:
    print(letter.upper())
