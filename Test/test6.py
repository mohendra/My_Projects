from random import seed
from random import randrange
from csv import reader
from math import sqrt

# function for importing and open csv file

def opencsv(filename):
    dataset=list() # this is ap
    with open(filename,'r') as file:

        csv_read=read(file)

        for row in csv_read:
            if not row:
                continue
            dataset.append(row)

    return dataset

filename='sonar.all-data.csv'

opencsv(filename)

#s
