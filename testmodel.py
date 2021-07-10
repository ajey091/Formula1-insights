# Import the necessary libraries
import pandas as pd
import numpy as np
from scipy import stats
import pmdarima as pmd
import matplotlib.pyplot as plt
import pybats
from pybats.loss_functions import MAPE
from pybats.analysis import analysis
from pybats.point_forecast import median

# import the data
standings = pd.read_csv("driver_standings.csv")
races = pd.read_csv("races.csv")
print(standings.head())
print(races.head())

races_2010 = races.loc[races['year']>2009,:]
ver = standings.loc[standings['driverId']==830,:]
ham = standings.loc[standings['driverId']==1,:]

plt.plot(ver['points'],label="VER")
plt.plot(ham['points'],label="HAM")
plt.legend()
plt.show()
