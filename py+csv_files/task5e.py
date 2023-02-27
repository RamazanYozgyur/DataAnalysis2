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
newlst=[]
for i in ['Brazil' ,'France','Japan','New Zealand','Poland','South Africa','Sweden','Ukraine']:
    newlst.append(list(df[df.Country==i].City.unique()))
colors=[['indianred','darkred'],['peru','darkorange'],['yellowgreen','palegreen'],['seagreen','springgreen'],['cyan','cadetblue'],['cornflowerblue','navy'],['darkorchid','plum'],['magenta','pink','crimson','orchid']]
cities=[['Brasília', 'Canoas'],
 ['Marseille', 'Paris'],
 ['Tokyo', 'Tottori'],
 ['Auckland', 'Hamilton'],
 ['Warsaw', 'Wroclaw'],
 ['Cape Town', 'Johannesburg'],
 ['Stockholm', 'Uppsala'],
 ['Kherson', 'Kiev', 'Lvov', 'Odesa']]
sns.set_style('whitegrid')
legendlst=[]
fig, axs = plt.subplots(3, 3,figsize=(10,10))
axs[-1,-1].axis('off')
for i in newlst:
    if newlst.index(i)<=2 : 
        for j in i:
            axs[0,newlst.index(i)%3].plot(df[df.City==j].groupby('year')[['AverageTemperatureCels','year']].mean().year,df[df.City==j].groupby('year')[['AverageTemperatureCels','year']].mean().AverageTemperatureCels,color=colors[newlst.index(i)][i.index(j)])
            legendlst.append(axs[0,newlst.index(i)%3].plot(df[df.City==j].groupby('year')[['AverageTemperatureCels','year']].mean().year,df[df.City==j].groupby('year')[['AverageTemperatureCels','year']].mean().AverageTemperatureCels,color=colors[newlst.index(i)][i.index(j)])
[0])
        axs[0,newlst.index(i)%3].set_xlim(1730,2020)
        axs[0,newlst.index(i)%3].set_ylim(-5,25)
        axs[0,newlst.index(i)%3].set_title(countries[newlst.index(i)])

    elif newlst.index(i)>2 and newlst.index(i)<=5 :
        for j in i:
            axs[1,newlst.index(i)%3].plot(df[df.City==j].groupby('year')[['AverageTemperatureCels','year']].mean().year,df[df.City==j].groupby('year')[['AverageTemperatureCels','year']].mean().AverageTemperatureCels,color=colors[newlst.index(i)][i.index(j)])
            legendlst.append(axs[1,newlst.index(i)%3].plot(df[df.City==j].groupby('year')[['AverageTemperatureCels','year']].mean().year,df[df.City==j].groupby('year')[['AverageTemperatureCels','year']].mean().AverageTemperatureCels,color=colors[newlst.index(i)][i.index(j)])
[0])                
        axs[1,newlst.index(i)%3].set_xlim(1730,2020)
        axs[1,newlst.index(i)%3].set_ylim(-5,25)
        axs[1,newlst.index(i)%3].set_title(countries[newlst.index(i)])
    else:
        axs[2,newlst.index(i)%3].set_xlim(1730,2020)
        axs[2,newlst.index(i)%3].set_ylim(-5,25)
        axs[2,newlst.index(i)%3].set_title(countries[newlst.index(i)])
        for j in i:
            axs[2,newlst.index(i)%3].plot(df[df.City==j].groupby('year')[['AverageTemperatureCels','year']].mean().year,df[df.City==j].groupby('year')[['AverageTemperatureCels','year']].mean().AverageTemperatureCels,color=colors[newlst.index(i)][i.index(j)])
            legendlst.append(axs[2,newlst.index(i)%3].plot(df[df.City==j].groupby('year')[['AverageTemperatureCels','year']].mean().year,df[df.City==j].groupby('year')[['AverageTemperatureCels','year']].mean().AverageTemperatureCels,color=colors[newlst.index(i)][i.index(j)])[0])
            axs[2,newlst.index(i)%3].tick_params('x', labelrotation=45)
fig.tight_layout(pad=0.0000000000005)
for ax in axs.flat:
    ax.label_outer()    
finallist=[]
for i in cities:
    for j in i:
        finallist.append(j)
    
plt.legend(legendlst,finallist,bbox_to_anchor=(1.1, 0.75), loc='lower left',title="Cities",fontsize=15)
    
fig.text(0.3, -0.05, 'Year of observation', ha='center',fontsize=20)
fig.text(-0.05, 0.5, 'Average temperature', va='center', rotation='vertical',fontsize=20)
fig.text(0.5, 1.01, 'Average temperature', ha='center',fontsize=25,color='black')
a= sys.argv[1]
if int(a)==1:
  plt.savefig('task5e.png',bbox_inches='tight')
  print(os.getcwd())
else:
  plt.tight_layout()
  plt.show()


