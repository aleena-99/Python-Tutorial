import pandas as pd
import matplotlib.pyplot as plt

df_sales = pd.read_csv("sales.csv")
plt.scatter(df_sales["month_number"], df_sales["toothpaste"])
plt.show()
df_sales[["facecream", "facewash"]].plot(kind="bar")
plt.show()
df_sales.sum().plot.pie()
plt.show()
