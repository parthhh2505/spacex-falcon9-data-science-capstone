# SpaceX Falcon 9 Data Science Capstone

IBM Applied Data Science Capstone project analyzing Falcon 9 launch and first-stage landing outcomes.

## Repository
https://github.com/parthhh2505/spacex-falcon9-data-science-capstone

## Project question
Can historical Falcon 9 mission attributes be used to predict whether the first stage lands successfully?

## Workflow
SpaceX API → Web Scraping → Data Wrangling → EDA → SQL → Folium → Plotly Dash → Machine Learning

## Dataset
The standard capstone analytical dataset contains 90 Falcon 9 records and a binary `Class` target:
- `1` = successful first-stage landing
- `0` = unsuccessful/no successful landing outcome

For reproducibility, the notebooks download a public capstone dataset at runtime:
https://raw.githubusercontent.com/adgsenpai/IBM-DataScience-SpaceX-Capstone/main/dataset_part_2.csv

## Machine learning
The standard workflow uses an 80/20 split (72 train / 18 test), categorical encoding, scaling, GridSearchCV, Logistic Regression, SVM, Decision Tree and KNN.

The supplied capstone presentation reports 83.33% test accuracy for each model on the standard 18-record test split. Because the test set is small, this is an evaluation snapshot rather than a guarantee of future performance.

## Run the dashboard
```bash
pip install -r requirements.txt
python dashboard/app.py
```

## Notebook order
1. `01_data_collection_api.ipynb`
2. `02_web_scraping.ipynb`
3. `03_data_wrangling.ipynb`
4. `04_eda_visualization.ipynb`
5. `05_eda_sql.ipynb`
6. `06_folium_launch_sites.ipynb`
7. `07_machine_learning.ipynb`

## Submission
Keep the repository public and submit the final PDF from `presentation/`.
