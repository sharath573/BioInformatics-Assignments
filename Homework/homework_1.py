"""
Homework 01
DO NOT RENAME THIS FILE OR ANY DEFINITIONS!
Place this file in your github repo inside of a folder titled "Homework".
"""


# String Functions
def fast_complement(dna):
    """
    Uses a dictionary to convert a DNA sequence into the complement strand.  C <--> G,  T <--> A
    :param dna: a string containing only the characters C, T, A, and G
    :return: a string containing only the characters C, T, A, and G
    """
    string = ''
    for char in dna:
        my_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        string = string + my_dict[char]
    return string

# print(fast_complement('CTAG'))

def remove_interval(s, start, stop):
    """
    Removes the interval of characters from a string or list inclusively, 0 based
    EX: remove_intervals('ABCDEFGHI', 2, 5) will return 'ABGHI'.
    :param s: a string
    :param start: a non-negative integer
    :param stop: a non-negative integer greater than the start integer.
    :return: a string
    """
    data = s[:start]+s[stop+1:]
    return data
# print(remove_interval('ABCDEFGHI', 2, 5))

def kmer_list(s, k):
    """
    Generates all kmers of size k for a string s and store them in a list
    :param s: any string
    :param k: any integer greater than zero
    :return: a list of strings
    """
    str = []
    a = len(s)
    for x in range(0, a - k + 1):
      str.append(s[x:x + k])

    return str

# print(kmer_list('CTAGAAAAGGGGGG', 4))

def kmer_set(s, k):
    """
    Generates all kmers of size k for a string s and store them in a set
    :param s: any string
    :param k: any integer greater than zero
    :return: a set of strings
    """
    my_set = set()
    a = len(s)
    for x in range(0, a - k + 1):
        my_set.add(s[x:x + k])

    return my_set


#print(kmer_set('CTAGAAAAGGGGGG', 4))

def kmer_dict(s, k):
    """
    Generates all kmers of size k for a string s and store them in a dictionary with the
    kmer(string) as the key and the number of occurances of the kmer as the value(int).
    :param s: any string
    :param k: any integer greater than zero
    :return: a set of strings
    """
    my_dict = {}
    a = len(s)
    for x in range(0, a - k + 1):
        my_dict[(s[x:x + k])] = 1

    return my_dict
#print(kmer_dict('CTAGAAAAGGGGGG', 4))
# Reading Files
import os

def head(file_name):
    """
    Prints the FIRST 10 lines of a file
    :param file_name: a string
    :return: None
    """
    with open('test_files/proper_fasta.fasta', 'r') as infile:
     seqs = infile.read()
     x = seqs.split('\n')
     for a in range(10):
       print(x[a])
    return
#head('proper_fasta.fasta')

def tail(file_name):
    """
    Prints the LAST 10 lines of a file
    :param file_name: a string
    :return: None
    """
    with open('test_files/proper_fasta.fasta', 'r') as infile:
        seqs = infile.read()
        x = seqs.split('\n')
        y = len(x)
        for a in range(y-10, y):
            print(x[a])

#tail('proper_fasta.fasta')

def print_even(file_name):
    """
    Prints the even numbered lines of a file
    :param file_name: a string
    :return: None
    """
    with open('test_files/proper_fasta.fasta', 'r') as infile:
        seqs = infile.read()
        x = seqs.split('\n')
        y = len(x)
        for a in range(0, y, 2):
            print(x[a])


#print_even('proper_fasta.fasta')

def csv_list(file_name):
    """
    Read in a CSV file to a 2D array (In python it is a list of lists)
    :param file_name: a string
    :return: a list of lists
    """
    with open('test_files/sharath.fasta', 'r') as infile:
        text = infile.readlines()
        list = []
        for a in text:
            char = a.split(',')
            list.append(char)

    return list

#print(csv_list(''))

def get_csv_column(file_name, column):
    """
    Reads in a CSV file and returns a list of values belonging to the column specified
    :param file_name: a string
    :param column: a positive integer
    :return: a list
    """
    with open('test_files/sharath.fasta', 'r') as infile:
        text = infile.readlines()
        list = []
        for a in text:
            char = a.split(',')
            list.append(char[column])
    return list

#print(get_csv_column('',0))

def fasta_seqs(file_name):
    """
    Reads in a FASTA file and returns a list of only the sequences
    :param file_name: a string
    :return: a list of strings
    """
    with open('test_files/proper_fasta.fasta', 'r') as infile:
        sequence = []
        text = infile.read()
        seqs = text.split('>')
        for seq in seqs:
            if seq != '':
                x = seq.split('\n', 1)
                temp = x[1].replace('\n', '')
                sequence.append(temp)
    return sequence


