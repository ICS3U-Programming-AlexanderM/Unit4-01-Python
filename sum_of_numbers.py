#!/usr/bin/env python3

# Created by: Alexander Matheson
# Created on: Jan 5 2022
# This program asks the user to enter a number
# and then uses a loop to calculate and display the sum
# of all numbers from 0 until that number.

def main():
    # determine loop and sum variables
    loop = 0
    sum = 0

    # get the user input
    user_number_string = input("Enter your number: ")
    print("")

    # check inputs
    try:
        user_number = int(user_number_string)
    except Exception:
        print("Invalid input, must be an integer.")
        quit()

    # check if number is positive or 0
    if user_number < 0:
        print("Number must be equal or greater than 0")
        quit()

    # calculate the sum of all numbers from 0 to user number
    while (loop <= user_number):
        sum = sum + loop
        print("Tracking {} times through loop.". format(loop))
        loop = loop + 1

    print("")
    print("The sum of the numbers from 0 to {} is {}."
          . format(user_number, sum))


if __name__ == "__main__":
    main()
