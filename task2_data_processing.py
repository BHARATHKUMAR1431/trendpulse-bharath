import pandas as pd
import os

file_path = "data/trends_20260408.json"

df = pd.read_json(file_path)

print(f"Loaded {len(df)} stories from {file_path}")

df = df.drop_duplicates(subset="post_id")
print("After removing duplicates:", len(df))

df = df.dropna(subset=["post_id", "title", "score"])
print("After removing nulls:", len(df))

df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].fillna(0).astype(int)

df = df[df["score"] >= 5]
print("After removing low scores:", len(df))

df["title"] = df["title"].str.strip()

output_path = "data/trends_clean.csv"

df.to_csv(output_path, index=False)

print(f"Saved {len(df)} rows to {output_path}")

print("\nStories per category:")
print(df["category"].value_counts())