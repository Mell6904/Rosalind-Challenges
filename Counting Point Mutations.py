"""
Problem

Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of corresponding symbols that differ in s and t.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).
"""

Dataset = open("Dataset.txt", "r")

lines = Dataset.read()
lineSplit = lines.splitlines()
Dataset.close()

lineOne = lineSplit[0]
lineTwo = lineSplit[1]

hammingDistance = 0
for i in range(len(lineOne)):
    if lineOne[i] != lineTwo[i]:
        hammingDistance += 1

print(hammingDistance)