#print(fasta_seqs('test_files/proper_fasta.fasta'))

def fasta_headers(file_name):
    """
    Reads in a FASTA file and returns a list of only the headers (Lines that start with ">")
    :param file_name: a string
    :return: a list of strings
    """
    with open('test_files/proper_fasta.fasta', 'r') as infile:
        head = []
        text = infile.read()
        seqs = text.split('>')
        for seq in seqs:
            x = seq.split('\n', 1)
            head.append(x[0])
    return head


#print(fasta_headers('test_files/proper_fasta.fasta'))

def fasta_dict(file_name):
    """
    Reads in a FASTA file and returns a dictionary of the format {header: sequence, ...}, where
    the sequence headers are keys and the sequence is the value
    :param file_name: a string
    :return: a dictionary
    """
    with open('test_files/proper_fasta.fasta', 'r') as infile:
        my_dict = {}
        text = infile.read()
        seqs = text.split('>')
        for seq in seqs:
            if seq == '':
              print('Empty line')
            else:
              x = seq.split('\n', 1)
              my_dict[x[0]] = x[1]
    return my_dict

#print(fasta_dict('test_files/proper_fasta.fasta'))

def fastq_to_fasta(file_name, new_name=None):
    """
    Reads in a FASTQ file and writes it to a new FASTA file. This definition should also
    keep the same file name and change the extension to from .fastq to .fasta if new_name is not specified.
    EX: fastq_to_fasta('ecoli.fastq') should write to a new file called ecoli.fasta
    :param file_name: a string
    :param new_name: a string
    :return: None
    """
    with open('test_files/proper_fastq.fastq', 'r') as infile:
        text = infile.read()
        file = open('test_files/proper_fastq.fasta', 'w')
        file.write(text)
        file.close()
    return

fastq_to_fasta('','')

# Transcription and Translation
def reverse_complement(dna):
    """
    Returns the strand of DNA that is the reverse complement of the sequence given
    :param dna: a string containing only the characters C, T, A, and G
    :return: a string containing only the characters C, T, A, and G
    """
    string = ''
    for char in dna:
        complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        string = string + complement[char]
    return string[::-1]

# print(reverse_complement('CTAGAAAAGGGGGG'))

def transcribe(dna):
    """
    Transcribes a string of DNA into RNA
    :param dna: a string containing only the characters C, T, A, and G
    :return: a string containing only the characters C, U, A, and G
    """
    string = ''
    for char in dna:
        complement = {'A': 'A', 'T': 'U', 'C': 'C', 'G': 'G'}
        string = string + complement[char]
    return string
#print(transcribe('CTAGAAAAGGGGGG'))
def translate(rna):
    """
    Translates the strand of RNA given into its amino acid composition.
    DO NOT INCLUDE * IN YOUR RETURN STRING
    :param rna: a string containing only the characters C, U, A, and G
    :return: a string containing only the characters G, A, L, M, F, W, K, Q, E, S, P, V, I, C, Y, H, R, N, D, and T
    """
    string = ''

    RNA_CODON_TABLE = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
           "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
           "UAU": "Y", "UAC": "Y", "UAA": "*", "UAG": "*",
           "UGU": "C", "UGC": "C", "UGA": "*", "UGG": "W",
           "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
           "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
           "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
           "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
           "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
           "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
           "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
           "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
           "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
           "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
           "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
           "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"}
    for i in range(0, len(rna), 3):
        s = RNA_CODON_TABLE[rna[i:i + 3]]
        if s == '*':
            string = string
        else:
            string = string + s
    return string
#print(translate('CCCUAGAAAAGGGGGGGG'))

def reading_frames(dna):
    """
    Generates a list of all 6 possible reading frames for a given strand of DNA
    For the non-biologists: https://en.wikipedia.org/wiki/Open_reading_frame
    :param dna: a string containing only the characters C, T, A, and G
    :return: a list of 6 strings containing only C, T, A, and G
    """
    list = []
    stra=''
    strb=''
    strc=''
    a = dna[1:]
    b = dna[2:]

    list.append(dna)
    for char in dna:
        complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        stra = stra + complement[char]
    list.append(stra[::-1])
    list.append(a)
    for char in a:
        complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        strb = strb + complement[char]
    list.append(strb[::-1])
    list.append(b)
    for char in b:
        complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        strc = strc + complement[char]
    list.append(strc[::-1])

    return list


#print(reading_frames('TAGGTACTAGC'))