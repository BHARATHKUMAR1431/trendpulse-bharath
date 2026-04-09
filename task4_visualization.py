import pandas as pd
import matplotlib.pyplot as plt
import os

file_path = "data/trends_analysed.csv"

df = pd.read_csv(file_path)

print("Loaded rows:", len(df))

os.makedirs("outputs", exist_ok=True)

top10 = df.sort_values(by="score", ascending=False).head(10)

plt.figure()
plt.barh(top10["title"], top10["score"])
plt.xlabel("Score")
plt.title("Top 10 Trending Stories by Score")
plt.gca().invert_yaxis()

plt.savefig("outputs/top10_scores.png", bbox_inches="tight")

category_counts = df["category"].value_counts()

plt.figure()
plt.bar(category_counts.index, category_counts.values)
plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.title("Stories per Category")

plt.savefig("outputs/category_distribution.png", bbox_inches="tight")

plt.figure()
plt.scatter(df["score"], df["num_comments"])
plt.xlabel("Score")
plt.ylabel("Comments")
plt.title("Score vs Comments")

plt.savefig("outputs/score_vs_comments.png", bbox_inches="tight")

print("Charts saved in outputs folder")