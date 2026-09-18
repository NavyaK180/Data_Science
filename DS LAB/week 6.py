import pandas as pd
from sklearn.datasets import load_iris
from statistics import mode
#load iris dataset
iris=load_iris()
df=pd.DataFrame(iris.data, columns=iris.feature_names)
print("First 5 rows of dataset:")
print(df.head())
#mean(Average)
mean_values=df.mean()
print("\n Mean values:")
print(mean_values)
#median (middle value)
median_values=df.median()
print("\nMedian values:")
print(median_values)
#mode(most frequent value)
#pandas mode returns a DataFrame(can be multiple modes)
mode_values=df.mode().iloc[0]
print("\nMode values:")
print(mode_values)

#do same for tips dataset also
import pandas as pd
# load tips dataset
df = pd.read_csv("tips.csv")
print("First 5 rows of dataset:")
print(df.head())
#mean(Average)
mean_values=df.mean(numeric_only=True)
print("\n Mean values:")
print(mean_values)
#median (middle value)
median_values=df.median(numeric_only=True)
print("\nMedian values:")
print(median_values)
#mode(most frequent value)
#pandas mode returns a DataFrame(can be multiple modes)
mode_values=df.mode().iloc[0]
print("\nMode values:")
print(mode_values)


import pandas as pd
from sklearn.datasets import load_iris
#load iris dataset
iris=load_iris()
df=pd.DataFrame(iris.data,columns=iris.feature_names)
print("First 5 rows of dataset:")
print(df.head())
#Range(max-min)
range_values=df.max()-df.min()
print("\nRange values:")
print(range_values)
#Variance
variance_values=df.var()
print("\nVariance values:")
print(variance_values)
#Standard Deviation
std_values=df.std()
print("\nStandard Deviation values:")
print(std_values)
#Interquartile Range(IQR)
Q1=df.quantile(0.25)
Q3=df.quantile(0.75)
IQR=Q3-Q1
print("\nInterquartile Range(IQR):")
print(IQR)

#apply this to tips dataset also
import pandas as pd
# load tips dataset
df = pd.read_csv("tips.csv")
print("First 5 rows of dataset:")
print(df.head())
#Range(max-min)
range_values=df.select_dtypes(include='number').max() - df.select_dtypes(include='number').min()
print("\nRange values:")
print(range_values)
#Variance
variance_values=df.select_dtypes(include='number').var()
print("\nVariance values:")
print(variance_values)
#Standard Deviation
std_values=df.select_dtypes(include='number').std()
print("\nStandard Deviation values:")
print(std_values)
#Interquartile Range(IQR)
Q1=df.select_dtypes(include='number').quantile(0.25)
Q3=df.select_dtypes(include='number').quantile(0.75)
IQR=Q3-Q1
print("\nInterquartile Range(IQR):")
print(IQR)


import pandas as pd
from sklearn.datasets import load_iris
#load iris dataset
iris=load_iris()
df=pd.DataFrame(iris.data,columns=iris.feature_names)
print("First 5 rows of dataset:")
print(df.head())
#Skewness(asymmetry of distribution)
skewness_values=df.skew()
print("\nSkewness values:")
print(skewness_values)
#Kurtosis(peakedness/tail heaviness)
kurtosis_values=df.kurt()
print("\nKurtosis values:")
print(kurtosis_values)

#tips dataset
import pandas as pd
# load tips dataset
df = pd.read_csv("tips.csv")
print("First 5 rows of dataset:")
print(df.head())
#Skewness(asymmetry of distribution)
skewness_values=df.select_dtypes(include='number').skew()
print("\nSkewness values:")
print(skewness_values)
#Kurtosis(peakedness/tail heaviness)
kurtosis_values=df.select_dtypes(include='number').kurt()
print("\nKurtosis values:")
print(kurtosis_values)