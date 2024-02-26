import json
import os
from datetime import datetime
from collections import Counter
import heapq

class Node:
    def __init__(self, symbol, freq):
        self.symbol = symbol
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

class CodeGenerator:
    def __init__(self):
        self.__huffman = {}

    def __build_huffman_tree(self, text):
        freq = Counter(text)
        heap = [Node(symbol, freq) for symbol, freq in freq.items()]
        heapq.heapify(heap)
        
        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)
            parent = Node(None, left.freq + right.freq)
            parent.left = left
            parent.right = right
            heapq.heappush(heap, parent)
        
        root = heap[0]
        self.__build_codes(root, "")

    def __build_codes(self, node, code):
        if node is not None:
            if node.symbol is not None:
                self.__huffman[node.symbol] = code
            self.__build_codes(node.left, code + "0")
            self.__build_codes(node.right, code + "1")

    def gen_code(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        self.__build_huffman_tree(text)
        
        timestamp = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        folder_name = os.path.join(os.getcwd(), timestamp)
        os.mkdir(folder_name)
        
        with open(os.path.join(folder_name, 'code.json'), 'w') as json_file:
            json.dump(self.__huffman, json_file, ensure_ascii=False)

def main():
    cgen = CodeGenerator()
    cgen.gen_code('my_file.txt')

if __name__ == "__main__":
    main()
