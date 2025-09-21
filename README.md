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

## Running the Analysis Script

**Run the Python script directly:**

```bash
python assignment.py
The script will output data statistics and display visualizations.
# 🦠 CORD-19 Data Analysis Application

## 📂 File Structure
```bash
.
├── app.py                 # Streamlit web application
├── assignment.py          # Data analysis script
├── metadata_sample.csv    # Dataset (not included in repository)
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
# 🦠 CORD-19 Data Analysis Application

## 📊 Data Description
The application analyzes the **CORD-19 dataset**, which includes:  
- Paper titles and abstracts  
- Publication dates  
- Journal information  
- Source metadata  

---

## 🔑 Key Functionalities

### 📂 Data Loading & Cleaning
- Handles missing values  
- Converts publication dates to datetime format  
- Calculates abstract word counts  

### 🔎 Data Exploration
- Basic statistics and data overview  
- Missing value analysis  
- Temporal distribution of publications  

### 📈 Visualizations
- Publications by year chart  
- Top journals bar chart  
- Word cloud of paper titles  
- Paper sources distribution (if available)  

---

## 🎨 Customization
You can adjust the app to fit your needs:  
- Change the number of top journals by editing `.head(10)`  
- Modify the **WordCloud** appearance via its parameters  
- Update the default year range in the Streamlit slider  

---

## 📋 Requirements
- Python 3.7+  
- Streamlit  
- Pandas  
- Matplotlib  
- WordCloud  

Install dependencies:  
```bash
pip install -r requirements.txt
## 📝 Notes
- The application expects a file named **`metadata_sample.csv`** in the same directory.  
- The original dataset can be found here: [CORD-19 on Kaggle](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)  
- For large datasets, consider using a subset of the data for better performance.  

---

## 🔮 Future Enhancements
Potential improvements include:  
- More interactive filters (e.g., by journal, source)  
- Topic modeling on abstracts  
- Citation analysis (if data is available)  
- Advanced NLP for text analysis  
- Export functionality for processed data & visualizations  

---

## 📜 License
This project is provided **for educational purposes only**.  
Please ensure compliance with the **CORD-19 dataset terms of use** when applying this project.  

   ```bash
   pip install streamlit pandas matplotlib wordcloud
