#!/usr/bin/env python3

import os, time, argparse

# Create the parser
parser = argparse.ArgumentParser(description='Descreve o programa')

# Add the arguments
parser.add_argument('--type', action = 'store', dest = 'type',
                           default = '.txt', required = False,
                           help = 'O tipo de arquivo que quer concatenar')

parser.add_argument('--label', action = 'store', dest = 'label',
                           default = "merged", required = False,
                           help = 'O tipo de arquivo que quer concatenar')

# Execute the parse_args() method
arguments = parser.parse_args()


start_time = time.time()

# name output file
merged_text = arguments.label + arguments.type

# list files to concatenate
arquivos = []

# search files by type

for file in os.listdir(os.getcwd()):
    if file.endswith(arguments.type):
        arquivos.append(file)

# open the output file

merge_file = open(merged_text, "wb")

for arquivo in arquivos:
    text_file = open("./" + arquivo, "rb")
    for line in text_file:
        merge_file.write(line)
    text_file.close()

merge_file.close()

total_time = time.time() - start_time

#print("--- Time: {:.2f} seconds ---")

print("Type file: {}".format(arguments.type) + "\n" +
      "Files concatened: {}".format(len(arquivos)) + "\n" +
      "Time: {:.2f} seconds". format(total_time))
