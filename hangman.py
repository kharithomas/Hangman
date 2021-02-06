# hangman game in python
# added visual of man's health 

import random
import string
from words import words


class Game:
    # returns valid word from words list
    def get_valid_word(self):
        word = random.choice(words)
        while '-' in word or ' ' in word:
            word = random.choice(words)
        return word.upper()

    # print man
    def print_man(self, lives: int):
        if lives == 6: print('   O\n - | -\n  / \\')
        elif lives == 5: print('   O\n - | -\n  /  ')
        elif lives == 4: print('   O\n - | -\n     ')
        elif lives == 3: print('   O\n - |  \n')
        elif lives == 2: print('   O\n -    \n')
        elif lives == 1: print('   O\n      \n')
        else: print('Your man has died!\n')

    def play_game(self):
        word = self.get_valid_word()
        word_letters = set(word)  # letters in our word
        alphabet = set(string.ascii_uppercase)  # full alphabet
        used_letters = set()  # currently picked letters
        health = 6  # amt of lives

        while len(word_letters) > 0 and health > 0:
            # print used letters
            print("Letters used: " + ' '.join(used_letters))
            self.print_man(health)

            # print current word
            word_list = [letter if letter in used_letters else '-' for letter in word]
            print("Current word: " + ' '.join(word_list))

            user_letter = input('Guess a letter: ').upper()
            # letter in available characters
            if user_letter in alphabet - used_letters:
                used_letters.add(user_letter)

                # letter exists in word
                if user_letter in word_letters:
                    word_letters.remove(user_letter)
                else:
                    health -= 1
                    print('Letter not in word!')

            elif user_letter in used_letters:
                print('Please use another letter!')
            else:
                print('Please use a valid character!')

        # player won or lost
        if health == 0:
            print('GAME OVER! The word was ', word)
        else:
            print('YOU WIN! The word was ', word)


game = Game()
game.play_game()
