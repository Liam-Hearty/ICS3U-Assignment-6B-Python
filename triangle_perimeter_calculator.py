#!/usr/bin/env python3

# Created by: Liam Hearty
# Created on: October 2019
# This program calculates perimeter of a triangle.


def calculate_perimeter(L1, L2, L3):
    # calculate perimeter and return perimeter

    import math

    # process
    perimeter = L1 + L2 + L3

    return perimeter


def main():
    # this function gets radius and height from user.

    try:
        # input
        length1_from_user = int(input("Enter the radius of a triangle (cm): "))
        length2_from_user = int(input("Enter the height of a triangle (cm): "))
        length3_from_user = int(input("Enter the height of a triangle (cm): "))
        print("")

        if (length1_from_user <= 0 or length2_from_user <= 0
           or length3_from_user <= 0):
            print("One of your values were less than 0, try again.")
            exit()

        # call functions
        perimeter = calculate_perimeter(length1_from_user,
                                        length2_from_user,
                                        length3_from_user)

        # output
        print("The perimeter is {} cm".format(perimeter))

    except ValueError:
        print("Please input a proper value.")


if __name__ == "__main__":
    main()
