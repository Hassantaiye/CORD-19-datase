import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# --- Page Config ---
st.set_page_config(page_title="CORD-19 Data Explorer", layout="wide")

# --- Load Data ---
@st.cache_data
def load_data():
    df = pd.read_csv("metadata_sample.csv")
    df = df.dropna(subset=["title", "publish_time"]).copy()
    df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")
    df["year"] = df["publish_time"].dt.year
    df["abstract_word_count"] = (
        df["abstract"].fillna("").apply(lambda x: len(x.split()))
    )
    return df

df = load_data()

# --- Title ---
st.title("📊 CORD-19 Data Explorer")
st.write("Interactive exploration of COVID-19 research papers metadata")

# --- Show Sample Data ---
if st.checkbox("Show raw data sample"):
    st.dataframe(df.head(20))

# --- Year Range Filter ---
year_min, year_max = int(df["year"].min()), int(df["year"].max())
year_range = st.slider("Select year range", year_min, year_max, (2020, 2021))
df_filtered = df[(df["year"] >= year_range[0]) & (df["year"] <= year_range[1])]

# --- Publications by Year ---
year_counts = df_filtered["year"].value_counts().sort_index().dropna()
plt.figure(figsize=(8, 5))
plt.bar(year_counts.index, year_counts.values)
plt.title("Publications by Year")
plt.xlabel("Year")
plt.ylabel("Count")
plt.savefig("publications_by_year.png")
plt.close()

# --- Top Journals ---
st.subheader("🏆 Top Journals Publishing COVID-19 Research")
top_journals = df_filtered["journal"].value_counts().head(10)
fig, ax = plt.subplots()
top_journals.plot(kind="bar", ax=ax)
ax.set_ylabel("Number of Papers")
st.pyplot(fig)

# --- Word Cloud of Titles ---
st.subheader("☁️ Frequent Words in Paper Titles")
titles = " ".join(df_filtered["title"].dropna().tolist())
if titles.strip():
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(titles)
    fig, ax = plt.subplots(figsize=(10,5))
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)
else:
    st.info("No titles available to generate a word cloud.")
    plt.show()