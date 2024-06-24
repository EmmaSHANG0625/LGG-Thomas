xdesc#Write a function which prompts the chooser player for his word and returns that word
def get_word() -> str:
    word = input("Entre a word: ")
    return word
    
#Write a function which prompts the chooser player for a number of lives and returns this number of lives
def get_lives() -> str:
    number_of_lives = int(input("Entre a number of lives: "))
    return number_of_lives

#Write a function which takes as argument:
def get_guess(suggested_letters) -> str:
    guessed_letter = input("Entre a letter")
    if len(guessed_letter) != 1:
        print("Please entre a sigle letter!")
    elif guessed_letter in suggested_letters:
        print("It has been already guessed, please enter another letter")
    else: 
        return guessed_letter
 
#Write a function outputs if the guess is correct or not and returns the current lives of the player depending on the outcome of the guess:
def assess_guess(secret_word: str, guessed_letter: str, lives_left: str): 

    if guessed_letter in secret_word:
        print("You got the correct letter!")
        return lives_left
    else:
        print("This letter is not in the word.")
        lives_left -= 1
        return lives_left
        
#Write a function which displays the secret word with white spaces between the letters, hiding the non-guessed letters by replacing them with '_'; returns True if the correct word has been found, False otherwise:
def display_word(secret_word: str, suggested_letters: list):
    for letter in secret_word:
        if letter in suggested_letters:
            display += letter + ' '
        else: 
            display += '_' 
        
    print(display)
    return '_' not in display

#A main() function which orchestrates a full game
def main():
    secret_word = get_word()
    lives = get_lives()
    suggested_letters = []
    
    while lives > 0: 
        guessed_letter = get_guess(suggested_letters)
        suggested_letters.append(guessed_letter)
        lives = assess_guess(secret_word, guessed_letter, lives)
        
        if display_word(secret_word, guessed_letter):
            print("congratulations! You've got the word!")
            return    

    print(f"Game over! The secret word was: {secret_word}")

    if __name__ == "__main__": 
        main()
