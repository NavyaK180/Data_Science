import seaborn as sns
tips=sns.load_dataset("tips")
print(tips.head())

#Define the problem:
#predicy whether a oassenger survived the titanic diasaster based on features
objective = "Classification: Survived (Yes/No)"
success_criteria="Accuracy > 80%"
constraints="Limited features, missing values,imbalanced classes"
print("Objective:",objective)
print("Success Criteria:",success_criteria)
print("Constraints:",constraints)

#Data collection
#import pandas as pd
#load dataset(Titanic dataset from seaborn or csv)
import seaborn as sns
df=sns.load_dataset("titanic")
print("Data shape:",df.shape)
print(df.head())
print(df.info())
print(df.describe())

#data cleaning & preprocessing
#handle missing values
import pandas as pd
import seaborn as sns
df=sns.load_dataset("titanic")
#fill missing values
df['age'].fillna(df['age'].median(),inplace=True)
df['embarked'].fillna(df['embarked'].mode()[0],inplace=True)
#drop duplicates
df.drop_duplicates(inplace=True)
#encode categorical variables
df=pd.get_dummies(df,columns=['sex','class','embarked'],drop_first=True)
#feature engineering family size
df['family_size']=df['sibsp']+df['parch']
print(df.head())

import pandas as pd
# Load student.csv
df = pd.read_csv("student.csv")
# Remove extra spaces from column names
df.columns = df.columns.str.strip()
# Handle missing values
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Attendance'] = df['Attendance'].fillna(df['Attendance'].median())
df['Math_Score'] = df['Math_Score'].fillna(df['Math_Score'].median())
df['Science_Score'] = df['Science_Score'].fillna(df['Science_Score'].median())
df['Email'] = df['Email'].fillna(df['Email'].mode()[0])
# Remove duplicate rows
df.drop_duplicates(inplace=True)
# Encode categorical variables
df = pd.get_dummies(df, columns=['Gender', 'Department', 'City'], drop_first=True)
# Feature engineering
df['Total_Score'] = df['Math_Score'] + df['Science_Score']
# Display data
print(df.head())


#exploratory data analysis (EDA)
import matplotlib.pyplot as plt
import seaborn as sns
#histogram of age
sns.histplot(df['Age'],bins=10,kde=True)
plt.title("Age Distribution")
plt.show()
# Histogram of Attendance
sns.histplot(df['Attendance'], bins=10, kde=True)
plt.title("Attendance Distribution")
plt.xlabel("Attendance")
plt.ylabel("Number of Students")
plt.show()
#HEATMAP
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#Select only numeric columns for correlation calculation
#numeric_df=df.select_dtypes(include=['number','bool'])
corr=df.corr(numeric_only=True)
print(corr)
sns.heatmap(corr,annot=True,cmap="coolwarm")
plt.title("Correlation matrix")
plt.show()
