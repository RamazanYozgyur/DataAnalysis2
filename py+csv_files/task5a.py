import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import utiy as ut
import sys
import os
df=ut.fnct(pd.read_csv('temperature.csv'))
colors=['indianred','peru','yellowgreen','seagreen','cyan','cornflowerblue','darkorchid','magenta']
lst=['Brazil' ,'France','Japan','New Zealand','Poland','South Africa','Sweden','Ukraine']
sns.set_style('darkgrid')
fig, axs = plt.subplots(3, 3,figsize=(10,10))
#axs[-1,-1].axis('off')
legendlst=[]
for i in range(3):
    for j in range(3):
        if i==2 and j==2:
            axs[i,j].axis('off')
        else:
            sns.set_style('darkgrid')
            axs[i,j].set_xlim(1730,2020)
            axs[i,j].set_ylim(-5,25)
            axs[i,j].plot(df[df.Country==lst[i*3+j]].groupby(['year'])[['AverageTemperatureCels','year']].mean().year,df[df.Country==lst[i*3+j]].groupby(['year'])[['AverageTemperatureCels','year']].mean().AverageTemperatureCels,color=colors[3*i+j])
            axs[i,j].set_title(lst[i*3+j],fontdict={'color':'black'})
            axs[i,j].grid(True)
            legendlst.append(axs[i,j].plot(df[df.Country==lst[i*3+j]].groupby(['year'])[['AverageTemperatureCels','year']].mean().year,df[df.Country==lst[i*3+j]].groupby(['year'])[['AverageTemperatureCels','year']].mean().AverageTemperatureCels,color=colors[3*i+j])
[0])
fig.tight_layout(pad=0.0000000000005)
for ax in axs.flat:
    ax.label_outer()

plt.legend(legendlst,lst,bbox_to_anchor=(1.1, 2), loc='lower left',title="Countries",fontsize=15)
fig.text(0.3, -0.05, 'Year', ha='center',fontsize=15)
fig.text(-0.05, 0.5, 'CountryAverage', va='center', rotation='vertical',fontsize=15)
a= sys.argv[1]
if int(a)==1:
  plt.savefig('task5a.png',bbox_inches='tight')
  print(os.getcwd())
else:
  plt.tight_layout()
  plt.show()

