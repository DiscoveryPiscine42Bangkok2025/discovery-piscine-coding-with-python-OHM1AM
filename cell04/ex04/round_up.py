import math

number = input("Give me a number: ")

try:
    num = float(number)
    rounded_num = math.ceil(num)
    print(rounded_num)
except ValueError:
    print("That's not a valid number.")