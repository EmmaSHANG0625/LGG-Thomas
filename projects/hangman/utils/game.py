import random

#Create Hangman class:
class Hangman: 
    def __init__(self):
        self.possible_words = ['becode', 'learning', 'mathematics', 'sessions', 'artificial', 'intelligence', 'technology']
        self.word_to_find = list(random.choice(self.possible_words))
        self.lives = 5
        self.correctly_guessed_letters = ['_'] * len(self.word_to_find)
        self.wrongly_guessed_letters = []
        self.turn_count = 0
        self.error_count = 0

    def get_guess(self) -> str:
        while True:
            guessed_letter = input("Enter a letter: ")
            if len(guessed_letter) != 1:
                print("Please entre a sigle letter!")
            elif guessed_letter in self.correctly_guessed_letters or guessed_letter in self.wrongly_guessed_letters:
                print("It has been already guessed, please enter another letter")
            else: 
                return guessed_letter

    def play(self):
        guessed_letter = self.get_guess()
        self.turn_count += 1

        if guessed_letter in self.word_to_find:
            for i, letter in enumerate(self.word_to_find):
                if letter == guessed_letter:
                    self.correctly_guessed_letters[i] = guessed_letter
            print("Good job! The letter is in the word.")
        else:
            self.wrongly_guessed_letters.append(guessed_letter)
            self.error_count += 1
            self.lives -= 1
            print(f"Sorry, the letter is not in the word. Lives left: {self.lives}")

        print(f"Wrong guess: {', '.join(self.wrongly_guessed_letters)}")
        print(f"Lives: {self.lives}, Erros: {self.error_count}, Turns: {self.turn_count}")
        print(f"Current word: {' '.join(self.correctly_guessed_letters)}")

    def start_game(self):
        while self.lives > 0 and '_' in self.correctly_guessed_letters:
            self.play()
           
            
        if self.lives == 0:
            self.game_over()
        
        else:
            self.well_played()
        

    def game_over(self):
        print("Game Over!")

    def well_played(self):
        word = ''.join(self.word_to_find)
        print(f"You found the word: {word} in {self.turn_count} turns with {self.error_count} errors!")




