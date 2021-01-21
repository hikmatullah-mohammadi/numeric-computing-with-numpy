from matplotlib import pyplot as plt
from datetime import datetime
import pandas as pd
import numpy as np

# read the data in an array
data = np.loadtxt('wind.data')

### to show "threshold" rows
##np.set_printoptions(threshold=10000000)

# saperate the data in two parts
wind = data[:, 3:]
date = data[:, :3]


##1. Calculate the min, max and mean windspeeds and standard deviations of the
##   windspeeds at each location over all the days.

locations = np.arange(1, 13)
mean = wind.mean(axis=0)
max_ = wind.max(axis=0)
min_ = wind.min(axis=0)

width = 0.25

plt.bar(locations+width, max_, width=width, label='Max', color='green')
plt.bar(locations, mean, width=width, label='Mean')
plt.bar(locations+(2*width), min_, width=width, label='Min', color='red')

plt.title('Windspeed Statistics')
plt.xlabel('Locations')
plt.ylabel('Windspeed')

plt.legend()
plt.show()

##2.  Find the average windspeed in January for each location.

jan = np.where(data[:, 1]==1)
jan_data = wind[jan]
jan_ave = jan_data.mean(axis=0)

locations = np.arange(1, 13)
plt.bar(locations, jan_ave, color='pink')

plt.title('Average Windspeed in January')
plt.xlabel('Locations')
plt.ylabel('Windspeed')

plt.show()

##3. plot the median wind speed on each day in first month.


# load data
data = np.loadtxt('wind.data')
# median for each row
median_w_s = data[:30, 3:].mean(axis=-1)

# first January
dates_ = np.array(data[:30, :3])

dates = []
for i in dates_:
    dates.append('19'+str(i).strip('[]'))

# convert to datetime
dates = pd.to_datetime(dates).sort_values()

# plot the data
plt.plot_date(dates, median_w_s, linestyle='-.')

# auto format the dates
plt.gcf().autofmt_xdate()

plt.title('median wind speed each day in first month')
# display the figure
plt.show()

