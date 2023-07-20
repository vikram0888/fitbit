## Thyroid Disease Detection

#### Problem Statement:
    


## Demo

video link here--->



## Technical Aspects

- Python 3.7 and more
- Important Libraries: sklearn, pandas, numpy, matplotlib & seaborn
- Front-end: HTML, CSS 
- Back-end: Flask framework
- IDE: Jupyter Notebook, Pycharm & VSCode
- Database: SQLite
- Deployment: Locally

# How to run this app 

Code is written in Python 3.7 and more. If you don't have python installed on your system, click here https://www.python.org/downloads/ to install.

- Create virtual environment  
```conda create -p venv python==3.7 -y ```

- Activate the environment     
```conda activate venv ```

- Install the packages     
```pip install -r requirements.txt ```

- Run the app     
```python webapp\project_library_layer\initializer\setup_configuration.py ```


# Workflow

## Data Collection

Thyroid Disease Data Set from UCI Machine Learning Repository.

Link:https://archive.ics.uci.edu/ml/datasets/thyroid+disease

## Data Pre-processing

   - Drop columns not useful for training the model. Such columns were selected while doing the EDA.
   - Replace the invalid values with numpy “nan” so we can use imputer on such values.
   - Encode the categorical values
   - Check for null values in the columns. If present, impute the null values using the KNN imputer.
   - After imputing, handle the imbalanced dataset by using RandomOverSampler

## Model Creation and Evaluation

- Various classification algorithms like Random Forest, XGBoost, KNN etc tested.
- Random Forest, XGBoost and KNN were all performed well. XGBoost, Random Forest was chosen for the final model training and testing.
- Hyper parameter tuning was performed using RandomizedSearchCV
- Model performance evaluated based on accuracy, confusion matrix, classification report.


## Database Connection
SQLite database used for this project.

## Model Deployment
The final model is deployed locally.

## Batch File Prediction User Interface
#### Login Page
![login page fitbit](https://github.com/vikram0888/fitbit/assets/100748938/b22fe9ca-d019-4136-84e2-48cd7be3052e)



#### Prediction Page
![prediction page](https://github.com/vikram0888/fitbit/assets/100748938/bd32d3f6-0efb-4e51-b168-97a102ae5441)





## initialize git repo

```
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin <github_url>
git push -u origin main
```


## to update the modification

```
git add .
git commit -m "proper message"
git push 
```


# Author

Vikram Jha: https://www.linkedin.com/in/vikram888/
