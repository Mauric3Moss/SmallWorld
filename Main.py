import random
import math
import sys
import os
import tkinter

def read_contacts(filename):
    contacts = []
    with open(filename, 'r') as file:
        for line in file:
            name, phone = line.strip().split(',')
            contacts.append((name.strip(), phone.strip()))
    return contacts

def write_similarities(filename, similarities):
    with open(filename, 'w') as file:
        for contact in similarities:
            file.write(f"{contact[0]},{contact[1]}\n")

def compare_contacts(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return list(set1.intersection(set2))

def main():
    # Input file names
    file1 = input("Enter the name of the first contact file: ")
    file2 = input("Enter the name of the second contact file: ")
    output_file = input("Enter the name for the output file: ")

    # Read contacts from both files
    contacts1 = read_contacts(file1)
    contacts2 = read_contacts(file2)

    # Compare contacts and find similarities
    similarities = compare_contacts(contacts1, contacts2)

    # Write similarities to the output file
    write_similarities(output_file, similarities)

    print(f"Similarities have been written to {output_file}")

if __name__ == "__main__":
    main()
