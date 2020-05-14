from numpy import *


def two_column_text_read(file_name):

        x = []
        y = []
        infile = open(file_name, 'r')
        for line in infile:
            p = line.split()
            x.append(float(p[0]))
            y.append(float(p[1]))
        infile.close()
        x, y = array(x), array(y)
        data = vstack((x,y)).T

        return data
