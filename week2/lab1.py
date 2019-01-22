# Program make a simple calculator that can add, subtract, multiply and divide

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

# Take input from the user 
choice = input("Enter choice(1/2/3/4):")

# Remember there is a difference between 4 and "4"
# "4" is the text representation of the number four
# 4 is a "integer". It is a actual number
# This is an important difference in Python

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Notice how I did choice == '1' instead of 
# choice == 1.
# The variable is the text, so it is different
# Also, you can use either double quotes (") or single quotes (')

# It is important to pay really close attention to detail when coding

# When print, using commas adds spaces for you

if choice == '1':
   print(num1,"+",num2,"=", num1+num2)

elif choice == '2':
   print(num1,"-",num2,"=", num1-num2)

elif choice == '3':
   print(num1,"*",num2,"=", num1*num2)

elif choice == '4':
   print(num1,"/",num2,"=", num1/num2)
else:
   print("Invalid input")