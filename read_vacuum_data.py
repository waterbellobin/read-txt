import numpy as np
import csv

x = []
x_t = []
y = []
y_log = []

with open('C:/Users/nosquest17/Desktop/Sujong/daily_works/20210125_read_vacuum_data/TB30Pressure-2021-01-22.csv', 'rt', encoding='UTF8') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
    for row in plots:
        x.append(row[0])
        y.append(row[1])

for i in range(len(x)):


print(y[0])


