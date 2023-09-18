import argparse
import encoder
import decoder

def main():
    parser = argparse.ArgumentParser(description="Huffman Compression Tool")
    parser.add_argument('-c', '--compress', action='store_true', help="Compress a file")
    parser.add_argument('-d', '--decompress', action='store_true', help="Decompress a file")
    parser.add_argument('-i', '--input', required=True, help="Input file")
    parser.add_argument('-o', '--output', required=True, help="Output file")

    args = parser.parse_args()

    if args.compress:
        encoder.encode_file(args.input, args.output)
        print("File compressed successfully.")
    elif args.decompress:
        decoder.decode_file(args.input, args.output)
        print("File decompressed successfully.")
    else:
        print("Please specify whether to compress (-c) or decompress (-d) a file.")

if __name__ == "__main__":
    main()
