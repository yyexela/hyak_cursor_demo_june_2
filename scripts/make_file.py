#!/usr/bin/env python3

import argparse
from pathlib import Path

def main(args):
    
    # Create the filename
    filename = Path(args.out_dir) / f"{args.id}.txt"
    
    try:
        # Create and open the file
        with open(filename, 'w') as f:
            f.write(f"This is file {args.id}")
        print(f"Successfully created {filename}")
    except IOError as e:
        print(f"Error creating file: {e}")

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Create a file with a numeric ID in its name')
    parser.add_argument('--id', type=int, required=True, help='The numeric ID to use in the filename')
    parser.add_argument('--out_dir', type=str, required=True, help='The output directory')
    
    # Parse arguments
    args = parser.parse_args()

    main(args)
