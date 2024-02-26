from huffman_coder import HuffmanCoder

def main():
    coder = HuffmanCoder()

    while True:
        choice = input("Enter '1' to encode text, '2' to decode text, or '3' to exit: ")

        if choice == '1':
            text = input("Enter text to encode: ")
            freq_dict = coder.build_frequency_dict(text)
            huffman_tree = coder.build_huffman_tree(freq_dict)
            coder.build_huffman_codes(huffman_tree, "")
            encoded_text = coder.encode_text(text)
            print(f"Encoded text: {encoded_text}")

        elif choice == '2':
            encoded_text = input("Enter text to decode: ")
            decoded_text = coder.decode_text(encoded_text)
            print(f"Decoded text: {decoded_text}")

        elif choice == '3':
            break

if __name__ == "__main__":
    main()
