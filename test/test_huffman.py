import unittest
import huffman  #import the Huffman module

class TestHuffmanCompression(unittest.TestCase):
    def test_huffman_compress_decompress(self):
        #test compression and decompression for a sample string
        original_text = "this is a sample text for testing Huffman compression and decompression"
        compressed_data, huffman_codes = huffman.huffman_compress(original_text)
        decompressed_text = huffman.huffman_decompress(compressed_data, huffman_codes)
        self.assertEqual(original_text, decompressed_text, "Compression and decompression did not produce the same result.")

    def test_empty_input(self):
        #test compression and decompression for an empty string
        original_text = ""
        compressed_data, huffman_codes = huffman.huffman_compress(original_text)
        decompressed_text = huffman.huffman_decompress(compressed_data, huffman_codes)
        self.assertEqual(original_text, decompressed_text, "Compression and decompression did not produce the same result for an empty input.")

if __name__ == '__main__':
    unittest.main()
