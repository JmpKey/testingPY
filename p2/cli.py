from morse_code import encode_morse, decode_morse

def main():
    choice = input("Выберите операцию (кодирование/декодирование): ").lower()
    
    if choice == 'кодирование':
        text = input("Введите текст для кодирования: ")
        morse_code = encode_morse(text)
        print("Закодированный текст: ", morse_code)
    elif choice == 'декодирование':
        morse_code = input("Введите код Морзе для декодирования: ")
        decoded_text = decode_morse(morse_code)
        print("Раскодированный текст: ", decoded_text)
    else:
        print("Ошибка: неверная операция")

    save_choice = input("Хотите сохранить результат в файл? (да/нет): ").lower()
    if save_choice == 'да':
        filename = input("Введите имя файла для сохранения: ")
        with open(filename, 'w') as file:
            if choice == 'кодирование':
                file.write(encode_morse(text))
            elif choice == 'декодирование':
                file.write(decode_morse(morse_code))
        print(f"Результат сохранен в файл {filename}")

if __name__ == "__main__":
    main()
