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
sns.set(rc={'figure.figsize':(17,9)})

flierprops = dict( markerfacecolor='black',
                  markeredgecolor='none')
boxprops = {'edgecolor':'k','facecolor':'white'}
medianprops = dict( linewidth=3)
sns.violinplot(data=df,x='country_id',y='AverageTemperatureCels'
);
plt.xlabel('country_id',fontsize=20,color='black')
plt.ylabel('AverageTemperatureCelsius',fontsize=20,color='black')
plt.grid(True,axis='x')
a= sys.argv[1]
if int(a)==1:
   plt.savefig('task3c.png')

   print(os.getcwd())
else:
   plt.show()












