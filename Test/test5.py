from random import seed
from random import randrange
from math import sqrt
from csv import reader

#function for loading csv file

def load_file(filename):

    dataset=list()

    with open(filename,'r') as file:

        data=reader(file)
        for row in data:

            if not row:
                continue

            dataset.append(row)

    return dataset

# we will now test the function

file='/Users/mohendra/Dropbox/My_Projects/Test/sd.csv'

L=load_file(file)

print L


