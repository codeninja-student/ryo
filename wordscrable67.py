from random import shuffle
#input()
#print()
word_list = [
    "supercalifragilisticexpialidocious",
    "Pseudopseudohypoparathyroidism ",
    "Floccinaucinihilipilification",
    "pneumonoultramicroscopicsilicovolcanoconiosis",
    "hippopotomonstrosesquippedaliophobia",
]
def scramble_word(word):
    letter_list = list(word)
    shuffle(letter_list)
    scramble = "".join(letter_list)
    return scramble
def play_game():
    score = 0
    for word in word_list:
        mixed_word = scramble_word(word)
        print(f"\nUnscramble this word: {mixed_word}")
        guess = input("Your answer: ")
        if guess == word:
            print("ABSOLUTE CHEATER-------DONT CHEAT")
            print('''                /                                    \
                ________________________________________
                |  CAUGHT YOU! Stop checking my code!  |
                \____________________________________/
                        \
                         \
                          \      ▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄
                          |     █  ▀ █▄  ▄█ ▀  █
                          |    ▐▌    ▀▀  ▀▀    ▐▌
                          \   █▌ ▄▀▀▀▀▀▀▀▄    █▌
                              █  ▐▌  ▄▄  ▐▌   █
                              ▐▌  ▀▄▄▄▄▄▄▀   ▐▌
                              ▐▌             ▐▌''')
            score += 1
        else:
            print(f"TRY AGAIN IM ANGRY")
            print('''                █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█  
                      █   ▄▄▄      ▄▄▄   █
                      █  ▐▀▀▀██  ██▀▀▀▌  █
                      █   ▀▀▀▀    ▀▀▀▀   █
                      █       ▄██▄       █
                      █      ▐▀██▀▌      █
                      █       ▀██▀       █
                      █   ▄▄▄▄▄▄▄▄▄▄▄▄   █
                      █  ▐▀▀▀▀▀▀▀▀▀▀▀▀▌  █
                      █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█''')
    print(f"\nGame Over! Final score: {score}")
play_game()