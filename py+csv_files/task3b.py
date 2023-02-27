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
flierprops = dict( markerfacecolor='black',
                  markeredgecolor='none')
boxprops = {'edgecolor':'k','facecolor':'white'}
medianprops = dict( linewidth=3)
sns.set(rc={'figure.figsize':(17,9)})
g=sns.boxplot(data=df,x='country_id',y='AverageTemperatureCels'
,flierprops=flierprops,boxprops=boxprops,color='none',medianprops=medianprops,showcaps=False);
lst=['NEW','BRA','SOU','UKR','FRA','SWE','JAP','POL']
for i in lst:
    y = df.AverageTemperatureCels[df.country_id==i]
    x = np.random.normal(lst.index(i), 0.13, size=len(y))
    plt.plot(x, y, 'r.', alpha=0.7, color='red')

plt.xlabel('country_id',fontsize=20,color='black')
plt.ylabel('AverageTemperatureCelsius',fontsize=20,color='black')
plt.grid(True,axis='x')
a= sys.argv[1]
if int(a)==1:
   plt.savefig('task3b.png')

   print(os.getcwd())
else:
   plt.show()












