#!/usr/bin/env python3

""" Concatenate multiple text files """

import os
import time
import argparse
import sys
from tqdm import tqdm

# Create the parser
parser = argparse.ArgumentParser(description='Program to join multiples text files')

# Add the arguments
parser.add_argument('--type', action='store', dest='type', default='.txt',
                    required=False,
                    help='file type: .txt and .csv is working good')

parser.add_argument('--label', action='store', dest='label', default="merged",
                    required=False, help='The output file name')

parser.add_argument('--override', action='store', dest='override', default="No",
                    required=False,
                    help='Remove existing file with same name as output file')

# Execute the parse_args() method
arguments = parser.parse_args()

start_time = time.time()

# name output file
merged_text = arguments.label + arguments.type

# lists if the file exists and decides what to do
# if file exist exit program
if os.path.exists(merged_text) and arguments.override == "No":
    print("Já existe um arquivo com mesmo nome." + "\n" + "Saindo ...")
    sys.exit()

# if file exist: remove it
if os.path.exists(merged_text) and arguments.override == "Yes":
    print("Overriding existing " + merged_text + " file... \n")
    os.remove(merged_text)

# list files to concatenate
file_list = []

# search files by type
for file in os.listdir(os.getcwd()):
    if file.endswith(arguments.type):
        file_list.append(file)

# open the output file
merge_file = open(merged_text, "wb")

# write each line of the files in file list
for file_item in tqdm(file_list):
    text_file = open("./" + file_item, "rb")
    for line in text_file:
        merge_file.write(line)
    text_file.close()

# close output file
merge_file.close()

# get the total time
total_time = time.time() - start_time

# print information about the precess
print("Type file: {}".format(arguments.type) + "\n" +
      "Files concatened: {}".format(len(file_list)) + "\n" +
      "Time: {:.2f} seconds".format(total_time))
