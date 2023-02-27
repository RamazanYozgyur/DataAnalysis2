import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import utiy as ut
import sys 
import os
df=ut.fnct(pd.read_csv('temperature.csv'))
plt.figure(figsize=(15,7))
sns.set_style('darkgrid')
plt.grid(True)
colors=['indianred','peru','yellowgreen','seagreen','cyan','cornflowerblue','darkorchid','magenta']
for i,j in zip(df.Country.unique(),colors):

    plt.plot(df[df.Country==i].groupby(['year'])[['AverageTemperatureCels','year']].mean().year,df[df.Country==i].groupby(['year'])[['AverageTemperatureCels','year']].mean().AverageTemperatureCels,color=j)
plt.grid(True)
plt.legend(['NewZealand','Brazil' ,'South Africa','Ukraine', 'France', 'Sweden',
        'Japan','Poland'],bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.,title='Countries',fontsize=15)
plt.xlabel('year',fontsize=15)
plt.ylabel('countryAverage',fontsize=15)
plt.xticks([1750,1800,1850,1900,1950,2000],['','1800','','1900','','2000'])
plt.tight_layout()
a= sys.argv[1]
if int(a)==1:
  plt.savefig('task4c.png',bbox_inches='tight')
  print(os.getcwd())
else:
  plt.show()

