from pandas import DataFrame, Series
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# Reads CSV file and translate the data into a DataFrame
data = pd.read_csv(r'./ss13hil.csv')
df = DataFrame(data)

# Creating series from the dataframe
hhl_series          = Series(df['HHL']).replace({1:"English Only",2:"Spanish",3:"Other Indo-European Languages",4:"Asian and Pacific Island Languages", 5:"Other"})
hincp_series        = Series(df['HINCP'].dropna())
valp_series         = Series(df['VALP'])
taxp_series         = Series(df['TAXP']).replace({1:0,2:1,3:50,4:100,5:150,6:200,7:250,8:300,9:350,10:400,11:450,12:500,13:550,14:600,15:650,16:700,17:750,18:800,19:850,20:900,
                                                    21:950,22:1000,23:1100,24:1200,25:1300,26:1400,27:1500,28:1600,29:1700,30:1800,31:1900,32:2000,33:2100,34:2200,35:2300,36:2400,
                                                    37:2500,38:2600,39:2700,40:2800,41:2900,42:3000,43:3100,44:3200,45:3300,46:3400,47:3500,48:3600,49:3700,50:3800,51:3900,52:4000,
                                                    53:4100,54:4200,55:4300,56:4400,57:4500,58:4600,59:4700,60:4800,61:4900,62:5000,63:5500,64:6000,65:7000,66:8000,67:9000,68:10000})

counts_hhl_series   = hhl_series.value_counts()

# Pie Graph of Household Languages
def graph_hhl():
    plt.subplot(2,2,1)
    plt.pie(counts_hhl_series, startangle = 242)
    plt.legend(counts_hhl_series.index, loc='upper left')
    plt.title("Household Languages")
    plt.ylabel('HHL')
    plt.axis('equal')

# Distribution of Household Income Histogram
def graph_hincp():
    plt.subplot(2,2,2)
    plt.title("Distribution of Household Income")
    plt.ylabel("Density")
    plt.xlabel("Household Income ($) - Log Scaled")
    plt.xscale('log')
    log_bins = np.logspace(1, 7, 100) 
    density = stats.gaussian_kde(hincp_series)
    n, x, _ = plt.hist(hincp_series, bins=log_bins, color='g', histtype='bar', alpha=.5, density=True)     
    plt.plot(x, density(x), 'k--')                                                          

# Bar chart of Thousands of Households for each number of vehicles
def graph_veh():
    plt.subplot(2,2,3)
    veh_data = (df.groupby('VEH')['WGTP'].sum())/1000
    plt.bar(veh_data.index, veh_data.values,color='red')
    plt.xticks(veh_data.index)
    plt.tick_params(axis="both", which="major")
    plt.tick_params(axis="both", which="minor")
    plt.ylabel("Thousands of Households")
    plt.xlabel("# of Vehicles")
    plt.title("Vehicles Available in Households")

# Scatter plot of Property Taxes vs Property Value
def graph_pt_pv():
    plt.subplot(2,2,4)
    scplot = plt.scatter(valp_series,taxp_series,marker='o',s = df['WGTP'],c=df['MRGP'],cmap='seismic',vmax=5000, alpha=.15) ##################
    plt.xlim([0, 1200000])
    plt.ylim([0, 10400])
    plt.colorbar(scplot, ticks=[1250,2500,3750,5000]).ax.set_ylabel('First Mortgage Payment (Monthly $)', rotation=90)
    plt.title('Property Taxes vs. Property Values')
    plt.xlabel('Property Value ($)')
    plt.ylabel('Taxes ($)')

def main():
    plt.figure(figsize=(18,10))
    graph_hhl()
    graph_hincp()
    graph_veh()
    graph_pt_pv()
    plt.savefig('pums.png')
    plt.show()

main()