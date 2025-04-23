#!/usr/bin/env python3
# Created by: Viviana Hurtado
# Date: april 08 2025
# The program is allows the user to enter a positive number.
# It then uses a while loop to add up all the whole numbers, starting
# from 0, until that number and display the sum to the user. Make sure to
# “catch” any invalid entries so that your program does not crash.
def main():
    user_input = input("Enter a whole number: ")

    # Check for decimals
    if "." in user_input:
        print("Please enter a whole number.")

    try:
        number = int(user_input)
        counter = 0
        total_sum = 0

        if number >= 0:
            while counter <= number:
                total_sum += counter
                counter += 1
        else:
            while counter >= number:
                total_sum += counter
                counter -= 1

        print("The sum is:", total_sum)

    except:
        print(user_input, "is not a integer.")


if __name__ == "__main__":
    main()
