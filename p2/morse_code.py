MORSE_CODE_DICT = {'А': '.-', 'Б': '-...', 'В': '.--', 'Г': '--.', 'Д': '-..', 'Е': '.', 'Ж': '...-', 'З': '--..',
                   'И': '..', 'Й': '.---', 'К': '-.-', 'Л': '.-..', 'М': '--', 'Н': '-.', 'О': '---', 'П': '.--.',
                   'Р': '.-.', 'С': '...', 'Т': '-', 'У': '..-', 'Ф': '..-.', 'Х': '....', 'Ц': '-.-.', 'Ч': '---.',
                   'Ш': '----', 'Щ': '--.-', 'Ъ': '.--.-.', 'Ы': '-.--', 'Ь': '-..-', 'Э': '..-..', 'Ю': '..--',
                   'Я': '.-.-', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
                   '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--', ';': '-.-.-.',
                   ':': '---...', '?': '..--..', '!': '-.-.--', '-': '-....-', ' ': '\t'}

def encode_morse(text):
    morse_code = ''
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + ' '
    return morse_code

def decode_morse(morse_code):
    morse_code_dict_reverse = {v: k for k, v in MORSE_CODE_DICT.items()}
    decoded_text = ''
    morse_code_split = morse_code.split(' ')
    for code in morse_code_split:
        if code in morse_code_dict_reverse:
            decoded_text += morse_code_dict_reverse[code]
    return decoded_text

