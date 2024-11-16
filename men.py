# Dodatkowe (niewymagane)
# 12. Gramy w szubienicę tekstowo

import random

def draw_word():
    words = [
        'politechnika',
        'lodz',
        'programowanie',
        'gornik',
        'konstantynopolitanczykowianeczka',
        'python',
        'aleksander',
        'ryba'
    ]
   
    return random.choice(words)

def display_board(guessed_letters, word):
    for letter in word:
        if letter in guessed_letters:
            print(letter, end=" ")
        else:
            print('_', end=" ")
    print()  

def play_game():
    stages = [
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / 
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |    
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |    
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |    |
           |    
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |    
           |    
           |
        --------
        """,
        """
           ------
           |    |
           |    
           |    
           |    
           |
        --------
        """,
        """
           ------
           |    
           |    
           |    
           |    
           |
        --------
        """,
        """
           
           |    
           |    
           |    
           |    
           |
        --------
        """,
        """
        --------
        """,
    ]


    guessed_letters = []
    max_attempts = 10
    word = draw_word()
    attempts_left = max_attempts

    while attempts_left > 0:
        display_board(guessed_letters, word)
        print(f'Pozostała liczba prób: {attempts_left}')    
        player_guess = input("Podaj literę lub zgadnij całe słowo: ").lower()

        if player_guess == word:
            print(f'Gratulacje, wygrałeś! Słowo: {word}\nLiczba prób: {max_attempts - attempts_left + 1}')
            break

        if player_guess in guessed_letters:
            print("Już podałeś tę literę, spróbuj ponownie.")
            continue

        if len(player_guess) == 1:
            guessed_letters.append(player_guess)
            if player_guess in word:
                print(f"Litera '{player_guess}' znajduje się w słowie!")
            else:
                print(f"Niestety, litera '{player_guess}' nie znajduje się w słowie.")
                attempts_left -= 1  
                print(stages[attempts_left])
        else:
            print("Nieprawidłowy wpis. Wprowadź pojedynczą literę lub zgadnij całe słowo.")
            continue

        word_guessed = True
        for letter in word:
            if letter not in guessed_letters:
                word_guessed = False
                break
        
        if word_guessed:
            print(f'Gratulacje odgadłeś słowo: {word}')
            break

    else:
        print(f"Koniec gry! Prawidłowe słowo to: {word}")

if __name__ == "__main__":
    input("Wciśnij ENTER, aby rozpocząć grę ")
    play_game()


