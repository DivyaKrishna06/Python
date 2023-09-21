import heapq
from collections import defaultdict, Counter

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(freq_dict):
    heap = [HuffmanNode(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged_node = HuffmanNode(None, left.freq + right.freq)
        merged_node.left = left
        merged_node.right = right
        heapq.heappush(heap, merged_node)

    return heap[0]

def build_huffman_codes(root):
    codes = {}
    
    def traverse(node, current_code):
        if node is None:
            return

        if node.char is not None:
            codes[node.char] = current_code
            return

        traverse(node.left, current_code + '0')
        traverse(node.right, current_code + '1')

    traverse(root, '')
    return codes

def compress(text):
    freq_dict = Counter(text)
    root = build_huffman_tree(freq_dict)
    codes = build_huffman_codes(root)
    
    compressed_data = ''
    for char in text:
        compressed_data += codes[char]

    return compressed_data, root

def decompress(compressed_data, root):
    decoded_text = ''
    current_node = root
    
    for bit in compressed_data:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right
        
        if current_node.char is not None:
            decoded_text += current_node.char
            current_node = root

    return decoded_text

if __name__ == "__main__":
    input_text = input('Enter the text for huffman encoding algorithm:')
        
    compressed_data, huffman_tree = compress(input_text)
    print("Compressed Data:", compressed_data)
    
    decompressed_text = decompress(compressed_data, huffman_tree)
    print("Decompressed Text:", decompressed_text)
