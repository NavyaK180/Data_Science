import pandas as pd
from sklearn.preprocessing import MinMaxScaler
#Example dataset
data=pd.DataFrame({
    'A':[10,20,30,40,50],
    'B':[5,15,25,35,45]
})
print(data)
#Apply min-Max
scaler=MinMaxScaler()
normalized_data=scaler.fit_transform(data)
#cconvert back to dataframe
normalized_df=pd.DataFrame(normalized_data,columns=data.columns)
print("Normalized Data (Min-Max Scaling)")
print(normalized_df)

from sklearn.preprocessing import StandardScaler
#apply standardization
scaler=StandardScaler()
standardized_data=scaler.fit_transform(data)
#convert back to dataframe
standardized_df=pd.DataFrame(standardized_data,columns=data.columns)
print("Standardized Data")
print(standardized_df)

#example categorical data
df=pd.DataFrame({'Color': ['Red', 'Blue', 'Green', 'Red', 'Blue']})
#one-hot encoding
one_hot=pd.get_dummies(df,columns=['Color'])
print("\nOne-hot Encoding:")
print(one_hot)

import pandas as pd
from sklearn.preprocessing import MinMaxScaler,StandardScaler,LabelEncoder
import seaborn as sns
#load dataset
tips=sns.load_dataset("tips") #or pd.read_csv("tips.csv")
print("Original Data (first 5 rows):")
print(tips.head())
#1.Normalization(Min-Max Scaling)
numeric_cols=tips.select_dtypes(include=['float64','int64']).columns
scaler_minmax=MinMaxScaler()
tips_normalized=tips.copy()
tips_normalized[numeric_cols]=scaler_minmax.fit_transform(tips[numeric_cols])
print("\nNormalized Data (first 5 rows):")
print(tips_normalized.head())
#2.standardization(z-score)
scaler_standard=StandardScaler()
tips_standardized=tips.copy()
tips_standardized[numeric_cols]=scaler_standard.fit_transform(tips[numeric_cols])
print("\nStandardized Data (first 5 rows):")
print(tips_standardized.head())
#3. encoding categorical variables
#(a) one-hot encoding
tips_onehot=pd.get_dummies(tips,columns=['sex','smoker','day','time'])
print("\nOne-Hot Encoded Data (first 5 rows):")
print(tips_onehot.head())

import pandas as pd
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
#load dataset
tips=sns.load_dataset("tips")
#select numeric columns
numeric_cols=tips.select_dtypes(include=['float64','int64'])
#step 1: standardize the data(important for pca)
scaler=StandardScaler()
scaled_data=scaler.fit_transform(numeric_cols)
#step 2: apply pca
pca=PCA(n_components=2)
pca_result=pca.fit_transform(scaled_data)
#step 3:create a dataframe with pca results
pca_df=pd.DataFrame(data=pca_result,columns=['PC1','PC2'])
print("Explained Variance ratio:",pca.explained_variance_ratio_)
print("\nPCA Result (first 5 rows):")
print(pca_df.head())

import matplotlib.pyplot as plt
plt.scatter(pca_df['PC1'],pca_df['PC2'],alpha=0.7)
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA Projection of Tips Dataset')
plt.show()  