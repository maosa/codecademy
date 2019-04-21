import pandas as pd
import numpy as np
# WILL PROBABLY CREATE AN ERROR !!!
from weather_data import london_data

print(str(len(london_data)) + " data points\n")

temp = london_data['TemperatureC']

print(temp.iloc[15:21])

average_temp = np.average(temp)
print("\nAverage temperature: " + str(average_temp.round(2)) + " Celsius\n")

var_temp = np.var(temp)
print("Temperature variance: " + str(var_temp.round(2)) + "\n")

std_temp = np.std(temp)
print("Temperature standard deviation: " + str(np.round(2)) + " Celsius\n")

july = london_data.loc[london_data['month'] == 7]['TemperatureC']

print(july.head())

july_mean = np.average(july)
print("\nAverage temperature in July: " + str(july_mean.round(2)) + " Celsius\n")

july_std = np.std(july)
print("\nTemperature standard deviation in July: " + str(july_std.round(2)) + " Celsius\n")

# DO THIS FOR ALL MONTHS
for i in range(1, 13):
    month = london_data.loc[london_data['month'] == i]['TemperatureC']
    avg = np.average(month)
    std = np.std(month)
    print("The average temperature in month %d is %.2f degrees Celsius and the standard deviation is %.2f\n" % (i, avg, std))
