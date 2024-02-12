import sys
from entropy_calculator import calculate_alphabet_power, calculate_entropy, calculate_redundancy

def main():
    if len(sys.argv) != 2:
        print("Usage: python entropy_cli.py <filename>")
        return
    
    filename = sys.argv[1]
    text = ''
    
    try:
        with open(filename, 'r') as file:
            text = file.read()
    except FileNotFoundError:
        print("Файл не найден")
        return
    
    alphabet_power = calculate_alphabet_power(text)
    entropy = calculate_entropy(text)
    redundancy = calculate_redundancy(text, entropy)
    
    print(f"Мощность алфавита: {alphabet_power}")
    print(f"Энтропия: {round(entropy, 2)} бит на символ")
    print(f"Резервирование: {round(redundancy, 2)}%")

if __name__ == "__main__":
    main()
