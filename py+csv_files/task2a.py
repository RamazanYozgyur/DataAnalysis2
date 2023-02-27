import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import utiy as ut
import sys 
import os
df=ut.fnct(pd.read_csv('temperature.csv'))
#plt.figure(figsize=(10,7))
fig,ax=plt.subplots(figsize=(10,7))
ax.scatter(df.year,df.AverageTemperatureCels,facecolor='none',edgecolor='black')
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
ax.set_xlabel('Year',fontsize=20)
ax.set_ylabel('AverageTemperatureCelsius',fontsize=20)
ax.yaxis.set_label_coords(-0.1,0.5)
a= sys.argv[1]
if int(a)==1:
    
   plt.savefig('task2a.png')

   print(os.getcwd())
else:
   plt.show()











