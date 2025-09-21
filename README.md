# CORD-19-datase

# 🦠 CORD-19 Data Analysis Application

## 📖 Overview
This project provides a comprehensive analysis of the **CORD-19 dataset**, which contains metadata about COVID-19 research papers.  
It includes both a **Streamlit web application** for interactive exploration and a **Python script** for automated analysis.

---

## ✨ Features

### 🔹 Streamlit App (`app.py`)
- Interactive data exploration with filtering capabilities  
- Visualizations including **bar charts** and **word clouds**  
- Year range filtering for temporal analysis  
- Display of **top journals** publishing COVID-19 research  
- Word cloud visualization of paper titles  

### 🔹 Analysis Script (`assignment.py`)
- Automated **data loading and cleaning**  
- Basic **data exploration** and statistics  
- Generation of visualizations for:
  - Publications by year  
  - Top journals  
  - Paper sources  
- Word cloud generation for paper titles  

---

## ⚙️ Installation

1. **Clone or download** the project files.  
2. Install required dependencies:

   ```bash
   pip install streamlit pandas matplotlib wordcloud


# 🦠 CORD-19 Data Analysis Application

## 📂 Prerequisite
Ensure you have the **`metadata_sample.csv`** file in the same directory as the scripts.

---

## 🚀 Usage

### Running the Streamlit App
1. Navigate to the project directory in your terminal.  
2. Run the following command:

   ```bash
   streamlit run app.py
3. The app will open in your default browser.
4. Use the sidebar controls to filter data by year range.
5. Explore visualizations and data samples.

# 🦠 CORD-19 Data Analysis Application

## 📂 File Structure

├── app.py # Streamlit web application
├── assignment.py # Data analysis script
├── metadata_sample.csv # Dataset
└── README.md # Project documentation

---

## 🚀 Overview
This project provides tools for exploring and analyzing the **CORD-19 dataset**, which contains metadata about COVID-19 research papers.  
It includes:  
- A **Streamlit app** for interactive data visualization.  
- A **Python script** for automated data analysis and statistics.  

---

## 🔑 Features
- Interactive filtering and exploration via Streamlit.  
- Visualizations: bar charts, word clouds, and publication trends.  
- Year range filtering for temporal analysis.  
- Display of top journals publishing COVID-19 research.  
- Automated analysis with data cleaning and statistics.  

---

## 📊 Data Description
The dataset includes:  
- Paper titles and abstracts  
- Publication dates  
- Journal information  
- Source metadata  

---

## 🎨 Customization
- Change the number of top journals displayed by editing `.head(10)`.  
- Modify **WordCloud** appearance via parameters.  
- Update default year ranges in the Streamlit slider.  

---

## 📋 Requirements
- Python 3.7+  
- Streamlit  
- Pandas  
- Matplotlib  
- WordCloud  

Install dependencies with:  
```bash
pip install -r requirements.txt
