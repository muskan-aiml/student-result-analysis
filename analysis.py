import pandas as pd
import matplotlib.pyplot as plt

# CSV file load karo
df = pd.read_csv("student record.csv")

# Check karo data sahi aaya kya
print(df.head())
df["Average"] = df[["Maths", "Physics", "Chemistry", "English", "Hindi" ]].mean(axis=1)
print(df[["Name", "Average"]])
# Sabse zyada average wala student
topper = df.loc[df["Average"].idxmax()]
print("Topper is:", topper["Name"], "with average:", topper["Average"])
# # Failed students
# failed_students = df[df["Average"] < 45]
# print("Failed Students:")
# print(failed_students[["Name", "Average"]])
# Failed students wo hain jinka kisi bhi subject mein marks 33 se kam hai
failed = df[(df["Maths"] < 33) | (df["Physics"] < 33) | (df["Chemistry"] < 33) | (df["English"] < 33) | (df["Hindi"] < 33)]
print("Failed students:")
print(failed[["Name", "Maths", "Physics", "Chemistry", "English", "Hindi"]])
subject_avg = df[["Maths", "Physics", "Chemistry", "English", "Hindi"]].mean()
print("Subject wise average:")
print(subject_avg)
plt.style.use('dark_background')
plt.bar(subject_avg.index, subject_avg.values)
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.title("Subject Wise Average")
plt.show()
Top5 = df.sort_values("Average", ascending=False).head(5)
print("Top 5 Students")
print(Top5[["Name", "Average"]])
plt.bar(Top5["Name"], Top5["Average"])
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.title("Top 5 Students")
plt.show()
plt.hist(df["Average"], bins=10, color="orange", edgecolor="black")
plt.xlabel("Average Marks")
plt.ylabel("Number of Students")
plt.title("Marks Distribution")
plt.savefig("marks_distribution.png")
plt.show()