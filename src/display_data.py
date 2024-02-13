import pandas as pd

#Load data
df_temperature = pd.read_csv("./data/temperature.csv")
df_population = pd.read_csv("./data/population.csv")

#Display 5 first rows
print("Temperature:\n",df_temperature.head(5))
print("Population:\n",df_population.head(5))