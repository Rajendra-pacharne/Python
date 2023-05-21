str=input("Enter a string")
ct=0
for i in str:
    if(i.islower()):
        ct=ct+1
if(ct>0):
    print("Count of lower case is ",ct)
else:
    print("There is no lower case character")


'''
Certainly! 

This code prompts the user to enter a string using the "input()" function and stores the user's input in the variable `str`. 

Next, it initializes a counter variable called `ct` to 0.

Then, it loops through each character in the input string by iterating through `str`.

For each character in the input string, the code checks if it is lowercase using the `islower()` string method. If the character is lowercase, it increments `ct` by 1.

After all the characters have been iterated over, the code checks if the value of `ct` is greater than 0. If it is, it prints the message "Count of lower case is [count]", where `count` is the final value of the `ct` variable. This indicates that there is at least one lowercase character in the input string. 

If the value of `ct` is not greater than 0, then it means that there are no lowercase characters in the input string, so the code instead prints the message "There is no lower case character".

Here's an example:

```
Enter a string: Hello, World!
Count of lower case is 8
```

In this example, the input string contains 8 lowercase characters, so the code prints the count of lowercase characters.

'''