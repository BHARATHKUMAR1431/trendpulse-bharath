# TrendPulse 📊

TrendPulse is a Python data pipeline that collects live trending stories from the HackerNews API, processes the data, performs analysis, and generates visual insights.

The project demonstrates practical skills in API handling, data cleaning, numerical analysis, and data visualisation using Python libraries such as Pandas, NumPy, and Matplotlib.

---

## Project Pipeline

The pipeline is divided into four stages:

1. **Data Collection**
   Fetches top trending stories from the HackerNews public API and stores structured data in JSON format.

2. **Data Processing**
   Cleans the dataset by removing duplicates, handling missing values, and filtering low-quality entries. The cleaned data is saved as a CSV file.

3. **Data Analysis**
   Uses Pandas and NumPy to compute statistics, identify trends, and create new analytical features such as engagement score and popularity flag.

4. **Data Visualisation**
   Generates charts that highlight key insights including top performing stories, category distribution, and relationship between score and discussion activity.

---

## Technologies Used

* Python 3
* requests
* pandas
* numpy
* matplotlib

---

## Project Structure

```
trendpulse
│
├── task1_data_collection.py
├── task2_data_processing.py
├── task3_analysis.py
├── task4_visualization.py
│
├── data
│   ├── trends_YYYYMMDD.json
│   ├── trends_clean.csv
│   └── trends_analysed.csv
│
└── outputs
    ├── top10_scores.png
    ├── category_distribution.png
    └── score_vs_comments.png
```

---

## How to Run

Install dependencies:

```
pip install requests pandas numpy matplotlib
```

Run scripts in order:

```
python task1_data_collection.py
python task2_data_processing.py
python task3_analysis.py
python task4_visualization.py
```

---

## Output

The pipeline produces:

* Structured dataset of trending stories
* Cleaned and analysed CSV files
* Visual charts showing trends and engagement patterns

---

## Purpose

This project demonstrates the complete workflow of transforming raw API data into meaningful insights through data processing and visualisation.
