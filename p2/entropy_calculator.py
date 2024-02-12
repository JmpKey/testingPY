import math

def calculate_alphabet_power(text):
    unique_symbols = len(set(text.lower()))
    return unique_symbols

def calculate_probabilities(text):
    n = len(text)
    symbols_count = {char: text.count(char) / n for char in set(text)}
    return symbols_count

def calculate_entropy(text):
    symbols_count = calculate_probabilities(text)
    entropy = -sum(prob * math.log2(prob) for prob in symbols_count.values())
    return entropy

def calculate_redundancy(text, entropy):
    n = len(text)
    alphabet_power = calculate_alphabet_power(text)
    redundancy = ((alphabet_power - entropy) / entropy) * 100
    return redundancy
