# Jaden Russell
# 11/2/2022
# SDEV 300

"""This program creates and presents the user with a
menu of multiple functions, and performs the desired function upon the user's input"""
import string
import secrets
from datetime import date
import math


def pass_gen(pass_length, upper_use, num_use, spec_use):
    """Defines the code of the program in pass_gen"""
    characters = string.ascii_lowercase
    if upper_use == 'y':
        characters = characters + string.ascii_uppercase
    if num_use == 'y':
        characters = characters + string.digits
    if spec_use == 'y':
        characters = characters + string.punctuation
    return ''.join(secrets.choice(characters) for i in range(pass_length))


def percent_calc():
    """Defines the code of the program in percent_calc"""
    numerator = float(input("Enter the numerator of your percentage"))
    while numerator < 0:
        numerator = float(input("The number you entered is invalid, please re-enter"))

    denominator = float(input("Enter the denominator of your percentage"))
    while denominator < 0:
        denominator = float(input("The number you entered is invalid, please re-enter"))

    places = int(input("Enter the number of decimal places to show"))
    while places < 0:
        places = int(input("The number you entered is invalid, please re-enter"))
    percent = (numerator / denominator) * 100

    print(f"The percentage of your numbers is: {percent : .{places}f}")


def days_from():
    """Defines the code of the program in days_from"""
    today = date.today()
    future = date(2025, 6, 4)
    days_apart = future - today
    return days_apart.days


def side_calc():
    """Defines the code of the program in side_calc"""
    a_side = int(input("Enter the length of side a of the triangle"))
    while a_side <= 0:
        a_side = int(input("The number you entered is invalid, please re-enter"))

    b_side = int(input("Enter the length of side b of the triangle"))
    while b_side <= 0:
        b_side = int(input("The number you entered is invalid, please re-enter"))

    c_angle = int(input("Enter the degrees of angle C of the triangle"))
    while c_angle <= 0:
        c_angle = int(input("The number you entered is invalid, please re-enter"))

    a_square = math.pow(a_side, 2)
    b_square = math.pow(b_side, 2)
    c_cos = math.cos(math.radians(c_angle))
    c_side = math.sqrt(a_square + b_square - (2 * a_side * b_side) * c_cos)
    return c_side


def vol_calc():
    """Defines the code of the program in vol_calc"""
    radius = int(input("Enter the radius of the cylinder"))
    while radius <= 0:
        radius = int(input("The number you entered is invalid, please re-enter"))

    height = int(input("Enter the height of the cylinder"))
    while height <= 0:
        height = int(input("The number you entered is invalid, please re-enter"))

    volume = (math.pi * math.pow(radius, 2)) * height
    return volume


def main():
    """Defines the code of the program in main"""
    print("Welcome to function variety program!\nWhich function would you like to perform?")
    print("1. Generate a secure password)
    print("2. Calculate and formulate a percentage")
    print("3. Find the number of days from today to July 4, 2025")
    print("4. Calculate the leg of a triangle")
    print("5. Calculate the volume of a right circular cylinder")
    print("6. Exit the program\n")
    choice = 0

    while choice > 6 or choice < 1:
        try:
            choice = int(input("Please enter the number of one of the six choices."))
        except:
            print("Your input was invalid, please re-enter.")
    if choice == 1:
        p_length = int(input("What is the length of your password?"))
        while p_length < 5:
            p_length = int(input("Your password is too short, please re-enter"))

        p_upper = input("Will your password include uppercase letters? (y/n)")
        while p_upper not in ('n', 'y'):
            p_upper = input("Your input is invalid, please re-enter")

        p_num = input("Will your password include numbers? (y/n)")
        while p_num not in ('n', 'y'):
            p_num = input("Your input is invalid, please re-enter")

        p_spec = input("Will your password include special characters? (y/n)")
        while p_spec not in ('n', 'y'):
            p_spec = input("Your input is invalid, please re-enter")

        print(f"Your secure password is {pass_gen(p_length, p_upper, p_num, p_spec)}")

    elif choice == 2:
        percent_calc()

    elif choice == 3:
        print(f"There are {days_from()} days until June 4, 2025")

    elif choice == 4:
        print(f"The length of side c of the triangle is {side_calc():.2f}")

    elif choice == 5:
        print(f"The volume of the right circular cylinder is {vol_calc():.2f}")
    print("Exiting the program. Thank you for using this program!")


main()
