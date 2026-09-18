import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[2,4,6,8,10]
plt.plot(x,y)
plt.show()
#example on diff values
x=[5,8,1,3,4]
y=[2,6,4,1,9]
plt.plot(x,y)
plt.show()

x=[1,2,3,4,5]
y=[2,4,6,8,10]
plt.title("Line Graph")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.plot(x,y)
plt.show()

import matplotlib.pyplot as plt
y1=[]
y2=[]
x=range(-100,100,10)
for i in x:
    y1.append(i**2)
for i in x:
    y2.append(-i**2)
plt.plot(x,y1)
plt.plot(x,y2)
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('simple graph')
plt.axhline()     #horizontal
plt.show()

import matplotlib.pyplot as plt
y1=[]
y2=[]
x=range(-100,100,10)
for i in x:
    y1.append(i**2)
for i in x:
    y2.append(-i**2)
plt.plot(x,y1)
plt.plot(x,y2)
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('simple graph')
plt.axhline()
plt.axvline()             #vertical
plt.show()

import matplotlib.pyplot as plt
y1=[]
y2=[]
x=range(-100,100,10)
for i in x:
    y1.append(i**2)
for i in x:
    y2.append(-i**2)
plt.plot(x,y1)
plt.plot(x,y2)
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('simple graph')
plt.axhline(color='red')
plt.axvline(color='green')
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv("temporal.csv")
plt.plot(df['deep learning'],df['machine learning'],color='red')
plt.xlabel('deep learning')
plt.ylabel('machine learning')
plt.title('line plot')
plt.savefig("temp.png")
plt.show()

plt.plot(df['Mes'],df['data science'],label='data science')
plt.plot(df['Mes'],df['machine learning'],label='machine learning')
plt.plot(df['Mes'],df['deep learning'],label='deep learning')
plt.xlabel('Date')
plt.ylabel('popularity')
plt.title('popularity of AI terms by date')
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv("temporal.csv")
plt.plot(df['deep learning'],df['machine learning'],color='red')
plt.xlabel('deep learning')
plt.ylabel('machine learning')
plt.title('line plot')
plt.xlim(10,100)
plt.ylim(0,50)
plt.grid(True)
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
data=sns.load_dataset("iris")
sns.pairplot(data,hue='species')
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
data=sns.load_dataset("tips")
c_p={'Male':'lightblue','Female':'green'}
sns.pairplot(data,hue='sex',palette=c_p)
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
data=sns.load_dataset("tips")
sns.pairplot(data[['total_bill','tip','size']])
plt.show()

import seaborn as sns
import numpy as np
x=np.random.randn(200)
y=np.random.randn(200)
sns.kdeplot()

import seaborn as sns
import numpy as np
x=np.random.randn(200)
y=np.random.randn(200)
sns.kdeplot(x,fill=True)
sns.kdeplot(y)

import seaborn as sns
import numpy as np
x=np.random.randn(200)
y=np.random.randn(200)
#sns.kdeplot(x,vertical=False)

import seaborn as sns
import numpy as np
x=np.random.randn(200)
y=np.random.randn(200)
sns.kdeplot(x=x,y=y)

import seaborn as sns
df=sns.load_dataset('iris')
sns.kdeplot(x=df['petal_length'])
sns.kdeplot(x=df['petal_width'],fill=True)

import seaborn as sns
df=sns.load_dataset('iris')
sns.kdeplot(x=df['petal_length'],y=df['petal_width'])

import seaborn as sns
df=sns.load_dataset('tips')
sns.displot(data['total_bill'],kde=True,color='red',bins=30)
plt.show()

import seaborn as sns
df=sns.load_dataset('tips')
sns.displot(data['total_bill'],kde=True,color='red',bins=20)
plt.show()

import seaborn as sns
df=sns.load_dataset('tips')
sns.jointplot(x='total_bill',y='tip',data=data)
plt.show()

import seaborn as sns
df=sns.load_dataset('tips')
sns.countplot(x='sex',hue='smoker',data=data)
plt.show()

import seaborn as sns
df=sns.load_dataset('tips')
sns.boxplot(data['total_bill'])
plt.show()

import seaborn as sns
df=sns.load_dataset('tips')
sns.boxplot(data['size'])
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
#loading the dataset 'tips'
df=pd.read_csv('tips.csv')
import numpy as np
plt.boxplot(df['total_bill'])
plt.show()

import seaborn as sns
import pandas as pd
df=pd.read_csv('temporal.csv')
df
sns.boxplot(df['data science'])
plt.show()

import seaborn as sns
import pandas as pd
import numpy as np
df=pd.read_csv('/content/temporal.csv')
Q1=np.percentile(df['data science'],25,method='midpoint')
Q3=np.percentile(df['data science'],75,method='midpoint')
IQR=Q3-Q1
print("the output of IQR")
print(IQR)

import seaborn as sns
import numpy as np
data=np.random.randint(1,100,(10,10))
sns.heatmap(data)
plt.show()

import seaborn as sns
import numpy as np
data=np.random.randint(1,100,(10,10))
sns.heatmap(data,vmin=30,vmax=70)

import seaborn as sns
import numpy as np
data=np.random.randint(1,100,(10,10))
sns.heatmap(data,vmin=30,vmax=70,annot=True)

import seaborn as sns
import numpy as np
data=np.random.randint(1,100,(10,10))
sns.heatmap(data,cmap='tab20',annot=True)

import seaborn as sns
data=sns.load_dataset('tips')
sns.heatmap(data[['tip']])

import seaborn as sns
data=sns.load_dataset('iris')
sns.heatmap(data[['petal_length']])

import matplotlib.pyplot as plt
data=[12,15,20,22,23,25,25,25,30,32,35,40]
plt.hist(data,bins=5,color='red',edgecolor='green')
plt.title("Histogram example")
plt.xlabel("Value Range")
plt.ylabel("Frequency")
plt.show()

import seaborn as sns
data=sns.load_dataset("tips")
plt.hist(data['total_bill'],bins=10,color='skyblue',edgecolor='black')
plt.title("Histogram example")
plt.xlabel("Value Range")
plt.ylabel("Frequency")
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('iris')
sns.violinplot(x='species',y='petal_length',data=df)
plt.title("violin plot")
plt.show()

#pip install dash
#import dash

import dash
from dash import dcc,html
app=dash.Dash(__name__)
app.layout=html.Div([
    html.H1("Dash Tutotrial")
    dcc.Graph(
        id="example",
        figure={
            "data":[
                {
                    "x":[1,2,3,4,5],
                    "y":[5,4,7,4,8],
                    "type": "line",
                    "name":"Trucks"
                },
                {
                    "x":[1,2,3,4,5],
                    "y":[6,3,5,3,7],
                    "type": "bar",
                    "name":"Ships"
                }
            ],
            "layout":{
                "title": "Basic Dashboard"
            }
        }
    )
])
app.run(debug=True, port = 8052)

