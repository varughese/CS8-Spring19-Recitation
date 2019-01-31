# Python program that play guess game with a user
from random import randint

#This allows to the user to input his first number
user_number=int(input("Guess the number:"))
number = randint(1, 10)
while number!= user_number:
	user_number=int(input("Guess the number:"))
print("Yay :), you found it!")