import pandas as pd

df_emp = pd.read_csv("employee.csv")
df_emp.head(7)
df_emp.sort_values("name")
emp_highest_salary = df_emp.loc[df_emp["salary"].idxmax(), "name"]
male_employees = df_emp[df_emp["gender"] == "Male"]["name"]
unique_teams = df_emp["team"].unique()

print(emp_highest_salary)
print(male_employees)
print(unique_teams)
