#############################################
# Name: project3.py
# Author: Maxwell Kawada
# Last Edited: 4/22/2024
# Purpose: To simulate a cahce and the hit rate for different
#          block sizes using a command line tool
#############################################

# The basic cache is
# • Cache Size: 2048 Bytes
# • Block Size: 2 words, or 8 bytes
# • Cache Placement Type: direct mapped
# • Write Policy: write back

# I will test Block Sizes: 2, 4, 8, 32 words
# Blocks in bytes        : 8, 16, 32, 128 bytes

# Argparser tutorial from https://www.codium.ai/blog/creating-powerful-command-line-tools-in-python-a-practical-guide/
import argparse
parser = argparse.ArgumentParser(description='This is a new command-line tool') # Creates an argparser object
parser.add_argument('input_file', help='Path to the input file')                # Adds an arguement to accept an input file
args = parser.parse_args()                                                      # Gathers arguements that can be called from args object

# Now we create a method of parsing through the input file
# We only need to recognize the keyword "read" and "write"

# https://www.geeksforgeeks.org/read-a-file-line-by-line-in-python/#
input = open(args.input_file, 'r')
Lines = input.readlines()



for line in Lines:
    
