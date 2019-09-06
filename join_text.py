#!/usr/bin/env python3

import os, shutil, time

start_time = time.time()

# name output file
merged_text = "merged.txt"

# list files to concatenate
arquivos = []

for file in os.listdir(os.getcwd()):
    if file.endswith(".txt"):
        arquivos.append(file)

# open the output file

merge_file = open(merged_text, "wb")

for arquivo in arquivos:
    text_file = open("./" + arquivo, "rb")
    for line in text_file:
        merge_file.write(line)
    text_file.close()

merge_file.close()

print("--- Finalized in {:.2f} seconds ---".format(time.time() - start_time))
