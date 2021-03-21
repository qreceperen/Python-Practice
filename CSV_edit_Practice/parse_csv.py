#!/usr/bin/env python3

import csv

with open('names.csv' , 'r') as csv_file: # csv_file is what you want to call file

    csv_reader = csv.reader(csv_file)
    # csv_reader is variable name it can be anything you want

    for line in csv_reader:
        print(line[2])
