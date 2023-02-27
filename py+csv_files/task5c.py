import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import utiy as ut
import sys
import os
df=ut.fnct(pd.read_csv('temperature.csv'))
colors=['indianred','peru','yellowgreen','seagreen','cyan','cornflowerblue','darkorchid','magenta']
countries=['Brazil' ,'France','Japan','New Zealand','Poland','South Africa','Sweden','Ukraine']
sns.set_style('whitegrid')

newlst=[]
for i in ['Brazil' ,'France','Japan','New Zealand','Poland','South Africa','Sweden','Ukraine']:
    newlst.append(list(df[df.Country==i].City.unique()))

fig, axs = plt.subplots(3, 3,figsize=(10,10))
axs[-1,-1].axis('off')
legendlst=[]
for i in newlst:
    if newlst.index(i)<=2 : 
        for j in i:
            axs[0,newlst.index(i)%3].plot(df[df.City==j].groupby('year')[['AverageTemperatureCels','year']].mean().year,df[df.City==j].groupby('year')[['AverageTemperatureCels','year']].mean().AverageTemperatureCels,color=colors[newlst.index(i)])
        axs[0,newlst.index(i)%3].set_xlim(1730,2020)
        axs[0,newlst.index(i)%3].set_ylim(-5,25)
        axs[0,newlst.index(i)%3].set_title(countries[newlst.index(i)])
        legendlst.append( axs[0,newlst.index(i)%3].plot(df[df.City==j].groupby('year')[['AverageTemperatureCels','year']].mean().year,df[df.City==j].groupby('year')[['AverageTemperatureCels','year']].mean().AverageTemperatureCels,color=colors[newlst.index(i)])
[0])
    elif newlst.index(i)>2 and newlst.index(i)<=5 :
        for j in i:
            axs[1,newlst.index(i)%3].plot(df[df.City==j].groupby('year')[['AverageTemperatureCels','year']].mean().year,df[df.City==j].groupby('year')[['AverageTemperatureCels','year']].mean().AverageTemperatureCels,color=colors[newlst.index(i)])
        axs[1,newlst.index(i)%3].set_xlim(1730,2020)
        axs[1,newlst.index(i)%3].set_ylim(-5,25)
        axs[1,newlst.index(i)%3].set_title(countries[newlst.index(i)])
        legendlst.append(axs[1,newlst.index(i)%3].plot(df[df.City==j].groupby('year')[['AverageTemperatureCels','year']].mean().year,df[df.City==j].groupby('year')[['AverageTemperatureCels','year']].mean().AverageTemperatureCels,color=colors[newlst.index(i)])
[0])
    else:
        axs[2,newlst.index(i)%3].set_xlim(1730,2020)
        axs[2,newlst.index(i)%3].set_ylim(-5,25)
        axs[2,newlst.index(i)%3].set_title(countries[newlst.index(i)])
        for j in i:
            axs[2,newlst.index(i)%3].plot(df[df.City==j].groupby('year')[['AverageTemperatureCels','year']].mean().year,df[df.City==j].groupby('year')[['AverageTemperatureCels','year']].mean().AverageTemperatureCels,color=colors[newlst.index(i)])
        legendlst.append(axs[2,newlst.index(i)%3].plot(df[df.City==j].groupby('year')[['AverageTemperatureCels','year']].mean().year,df[df.City==j].groupby('year')[['AverageTemperatureCels','year']].mean().AverageTemperatureCels,color=colors[newlst.index(i)])
[0])
fig.tight_layout(pad=0.0000000000005)
for ax in axs.flat:
    ax.label_outer()
plt.legend(legendlst,countries,bbox_to_anchor=(1.1, 2), loc='lower left',title="Countries",fontsize=15)

fig.text(0.3, -0.05, 'Year', ha='center',fontsize=15)
fig.text(-0.05, 0.5, 'CityAverage', va='center', rotation='vertical',fontsize=15)

a= sys.argv[1]
if int(a)==1:
  plt.savefig('task5c.png',bbox_inches='tight')
  print(os.getcwd())
else:
  plt.tight_layout()
  plt.show()


