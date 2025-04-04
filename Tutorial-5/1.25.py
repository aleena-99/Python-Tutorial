import pandas as pd

df_student = pd.read_csv("student.csv")
avg_cgpa = df_student["CGPA"].mean()
above_9 = df_student[df_student["CGPA"] > 9]
cse_above_9 = df_student[(df_student["Branch"] == "CSE") & (df_student["CGPA"] > 9)]
max_cgpa_student = df_student.loc[df_student["CGPA"].idxmax()]
branch_avg_cgpa = df_student.groupby("Branch")["CGPA"].mean()

print(avg_cgpa)
print(above_9)
print(cse_above_9)
print(max_cgpa_student)
print(branch_avg_cgpa)
