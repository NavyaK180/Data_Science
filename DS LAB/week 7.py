import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
#load iris dataset
iris=load_iris()
df=pd.DataFrame(iris.data,columns=iris.feature_names)
df['species']=iris.target
#1.univariate visualizations
#histogram
plt.figure(figsize=(6,4))
sns.histplot(df['sepal length (cm)'],bins=20,kde=True)
plt.title("Histogram of sepal Length")
plt.show()

#Boxplot
plt.figure(figsize=(6,4))
sns.boxplot(df['sepal length (cm)'])
plt.title("Boxplot of sepal Length")
plt.show()

#Pie Chart (species distribution)
species_counts=df['species'].value_counts()
plt.figure(figsize=(6,6))
plt.pie(species_counts, labels=iris.target_names, autopct='%1.1f%%')
plt.title("Species Distribution (Pie Chart)")
plt.show()

#2. Bivariate Visualizations
#Scatter plot
plt.figure(figsize=(6,4))
sns.scatterplot(x=df['sepal length (cm)'],y=df['sepal width (cm)'], hue=df['species'])
plt.title("Scatterplot: Sepal length vs Sepal width  ")
plt.show()

#Line Chart(trend of sepal length across samples)
plt.figure(figsize=(6,4))
plt.plot(df['sepal length (cm)'])
plt.title("Line Chart of Sepal Length")
plt.xlabel("Sample Index")
plt.ylabel("Sepal Length (cm)")
plt.show()

#Bar Chart(mean sepal lenght per species)
plt.figure(figsize=(6,4))
sns.barplot(x=df['species'],y=df['sepal length (cm)'])
plt.title("Bar Chart: Mean Sepal Length by Species")
plt.xticks([0,1,2], iris.target_names)
plt.show()

#3. Multivariate Visualizations
# Heatmap (correlation matrix)
plt.figure(figsize=(8,4))
sns.heatmap(df.iloc[:,:4].corr(), annot = True, cmap="coolwarm")
plt.title("Heatmap of Feature Correlations")
plt.show()
#Bubble Chart (scatterplot with size = petal length)
plt.figure(figsize=(6,4))
plt.scatter(df['sepal length (cm)'],df['sepal width (cm)'],s=df['petal length (cm)']*20, alpha=0.5, c= df['species'])
plt.title("Bubble Chart: Sepal vs Petal (size = petal length)")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.show()
# Pair plot
sns.pairplot(df.iloc[:,:4])
plt.suptitle("Pair Plot of Iris Feature", y= 1.02)
plt.show()

# 4. Adavanced Techniques
# Violin Plot
plt.figure(figsize=(6,4))
sns.violinplot(x=df['species'], y = df['sepal length (cm)'])
plt.title("Violin Plot: Sepal Length by Species")
plt.xticks([0,1,2], iris.target_names)
plt.show()  


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# load tips dataset
tips = sns.load_dataset("tips")
# 1. univariate visualizations
# histogram
plt.figure(figsize=(6,4))
sns.histplot(tips['total_bill'], bins=20, kde=True)
plt.title("Histogram of Total Bill")
plt.show()
# Boxplot
plt.figure(figsize=(6,4))
sns.boxplot(tips['total_bill'])
plt.title("Boxplot of Total Bill")
plt.show()
# Pie Chart (day distribution)
day_counts = tips['day'].value_counts()
plt.figure(figsize=(6,6))
plt.pie(day_counts, labels=day_counts.index, autopct='%1.1f%%')
plt.title("Day Distribution (Pie chart)")
plt.show()

# 2. Bivariate Visualizations

# Scatterplot
plt.figure(figsize=(6,4))
sns.scatterplot(x=tips['total_bill'], y=tips['tip'], hue=tips['sex'])
plt.title("Scatterplot: Total Bill vs Tip")
plt.show()

# Line chart
plt.figure(figsize=(6,4))
plt.plot(tips['total_bill'])
plt.title("Line Chart for Total Bill")
plt.show()

# Bar Chart
plt.figure(figsize=(6,4))
sns.barplot(x=tips['day'], y=tips['total_bill'])
plt.title("Bar Chart: Mean Total Bill by Day")
plt.show()

#3.multivariate visualization
# Heatmap (correlation matrix)
plt.figure(figsize=(8,4))
sns.heatmap(tips.iloc[:,:4].corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Heatmap of Tips Feature Correlations")
plt.show()

# Bubble Chart (scatterplot with size = tip)
plt.figure(figsize=(6,4))
plt.scatter(
    tips['total_bill'],
    tips['tip'],
    s=tips['size']*20,
    alpha=0.5,
    c=tips['size']
)
plt.title("Bubble Chart: Total Bill vs Tip (size = party size)")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.show()

# Pair plot
sns.pairplot(tips.iloc[:,:4])
plt.suptitle("Pair Plot of Tips Features", y=1.02)
plt.show()

# 4. Advanced Techniques
# Violin Plot
plt.figure(figsize=(6,4))
sns.violinplot(x=tips['day'], y=tips['total_bill'])
plt.title("Violin Plot: Total Bill by Day")
plt.show()