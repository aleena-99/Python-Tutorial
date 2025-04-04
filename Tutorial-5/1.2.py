import pandas as pd
import matplotlib.pyplot as plt

df_sales = pd.read_csv("sales.csv")
df_sales.plot(x="month_number", y=["facecream", "facewash"], marker='o')
plt.legend()
plt.show()
