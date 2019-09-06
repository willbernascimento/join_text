import os, shutil, time

start_time = time.time()

# name output file
merged_text = "merged.txt"

# open the output file
merge_file = open(merged_text, "wb")

# list files to concatenate
arquivos = []

for file in os.listdir("./cand_04/"):
    if file.endswith(".txt"):
        arquivos.append(file)

for arquivo in arquivos:
    text_file = open("./cand_04/" + arquivo, "rb")
    for line in text_file:
        merge_file.write(line)
    text_file.close()

merge_file.close()

print("--- {:.2f} seconds ---".format(time.time() - start_time))
