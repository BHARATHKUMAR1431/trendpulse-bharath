import pandas as pd
import numpy as np

file_path = "data/trends_clean.csv"

df = pd.read_csv(file_path)

print("Loaded data:", df.shape)

print("\nFirst 5 rows:")
print(df.head())

avg_score = np.mean(df["score"])
avg_comments = np.mean(df["num_comments"])

print("\nAverage score:", int(avg_score))
print("Average comments:", int(avg_comments))

print("\n--- NumPy Stats ---")

mean_score = np.mean(df["score"])
median_score = np.median(df["score"])
std_score = np.std(df["score"])

print("Mean score:", int(mean_score))
print("Median score:", int(median_score))
print("Std deviation:", int(std_score))

print("Max score:", np.max(df["score"]))
print("Min score:", np.min(df["score"]))

most_category = df["category"].value_counts().idxmax()
count_category = df["category"].value_counts().max()

print("\nMost stories in:", most_category, "(", count_category, "stories )")

most_comments_row = df.loc[df["num_comments"].idxmax()]

print("\nMost commented story:")
print(most_comments_row["title"], "-", most_comments_row["num_comments"], "comments")

df["engagement"] = df["num_comments"] / (df["score"] + 1)

df["is_popular"] = df["score"] > avg_score

output_path = "data/trends_analysed.csv"

df.to_csv(output_path, index=False)

print("\nSaved to", output_path)