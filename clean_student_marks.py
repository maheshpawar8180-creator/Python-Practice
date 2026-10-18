import pandas as pd

# Create a DataFrame. None represents a mark that is missing.
students = {
    "Name": ["Aisha", "Ben", "Carlos", "Divya", "Ethan"],
    "Marks": [85, 92, None, 78, None],
}
df = pd.DataFrame(students)

# Check how many marks are missing before cleaning.
print("Missing marks before cleaning:")
print(df["Marks"].isna().sum())

# Calculate the average of the available marks, then fill in missing marks.
average_marks = df["Marks"].mean()
df["Marks"] = df["Marks"].fillna(average_marks)

# Display the cleaned DataFrame.
print("\nCleaned DataFrame:")
print(df)

# Verify that the DataFrame has no missing values left.
if df.isna().sum().sum() == 0:
    print("\nVerified: no missing values remain.")
else:
    print("\nMissing values still remain.")
