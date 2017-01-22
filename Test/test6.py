from random import seed
from random import randrange
from csv import reader
from math import sqrt

# function for importing and open csv file



def lfile(filename):
    dataset=list() # declaration of placeholder to store the dataset
    with open(filename, 'r') as file:

        data=reader(file)
        for row in data:
            if not row:
                continue

            dataset.append(row)

    return dataset



file='/Users/mohendra/Dropbox/My_Projects/Test/sd.csv'

L=lfile(file)

print L

