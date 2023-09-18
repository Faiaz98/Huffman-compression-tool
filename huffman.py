import heapq
from collections import defaultdict
import pickle #for serializing and deserializing the huffman tree

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
        
    #create a priority queue (min-heap) to build the huffman tree
    min_heap = [HuffmanNode(char, freq) for char, freq in freq_counter.items()]
    