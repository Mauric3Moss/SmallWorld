import random
import math
import sys
import os
import tkinter
import re
import time

def normalize_name(name):
    """Normalize the contact name by converting it to lowercase and stripping extra spaces."""
    return name.strip().lower()

def normalize_phone(phone):
    """Normalize the phone number by removing spaces, dashes, and parentheses."""
    return re.sub(r'[\s\-\(\)]', '', phone)

def read_contacts(filename):
    """Reads contacts from a file and returns a list of normalized (name, phone) tuples."""
    contacts = []
    with open(filename, 'r') as file:
        for line in file:
            name, phone = line.strip().split(',')
            # Normalize the name and phone before adding to contacts
            contacts.append((normalize_name(name), normalize_phone(phone.strip())))
    return contacts

def write_similarities(filename, similarities):
    """Writes the number of similarities and the matching contacts to a file."""
    with open(filename, 'w') as file:
        # Write the number of similarities at the top
        file.write(f"Number of similarities: {len(similarities)}\n")
        if similarities:
            # Write each similar contact (name, phone) on a new line
            for contact in similarities:
                file.write(f"{contact[0]},{contact[1]}\n")
        else:
            file.write("No matching contacts found.\n")

def compare_contacts(list1, list2):
    """Compares two contact lists and returns a list of contacts that appear in both."""
    set1 = set(list1)
    set2 = set(list2)
    # Intersection will automatically compare both name and phone (normalized)
    return list(set1.intersection(set2))

def monitor_files(file1, file2, output_file, interval=5):
    """Continuously monitors the contact files for changes and updates the output file."""
    last_similarities_count = None  # Track the last count of similarities
    
    while True:
        # Read contacts from both files
        contacts1 = read_contacts(file1)
        contacts2 = read_contacts(file2)

        # Compare contacts and find similarities
        similarities = compare_contacts(contacts1, contacts2)

        # Only update the output file if the number of similarities has changed
        if len(similarities) != last_similarities_count:
            write_similarities(output_file, similarities)
            print(f"Updated similarities written to {output_file}. Total: {len(similarities)}")
            last_similarities_count = len(similarities)
        
        # Wait for the specified interval before checking again
        time.sleep(interval)

def main():
    # Input file names
    file1 = input("Enter the name of the first contact file: ")
    file2 = input("Enter the name of the second contact file: ")
    output_file = input("Enter the name for the output file: ")

    # Start monitoring the files
    monitor_files(file1, file2, output_file)

if __name__ == "__main__":
    main()

