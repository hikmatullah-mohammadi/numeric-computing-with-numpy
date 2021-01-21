import numpy as np
# Constants that indicate what data is held in each column of
# the 'dow' array.
OPEN = 0
HIGH = 1
LOW = 2
CLOSE = 3
VOLUME = 4
ADJ_CLOSE = 5

# load the data
data = np.loadtxt('dow.csv', delimiter=',')

##1. Create a "mask" array that indicates which rows have a volume
##   greater than 5.5 billion.
great_volume = data[:, VOLUME] > 5500000000
print('The rows which have a volume greater than 5.5 bilion: ')
print(data[:, VOLUME][great_volume])
print()

##2. How many are there?
number_of_great_volumes = np.sum(great_volume)
print('Number of the rows with a volume of more than 5.5 bilion: ')
print('>>', number_of_great_volumes)
print()

##3. Find the index of every row (or day) where the volume is greater
##   than 5.5 billion.

great_volumes_indeces = np.where(great_volume)
print('Their indeces: ')
print(great_volumes_indeces)

