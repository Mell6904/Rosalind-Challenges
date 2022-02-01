"""
Problem
The 20 commonly occurring amino acids are abbreviated by using 20 letters from the English alphabet (all letters except for B, J, O, U, X, and Z). Protein strings are constructed from these 20 symbols. Henceforth, the term genetic string will incorporate protein strings along with DNA strings and RNA strings.

The RNA codon table dictates the details regarding the encoding of specific codons into the amino acid alphabet.

Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

Return: The protein string encoded by s.
"""

Dataset = open("Dataset.txt", "r")
Dataset = Dataset.read()
n = 3
Dataset = [Dataset[i:i+n] for i in range(0, len(Dataset), n)]

print(Dataset)

for i in Dataset:
    if i == "AUG":
        print("M", end="")
    elif i == "UUU" or i == "UUC":
        print("F", end="")
    elif i == "UUA" or i == "UUG":
        print("L", end="")
    elif i == "UCU" or i == "UCC" or i == "UCA" or i == "UCG":
        print("S", end="")
    elif i == "UAU" or i == "UAC":
        print("Y", end="")
    elif i == "UGU" or i == "UGC":
        print("C", end="")
    elif i == "UGG":
        print("W", end="")
    elif i == "CUU" or i == "CUC" or i == "CUA" or i == "CUG":
        print("L", end="")
    elif i == "CCU" or i == "CCC" or i == "CCA" or i == "CCG":
        print("P", end="")
    elif i == "CAU" or i == "CAC":
        print("H", end="")
    elif i == "CAA" or i == "CAG":
        print("Q", end="")
    elif i == "CGU" or i == "CGC" or i == "CGA" or i == "CGG":
        print("R", end="")
    elif i == "AUU" or i == "AUC" or i == "AUA":
        print("I", end="")
    elif i == "ACU" or i == "ACC" or i == "ACA" or i == "ACG":
        print("T", end="")
    elif i == "AAU" or i == "AAC":
        print("N", end="")
    elif i == "AAA" or i == "AAG":
        print("K", end="")
    elif i == "AGU" or i == "AGC":
        print("S", end="")
    elif i == "AGA" or i == "AGG":
        print("R", end="")
    elif i == "GUU" or i == "GUC" or i == "GUA" or i == "GUG":
        print("V", end="")
    elif i == "GCU" or i == "GCC" or i == "GCA" or i == "GCG":
        print("A", end="")
    elif i == "GAU" or i == "GAC":
        print("D", end="")
    elif i == "GAA" or i == "GAG":
        print("E", end="")
    elif i == "GGU" or i == "GGC" or i == "GGA" or i == "GGG":
        print("G", end="")
    elif i == "UAA" or i == "UAG" or i == "UGA":
        quit()
