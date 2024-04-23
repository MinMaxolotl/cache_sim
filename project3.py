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

# Next I will initalize the states for all of the caches I will be testing
c_size = 1024
b_size = [8, 16, 32, 128]

# Address bits: 8 bytes = 32 bits
# Size of each way = cache_ size / # ways 
# • Only using direct mapping (# ways = 1), so size of each way always = cache_size = 1024
# Number of blocks = size of each way / block size (bytes)

num_blocks = [128, 64, 32, 8]

# Bits for offset comes from block size = 2^x, where x = # offset bits

offset_bits = [3, 4, 5, 7]

# Bits for index: number of blocks = 2^y, where y = # of index bits

index_bits = [7, 6, 5, 3]

# Tag bits = 32 bits - offset_bits - tag_bits = 32 - 10 = 22 bits

tag_bits = 22

# Order of address goes as such: tag -> index -> offset

# I now create a function that will perform the bulk of the work
def read(address):
    print("reading")

def write(address):
    print("writing")

def parse(line):
    words = line.split()
    if words[0] == "read":
        read(words[1])
        
    elif words[1] == "write":
        write(words[1])


     



# Now we create a method of parsing through the input file
# We only need to recognize the keyword "read" and "write"

# https://www.geeksforgeeks.org/read-a-file-line-by-line-in-python/#
input = open(args.input_file, 'r')
Lines = input.readlines()



for line in Lines:
    print(line)

    
