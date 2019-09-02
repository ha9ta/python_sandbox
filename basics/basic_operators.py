# Python program for simple calculator


# Function to add two numbers
def add(num1, num2):
    return num1 + num2


# Function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2


# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2


# Function to divide two numbers
def divide(num1, num2):
    return num1 / num2


print("Please select operation -\n"
      "1. Add\n"
      "2. Subtract\n"
      "3. Multiply\n"
      "4. Divide\n")

# Take input from the user
# condition = True
# while condition:
#     select = input("Select operations form 1, 2, 3, 4 :")
#     number_1 = int(input("Enter first number: "))
#     number_2 = int(input("Enter second number: "))
#     condition = False
#     if select == '1':
#         print(number_1, "+", number_2, "=",
#               add(number_1, number_2))
#
#     elif select == '2':
#         print(number_1, "-", number_2, "=",
#               subtract(number_1, number_2))
#
#     elif select == '3':
#         print(number_1, "*", number_2, "=",
#               multiply(number_1, number_2))
#
#     elif select == '4':
#         print(number_1, "/", number_2, "=",
#               divide(number_1, number_2))
#     else:
#         print("Invalid input")
#         condition = True

condition = True
select = None
while condition:
    select = input("Select operations form 1, 2, 3, 4 :")
    if 1 < int(select) < 5:
        condition = False
    else:
        print('invalid input')

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
if select == '1':
    print(number_1, "+", number_2, "=",
          add(number_1, number_2))

elif select == '2':
    print(number_1, "-", number_2, "=",
          subtract(number_1, number_2))

elif select == '3':
    print(number_1, "*", number_2, "=",
          multiply(number_1, number_2))

else:
    print(number_1, "/", number_2, "=",
          divide(number_1, number_2))
