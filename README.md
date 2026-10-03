# SpaceX Falcon 9 Data Science Capstone

## Project Overview

This project analyzes SpaceX Falcon 9 launch data to understand launch and landing patterns and predict the success of the Falcon 9 first-stage landing.

The project follows a complete data science workflow including data collection, web scraping, data wrangling, exploratory data analysis, SQL analysis, geospatial visualization, interactive dashboard development, and machine learning.

## Project Objectives

- Collect Falcon 9 launch data using the SpaceX API and web scraping.
- Clean and prepare the collected data.
- Perform exploratory data analysis and visualization.
- Analyze the data using SQL queries.
- Visualize launch-site locations using Folium.
- Build an interactive Plotly Dash dashboard.
- Predict first-stage landing success using machine learning models.
- Compare different classification models and identify useful insights.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Plotly Dash
- Folium
- SQL / SQLite
- Scikit-learn
- Jupyter Notebook

## Project Workflow

1. Data Collection
2. Web Scraping
3. Data Wrangling
4. Exploratory Data Analysis
5. SQL Analysis
6. Geospatial Analysis with Folium
7. Interactive Visualization with Plotly Dash
8. Predictive Analysis using Machine Learning

## Data Collection

Launch data was collected from the SpaceX API and supplemented with information obtained through web scraping.

The collected information includes launch sites, payload information, booster details, launch outcomes, dates, and landing results.

## Exploratory Data Analysis

The analysis investigates relationships between:

- Launch sites
- Payload mass
- Booster versions
- Launch success
- Landing outcomes
- Launch year and success trends

Visualizations include scatter plots, bar charts, yearly trends, and other statistical graphics.

## SQL Analysis

SQL queries were used to independently analyze the dataset and answer questions related to:

- Number of launch sites
- Launch-site performance
- Payload statistics
- Successful and unsuccessful landings
- Launch rankings
- Launch outcomes

## Folium Geospatial Analysis

Folium was used to create an interactive map showing SpaceX launch sites.

The map includes launch-site markers, launch information, marker clustering, and geographic/proximity analysis.

## Plotly Dash Dashboard

An interactive dashboard was developed using Plotly Dash.

The dashboard provides:

- Launch-site selection
- Landing-success visualization
- Payload range filtering
- Payload versus landing-outcome analysis
- Interactive charts

## Machine Learning

The landing outcome was treated as a binary classification problem.

The following models were evaluated:

- Logistic Regression
- Support Vector Machine
- Decision Tree
- K-Nearest Neighbors

The models were evaluated using classification accuracy and other performance metrics, including confusion matrices.

## Key Result

The final machine learning analysis compares multiple classification models to determine which approach provides the most reliable prediction of Falcon 9 first-stage landing success.

## Repository Structure

```text
spacex-falcon9-data-science-capstone/
│
├── README.md
├── .gitignore
│
├── notebooks/
│   ├── data_collection.ipynb
│   ├── web_scraping.ipynb
│   ├── data_wrangling.ipynb
│   ├── eda.ipynb
│   ├── sql_analysis.ipynb
│   ├── folium_map.ipynb
│   └── machine_learning.ipynb
│
├── dashboard/
│   ├── app.py
│   └── requirements.txt
│
├── data/
│   └── spacex_dataset.csv
│
└── images/
    ├── eda_charts.png
    ├── confusion_matrix.png
    └── dashboard.png
