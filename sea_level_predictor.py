import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df= pd.read_csv("/workspace/boilerplate-sea-level-predictor/epa-sea-level.csv")
   
    # Create scatter plot
    plt.scatter(df['Year'], df["CSIRO Adjusted Sea Level"])
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
   

    # Create scatter plot
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])
    lmin=np.arange(df["Year"].min(),2050,1)
    plt.plot(lmin,linregress(df["Year"], df["CSIRO Adjusted Sea Level"]).slope*lmin+linregress(df["Year"], df["CSIRO Adjusted Sea Level"]).intercept)
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
 

    # Create first line of best fit

    x1 = np.arange(df["Year"].min(), 2051,1)
    linea = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    y1= x1*linea.slope+linea.intercept
    plt.plot(x1,y1)
    plt.title('Rise in Sea Level')
    plt.ylabel('Sea Level (inches)')
    plt.xlabel('Year')
  
      # Create second line of best fit
    df_2000 = df[df["Year"] >= 2000]
    res_2000 = linregress(df_2000['Year'], df_2000["CSIRO Adjusted Sea Level"])
    x_pred_2000 = pd.Series([i for i in range(2000, 2051)])
    y_pred_2000 = res_2000.slope*x_pred_2000 + res_2000.intercept
    plt.plot(x_pred_2000, y_pred_2000, "r")



     # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
