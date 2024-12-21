# Subscripting 
print("Hello"[4])
print("Welcome"[-1])


# String 
print("123" + "456") # Concatenation


# Integer = Whole Number 
print(123 + 456)

# Large Integers
print(123_456_789) # its like the coma in the big numbers like 123,456,789

# Float = Floating Point Number 
print(3.14159)

# Boolean
print(True)
print(False)

print(len("123456"))

# How to find whats the type of anything
print(type("Hello"))
print(type(123))
print(type(123.4))
print(type(True))

# Convert String to Integer but should be numbers not characters
print(int("123") + int("456"))

# Task to fix the error 
print("Number of letters : " + str(len(input("Enter Name "))))

user_name = input("Enter Name ")
len_name = len(user_name)

print(type("The Number :")) # str
print(type(len_name)) # int

str_len = str(len_name)
print("The Number :" + str_len)


print("My age: " + str(12)) # str
print(123 + 456) # plus
print(7 - 5) # minus
print(3 * 2) # multiply 
print(5 / 3) # Divide float
print(5 // 3) # Divide int
print(2 ** 3) # power


# PEMDAS LR

# ()
# **
# * OR /
# + OR -

print(3 * 3 + 3 / 3 - 3)
print(3 * (3 + 3) / 3 - 3) # to make the output = 3

bmi = 84 / 1.65 ** 2
print(bmi)

print(int(bmi))
print(round(bmi)) # to the highest or loest int number
print(round(3.1))
print(round(3.9))
print(round(bmi, 2)) # to print 2 digets after the 0.0

score = 0
# score = score + 1
score += 1 
# += 
# -=
# *=
# /=
print(score)


# f-strings 
score = 0
height = 1.8
is_winning = True

print(f"Your Score is = {score}, your height is {height}, and you are winnig is {is_winning}")
