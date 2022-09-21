import random

# Board with possible game status
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

# Variable used for chances used
n = 0


# Gets random words from file
def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()


# Transforms random word into usable variables and sets another for game progress
palavra = rand_word()
palavra2 = list(palavra)
c = ["_" for i in palavra]

# Main game loop
while n <= 6:
    print(board[n])
    print(" ".join(c))
    guess = str(input("\nletra: "))

    if guess not in palavra:
        print("errou")
        n += 1

    if guess in palavra:
        print("acertou")
        t = palavra2.index(guess)

        for i in palavra2:
            c[t] = guess
            palavra2[t] = '.'

        if c == list(palavra):
            print(board[n])
            print("".join(c))
            print("ganhou")
            break

    if n == 6:
        print("perdeu")
        print(f"a palavra era: {palavra}")
        break
