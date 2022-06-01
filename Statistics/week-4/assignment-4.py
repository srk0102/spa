# -*- coding: utf-8 -*-
# Name: 
# Date: 
# Course: 
# Term: 
# Assignment Name: Programming Assignment 4 – Estimating Probabilities

import pandas as pd
from pandas import DataFrame

# Function to print probability of car_types.
def output_simple_probabilities(df, output_fn):
    for make in sorted(set(df.make)):
        p_rating = ((df.loc[df['make'].isin([make])]).index.size / float(df.index.size))*100
        print("Prob(make={}) = {:.2f}%".format(make, p_rating))

#function to probability of car_type with aspirants.
def output_conditional_probabilities(df, output_fn):
    for car_type in sorted(set(df.make)):
        car_total = 0
        std_car = 0
        t_car = 0
        for aspiration, car in zip(df.aspiration, df.make):
            if(car == car_type and aspiration == "std"):
                car_total += 1
                std_car += 1
            elif(car == car_type and aspiration == "turbo"):
                car_total += 1
                t_car += 1
        print ("Prob(std|make={}) = {:.2f}%".format(car_type, (std_car/car_total)*100))
        print ("Prob(turbo|make={}) = {:.2f}%".format(car_type, (t_car/car_total)*100))

if __name__ == "__main__":
    print("Course: ")
    print("NAME: ")
    print( "PROGRAMMING ASSIGNMENT #4 \n")
    # Reading csv file using pandas.
    data = pd.read_csv (r'C:\Users\srk\Desktop\spa\Statistics\week-4\cars.csv')
    output_conditional_probabilities(data, print_to_console)
    print()
    output_simple_probabilities(data, print_to_console)