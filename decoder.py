import huffman  #import the Huffman module you created
import pickle  #import the pickle module for deserialization

def decode_file(input_file, output_file):
    with open(input_file, 'rb') as infile, open(output_file, 'w') as outfile:
        huffman_codes = pickle.load(infile)
        compressed_data = infile.read().decode('utf-8')
        decompressed_data = huffman.huffman_decompress(compressed_data, huffman_codes)
        outfile.write(decompressed_data)
