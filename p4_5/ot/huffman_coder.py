from heapq import heappush, heappop, heapify
from collections import defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

class HuffmanCoder:
    def __init__(self):
        self.codes = {}
        self.reverse_mapping = {}

    def build_frequency_dict(self, text):
        freq_dict = defaultdict(int)
        for char in text:
            freq_dict[char] += 1
        return freq_dict

    def build_huffman_tree(self, freq_dict):
        priority_queue = []
        for char, freq in freq_dict.items():
            heappush(priority_queue, Node(char, freq))

        while len(priority_queue) > 1:
            left = heappop(priority_queue)
            right = heappop(priority_queue)

            merged = Node(None, left.freq + right.freq)
            merged.left = left
            merged.right = right

            heappush(priority_queue, merged)

        return priority_queue[0]

    def build_huffman_codes(self, node, current_code):
        if node is None:
            return

        if node.char is not None:
            self.codes[node.char] = current_code
            self.reverse_mapping[current_code] = node.char
            return

        self.build_huffman_codes(node.left, current_code + "0")
        self.build_huffman_codes(node.right, current_code + "1")

    def encode_text(self, text):
        encoded_text = ""
        for char in text:
            encoded_text += self.codes[char]
        return encoded_text

    def decode_text(self, encoded_text):
        current_code = ""
        decoded_text = ""
        for bit in encoded_text:
            current_code += bit
            if current_code in self.reverse_mapping:
                char = self.reverse_mapping[current_code]
                decoded_text += char
                current_code = ""
        return decoded_text
