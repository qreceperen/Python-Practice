#!/usr/bin/env python3

import csv

with open('names.csv' , 'r') as csv_file: # csv_file is what you want to call file
    csv_reader = csv.reader(csv_file)

    with open ('new_names.csv' ,'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter ='\t')
    # a new csv file is created
    # csv_writer is the variable it can be any name.

        for line in csv_reader:
            csv_writer.writerow(line)

        # All the rows are taken from names.csv file through csv_reader variable
        # all rows are written in a new_names.csv file through csv_writer.writerow(line)
