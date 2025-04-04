import pandas as pd

df_auto = pd.read_csv("auto.csv")
df_auto = df_auto.dropna()
most_expensive = df_auto.loc[df_auto["price"].idxmax(), "company"]
toyota_cars = df_auto[df_auto["company"] == "Toyota"]
total_cars = df_auto["company"].value_counts()
highest_priced_car = df_auto[df_auto["price"] == df_auto["price"].max()]
average_mileage = df_auto["average-mileage"].mean()
df_auto_sorted = df_auto.sort_values(by="price")

print(most_expensive)
print(toyota_cars)
print(total_cars)
print(highest_priced_car)
print(average_mileage)
print(df_auto_sorted)
