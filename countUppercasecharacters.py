str=input("Enter a string")
ct=0
for i in str:
    if(i.isupper()):
        ct=ct+1
if(ct>0):
    print("Count of Upper case is ",ct)
else:
    print("There is no Upper case character")


'''
This is a Python code that accepts an input string from the user and counts the number of uppercase characters in it. It then prints either the count of uppercase characters or a message indicating there are no uppercase characters.

Here's what each line of the code does:

- `str=input("Enter a string")`: This prompts the user to enter a string and assigns the user's input to a variable named `str`.

- `ct=0`: This initializes a variable named `ct` to 0, which will keep track of the number of uppercase characters in the input string.

- `for i in str:`: This starts a loop that iterates through each character in the input string.

- `if(i.isupper()):`: This if statement checks if the current character being iterated over is an uppercase letter using the `isupper()` method provided by Python for string objects. If the condition is true, it increments the counter variable (`ct`) by 1.

- `if(ct>0):`: This checks if the value stored in the `ct` variable is greater than 0. If this condition is true, it means that there was at least one uppercase character in the input string, so it prints a message saying how many uppercase characters were found.

- `print("Count of Upper case is ",ct)`: This prints the message "Count of Upper case is" followed by the value stored in the `ct` variable.

- `else:`: If the `if` condition above evaluates to `False`, this clause is executed instead.

- `print("There is no Upper case character")`: This line simply prints the message "There is no Upper case character" as there are no uppercase characters found in the input string.

Overall, this code provides a simple way of counting the number of uppercase characters in a string and printing out a message accordingly.

'''