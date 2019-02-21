# Lottery Numbers
import random


def generateLottoNumbers():
    # Initialise an empty list that will be used to store the 6 lucky numbers!
    lottery_numbers = []

    for i in range(0, 6):
        number = random.randint(1, 90)
        # Check if this number has already been picked and ...
        while number in lottery_numbers:
            # ... if it has, pick a new number instead
            number = random.randint(1, 90)

        # Now that we have a unique number, let's append it to our list.
        lottery_numbers.append(number)

    # Sort the list in ascending order
    lottery_numbers.sort()

    # Display the lsit on screen:
    print(">>> Today's lottery numbers are: ")
    print(lottery_numbers)
    return lottery_numbers


print("Enter your lotto numbers (5 number):  ")
count = 0
tip_lst = []

while count < 5:
    # get the exception of the casting
    try:
        num = int(input("Give number " + str(count + 1) + ":"))
    except ValueError:
        print("Please give a number")
        continue
    # check if the numbers are unique
    if num in tip_lst:
        print("Please give a unique number")
        continue
    # check if the numbers are between 1 - 90
    if num <= 0 or num > 90:
        continue

    tip_lst.append(num)
    count += 1

tip_lst.sort()
print("Tip numbers: " + str(tip_lst))

lottery_numbers = generateLottoNumbers()
if tip_lst == lottery_numbers:
    print("You won. Let's buy a ferrari.")
else:
    print("You didn't won. Let's get the bus.")
