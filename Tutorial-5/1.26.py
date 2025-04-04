import pandas as pd
import matplotlib.pyplot as plt

df_weather = pd.read_csv("weather.csv")
df_weather.head(10)
max_temp = df_weather["temperature"].max()
min_temp = df_weather["temperature"].min()
places_below_28 = df_weather[df_weather["temperature"] < 28]["place"]
cloudy_places = df_weather[df_weather["weather"] == "Cloudy"]["place"]
weather_counts = df_weather["weather"].value_counts()
df_weather.plot(x="date", y="temperature", kind="bar")
plt.show()

print(max_temp)
print(min_temp)
print(places_below_28)
print(cloudy_places)
print(weather_counts)
