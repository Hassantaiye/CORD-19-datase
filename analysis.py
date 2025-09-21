# assignment.py
# ---------------------------------------------------------
# CORD-19 Data Analysis Assignment
# ---------------------------------------------------------
# Steps:
# 1. Load and explore data
# 2. Clean and prepare dataset
# 3. Perform analysis and create visualizations
# ---------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import os

# --- Part 1: Data Loading and Basic Exploration ---
print("Loading data...")
df = pd.read_csv("metadata_sample.csv")

# Inspect the data
print("\nFirst 5 rows:")
print(df.head())
print("\nDataFrame shape:", df.shape)
print("\nInfo:")
print(df.info())
print("\nMissing values (top 10 columns):")
print(df.isnull().sum().sort_values(ascending=False).head(10))

# --- Part 2: Data Cleaning and Preparation ---
print("\nCleaning data...")

# Convert publish_time to datetime
df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")
df["year"] = df["publish_time"].dt.year

# Abstract word count
df["abstract_word_count"] = df["abstract"].fillna("").apply(lambda x: len(x.split()))

# Remove rows with missing title or publish_time
df_clean = df.dropna(subset=["title", "publish_time"]).copy()

print("Cleaned DataFrame shape:", df_clean.shape)

# --- Part 3: Data Analysis and Visualization ---

# Publications by year
year_counts = df_clean["year"].value_counts().sort_index()
plt.figure(figsize=(8, 5))
plt.bar(year_counts.index, year_counts.values)
plt.title("Publications by Year")
plt.xlabel("Year")
plt.ylabel("Count")
plt.show()
plt.close()

# Top journals
top_journals = df_clean["journal"].value_counts().head(10)
plt.figure(figsize=(10, 6))
top_journals.plot(kind="bar")
plt.title("Top Journals Publishing COVID-19 Research")
plt.xlabel("Journal")
plt.ylabel("Count")
plt.xticks(rotation=45, ha="right")
plt.show()
plt.close()

# Word cloud of titles
titles_text = " ".join(df_clean["title"].dropna().astype(str).tolist())
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(titles_text)
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Word Cloud of Paper Titles")
plt.show()
plt.close()

# Distribution by source_x (paper source)
if "source_x" in df_clean.columns:
    source_counts = df_clean["source_x"].value_counts().head(10)
    plt.figure(figsize=(10, 6))
    source_counts.plot(kind="bar")
    plt.title("Top Sources of Papers")
    plt.xlabel("Source")
    plt.ylabel("Count")
    plt.xticks(rotation=45, ha="right")
    plt.show()
    plt.close()

