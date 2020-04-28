from numpy import *


def load_data(constantsfile):
    constants = {}
    infile = open('constants.txt', 'r')

    # read lines starting from third row
    lines = infile.readlines()[2:]
    for line in lines:
        title = line[:27].strip()
        # store constant titles in dictionary
        #having trouble with not reading remaining line for float values
        value = float(line[27:]).split()[0]
        constants[title] = value
    infile.close()
    return constants


fundamental_constants = load_data('constants.txt')

for constants, value in fundamental_constants.iteritems():
    print %g(constants, value)
