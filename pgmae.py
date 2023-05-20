import random
import tkinter as tk

# create the main window
root = tk.Tk()
root.title("Number Guessing Game")

# generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# define the function to check the user's guess
def check_guess():
    # get the user's guess from the entry widget
    guess = int(guess_entry.get())
    # check if the guess is correct
    if guess == secret_number:
        result_label.config(text="Congratulations! You guessed the number.")
    # check if the guess is too low
    elif guess < secret_number:
        result_label.config(text="Your guess is too low. Try again.")
    # otherwise, the guess must be too high
    else:
        result_label.config(text="Your guess is too high. Try again.")

# create the widgets
guess_label = tk.Label(root, text="Guess a number between 1 and 100:")
guess_entry = tk.Entry(root)
guess_button = tk.Button(root, text="Guess", command=check_guess)
result_label = tk.Label(root, text="")

# add the widgets to the window
guess_label.pack()
guess_entry.pack()
guess_button.pack()
result_label.pack()

# start the main loop
root.mainloop()
