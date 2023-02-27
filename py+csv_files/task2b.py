import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import utiy as ut
import sys 
import os
df=ut.fnct(pd.read_csv('temperature.csv'))
#fig,ax=plt.subplots(figsize=(10,7))
sns.set_style("darkgrid")
g=sns.relplot(data=df,x='year',y='AverageTemperatureCels',facecolor='black',edgecolor='black')
g.fig.set_size_inches(10,7)
plt.xlabel('Year',fontsize=20)
plt.ylabel('AverageTemperatureCelsius',fontsize=20)
plt.xticks([1750,1800,1850,1900,1950,2000],['','1800','','1900','','2000'])
a= sys.argv[1]
if int(a)==1:

   plt.savefig('task2b.png')

   print(os.getcwd())
else:
   plt.show()










