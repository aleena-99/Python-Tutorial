import pandas as pd
import matplotlib.pyplot as plt

df_students = pd.read_csv("stud.csv")
df_students.set_index("rollno", inplace=True)
df_students[["name", "mark"]]
df_students.sort_values(by="name")
df_students.sort_values(by="mark", ascending=False)
avg_mark = df_students["mark"].mean()
median_mark = df_students["mark"].median()
mode_mark = df_students["mark"].mode()[0]
min_mark = df_students["mark"].min()
max_mark = df_students["mark"].max()
variance_mark = df_students["mark"].var()
std_dev_mark = df_students["mark"].std()
plt.hist(df_students["mark"])
plt.show()
df_students.drop(columns=["place"], inplace=True)

print(avg_mark, median_mark, mode_mark, min_mark, max_mark, variance_mark, std_dev_mark)
