#!/usr/bin/env python3

# Created by: Ntare Katarebe
# Created on: May 2021
# This program adds up your numbers
#    with numbers inputted from the user


def main():
    # This function adds up your numbers
    sum = 0

    # input
    adding_string = input("How many numbers are you going to add: ")
    # process/output
    try:
        adding = int(adding_string)
        for add in range(adding):
            add = int(input("Enter a number to add: "))
            if add < 0:
                continue
            sum = sum + add
        print("Sum of just the positive numbers is: {}".format(sum))
    except Exception:
        print("{} is not an integer".format(adding_string))
        print("\nDone.")


if __name__ == "__main__":
    main()
