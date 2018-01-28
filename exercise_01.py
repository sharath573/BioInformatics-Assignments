"""
Exercise 1
Place this script inside a new folder in your github repository called "Exercises".
This will be the directory for all of your in-class exercises this semester.

By the end of class on Thursday 1/25, students should have:
    - Created a private github repo for this class
    - Added their information to this sheet:
        https://docs.google.com/spreadsheets/d/1EKNYOqTnxelmBT4jqotRbUer5eVvWYM9RloN5doScyo/edit?usp=sharing
    - Added my github account (kylelevi) as a collaborator for their private repository
    - Completed these definitions and pushed this script to a folder called "Exercises" in their repo

"""
print("<----Function1---->")
def hello():
    print("Hello world")
    """
    Prints "Hello World"
    :return: None
    """
    return


hello()

print("<----Function2---->")


def percent_decimal(i):

    if i < 1:
        i = i*100
        print("Percentage value", i, "%")
    elif i > 1:
        i = i/100
        print("Decimal number", i)
    """
    Converts a percentage to a decimal or a decimal to a percentage depending on the input i
    :param i: a float between 0 and 100
    :return: a float between 0 and 100
    """
    return


percent_decimal(0.5)

print("<----Function3---->")


def exponent(integer, power):
    print("Integer:", integer)
    print("Power:", power)
    y = integer
    for x in range(power-1):
        integer = integer*y
    """
    Using a loop (no imports!), raise the integer given to the power provided. (integer^power)
    :param integer: a positive, non zero, integer
    :param power: a positive, non zero, integer
    :return: an integer
    """
    print("Answer:", integer)
    return


exponent(2, 3)

print("<----Function4---->")


def complement(dna):
    print("Given data:", dna)
    string = ''
    for char in dna:
        if char == 'C':
            string = string + 'G'
        elif char == 'G':
            string = string + 'C'
        elif char == 'A':
            string = string + 'T'
        elif char == 'T':
            string = string + 'A'
        else:
            string = string + char
    """
    Returns the complement strand of DNA to the input.  C <--> G,  A <--> T
    :param dna: String containing only C, T, A, and G
    :return: String containing only C, T, A, and G
    """
    return string


data = complement('ABCDAAGGCCTT')

print("Modified data:", data)
