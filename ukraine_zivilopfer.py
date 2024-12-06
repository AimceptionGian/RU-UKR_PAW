import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ukraine_krieg_zivile_opfer.csv')

df_civilian = pd.DataFrame(df)

fig, ax = plt.subplots()

bar_width = 0.35
index = range(len(df_civilian))  

color_adults = '#A1C6EA'  
color_children = '#F9D3B4'

bars_adults = ax.bar(index, df_civilian['Erwachsene'], color=color_adults, label='Erwachsene (Getötet/Verletzt)', width=bar_width)
bars_children = ax.bar(index, df_civilian['Kinder'], bottom=df_civilian['Erwachsene'], color=color_children, label='Kinder (Getötet/Verletzt)', width=bar_width)

for i in range(len(df_civilian)):
    ax.text(i, df_civilian['Erwachsene'][i] / 2, f'{df_civilian["Erwachsene"][i]}', ha='center', color='black', fontsize=10, verticalalignment='center')
    ax.text(i, df_civilian['Erwachsene'][i] + df_civilian['Kinder'][i] / 2, f'{df_civilian["Kinder"][i]}', ha='center', color='black', fontsize=10, verticalalignment='center')
  
    total = df_civilian['Erwachsene'][i] + df_civilian['Kinder'][i]
    ax.text(i, total + 1000, f'{total}', ha='center', color='black', fontsize=12, fontweight='bold', verticalalignment='bottom')
  
ax.set_xlabel('Kategorie')
ax.set_ylabel('Anzahl der Opfer')
ax.set_title('Zivilopfer im Ukraine-Krieg (2024)')

ax.set_xticks(index)
ax.set_xticklabels(df_civilian['Kategorie'])

max_value = df_civilian['Erwachsene'].max() + df_civilian['Kinder'].max() + 4000 
ax.set_ylim(0, max_value)

ax.legend()

plt.tight_layout()
plt.savefig('zivilopfer_ukraine_krieg_pastellfarben_optimiert_skala.png')
plt.show()
