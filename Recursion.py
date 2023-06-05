import sys  # Importing the sys module allows access to system-specific parameters and functions.

# Set the recursion limit to 50.
sys.setrecursionlimit(50)

# Print the current recursion limit.
print(sys.getrecursionlimit())

# Define a function called 'greet'.
def greatt():
    print("Hello")  # Print "Hello" to the console.
    greatt()  # Call the 'greet' function again, creating a recursive loop.

# Call the 'greet' function to start the recursive loop.
greatt()
