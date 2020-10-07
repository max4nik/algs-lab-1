import csv

from model.chainsaw import Chainsaw


def read_chainsaws_from_csv(file):
    chainsaws = []
    with open(file, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            chainsaws.append(Chainsaw(row[0], int(row[1]), int(row[2])))
    return chainsaws
