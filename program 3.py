from operator import truediv
'''
name = "vaibhav"
car = "maruti"
email = "vabkumar6@gmail.com"

print(f"your email is {email}")

distance = 5.5
print(f"you ran {distance}km")

is_online = False
if is_online:
    print("you are online")
else:
    print("you are ded")
'''

#TypeCasting - the processes of converting a variable from one data type to another
# str(), int(), float(), bool()
'''name = "vaibhav"
age = 19
gpa = 3.1
is_student = True

age = float(age)

print(age)'''

# Input() : A function that prompts the user to input data
# Returns the entered data as a string
'''
name = input("what is your name? :")
age = int(input("what is your age? :"))

# or we can change the entered data "string" to an int by adding int() ex:- age = int(age) ;)
age = age + 1
print(f"hello {name}!")
print("HAPPY BIRTHDAY!")
print(f"you are gonna be {age} years old!!")
'''
# Excersise 1 area of a rectangle
Length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
Area = Length * width
print(Area)
