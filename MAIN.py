import pandas as pd
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

df = pd.read_csv("study_hours.csv", parse_dates=["date"])

# Print the data in the terminal
print("      STUDY HOURS TRACKER     ")
print("total Number of Subjects = ", df["subject"].nunique())

for index, row in df.iterrows():
    print("date:", row["date"])
    print("name of subject:", row["subject"])
    print("Day is:", row["day"])
    print("no of hours studied:", row["hours"])

print("Total Hours Studied:", df["hours"].sum())

# Rows = subjects, columns = days, values = total hours
pivot = df.pivot_table(index="subject", columns="day", values="hours",
                       aggfunc="sum", fill_value=0)

# Stacked horizontal bars: one segment per day
fig, ax = plt.subplots(figsize=(9, 5), num="Study Hours Tracker")
left = [0] * len(pivot.index)

for day in pivot.columns:
    values = pivot[day].values
    bars = ax.barh(pivot.index, values, left=left, label=day)
    # Label each segment with its hours; hide labels for zero-hour segments
    labels = [f"{v:.1f}h" if v > 0 else "" for v in values]
    ax.bar_label(bars, labels=labels, label_type="center", color="white", fontsize=9)
    left = [l + v for l, v in zip(left, values)]

# Show each subject's total at the end of its bar
for i, total in enumerate(left):
    ax.text(total + 0.1, i, f"{total:.1f}h total", va="center")

ax.set_title("Study Hours per Subject by Day")
ax.set_xlabel("Hours Studied")
ax.set_ylabel("Subject")
ax.legend(title="Day")
ax.grid(True, axis="x", linestyle="--", alpha=0.6)

plt.tight_layout()
plt.show()