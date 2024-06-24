# Hangman Game

## Description
Hangman is a classic and entertaining word-guessing game that is fun for all ages. Our game works as a word is randomly and automaticly choosed in a word-base, and the player attempts to figure out the word by suggesting individual letters. The player has 5 lives of incorrect guesses, and for each incorrect guess, they lose a life.

### Game Features
- Input Validation: Ensures the player enters only a single letter and has not guessed the letter before.
- Game State Display: Shows the current state of the word with correctly guessed letters and underscores for remaining letters, along with the number of wrong guesses, lives left, error count, and turn count.
- Feedback: Provides feedback after each guess, indicating whether the guess was correct or not.
- Game Over Conditions: The game ends with a "Game Over" message if the guesser runs out of lives, or a congratulatory message if the guesser successfully finds the word.

### Example Game Play
Chooser selects the word "python" and sets 5 lives.
Guesser starts guessing:
Guesses 'p': Correct! Current word: p _ _ _ _ _
Guesses 'x': Incorrect. Lives left: 4. Current word: p _ _ _ _ _
Guesses 'y': Correct! Current word: p y _ _ _ _
Guesses 'h': Correct! Current word: p y _ h _ _
Guesses 'o': Correct! Current word: p y _ h o _
Guesses 'n': Correct! Current word: p y _ h o n
Game Result: The guesser wins by finding the word "python".

## Installation & Usage
To get started with the project, follow these steps:

- copy the hangman folder and open it
- Make sure you have Python 3.x installed. You can download it from python.org.
- Run the main.py and follow the on-screen instructions.

## Contributor: Hui SHANG
