import numpy as np

array_from_file = np.loadtxt("C:/Users/nosquest17/Desktop/Sujong/daily_works/20210125_read_vacuum_data/TB30Pressure-2021-01-22.log", dtype=str)

print(len(array_from_file))
time_high_vacuum = np.zeros(shape=(len(array_from_file),2))

#time_high_vacuum = array_from_file[:,0]

print(time_high_vacuum)
print(array_from_file[0][1])