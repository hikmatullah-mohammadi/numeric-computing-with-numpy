import numpy as np
from matplotlib import pyplot as plt

# read the data in an array
data = np.loadtxt('wind.data')

### to show "threshold" rows
##np.set_printoptions(threshold=10000000)

# saperate the data in two parts
wind = data[:, 3:]
date = data[:, :3]

##1. Calculate the min, max and mean windspeeds and standard deviation of the
##   windspeeds over all the locations and all the times.
print('1. Over all the locations and all the times:')
print('Max: ', wind.max())
print('Min: ',wind.min())
print('Mean: ',wind.mean())
print('Std: ',wind.std())
print()



##2. Calculate the min, max and mean windspeeds and standard deviations of the
##   windspeeds at each location over all the days.

print('2. At each location:')
print('Max: ', wind.max(axis=0))
print('Min: ', wind.min(axis=0))
print('Mean: ', wind.mean(axis=0))
print('Std: ', wind.std(axis=0))
print()

### using matpotlib
##locations = np.arange(1, 13)
##mean = wind.mean(axis=0)
##max_ = wind.max(axis=0)
##min_ = wind.min(axis=0)
##
##width = 0.25
##
##plt.bar(locations+width, max_, width=width, label='Max', color='green')
##plt.bar(locations, mean, width=width, label='Mean')
##plt.bar(locations+(2*width), min_, width=width, label='Min', color='red')
##
##plt.title('Windspeed Statistics')
##plt.xlabel('Locations')
##plt.ylabel('Windspeed')
##
##plt.legend()
##plt.show()

##3. Calculate the min, max and mean windspeed and standard deviations of the
##   windspeeds across all the locations at each day.

print('3. At each day:')
print('Max: ', wind.max(axis=-1))
print('Min: ', wind.min(axis=-1))
print('Mean: ', wind.mean(axis=-1))
print('Std: ', wind.std(axis=-1))
print()

##4. Find the location which has the greatest windspeed on each day.

print('4. The locations with the greatest windspeed on each day:')
print(wind.argmax(axis=-1))
print()
##5. Find the year, month and day on which the greatest windspeed was recorded.

print('5. Time(y, m, d) with greatest windspeed:')
m = wind.max()
a = np.where(wind==m)
print('y. m. d. : ', str(date[a[0]]).strip(']['))
print()

##6.  Find the average windspeed in January for each location.

print('6. January average for each location:')
jan = np.where(data[:, 1]==1)
jan_data = wind[jan]
jan_ave = jan_data.mean(axis=0)
print(jan_ave)

## matplotlib
##locations = np.arange(1, 13)
##plt.bar(locations, jan_ave, color='pink')
##
##plt.title('Average Windspeed in January')
##plt.xlabel('Locations')
##plt.ylabel('Windspeed')
##
##plt.show()

