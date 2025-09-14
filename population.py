import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("data.csv")

# ----- Histogram: Median Age -----
plt.figure(figsize=(8,5))
plt.hist(df["median_age"], bins=10, color="skyblue", edgecolor="black", alpha=0.8)
plt.title("Distribution of Median Age", fontsize=14)
plt.xlabel("Median Age")
plt.ylabel("Frequency")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()

# ----- Bar Chart: Average Fertility Rate by Region -----
plt.figure(figsize=(10,6))
colors = plt.cm.Set3(range(len(df["region"].unique())))  # colorful colormap
df.groupby("region")["fertility_rate"].mean().plot(
    kind="bar", color=colors, edgecolor="black"
)
plt.title("Average Fertility Rate by Region", fontsize=14)
plt.xlabel("Region")
plt.ylabel("Average Fertility Rate")
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()
