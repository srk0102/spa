#Import Dependencies
import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt
from scipy.stats import norm
import scipy

#Load DataSet run Initial
global_temps = pd.read_csv('globtemp.csv')
global_temps.describe()

def convert_temp(celsius):
    return celsius * 1.8 + 32
#Test Function
convert_temp(12.548)

#Create Norm Inverse Function for Simulation
def norminv(prob, mu, sigma):
    x = scipy.stats.norm(mu, sigma)
    return x.ppf(prob)

global_temps.tail()

#Create new dataset where group on is done by year
temps_year = global_temps.groupby(['Date']).mean()
#Filter Years less than 1850 where data is unreliable
temps_year = temps_year[temps_year.index > 1849]

#Create new columns of Farenheit converted Temperatures
temps_year['stdTemp'] = temps_year['std'].apply(lambda x: convert_temp(x))
temps_year['MeanTemp'] = temps_year['Mean'].apply(lambda x: convert_temp(x))

#Plot Average Land Temperatures (1850-2015)
plt.plot(temps_year['stdTemp'])
plt.ylabel('Temp(Farenheit)')
plt.xlabel('Year')
plt.title('Average Land Tempatures by Year (1850- 2004)')
plt.gcf().autofmt_xdate()
plt.grid()
plt.show()

#Plot Average Land Temperatures (1850-2015)
plt.plot(temps_year['MeanTemp'])
plt.ylabel('Temp(Farenheit)')
plt.xlabel('Year')
plt.title('Average Land Tempatures by Year (1850- 2004)')
plt.gcf().autofmt_xdate()
plt.grid()
plt.show()

#Plot by Max and Average Temperatures
plt.plot(temps_year['stdTemp'])
plt.plot(temps_year['MeanTemp'])
plt.ylabel('Temp(Farenheit)')
plt.xlabel('Year')
plt.title('Average and Max Land Temperatures (1850 - 2015)')
plt.legend(loc='best')
plt.gcf().autofmt_xdate()
plt.grid()
plt.show()

num_simulations = 2000
for j in range(num_simulations):
    lst = []
    indices = []
    last = 0
    for current in temps_year['stdTemp']:
        if len(lst) == 0:
            lst.append(np.nan)
            last = current
        else:
            lst.append(current / last)
            last = current
    indices = temps_year.index.values.tolist()

    for i in range(len(indices)):
        indices[i] = int(indices[i])
    change_results = pd.DataFrame(lst, index = indices, columns = ['yr_yr_change'])
    result = pd.concat([temps_year, change_results], axis=1)
    changed_avg = result['yr_yr_change'].mean()
    changed_stdev = np.std(result['yr_yr_change'])
    #Run 10 years of simulation from last year using norminv function and random variable
    simulation_end = []
    num_years = 10
    for item in temps_year['stdTemp']:
        simulation_end.append(item)
    yr_end = simulation_end[-1]
    for i in range(num_years):
        yr_end = norminv(np.random.random_sample(), changed_avg, changed_stdev) * yr_end
        indices.append(indices[-1] + 1)
        simulation_end.append(yr_end)
    simulation = pd.DataFrame(simulation_end, index = indices, columns = [str(j)])
    if j == 0:
        #Initialize New DataFrame with First Years Results
        simulation_compiled = simulation
    else:
        simulation_compiled = pd.concat([simulation_compiled, simulation], axis=1)
    if j % 1000 == 0:
        print (str(j) + ' Number of Simulations Complete')

#Add columns of Statistically Significant Forecasts for each year
simulation_compiled['mean'] = simulation_compiled.mean(axis = 1)
simulation_compiled['max'] = simulation_compiled.max(axis = 1)
simulation_compiled['min'] = simulation_compiled.min(axis = 1)
simulation_compiled['median'] = simulation_compiled.median(axis = 1)
simulation_compiled['75th'] = simulation_compiled.quantile(.75, axis = 1)
simulation_compiled['25th'] = simulation_compiled.quantile(.25, axis = 1)

fig, ax = plt.subplots(figsize=(10,7))
ax.plot(simulation_compiled['mean'])
ax.plot(simulation_compiled['max'])
ax.plot(simulation_compiled['min'])
ax.plot(simulation_compiled['median'])
ax.plot(simulation_compiled['75th'])
ax.plot(simulation_compiled['25th'])
plt.title('Predicted Forecast by Year in Farenheit')
ax.axvline(2016, color = 'r', linestyle='--', label = 'Simulation Begins')
ax.legend(loc = 'best')
fig.tight_layout()
ax.grid()

print (simulation_compiled['mean'][2015], simulation_compiled['mean'][2115], simulation_compiled['75th'][2115])