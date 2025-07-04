#Ttitanic_Prediction
What is this Project About?

This project is a beginner-friendly exercise to learn data preprocessing for population prediction using Microsoft Fabric, a powerful cloud platform for data analytics and machine learning. It processes a dataset of population data (like the number of males and females in different countries and age groups over time) to prepare it for analysis or prediction tasks. The project uses PySpark, a tool for handling large datasets, to clean and transform the data in Microsoft Fabric’s environment. It’s a great way to start learning how to work with real-world data in the cloud!

Although this project focuses on population data, you can explore related concepts like data analysis and machine learning through Microsoft Learn’s module "Analyze sentiment in text with Keras" for additional context on preparing data for AI tasks.

Project Details

What Does the Project Do?





Goal: The project cleans and organizes population data from a table (called Bronze_LH.Bronzed_Fact) to make it ready for analysis or building a model to predict future population trends.



Dataset: The data includes population information for various countries (e.g., Guyana, Botswana), years (e.g., 2050–2100), age groups (e.g., 100+), and populations split by gender (male and female). The notebook loads 1,000 rows from a larger dataset stored in Microsoft Fabric’s data lake.



Microsoft Fabric: The project runs in Microsoft Fabric, a cloud platform that combines data storage, processing, and analytics tools like PySpark and data lakes, making it easy to work with big data.

How the Data is Prepared





Loading Data: The code loads data from a table (Bronze_LH.Bronzed_Fact) in Microsoft Fabric using PySpark, selecting columns for location (country), time (year), age group, and male/female populations.



Cleaning Age Groups: Fixes errors in the AgeGrp column, like changing "09-May" or "9-May" to "5-9", "14-Oct" to "10-14", and "#N/A" to "NA" to make the data consistent.



Renaming Columns: Renames PopMale to Male and PopFemale to Female for clarity.



Changing Data Types: Converts the Time column to integers (e.g., 2050) and Male/Female columns to decimals (e.g., 0.007) for accurate calculations.



Reshaping Data: Transforms the data so that Male and Female populations are combined into a single Population column, with a new Gender column (Male or Female) to make the data easier to analyze.



Saving Data: Saves the cleaned data as a new table (silver_Fact) in Microsoft Fabric’s data lake in Delta format, which is great for storing and querying large datasets.



Exploring Data: Shows a summary of how many records exist for each country (e.g., Guyana has 32 records, Kiribati has 51).

What the Code Shows





Sample Data: Displays a table with columns like location (e.g., Guyana), time (e.g., 2064), age group (e.g., 100+), and male/female populations (e.g., 0.007 and 0.015 million).



Summary: Shows a count of records per country (e.g., Tunisia has 51 records), helping you understand the dataset’s scope.



Cleaned Output: The final table (silver_Fact) is organized for future analysis, with clean age groups, proper data types, and a reshaped structure.

Skills Gained

By working on this project in Microsoft Fabric, you’ll learn these beginner-friendly skills:





Data Preprocessing: Learn how to clean and organize messy data (e.g., fixing age group names, renaming columns) to make it usable for analysis.



PySpark Programming: Gain experience using PySpark to process large datasets, including selecting columns, cleaning data, and reshaping tables.



Microsoft Fabric: Understand how to use Microsoft Fabric’s cloud environment, including data lakes and PySpark notebooks, for data analytics tasks.



Data Transformation: Practice reshaping data (e.g., unpivoting male/female columns) to make it easier for machine learning or reporting.



Working with Big Data: Get hands-on experience with tools like Delta tables for storing and managing large datasets in the cloud.



Data Exploration: Learn to summarize data (e.g., counting records by country) to understand its structure and patterns.



Python and SQL Basics: Use Python (via PySpark) and simple SQL queries to load and manipulate data, building foundational coding skills.

Things to Know





No Prediction Model Yet: This notebook focuses on cleaning data, not building a prediction model. The Microsoft Learn module on sentiment analysis can guide you on how to add machine learning steps for prediction tasks.



Beginner-Friendly: The project is simple and focuses on data preparation, making it a great starting point for learning data analytics in Microsoft Fabric.



Microsoft Fabric Advantage: Using Fabric’s cloud tools (like PySpark and Delta tables) makes it easy to handle large datasets and scale up for bigger projects.
