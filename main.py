import pandas as pd

# Open file
df = pd.read_csv("morse_code.csv")
morse = df.to_dict()

# Ask user what way to translate
translate_from = input('\nEnglish -> Morse   (E)\nMorse   -> English (M)\n           Quit    (Q)\n').upper()
go_on = translate_from
# Gets initial phrase
phrase = input("\nEnter phrase to translate:\n").upper()

# Continues till user types Q
while go_on != 'Q':

    # --------MORSE TO ENGLISH-------- #
    if translate_from == 'M':
        new_phrase = ''
        # split the input bc morse has a space between letters
        phrase = phrase.split(' ')
        for letter in phrase:
            if letter == '':
                new_phrase += ' '
            else:
                translate = df[df['morse_code'] == letter]['english'].values[0]
                new_phrase += translate
    # --------ENGLISH TO MORSE-------- #
    elif translate_from == 'E':
        new_phrase = ''
        for letter in phrase:
            if letter == ' ':
                new_phrase += ' '  # add two spaces between morse-words
            else:
                translate = df[df['english'] == letter]['morse_code'].values[0]
                new_phrase += translate + ' '  # add one space between morse-letters

    print(new_phrase)
    # Get the next phrase and see if it should continue
    phrase = input().upper()
    go_on = phrase

print('Exiting')
