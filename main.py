import pandas as pd

# Open file
df = pd.read_csv("morse_code.csv")
morse = df.to_dict()


# Ask user if they want to English(1) or Morse Code(2)
translate_to = input('\nEnglish -> Morse (E)\nMorse -> English (M)\nQuit (Q)\n').upper()
go_on = translate_to
phrase = input("\nEnter phrase to translate:\n").upper()

while go_on != 'Q':

    if translate_to == 'M':
        new_phrase = ''
        # split the input bc morse has a sace between letters
        phrase = phrase.split(' ')
        for letter in phrase:

            if letter == '':
                new_phrase += ' '
            else:
                translate = df[df['morse_code'] == letter]['english'].values[0]
                new_phrase += translate
    elif translate_to == 'E':
        new_phrase = ''
        for letter in phrase:
            if letter == ' ':
                new_phrase += ' '  # add two spaces between morse-words
            else:
                translate = df[df['english'] == letter]['morse_code'].values[0]
                new_phrase += translate + ' '  # add space between morse-letters

    print(new_phrase)
    # Get the next one and see if it should go on
    phrase = input().upper()
    go_on = phrase


print('Exiting')