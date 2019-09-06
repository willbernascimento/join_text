import argparse, os, sys


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

if arguments.type == ".csv":
    print("Juntar Arquivos .csv" + "\n" + "Nome do output:" + arguments.label + arguments.type)

else:
    print("usando o padrão .txt"+ "\n" + "Nome do output:" + arguments.label + arguments.type)