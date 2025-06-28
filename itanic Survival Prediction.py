import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the training dataset
df = pd.read_csv('train.csv')  # Adjust path to where you saved train.csv

# Display basic info
print(df.info())
print(df.head())

# Set plot style
sns.set(style="whitegrid")

# Survival by Sex
plt.figure(figsize=(8, 6))
sns.barplot(x='Sex', y='Survived', data=df)
plt.title('Survival Rate by Sex')
plt.ylabel('Survival Rate')
plt.savefig('survival_by_sex.png')  # Save for Appendix
plt.show()

# Survival by Pclass
plt.figure(figsize=(8, 6))
sns.barplot(x='Pclass', y='Survived', data=df)
plt.title('Survival Rate by Passenger Class')
plt.ylabel('Survival Rate')
plt.savefig('survival_by_pclass.png')
plt.show()

# Age distribution by Survival
plt.figure(figsize=(8, 6))
sns.histplot(data=df, x='Age', hue='Survived', bins=30, alpha=0.5)
plt.title('Age Distribution by Survival')
plt.savefig('age_by_survival.png')
plt.show()

# Copy dataframe for preprocessing
df_processed = df.copy()

# Impute missing Age with median
df_processed['Age'].fillna(df_processed['Age'].median(), inplace=True)

# Drop Cabin (too many missing values) and irrelevant columns
df_processed.drop(['Cabin', 'PassengerId', 'Name', 'Ticket'], axis=1, inplace=True)

# Encode categorical variables
df_processed['Sex'] = df_processed['Sex'].map({'male': 0, 'female': 1})
df_processed['Embarked'] = df_processed['Embarked'].fillna('S')  # Fill 2 missing with mode 'S'
df_processed = pd.get_dummies(df_processed, columns=['Embarked'], drop_first=True)

# Check processed data
print(df_processed.info())
print(df_processed.head())

# Create FamilySize
df_processed['FamilySize'] = df_processed['SibSp'] + df_processed['Parch'] + 1  # +1 for the passenger

# Create IsAlone
df_processed['IsAlone'] = (df_processed['FamilySize'] == 1).astype(int)

# Drop original SibSp and Parch (optional, based on preference)
df_processed.drop(['SibSp', 'Parch'], axis=1, inplace=True)

print(df_processed.head())

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Define features (X) and target (y)
X = df_processed.drop('Survived', axis=1)
y = df_processed['Survived']

# Split data (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train logistic regression model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.4f}")

