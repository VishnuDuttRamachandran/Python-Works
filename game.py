import random
import tkinter as tk

# Set the list of words
words = ["apple", "banana", "orange", "grape", "strawberry"]

# Choose a random word from the list
word = random.choice(words)

# Set the maximum number of guesses
max_guesses = 3

# Set the number of remaining guesses to the maximum
remaining_guesses = max_guesses

# Set the running flag to True
running = True

# Create the main window
window = tk.Tk()
window.title("Wordle")

# Create a frame to hold the letter labels
frame = tk.Frame(window)
frame.pack()

# Create a list of letter labels
letters = []
for letter in word:
    label = tk.Label(frame, text=letter, font=("Helvetica", 36), width=2)
    letters.append(label)
    label.pack(side="left")

# Create a function to update the labels
def update_labels(guess):
    global remaining_guesses, running

    # Set the default label color to grey
    color = "grey"

    # Check if the guess is correct
    if guess == word:
        # Set the label color to green
        color = "green"
        # End the game
        running = False
    else:
        # Decrement the number of remaining guesses
        remaining_guesses -= 1

        # Check if the player has run out of guesses
        if remaining_guesses == 0:
            # End the game
            running = False
        else:
            # Check if any of the letters are in the guess
            for i, letter in enumerate(word):
                if letter in guess:
                    # Set the label color to yellow
                    color = "yellow"

    # Update the label colors
    for label in letters:
        label.configure(fg=color)

# Run the game loop
while running:
    # Check if the player has run out of guesses
    if remaining_guesses == 0:
        # Print a message and end the game
        print("You ran out of guesses! The word was:", word)
        running = False

        # Show the word
        for label, letter in zip(letters, word):
            label.configure(fg="black")
    else:
        # Get the player's guess
        guess = input("Enter your guess: ")

        # Update the labels
        update_labels(guess)

        # Update the window
        window.update()

# Print a message and end the game
print("Thanks for playing!")

# Run the tkinter event loop
window.mainloop()

