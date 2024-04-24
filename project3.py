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

# Next I want to set up all the other variables that I will be printing after a read or write completes
mapping_type = "DM" # Always DM in my case
write_policy = "WB" # Alwaays WB in my case
hit_rate = 0.00     # This will be modified, percentage of cache hit
MemToCache = 0      # This will be modified, number of bytes put into cache from memory
CahceToMem = 0      # This will be modified, number of bytes put into memory from cache

# Other output variables is cache size, block size, and number of blocks, which are all created above


# In direct mapped, we have two columns the size of # of blocks, one of them being for tag, the other for data
# I create a cache table for each block size, and can be accessed by calling cache[0-4][tag][index][offset]
# The enture cache is empty, and filled with None values

tag_col = [[None] * num_blocks[0], [None] * num_blocks[1], [None] * num_blocks[2], [None] * num_blocks[3]]
v_col = [[None] * num_blocks[0], [None] * num_blocks[1], [None] * num_blocks[2], [None] * num_blocks[3]]

block = [[None]*b_size[0], [None]*b_size[1], [None]*b_size[2], [None]*b_size[3]]

cache_data = [[block[0]*num_blocks[0]], [block[1]*num_blocks[1]], [block[2]*num_blocks[2]], [block[3]*num_blocks[3]]]



# I now create a function that will perform the bulk of the work
def read(address, setting):
    print("reading")

    # Caclcualate the tag, block index, and block offset so we can check if the cache contains the data
    tag = int(address) // c_size
    block_index = (int(address) // b_size[setting]) % num_blocks[setting]
    block_offset = int(address) % b_size[setting]

    #If theres nothing in the cache at that location, then its a cache miss
    #If the verify bit is zero at the block index, then its a cache miss
    #If the tags do not match at the block index, then its a cache miss
        
    if ((v_col[setting][block_index] == 0) or (tag != tag_col[setting][block_index])): 
        # When there is a cache miss, we pull data from memory and fill the cache, I use a filler value of 1
        MemToCache = MemToCache + b_size[setting]

        # # Loop that fills out the entire block
        # i = 0
        # while i < (b_size[setting]/4):
        #     cache_data[setting][block_index][i] = 1
        #     i += 4
        
        tag_col[setting][block_index] = tag # We set the tag value as the one we solved for earlier
        v_col[setting][block_index] = 1 # after filling the blocks, we set v = 1
        
        

def write(address, setting): # We use the write back methodology
    print("writing")

def results(setting):
    # Print the final results
    print(f"{c_size} {b_size[setting]} {mapping_type} {write_policy} {hit_rate} {MemToCache} {CahceToMem}")

    # reset the values back to initial state
    hit_rate = 0.00     # This will be modified, percentage of cache hit
    MemToCache = 0      # This will be modified, number of bytes put into cache from memory
    CahceToMem = 0      # This will be modified, number of bytes put into memory from cache
    

def parse(line, setting): # Setting will be between 0 and 3 to account for the block size we are working with
    words = line.split()
    if words[0] == "read":
        read(words[1][2:], setting) # The [2:] is so that we remove the 0x part of the address

    elif words[0] == "write":
        write(words[1][2:], setting)


# Now we create a method of parsing through the input file
# We only need to recognize the keyword "read" and "write"

# https://www.geeksforgeeks.org/read-a-file-line-by-line-in-python/#
input = open(args.input_file, 'r')
Lines = input.readlines()
counter = 0

while counter < 4:
    for line in Lines:
        parse(line, counter)

    results(counter)
    counter += 1
    
