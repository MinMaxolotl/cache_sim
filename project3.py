# Argparser tutorial from https://www.codium.ai/blog/creating-powerful-command-line-tools-in-python-a-practical-guide/
import argparse
parser = argparse.ArgumentParser(description='This is a new command-line tool') # Creates an argparser object
parser.add_argument('input_file', help='Path to the input file')                # Adds an arguement to accept an input file
args = parser.parse_args()                                                      # Gathers arguements that can be called from args object

# Now we create a method of parsing through the input file
# We only need to recognize the keyword "read" and "write"