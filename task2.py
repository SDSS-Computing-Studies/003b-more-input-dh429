#!python3
"""
##### Task 2
A population can be modeled by the following:
future population = (current population)*(1+r)^(time in years) 
Have the user enter the current population, the rate of growth as a decimal and the number of DAYS.
Calculate the expected future population

Enter the population: 25000000
Enter the rate of growth in percent: 2.1
Enter the number of days: 12
There will be 25017087 people after 12 days
"""

cpop = input("Enter the current population:")
cpop = float(cpop)

rate = input("Enter the rate of growth in percent:")
rate = float(rate)
numrate = rate / 100

days = input("Enter the number of days:")
days = int(days)
years = days/365

npop = cpop*(1+numrate)**years
npop = round(npop)

print(f"There will be {npop} after {days} days")
