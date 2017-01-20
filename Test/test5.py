from random import seed
from random import randrange
from math import sqrt

# function for loading the csv file

def load_csv(filename):
    dataset=list()
    with open(filename,'r') as file:
        csv_reader=read(file)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)
    return dataset



