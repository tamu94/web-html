# Dependencies and Setup
import pandas as pd
import time
import os
from flask import Flask, jsonify, render_template
import json
import plotly
import plotly.graph_objects as go
import numpy as np

# Import CSV file and convert to dataframe
filename = "citiesfinal.csv"
path = os.path.join("Resources", filename)
df = pd.read_csv(path)

# Create directory to store results
script_dir = os.path.dirname("")
results_dir = os.path.join(script_dir, "Results/")
if not os.path.isdir(results_dir):
    os.makedirs(results_dir)
df.drop(
    df.columns[df.columns.str.contains("unnamed", case=False)], axis=1, inplace=True
)

# Convert temperature data to Fahrenheit
df["Temp_F"] = df["temp"].apply(lambda x: x * 9 / 5 - 459.67)
df["Temp_Min_F"] = df["temp_min"].apply(lambda x: x * 9 / 5 - 459.67)
df["Temp_Max_F"] = df["temp_max"].apply(lambda x: x * 9 / 5 - 459.67)
# Convert Wind Speed from m/sec to MPH
df["wind_speed_mph"] = df["wind_speed"].apply(lambda x: x * 2.237)
#Create dummy latitude colume to use as index for plot trendlines
# df["lat_dummy"] = df["lat"]
# #Fit line with polynomial of degree = 3
# z = np.polyfit(x = df.loc[:, "lat"], y = df.loc[:,"Temp_F"], deg =3)
# p = np.poly1d(z)
# df["trendline"] = p(df.loc[:, "lat"])
# #Determine Date of run
# date  = time.strftime("%b/%d/%Y")
# #Create scatterplot of Latitude vs Temperature
# ax = df.plot.scatter(figsize=(12,8), x="lat", y="Temp_F")
# df.set_index("lat_dummy", inplace = True)
# df.sort_index(ascending = False)
# ax.set_xlabel("Latitude", fontsize=10)
# ax.set_ylabel("Temperature (F)", fontsize=10 )
# ax.set_title(f"Latitude versus Temperature {date}", fontsize = 12)
# ax.set_xlim([-70, 70])
# plt.xticks([-70, -60, -50, -40, -30, -20, -10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90])
# ax.yaxis.grid(True)
# ax.xaxis.grid(True)
# plt.savefig(results_dir + "Lat_versus_Temp.png")
# # Create plot of Latitude versus Humidity
# ax = df.plot.scatter(figsize=(12,8), x="lat", y="humidity")
# ax.set_xlabel("Latitude", fontsize=10)
# ax.set_ylabel("Humidity (%)", fontsize=10 )
# ax.set_title(f"Latitude versus Humidity {date}", fontsize = 12)
# ax.yaxis.grid(True)
# ax.xaxis.grid(True)
# plt.savefig(results_dir + "Lat_versus_Humidity.png")
# # plot Latitude vs Cloudiness
# ax = df.plot.scatter(figsize=(12,8), x="lat", y="clouds_percent")
# ax.set_xlabel("Latitude", fontsize=10)
# ax.set_ylabel("Cloudiness (%)", fontsize=10 )
# ax.set_title(f"Latitude versus Cloudiness {date}", fontsize = 12)
# ax.yaxis.grid(True)
# ax.xaxis.grid(True)
# plt.savefig(results_dir + "Lat_versus_Cloudiness.png")
# # Plot Latitude vs Wind Speed
# ax = df.plot.scatter(figsize=(12,8), x="lat", y="wind_speed_mph")
# ax.set_xlabel("Latitude", fontsize=10)
# ax.set_ylabel("Windspeed (MPH)", fontsize=10 )
# ax.set_title(f"Latitude versus Wind Speed {date}", fontsize = 12)
# ax.yaxis.grid(True)
# ax.xaxis.grid(True)
# plt.savefig(results_dir + "Lat_versus_Windspeed.png")

# Latitude vs Termperature Plot

def plot():

    trace = go.Scatter(x=df["lat"], 
                    y=df["Temp_F"], 
                    mode="markers", 
                    text=df["name"])

    data = [trace]
    layout = dict(title = "Latitude versus Temperature for Selected Cities Jan 5, 2020", xaxis_title = "Latitude", yaxis_title = "Temp (F)")
    fig  = dict(data=data, layout=layout)

    return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)


if __name__ == "__main__":
    print(plot())
