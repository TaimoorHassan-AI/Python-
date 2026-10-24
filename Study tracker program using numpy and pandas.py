import pandas as pd
import numpy as np
df = pd.read_csv("study_hours.csv", parse_dates=["date"])
# Data is loaded and Shown in the output Terminal
print("      STUDY HOURS TRACKER     ")
no_of_subjects=5
print("total Number of Subjects = ",no_of_subjects)
#showing subjects name
df = pd.read_csv("study_hours.csv")
for index,row in df.iterrows():
    print("date:",row["date"])
    print("name of subject:",row["subject"])
    print("Day is:",row["day"])
    print("no of hours studied:",row["hours"])
total_hours = df["hours"].sum()
print("Total Hours Studied:", total_hours)

    

