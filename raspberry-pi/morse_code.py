# 100% NOT Paul Schakel, Spencer Crusse
# Morse Code Part 1

# This says what each letter is translated to in morse code
MORSE_CODE = { 'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-'}

while True:
    to_translate = input("Enter the phrase you would like translated: ") # Text shows upon code startup and allows you to type in a word after
    if to_translate == "-q": # If "-q" is typed and entered, the code finishes running 
        break
    translated = ""
    for char in to_translate: # Loop through message
        if char == " ": # Types "/" between words to show the division
            translated += "/"
        else:
            translated += MORSE_CODE[char.upper()] + " " # Runs the input letters through the dictionary and gives the output
    print(translated + "\n\n")
