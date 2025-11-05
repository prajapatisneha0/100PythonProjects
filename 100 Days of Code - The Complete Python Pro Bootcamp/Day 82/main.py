
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----',
    ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.',
    '-': '-....-', '(': '-.--.', ')': '-.--.-'
}

MORSE_TO_TEXT = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z',
    '.----': '1', '..---': '2', '...--': '3', '....-': '4',
    '.....': '5', '-....': '6', '--...': '7', '---..': '8',
    '----.': '9', '-----': '0'
}


def text_to_morse(text):
    text = text.upper()
    morse_code = ""
    for char in text:
        if char != " ":
            morse_code += MORSE_CODE_DICT.get(char,"") + " "
        else:
            morse_code += "/ "
    return morse_code.strip()


def morse_to_text(morse_code):
    words = morse_code.split(" / ")
    text = ""
    for word in words:
        letters = word.split(" ")
        for letter in letters:
            text += MORSE_TO_TEXT.get(letter,"")
        text += " "
    return text.strip()


if __name__ == "__main__":
    while(1):
        user = int(input("Choose 1. Text to morse converter\n"
                     "2. Morse to text converter: "))
        if user == 1:
            user_input = input("Enter text to convert into Morse Code: ")
            result = text_to_morse(user_input)
            print(f"Morse Code: {result}")
        else:
            code = input("Enter Morse Code to convert into Text: ")
            print(f"Text: " ,morse_to_text(code))