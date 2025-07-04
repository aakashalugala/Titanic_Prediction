Titanic Survival Prediction Project

What is this Project About?

This project is a beginner-friendly exercise to learn data analysis and machine learning using Python in PyCharm, a popular code editor for local development. It uses the famous Titanic dataset to predict whether passengers survived the Titanic disaster based on features like their age, sex, and passenger class. The project involves loading data, exploring it with visualizations, cleaning it, and building a simple machine learning model. It’s a great way to start learning data science and predictive modeling on your own computer!

For additional context on data analysis and machine learning, you can explore Microsoft Learn’s module "Analyze sentiment in text with Keras" to learn about processing data for predictive tasks.

Project Details

What Does the Project Do?





Goal: The project analyzes the Titanic dataset to understand survival patterns and builds a machine learning model to predict whether a passenger survived based on their characteristics.



Dataset: The data comes from a CSV file (train.csv) containing information about Titanic passengers, including:





Survived: Whether the passenger survived (0 = No, 1 = Yes).



Pclass: Passenger class (1 = First, 2 = Second, 3 = Third).



Sex: Male or female.



Age: Passenger’s age.



SibSp: Number of siblings/spouses aboard.



Parch: Number of parents/children aboard.



Embarked: Port of embarkation (C = Cherbourg, Q = Queenstown, S = Southampton).



Local Development with PyCharm: The project runs on a local machine using PyCharm, a free and user-friendly IDE for Python development, leveraging libraries like Pandas, Matplotlib, Seaborn, and Scikit-learn.

How Data is Used





Loading Data: The project loads the Titanic dataset from a local CSV file (train.csv) using Pandas, a Python library for data manipulation. The CSV file is assumed to be in the same directory as the script or a specified path in PyCharm.



Exploring Data: The code generates visualizations (bar charts and histograms) to explore survival rates by sex, passenger class, and age distribution.



Cleaning Data: The data is preprocessed by filling missing values, encoding categorical variables (like sex and port of embarkation), and creating new features (like family size).



Modeling: The cleaned data is used to train a machine learning model to predict survival.

What the Code Does





Load and Inspect Data: Reads the train.csv file and displays basic information (e.g., column types, missing values) and the first few rows.



Visualize Data:





Creates a bar chart showing survival rates by sex (e.g., females had a higher survival rate).



Creates a bar chart showing survival rates by passenger class (e.g., first-class passengers had a higher survival rate).



Creates a histogram showing age distribution for survivors and non-survivors.



Saves all plots as PNG files (survival_by_sex.png, survival_by_pclass.png, age_by_survival.png) for reference.



Preprocess Data:





Fills missing Age values with the median age.



Drops columns with too many missing values (Cabin) or irrelevant data (PassengerId, Name, Ticket).



Converts Sex to numbers (male = 0, female = 1) and encodes Embarked into dummy variables (e.g., Embarked_Q, Embarked_S).



Creates new features: FamilySize (total family members) and IsAlone (whether the passenger was alone).



Build Model: Trains a Logistic Regression model (a simple machine learning algorithm) to predict survival based on the processed features.



Evaluate Model: Tests the model on 20% of the data and prints the accuracy (e.g., percentage of correct predictions).

What the Code Shows





Data Info: Displays the dataset’s structure (e.g., 891 rows, 12 columns, some missing values in Age and Cabin).



Visualizations:





Bar chart: Higher survival rates for females compared to males.



Bar chart: Higher survival rates for first-class passengers compared to second or third class.



Histogram: Age distribution, showing how survival varies by age group.



Processed Data: Shows the cleaned dataset with new columns (FamilySize, IsAlone, Embarked_Q, Embarked_S) and no missing values in key columns.



Model Accuracy: Prints the model’s accuracy (e.g., Model Accuracy: 0.7821), indicating how well it predicts survival.

Skills Gained

By working on this project in PyCharm on your local machine, you’ll learn these beginner-friendly skills:





Data Loading and Exploration: Learn to load CSV files with Pandas and explore data with basic statistics and visualizations.



Data Visualization: Create bar charts and histograms using Matplotlib and Seaborn to understand patterns in data.



Data Preprocessing: Gain experience cleaning data by handling missing values, encoding categorical variables, and creating new features.



Machine Learning Basics: Build and evaluate a simple machine learning model (Logistic Regression) using Scikit-learn to predict outcomes.



Python Programming: Use Python libraries (Pandas, Matplotlib, Seaborn, Scikit-learn) to process and analyze data.



Feature Engineering: Learn to create meaningful features like FamilySize and IsAlone to improve model performance.



Local Development with PyCharm: Understand how to set up and run Python projects in PyCharm, a popular IDE for data science.

Things to Know





Local Execution: The project runs locally in PyCharm, so you need to have Python and the required libraries (pandas, matplotlib, seaborn, scikit-learn) installed. You can install them using pip install pandas matplotlib seaborn scikit-learn in your terminal.



Dataset Requirement: The train.csv file (available from sources like Kaggle) must be in the same directory as the script or you need to specify its path in PyCharm.



Beginner-Friendly: The project is simple, focusing on data exploration, preprocessing, and basic machine learning, making it ideal for learning data science.
