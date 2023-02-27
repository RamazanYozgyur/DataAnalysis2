import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import utiy as ut
import sys
import os
df=ut.fnct(pd.read_csv('temperature.csv'))
plt.figure(figsize=(10,7))
sns.set_style("darkgrid")
dff=df.groupby(['year','Country'])[['AverageTemperatureCels','year']].mean()
plt.plot(dff.year,dff.AverageTemperatureCels,color='black')
plt.xlabel('year',fontsize=15)
plt.ylabel('countryAverage',fontsize=15)
plt.grid(True)
plt.xticks([1750,1800,1850,1900,1950,2000],['','1800','','1900','','2000'])
a=sys.argv[1]
if int(a)==1:
  plt.savefig('task4a.png')

  print(os.getcwd())
else:
  plt.show()
