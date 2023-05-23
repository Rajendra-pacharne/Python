# Prompt the user to enter a year
year = int(input("Enter a Year: "))

# Check if the year is divisible by 4 and either not divisible by 100 or divisible by 400
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    # If the conditions are satisfied, it is a leap year
    print("Leap year")
else:
    # If the conditions are not satisfied, it is not a leap year
    print("Not a Leap year")


'''
Explanation:

The user is prompted to enter a year, and the input is stored in the year variable.
The code then checks the conditions for a leap year.
The first condition year % 4 == 0 checks if the year is divisible by 4. If it is not divisible by 4, it cannot be a leap year.
The second condition (year % 100 != 0 or year % 400 == 0) checks two sub-conditions:
year % 100 != 0 checks if the year is not divisible by 100. This condition excludes most century years (e.g., 1900, 2000) unless they are divisible by 400.
year % 400 == 0 checks if the year is divisible by 400. This condition ensures that century years divisible by 400 are considered leap years.
If both conditions are satisfied, the code prints "Leap year."
If any of the conditions are not satisfied, the code prints "Not a Leap year."
In summary, the code determines whether a given year is a leap year based on the rules: it should be divisible by 4, not divisible by 100 unless it is divisible by 400.

'''