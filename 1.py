#TOPIC-1
# TASK--3
#printing my name n greetings
print("My name is:ABC")
print("Hello everyone! Hope you're all doing great!")

# Task 5: Python script with explanatory comments
# This line prints the user's name
print("Name: ABC")
# This line stores a greeting message in a variable
greeting = "Good morning, everyone!"
# This line prints the greeting stored in the variable
print(greeting)
# We can also use string concatenation
print("Message: " + greeting)



#TOPIC-2
# Write a script to calculate the area and perimeter of a rectangle using variables.
length=20
width=30 
area=length*width
perimeter= 2*(length+ width)
print("The area of rectangle is:",area)
print("THe perimeter of rectangle is :",perimeter)

#Write a script that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number
a=int(input("enter first number: "))
b=int(input("enter second number: "))
if(a>b):
    print("first number is greater than second number")
elif(a<b):
    print("first number is smaller than second number")   
else:
    print("Both numbers  are equal") 

#Write a script that checks if a given year is a leap year (divisible by 4, but not by 100 unless also divisible by 400).         
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

#Write a script that concatenates two strings and prints the result.
s1="Hello Everyone!!"
s2="Good Morning!"
result=s1+s2
print("Concatinated string is:",result)



