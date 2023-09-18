import huffman  #import the Huffman module you created
import pickle  #import the pickle module for serialization

def encode_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'wb') as outfile:
        data = infile.read()
        compressed_data, huffman_codes = huffman.huffman_compress(data)
        pickle.dump(huffman_codes, outfile)
        outfile.write(compressed_data.encode('utf-8'))
