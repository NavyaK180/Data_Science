import pandas as pd
data={'apples':[3,2,0,1], 'oranges':[0,3,7,2]}
df=pd.DataFrame(data)
print (df)
df=pd.DataFrame(data, index=['Ahmed','Ali','Rashed','Hamza'])
print(df)

#csv file
import pandas as pd
df=pd.read_csv('Iris.csv')
print(df)
#df.info()
#df.head()
#df.tail()
#df.shape()
#TOP ROWS
print(df.head(10))
#deatils of the dataset
print(df.info())
#bottom rows
print(df.tail(3))
#no of rows and columns
print(df.shape)

#json file
import pandas as pd
df=pd.read_json("sample1.json")
print(df)

#
import pandas as pd
df=pd.read_csv("Iris.csv")
print(df.shape)
#hai
dup_df=pd.concat([df,df])
print(dup_df.shape)
#to drop duplicates
dup_df.drop_duplicates(inplace=True)
print(dup_df.shape)

#dataframe to csv conversion
import pandas as pd
data=[1,2,3,10,20,30]
df=pd.DataFrame(data)
print(df)

import pandas as pd
data={'Name':['AA','BB'], 'Age':[30,45]}
df=pd.DataFrame(data)
print(df)
#to create new csv file 
df.to_csv('abc.csv',index=True) # or df.to_csv('abc.csv')

import pandas as pd
data={'col_1':[3,2,1,0], 'col_2':['a','b','c','d']}
df=pd.DataFrame.from_dict(data)
print(df)
data={'row_1':[3,2,1,0], 'row_2':['a','b','c','d']}
df=pd.DataFrame.from_dict(data,orient='index')
print(df)
data={'row_1':[3,2,1,0],'row_2':['a','b','c','d']}
df=pd.DataFrame.from_dict(data,orient='index',columns=['A','B','C','D'])
print(df)
 
#ASSIGNMENT
import pandas as pd
# Creating the dataset
data = {
    "Roll No": [101,102,103,104,105,106,107,108,109,110],
    "Name": ["Aarav","Bhavya","Navya","Deepika","Sahasra","Nandini","Hasini","Keerthi","Saranya","Sai"],
    "Age": [19,20,19,21,20,19,22,20,21,19],
    "Section": ["A","A","B","A","B","C","A","B","C","A"],
    "DS": [88,76,91,85,79,92,68,87,90,81],
    "QC": [82,89,85,78,91,88,75,84,86,80],
    "TOC": [90,81,87,84,83,95,72,89,88,85]
}
# Create DataFrame
df = pd.DataFrame(data)
# Display the DataFrame
print(df)
# Convert DataFrame to CSV
df.to_csv("students.csv", index=False)

import pandas as pd
# Read the CSV file
df = pd.read_csv("students.csv")
# Display the entire dataset
print(df)
# Display the first 5 rows
print(df.head())
# Display the last 5 rows
print(df.tail())
# Display dataset information
df.info()
# Display the number of rows and columns
print(df.shape)

import pandas as pd
# Read the CSV file
df = pd.read_csv("students.csv")
print(df)
# Create duplicate rows (duplicate first 2 rows)
df_duplicate = pd.concat([df, df.iloc[0:2]], ignore_index=True)
print(df_duplicate)
# Check duplicate rows
print(df_duplicate[df_duplicate.duplicated()])
# Remove duplicate rows
df_no_duplicates = df_duplicate.drop_duplicates()
print(df_no_duplicates)
# Save the cleaned dataset
df_no_duplicates.to_csv("students_no_duplicates.csv", index=False)
