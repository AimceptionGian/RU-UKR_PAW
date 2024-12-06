import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ukraine_militaerausgaben.csv')
df_ukraine = pd.DataFrame(df)

fig, ax1 = plt.subplots()

ax1.set_xlabel('Jahr')
ax1.set_ylabel('Anteil am BIP (%)', color='tab:blue')
ax1.bar(df_ukraine['Jahr'], df_ukraine['Anteil_am_BIP'], color='tab:blue', alpha=0.6, label='Anteil am BIP (%)')  
ax1.tick_params(axis='y', labelcolor='tab:blue')

ax2 = ax1.twinx()
ax2.set_ylabel('Absolut in Mrd USD', color='tab:green')
ax2.plot(df_ukraine['Jahr'], df_ukraine['Absolut_in_Mrd_USD'], color='tab:green', marker='o', label='Absolut in Mrd USD')
ax2.tick_params(axis='y', labelcolor='tab:green')

ax1.set_ylim(0, df_ukraine['Anteil_am_BIP'].max() * 1.1)  

ax1.set_xticks(df_ukraine['Jahr'])  
ax1.set_xticklabels(df_ukraine['Jahr'], rotation=45)  

plt.title('Militärausgaben der Ukraine (2008-2023)')
fig.tight_layout()

plt.savefig('ukraine_militaerausgaben_gesamt_linie_und_balken.png')

plt.show()
