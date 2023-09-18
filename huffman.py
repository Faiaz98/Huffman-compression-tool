import heapq
from collections import defaultdict
import pickle  #for serializing and deserializing the Huffman tree

class HuffmanNode:
    def __init__(self, character, frequency):
        self.character = character
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency

def build_huffman_tree(data):
    #count the frequency of each character in the input data
    freq_counter = defaultdict(int)
    for char in data:
        freq_counter[char] += 1

    #create a priority queue (min-heap) to build the Huffman tree
    min_heap = [HuffmanNode(char, freq) for char, freq in freq_counter.items()]
    heapq.heapify(min_heap)

    while len(min_heap) > 1:
        #extract the two nodes with the lowest frequencies
        left_node = heapq.heappop(min_heap)
        right_node = heapq.heappop(min_heap)

        #create a new internal node with the combined frequency
        internal_node = HuffmanNode(None, left_node.frequency + right_node.frequency)
        internal_node.left = left_node
        internal_node.right = right_node

        #add the internal node back to the heap
        heapq.heappush(min_heap, internal_node)

    return min_heap[0]  #the root of the Huffman tree

def build_huffman_codes(node, current_code="", huffman_codes={}):
    if node is None:
        return

    if node.character is not None:
        huffman_codes[node.character] = current_code
        return

    build_huffman_codes(node.left, current_code + "0", huffman_codes)
    build_huffman_codes(node.right, current_code + "1", huffman_codes)

def huffman_compress(data):
    root = build_huffman_tree(data)
    huffman_codes = {}
    build_huffman_codes(root, "", huffman_codes)

    compressed_data = "".join([huffman_codes[char] for char in data])
    return compressed_data, huffman_codes

def huffman_decompress(compressed_data, huffman_codes):
    reverse_huffman_codes = {code: char for char, code in huffman_codes.items()}

    current_code = ""
    decompressed_data = []
    for bit in compressed_data:
        current_code += bit
        if current_code in reverse_huffman_codes:
            char = reverse_huffman_codes[current_code]
            decompressed_data.append(char)
            current_code = ""

    return "".join(decompressed_data)
